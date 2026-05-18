#!/usr/bin/env bash
# B-8.3 — G.4 #48 — Preuve concurrency dbt-snapshot via queue + daemon.
#
# D7+D9 : daemon encapsulé ici (pas de cible Makefile autonome). Cleanup
# via trap. Preuve post-hoc (timestamps) plutôt que photographie d'instant
# fragile RUNNING+QUEUED.
#
# Flow :
#   1. Vérifie prérequis : DAGSTER_HOME pointe vers dagster.yaml lisible.
#   2. Lance 2 `dagster job launch` sur snapshot_indicateur_job DAEMON
#      ARRÊTÉ → 2 runs en état QUEUED.
#   3. Démarre `dagster-daemon run` en background, capture PID.
#   4. Attend que la queue soit vide (polling 'dagster run list
#      --filter status=QUEUED' toutes les 2s, timeout 120s).
#   5. Stop daemon proprement (trap cleanup en EXIT).
#   6. Lit start_time/end_time des 2 derniers runs.
#   7. Prouve post-hoc : intervalles [start, end] disjoints (run B
#      start ≥ run A end).
#   8. Vérifie que les 2 runs sont en SUCCESS.
#
# Exit 0 si preuve réussie, exit 1 sinon. Sortie verbatim copiée
# dans RESULT.md Mission K.
#
# ADR-0033 — concurrency=1 sur tag 'dagster/dbt_snapshot'.
# dagster.yaml — run_queue: {} + tag_concurrency_limits limit=1.

set -euo pipefail

# ------------------------------------------------------------------
# Configuration
# ------------------------------------------------------------------

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

export DAGSTER_HOME="${DAGSTER_HOME:-$REPO_ROOT}"
VENV_BIN="$REPO_ROOT/.venv/bin"

JOB_NAME="snapshot_indicateur_job"
MODULE="aporiapolis"
QUEUE_TIMEOUT_SEC=120
POLL_INTERVAL_SEC=2

DAEMON_PID_FILE="/tmp/aporiapolis-dagster-daemon.pid"
DAEMON_LOG_FILE="/tmp/aporiapolis-dagster-daemon.log"

# ------------------------------------------------------------------
# Cleanup (trap)
# ------------------------------------------------------------------

cleanup() {
    local exit_code=$?
    if [[ -f "$DAEMON_PID_FILE" ]]; then
        local pid
        pid=$(cat "$DAEMON_PID_FILE" 2>/dev/null || true)
        if [[ -n "${pid:-}" ]] && kill -0 "$pid" 2>/dev/null; then
            echo "--- cleanup: stopping daemon PID $pid"
            kill "$pid" 2>/dev/null || true
            sleep 1
            if kill -0 "$pid" 2>/dev/null; then
                kill -9 "$pid" 2>/dev/null || true
            fi
        fi
        rm -f "$DAEMON_PID_FILE"
    fi
    if [[ $exit_code -ne 0 ]]; then
        echo "--- cleanup: non-zero exit ($exit_code). Daemon log tail:"
        [[ -f "$DAEMON_LOG_FILE" ]] && tail -30 "$DAEMON_LOG_FILE" || true
    fi
    exit $exit_code
}

trap cleanup EXIT INT TERM

# ------------------------------------------------------------------
# Phase 1 — Sanity
# ------------------------------------------------------------------

echo "=== Phase 1 — Sanity ==="
echo "REPO_ROOT=$REPO_ROOT"
echo "DAGSTER_HOME=$DAGSTER_HOME"
echo "JOB_NAME=$JOB_NAME"

if [[ ! -f "$DAGSTER_HOME/dagster.yaml" ]]; then
    echo "ERROR: dagster.yaml introuvable à $DAGSTER_HOME/dagster.yaml"
    exit 1
fi

if [[ ! -x "$VENV_BIN/dagster" ]]; then
    echo "ERROR: .venv/bin/dagster introuvable. Lancer 'make install'."
    exit 1
fi

# Vérification rapide que l'instance lit bien la queue.
# Ne pas piper directement vers `head` sous `set -o pipefail` :
# `dagster instance info` peut recevoir SIGPIPE quand `head` ferme tôt.
"$VENV_BIN/dagster" instance info > /tmp/aporiapolis-dagster-instance-info.txt
sed -n '1,35p' /tmp/aporiapolis-dagster-instance-info.txt
"$VENV_BIN/python" - <<'PYEOF'
from dagster import DagsterInstance

inst = DagsterInstance.get()
print("run_coordinator_runtime:", type(inst.run_coordinator).__name__)
print("run_queue_runtime:", inst.get_concurrency_config().run_queue_config)
PYEOF

# ------------------------------------------------------------------
# Phase 2 — Lance 2 runs daemon ARRÊTÉ
# ------------------------------------------------------------------

echo ""
echo "=== Phase 2 — Lancer 2 runs (daemon arrêté → état QUEUED) ==="

LAUNCH_A=$("$VENV_BIN/dagster" job launch -m "$MODULE" -j "$JOB_NAME" 2>&1 | tee /dev/stderr)
LAUNCH_B=$("$VENV_BIN/dagster" job launch -m "$MODULE" -j "$JOB_NAME" 2>&1 | tee /dev/stderr)

# Vérifier qu'au moins 2 runs sont en QUEUED.
sleep 1
QUEUED_COUNT=$("$VENV_BIN/python" - <<'PYEOF'
from dagster import DagsterInstance
from dagster._core.storage.dagster_run import DagsterRunStatus

inst = DagsterInstance.get()
runs = inst.get_runs(limit=100)
print(sum(
    1
    for run in runs
    if run.job_name == "snapshot_indicateur_job"
    and run.status == DagsterRunStatus.QUEUED
))
PYEOF
)
echo "Runs en état QUEUED juste après launch : $QUEUED_COUNT"

