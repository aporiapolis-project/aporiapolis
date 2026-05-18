# AporiaPolis — Makefile (B-8.2 v2.2)
# Convention Python : uv + virtualenv repo-local .venv (pré-vol §36).
# Source of truth des dépendances : pyproject.toml top-level.
# Aucun pip install --user ni --break-system-packages.

.PHONY: install db.up db.migrate db.show-schemas demo-ingest clean

VENV := .venv
PYTHON := $(VENV)/bin/python
DAGSTER := $(VENV)/bin/dagster

# B-8.3 — D7, SD2 — Variables d'environnement Dagster + dbt.
# DAGSTER_HOME : chemin où `dagster.yaml` est lu. Défaut = racine repo.
#   Override possible : `DAGSTER_HOME=/tmp/... make ...`.
# DBT_PROFILES_DIR : chemin où `profiles.yml` est lu. Défaut = `dbt/`.
DAGSTER_HOME ?= $(CURDIR)
DBT_PROFILES_DIR ?= $(CURDIR)/dbt
export DAGSTER_HOME
export DBT_PROFILES_DIR

# Création du virtualenv via uv. Idempotent : uv venv ne recrée pas
# si .venv existe déjà.
$(VENV)/bin/python:
	uv venv $(VENV)

# Installation editable depuis pyproject.toml. Cible cible commune
# pour toutes les opérations qui ont besoin de duckdb / dagster /
# pyarrow / requests / pyyaml.
install: $(VENV)/bin/python
	uv pip install -p $(PYTHON) -e .

# Préparation du dossier DuckDB local + sanity ping de la lib duckdb.
# Dépend de install (B-8.2 v2.2 — retrait du double-install duckdb).
db.up: install
	@mkdir -p data/duckdb
	@$(PYTHON) -c "import duckdb; con = duckdb.connect('data/duckdb/aporiapolis.duckdb'); con.close(); print('DuckDB ready (data/duckdb/aporiapolis.duckdb + .venv)')"

# Exécute toutes les migrations versionnées de migrations/*.sql dans
# l'ordre lexicographique. Idempotent (les migrations utilisent
# CREATE IF NOT EXISTS).
db.migrate: db.up
	@$(PYTHON) -c "import duckdb; from pathlib import Path; con = duckdb.connect('data/duckdb/aporiapolis.duckdb'); files = sorted(Path('migrations').glob('*.sql')); [con.execute(f.read_text()) for f in files]; con.close(); print(f'Applied {len(files)} migration(s) from migrations/')"

# Liste les schémas DuckDB (utile pour la sanity check post-migrate).
db.show-schemas: install
	@$(PYTHON) -c "import duckdb; con = duckdb.connect('data/duckdb/aporiapolis.duckdb'); rows = con.execute('SELECT schema_name FROM information_schema.schemata ORDER BY schema_name').fetchall(); [print(r[0]) for r in rows]; con.close()"

.PHONY: dbt.run dbt.test dbt.snapshot

# B-8.3 — G.3 — Exécute `dbt run` sur tous les modèles staging + marts.
dbt.run: $(VENV)
	@$(VENV)/bin/dbt run --target dev

# B-8.3 — G.3 — Exécute `dbt test` sur tous les tests dbt.
dbt.test: $(VENV)
	@$(VENV)/bin/dbt test --target dev

# B-8.3 — G.4 — Exécute `dbt snapshot` sur tous les snapshots.
dbt.snapshot: $(VENV)
	@$(VENV)/bin/dbt snapshot --target dev

# Démonstrateur end-to-end ingestion OWID CO2 (B-8.2).
# Chaîne : install → db.up → db.migrate → dagster job execute.
# Appelle .venv/bin/dagster (pas dagster nu) pour garantir l'isolation
# du virtualenv repo-local.
# Test env frais attendu :
#   rm -rf data/duckdb data/bronze .venv && make demo-ingest
demo-ingest: db.migrate
	@$(DAGSTER) job execute -m aporiapolis -j ingest_owid_climate
	@echo "demo-ingest exit 0 — voir data/bronze/ et raw.owid_co2_emissions"

.PHONY: demo-stage

# B-8.3 — Démo complète bout-en-bout, déterministe.
# Chaîne : install → db.up → db.migrate →
#         dagster job execute ingest_owid_climate (B-8.2) →
#         dbt run → dbt test → dbt snapshot (B-8.3).
# Critère B-8.3 §5 : exit 0 sur env totalement frais.
demo-stage: install db.up db.migrate
	@$(DAGSTER) job execute -m aporiapolis -j ingest_owid_climate
	@$(MAKE) dbt.run
	@$(MAKE) dbt.test
	@$(MAKE) dbt.snapshot
	@echo "demo-stage: chain complete (raw → staging → marts → snapshot)"

.PHONY: demo-stage-concurrency

# B-8.3 — G.4 #48 — Preuve concurrency one-shot.
# Appelle scripts/test_concurrency.sh qui :
#  - lance 2 runs snapshot_indicateur_job daemon arrêté (QUEUED),
#  - démarre daemon en background (trap pour cleanup),
#  - attend que la queue soit vide,
#  - prouve post-hoc le non-chevauchement des intervalles d'exécution.
# Prérequis : `make demo-stage` doit avoir tourné au moins une fois
# (mart peuplé).
demo-stage-concurrency: $(VENV)
	@bash scripts/test_concurrency.sh

# Nettoyage local (utile pour tester env frais).
# Ne supprime pas le .duckdb par défaut (préservation des données
# locales). Pour reset complet : rm -rf data/duckdb data/bronze .venv
clean:
	rm -rf .venv
	@echo "clean — .venv supprimé. data/ préservé."
