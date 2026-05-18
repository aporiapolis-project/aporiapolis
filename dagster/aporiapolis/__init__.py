"""AporiaPolis — Dagster Definitions.

Expose les assets, le job nommé ``ingest_owid_climate`` (acceptance G.2
#46 verbatim) et le ``ScheduleDefinition`` quotidien 02:00 UTC (D5).

Notes architecturales :

- Pas de limite de concurrence dbt-snapshot ici. Cette config est
  une responsabilité d'**instance** Dagster (``dagster.yaml``),
  pas des Definitions Python. Voir ADR-0033.
- Pas d'instance Dagster (``dagster.yaml``) créée en B-8.2 — non
  nécessaire pour ``dagster job execute`` en mode éphémère.
- Le schedule est déclaratif. Il ne se déclenche pas sans un
  ``dagster-daemon`` actif (non lancé en B-8.2 — décision MVP).
"""

from __future__ import annotations

from dagster import (
    AssetSelection,
    DefaultScheduleStatus,
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    load_assets_from_modules,
)

from aporiapolis.assets import dbt_models, owid_co2_emissions
from aporiapolis.assets.dbt_models import (
    DBT_SNAPSHOT_TAG_KEY,
    dbt_run_models,
    dbt_snapshot_indicateur,
)

# Charge automatiquement tous les @asset déclarés dans le module
# aporiapolis.assets.*.
all_assets = load_assets_from_modules([owid_co2_emissions, dbt_models])

# Job nommé requis par l'acceptance G.2 #46 verbatim.
# Matérialise les 2 assets bronze + raw dans l'ordre topologique
# (raw dépend de bronze, Dagster gère l'ordre).
# Sélection par groupe : tous les assets `group_name="ingestion_owid"`
# (en B-8.2 : bronze + raw OWID ; robuste à l'ajout futur d'assets
# OWID dans le même groupe en B-8.3+).
ingest_owid_climate = define_asset_job(
    name="ingest_owid_climate",
    selection=AssetSelection.groups("ingestion_owid"),
    description=(
        "Ingestion end-to-end OWID CO2 emissions : "
        "bronze (download + parquet horodaté ADR-0031) → "
        "raw (TRUNCATE+INSERT DuckDB miroir ~70 colonnes). "
        "Acceptance G.2 #46."
    ),
)

# B-8.3 — G.3 #47 — Job dbt run (staging + marts).
# Aucun run_tag : ce job est libre de concurrence.
run_dbt_models_job = define_asset_job(
    name="run_dbt_models_job",
    selection=AssetSelection.assets(dbt_run_models),
    description=(
        "Exécute dbt run sur tous les modèles staging + marts. "
        "B-8.3 G.3 #47."
    ),
)

# B-8.3 — G.4 #48 — Job dbt snapshot.
# run_tag 'dagster/dbt_snapshot' figé verbatim ADR-0033 + dagster.yaml.
# Sérialisé par tag_concurrency_limits (limit=1) côté instance queue.
snapshot_indicateur_job = define_asset_job(
    name="snapshot_indicateur_job",
    selection=AssetSelection.assets(dbt_snapshot_indicateur),
    run_tags={DBT_SNAPSHOT_TAG_KEY: ""},
    description=(
        "Exécute dbt snapshot_indicateur. Run tag "
        f"{DBT_SNAPSHOT_TAG_KEY!r} pour sérialisation queue "
        "(ADR-0033, dagster.yaml). B-8.3 G.4 #48."
    ),
)

# Schedule quotidien 02:00 UTC requis par l'acceptance G.2 #46
# verbatim. Statut par défaut STOPPED : même avec un dagster-daemon
# actif, le schedule ne démarrera pas sans toggle manuel. C'est
# cohérent avec la doctrine MVP « fraîcheur prouvée nécessaire ».
daily_ingest_owid = ScheduleDefinition(
    name="daily_ingest_owid",
    job=ingest_owid_climate,
    cron_schedule="0 2 * * *",
    execution_timezone="UTC",
    default_status=DefaultScheduleStatus.STOPPED,
    description=(
        "Schedule quotidien 02:00 UTC pour ingest_owid_climate. "
        "Statut STOPPED par défaut — à activer manuellement quand "
        "la fraîcheur quotidienne sera prouvée nécessaire (B-8.6+)."
    ),
)

defs = Definitions(
    assets=all_assets,
    jobs=[
        ingest_owid_climate,
        run_dbt_models_job,
        snapshot_indicateur_job,
    ],
    schedules=[daily_ingest_owid],
)
