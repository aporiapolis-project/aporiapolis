# AporiaPolis — Makefile (B-8.2 v2.2)
# Convention Python : uv + virtualenv repo-local .venv (pré-vol §36).
# Source of truth des dépendances : pyproject.toml top-level.
# Aucun pip install --user ni --break-system-packages.

.PHONY: install db.up db.migrate db.show-schemas demo-ingest clean

VENV := .venv
PYTHON := $(VENV)/bin/python
DAGSTER := $(VENV)/bin/dagster

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

# Démonstrateur end-to-end ingestion OWID CO2 (B-8.2).
# Chaîne : install → db.up → db.migrate → dagster job execute.
# Appelle .venv/bin/dagster (pas dagster nu) pour garantir l'isolation
# du virtualenv repo-local.
# Test env frais attendu :
#   rm -rf data/duckdb data/bronze .venv && make demo-ingest
demo-ingest: db.migrate
	@$(DAGSTER) job execute -m aporiapolis -j ingest_owid_climate
	@echo "demo-ingest exit 0 — voir data/bronze/ et raw.owid_co2_emissions"

# Nettoyage local (utile pour tester env frais).
# Ne supprime pas le .duckdb par défaut (préservation des données
# locales). Pour reset complet : rm -rf data/duckdb data/bronze .venv
clean:
	rm -rf .venv
	@echo "clean — .venv supprimé. data/ préservé."
