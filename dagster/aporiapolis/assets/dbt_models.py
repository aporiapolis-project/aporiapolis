"""B-8.3 — G.3 #47 + G.4 #48 — Assets Dagster pour dbt run + dbt snapshot.

Approche subprocess (D4 acté) : appelle `.venv/bin/dbt` directement,
pas `dagster-dbt`. Surface API minimale (P6). Déclencheur de révision
documenté ADR-0033 + BRIEF B-8.3 §D4 : reconsidérer `dagster-dbt`
quand (a) besoin de lineage manifest-driven, (b) sélection dbt native
côté Dagster, (c) plusieurs familles de modèles/snapshots à orchestrer.

Source: OWID (CC BY 4.0) — https://ourworldindata.org/co2-emissions
ADR-0031 — DuckDB+parquet local MVP.
ADR-0033 — dbt-snapshot concurrency=1 (run_tag `dagster/dbt_snapshot`).
"""

import os
import subprocess
from pathlib import Path

from dagster import (
    AssetExecutionContext,
    MaterializeResult,
    MetadataValue,
    asset,
)

# Tag run figé verbatim — cohérent ADR-0033 + dagster.yaml.
DBT_SNAPSHOT_TAG_KEY = "dagster/dbt_snapshot"


def _repo_root() -> Path:
    """Retourne la racine du repo AporiaPolis."""
    # On suppose que ce fichier vit en dagster/aporiapolis/assets/.
    return Path(__file__).resolve().parents[3]


def _dbt_executable() -> Path:
    """Chemin vers `.venv/bin/dbt` (P6 — pas de PATH magique)."""
    root = _repo_root()
    candidate = root / ".venv" / "bin" / "dbt"
    if not candidate.exists():
        raise RuntimeError(
            f"dbt executable absent à {candidate}. "
            f"Lancer `uv pip install -e .` depuis {root}."
        )
    return candidate


def _run_dbt(
    context: AssetExecutionContext,
    *args: str,
) -> subprocess.CompletedProcess[str]:
    """Exécute une commande dbt en subprocess, log stdout/stderr."""
    root = _repo_root()
    env = os.environ.copy()
    env.setdefault("DBT_PROFILES_DIR", str(root / "dbt"))
    cmd = [str(_dbt_executable()), *args]
    context.log.info(f"dbt subprocess: {' '.join(cmd)}")
    result = subprocess.run(
        cmd,
        cwd=str(root),
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.stdout:
        context.log.info(result.stdout)
    if result.stderr:
        context.log.warning(result.stderr)
    if result.returncode != 0:
        raise RuntimeError(
            f"dbt subprocess returned {result.returncode}. Cmd: {' '.join(cmd)}"
        )
    return result


@asset(
    name="dbt_run_models",
    description=(
        "Exécute `dbt run --target dev` sur tous les modèles staging+marts. "
        "B-8.3 — G.3 #47."
    ),
    compute_kind="dbt",
    group_name="dbt",
)
def dbt_run_models(context: AssetExecutionContext) -> MaterializeResult:
    """Run all dbt models (staging + marts) via subprocess."""
    result = _run_dbt(context, "run", "--target", "dev")
    return MaterializeResult(
        metadata={
            "stdout_tail": MetadataValue.text(result.stdout[-2000:]),
            "command": MetadataValue.text("dbt run --target dev"),
        }
    )


@asset(
    name="dbt_snapshot_indicateur",
    description=(
        "Exécute `dbt snapshot --select snapshot_indicateur --target dev`. "
        "B-8.3 — G.4 #48. Strategy `check` sur (value, unit, source). "
        "Run tag `dagster/dbt_snapshot` posé au niveau du JOB "
        "(snapshot_indicateur_job dans __init__.py), pas sur l'asset."
    ),
    compute_kind="dbt",
    group_name="dbt",
    deps=[dbt_run_models],
)
def dbt_snapshot_indicateur(
    context: AssetExecutionContext,
) -> MaterializeResult:
    """Run dbt snapshot_indicateur via subprocess."""
    result = _run_dbt(
        context,
        "snapshot",
        "--select",
        "snapshot_indicateur",
        "--target",
        "dev",
    )
    return MaterializeResult(
        metadata={
            "stdout_tail": MetadataValue.text(result.stdout[-2000:]),
            "command": MetadataValue.text(
                "dbt snapshot --select snapshot_indicateur --target dev"
            ),
            "tag_key": MetadataValue.text(DBT_SNAPSHOT_TAG_KEY),
            "tag_note": MetadataValue.text(
                "Run tag posé sur snapshot_indicateur_job (run_tags=), "
                "pas op_tags asset. Cf. ADR-0033."
            ),
        }
    )