if [[ "$QUEUED_COUNT" -lt 2 ]]; then
    echo "WARN: moins de 2 runs en QUEUED ; le daemon pourrait déjà tourner. Continuons en preuve post-hoc."
fi

# ------------------------------------------------------------------
# Phase 3 — Démarre daemon en background
# ------------------------------------------------------------------

echo ""
echo "=== Phase 3 — Démarrer dagster-daemon en background ==="

"$VENV_BIN/dagster-daemon" run -m "$MODULE" -d "$REPO_ROOT" > "$DAEMON_LOG_FILE" 2>&1 &
DAEMON_PID=$!
echo "$DAEMON_PID" > "$DAEMON_PID_FILE"
echo "daemon PID=$DAEMON_PID (log: $DAEMON_LOG_FILE)"

sleep 3  # laisser le daemon initialiser ses singletons.

# ------------------------------------------------------------------
# Phase 4 — Attente queue vide
# ------------------------------------------------------------------

echo ""
echo "=== Phase 4 — Attendre que la queue se vide ==="

WAITED=0
while [[ $WAITED -lt $QUEUE_TIMEOUT_SEC ]]; do
    COUNTS=$("$VENV_BIN/python" - <<'PYEOF'
from dagster import DagsterInstance
from dagster._core.storage.dagster_run import DagsterRunStatus

inst = DagsterInstance.get()
runs = [r for r in inst.get_runs(limit=100) if r.job_name == "snapshot_indicateur_job"]
queued = sum(1 for r in runs if r.status == DagsterRunStatus.QUEUED)
running = sum(
    1
    for r in runs
    if r.status in {DagsterRunStatus.STARTING, DagsterRunStatus.STARTED}
)
print(f"{queued} {running}")
PYEOF
)
    read -r PENDING RUNNING <<< "$COUNTS"
    echo "[t=$WAITED s] QUEUED=$PENDING STARTED=$RUNNING"
    if [[ "$PENDING" -eq 0 ]] && [[ "$RUNNING" -eq 0 ]]; then
        echo "Queue vide après ${WAITED}s."
        break
    fi
    sleep $POLL_INTERVAL_SEC
    WAITED=$((WAITED + POLL_INTERVAL_SEC))
done

if [[ $WAITED -ge $QUEUE_TIMEOUT_SEC ]]; then
    echo "ERROR: timeout ${QUEUE_TIMEOUT_SEC}s en attendant que la queue se vide."
    exit 1
fi

# ------------------------------------------------------------------
# Phase 5 — Lecture timestamps + preuve post-hoc
# ------------------------------------------------------------------

echo ""
echo "=== Phase 5 — Lecture timestamps des 2 derniers runs ==="

# Récupère les runs les plus récents pour trace humaine.
"$VENV_BIN/dagster" run list --limit 8 > /tmp/runs.txt
cat /tmp/runs.txt

# Preuve post-hoc en Python (plus robuste que grep).
"$VENV_BIN/python" - <<'PYEOF'
import json
import subprocess
import sys
from datetime import datetime

# Appelle GraphQL via gh-style API Dagster pour récupérer les timestamps
# précis. Fallback : parsing de `dagster run list` plus permissif.
try:
    from dagster import DagsterInstance
except ImportError:
    print("ERROR: import DagsterInstance failed", file=sys.stderr)
    sys.exit(1)

inst = DagsterInstance.get()
records = inst.get_run_records(limit=50)
matching = [
    record
    for record in records
    if record.dagster_run.job_name == "snapshot_indicateur_job"
]
matching.sort(key=lambda record: record.create_timestamp)
last_two = matching[-2:]

if len(last_two) < 2:
    print(f"ERROR: only {len(last_two)} runs found for snapshot_indicateur_job", file=sys.stderr)
    sys.exit(1)

a_record, b_record = last_two
a = a_record.dagster_run
b = b_record.dagster_run
print("Run A:")
print(f"  run_id    : {a.run_id}")
print(f"  status    : {a.status}")
print(f"  created_at: {a_record.create_timestamp}")
print(f"  start_time: {a_record.start_time}")
print(f"  end_time  : {a_record.end_time}")
print("Run B:")
print(f"  run_id    : {b.run_id}")
print(f"  status    : {b.status}")
print(f"  created_at: {b_record.create_timestamp}")
print(f"  start_time: {b_record.start_time}")
print(f"  end_time  : {b_record.end_time}")

# Vérification non-chevauchement post-hoc.
errors = []
if str(a.status) != "DagsterRunStatus.SUCCESS":
    errors.append(f"Run A status={a.status}, attendu SUCCESS")
if str(b.status) != "DagsterRunStatus.SUCCESS":
    errors.append(f"Run B status={b.status}, attendu SUCCESS")
if a_record.end_time is None or b_record.start_time is None:
    errors.append("Timestamps manquants — preuve impossible")
elif b_record.start_time < a_record.end_time:
    errors.append(
        f"CHEVAUCHEMENT : run B start={b_record.start_time} < "
        f"run A end={a_record.end_time}. "
        "tag_concurrency_limits NON respecté."
    )

if errors:
    print("\nERROR(s):", file=sys.stderr)
    for e in errors:
        print(f"  - {e}", file=sys.stderr)
    sys.exit(1)

print("\nVERDICT : non-chevauchement vérifié post-hoc. "
      "tag_concurrency_limits respecté. #48 fermable acceptance-based.")
PYEOF

echo ""
echo "=== Phase 6 — Cleanup (via trap) ==="
# trap EXIT prendra le relais.
