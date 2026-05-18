# AporiaPolis — Makefile
#
# Cibles bootstrap local DuckDB. ADR-0031 stack hybride MVP local
# (DuckDB+parquet) / prod (Postgres+Object Storage). Refs #45 [G.1].
#
# Prérequis : `uv` disponible sur le PATH. La cible db.up crée un
# virtualenv local `.venv` et y installe `duckdb` à la demande.
#
# Tout exécute en Python inline pour rester homogène entre les envs
# (pas de dépendance au CLI duckdb qui est packagé séparément du
# module Python — duckdb-cli vs duckdb).

.PHONY: help db.up db.migrate db.show-schemas

DUCKDB_PATH := data/duckdb/aporiapolis.duckdb
MIGRATIONS_DIR := migrations
PYTHON := .venv/bin/python

help:
	@echo "Cibles AporiaPolis MVP local :"
	@echo "  make db.up           Crée data/duckdb/ et prépare .venv via uv"
	@echo "  make db.migrate      Applique migrations/*.sql sur DuckDB"
	@echo "  make db.show-schemas Liste les schémas DuckDB (diagnostic)"

db.up:
	@mkdir -p $(dir $(DUCKDB_PATH))
	@if [ ! -x "$(PYTHON)" ]; then \
		echo "Virtualenv absent — création via uv..."; \
		uv venv .venv; \
	fi
	@if ! $(PYTHON) -c "import duckdb" 2>/dev/null; then \
		echo "Module Python duckdb absent — installation..."; \
		uv pip install --python "$(PYTHON)" duckdb \
			|| (echo "Échec uv pip install duckdb dans .venv." \
				&& echo "Vérifier la disponibilité réseau et la config uv." \
				&& exit 1); \
	fi
	@echo "DuckDB ready ($(DUCKDB_PATH) + .venv)"

db.migrate:
	@$(PYTHON) -c "import duckdb, glob, sys; \
files = sorted(glob.glob('$(MIGRATIONS_DIR)/*.sql')); \
conn = duckdb.connect('$(DUCKDB_PATH)'); \
[conn.execute(open(f).read()) for f in files]; \
conn.close(); \
print(f'Applied {len(files)} migration(s) from $(MIGRATIONS_DIR)/')"

db.show-schemas:
	@$(PYTHON) -c "import duckdb; \
conn = duckdb.connect('$(DUCKDB_PATH)'); \
rows = conn.execute('SELECT schema_name FROM information_schema.schemata ORDER BY schema_name').fetchall(); \
print('\n'.join(r[0] for r in rows)); \
conn.close()"
