"""Assets Dagster pour l'ingestion OWID CO2 emissions (B-8.2 G.2 #46).

Deux assets chaînés (D1) :

* ``owid_co2_emissions_bronze`` — télécharge le CSV OWID complet
  (full dataset, toutes lignes, toutes colonnes — D2), valide le
  header contre ``expected_source_header`` (fail-fast sur drift exact)
  et écrit un parquet horodaté au path canonique ADR-0031.
* ``raw_owid_co2_emissions`` — lit le parquet bronze le plus récent
  et fait TRUNCATE+INSERT dans ``raw.owid_co2_emissions``
  (transaction explicite — SD7). Miroir 1:1 du bronze (D6 v3,
  conforme doctrine B-8.1 ``docs/dwh/modelisation.md``).

Le path canonique du parquet bronze est défini par ADR-0031 :

    data/bronze/owid/co2_emissions/snapshot_date=YYYY-MM-DD/co2_emissions.parquet

Aucune dépendance à dbt-snapshot ni à ``tag_concurrency_limits`` ici
(cf. SD6 + ADR-0033). Les futurs dbt-snapshots vivront ailleurs.
"""

import io
from datetime import datetime, timezone
from importlib.resources import files
from pathlib import Path
from typing import Any, Mapping

import duckdb
import pyarrow as pa
import pyarrow.csv as pa_csv
import pyarrow.parquet as pq
import requests
import yaml
from dagster import AssetExecutionContext, MetadataValue, Output, asset
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


# ---------------------------------------------------------------------------
# Helpers — config loading + HTTP session + bronze path
# ---------------------------------------------------------------------------


def _load_owid_config() -> Mapping[str, Any]:
    """Charge la config machine OWID depuis le package data YAML."""
    resource = files("aporiapolis.config.sources").joinpath("owid.yaml")
    return yaml.safe_load(resource.read_text(encoding="utf-8"))


def _build_session(http_config: Mapping[str, Any]) -> requests.Session:
    """Construit une Session requests avec timeout + retry exponentiel
    selon les SLOs YAML (SD3)."""
    retry_config = http_config.get("retry", {})
    retry = Retry(
        total=retry_config.get("total", 3),
        backoff_factor=retry_config.get("backoff_factor", 1.0),
        status_forcelist=retry_config.get(
            "status_forcelist", [500, 502, 503, 504]
        ),
        allowed_methods=frozenset(["GET", "HEAD"]),
    )
    adapter = HTTPAdapter(max_retries=retry)
    session = requests.Session()
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session


def _bronze_parquet_path(snapshot_date: str) -> Path:
    """Path canonique ADR-0031 pour le parquet bronze OWID."""
    return Path(
        "data/bronze/owid/co2_emissions"
        f"/snapshot_date={snapshot_date}/co2_emissions.parquet"
    )


def _today_snapshot_date() -> str:
    """Snapshot date du jour en UTC (ADR-0031, format YYYY-MM-DD)."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


# ---------------------------------------------------------------------------
# Header contract — fail-fast sur drift exact (manquante OU ajoutée)
# ---------------------------------------------------------------------------


class OwidHeaderDriftError(RuntimeError):
    """Levée quand le header CSV OWID dérive de expected_source_header.

    Cas (a) : une colonne contractuelle est manquante.
    Cas (b) : une colonne non contractuelle est apparue.
    Dans les deux cas, raw ne peut plus être un miroir 1:1 du bronze
    sans réviser la migration 002 et le YAML.
    """


def _validate_header(
    actual_columns: list[str],
    expected_columns: list[str],
) -> None:
    """Compare deux listes ordonnées et raise OwidHeaderDriftError sur
    différence stricte (ensembliste OU d'ordre).

    Le test `test_owid_header_contract.py` couvre les 2 cas (manquant
    et ajouté).
    """
    actual_set = set(actual_columns)
    expected_set = set(expected_columns)

    missing = expected_set - actual_set
    added = actual_set - expected_set

    if missing or added:
        raise OwidHeaderDriftError(
            "Drift du header CSV OWID vs expected_source_header :\n"
            f"  Colonnes manquantes : {sorted(missing) or '(aucune)'}\n"
            f"  Colonnes ajoutées   : {sorted(added) or '(aucune)'}\n"
            "Action requise : réviser dagster/aporiapolis/config/"
            "sources/owid.yaml + migrations/002_create_raw_owid_co2_"
            "emissions.sql + test_owid_header_contract.py."
        )


# ---------------------------------------------------------------------------
# Asset bronze — download CSV + write parquet horodaté
# ---------------------------------------------------------------------------


@asset(
    name="owid_co2_emissions_bronze",
    group_name="ingestion_owid",
    description=(
        "Télécharge le CSV OWID CO2 emissions complet, valide le "
        "header contre expected_source_header (fail-fast sur drift "
        "exact), écrit un parquet horodaté au path canonique ADR-0031."
    ),
)
def owid_co2_emissions_bronze(context: AssetExecutionContext) -> Output[Path]:
    config = _load_owid_config()
    url = config["url"]
    expected_columns = config["expected_source_header"]
    http_config = config.get("http", {})
    timeout = http_config.get("timeout_seconds", 30)

    session = _build_session(http_config)

    context.log.info(f"Downloading OWID CO2 emissions from {url}")
    response = session.get(url, timeout=timeout)
    response.raise_for_status()
    csv_bytes = response.content

    # Lire le CSV via pyarrow (efficient, validation de schema implicite).
    table = pa_csv.read_csv(io.BytesIO(csv_bytes))

    # Fail-fast sur drift exact du header.
    actual_columns = table.column_names
    _validate_header(actual_columns, expected_columns)

    snapshot_date = _today_snapshot_date()
    parquet_path = _bronze_parquet_path(snapshot_date)
    parquet_path.parent.mkdir(parents=True, exist_ok=True)
    pq.write_table(table, parquet_path)

    context.log.info(
        f"Bronze parquet écrit : {parquet_path} "
        f"({table.num_rows} lignes, {table.num_columns} colonnes)"
    )

    return Output(
        value=parquet_path,
        metadata={
            "snapshot_date": snapshot_date,
            "parquet_path": MetadataValue.path(str(parquet_path)),
            "num_rows": table.num_rows,
            "num_columns": table.num_columns,
            "source_url": url,
        },
    )


# ---------------------------------------------------------------------------
# Asset raw — load parquet bronze → DuckDB raw (TRUNCATE+INSERT atomique)
# ---------------------------------------------------------------------------

DUCKDB_PATH = "data/duckdb/aporiapolis.duckdb"


@asset(
    name="raw_owid_co2_emissions",
    group_name="ingestion_owid",
    description=(
        "Charge le parquet bronze OWID dans raw.owid_co2_emissions "
        "(miroir 1:1, ~70 colonnes, conforme doctrine B-8.1). "
        "TRUNCATE+INSERT dans une transaction DuckDB atomique."
    ),
)
def raw_owid_co2_emissions(
    context: AssetExecutionContext,
    owid_co2_emissions_bronze: Path,
) -> Output[int]:
    # La dépendance vers owid_co2_emissions_bronze est déclarée
    # implicitement par le nom du paramètre (convention Dagster
    # software-defined assets). Pas besoin de deps=[...] explicite.
    parquet_path = owid_co2_emissions_bronze

    context.log.info(
        f"Loading {parquet_path} into raw.owid_co2_emissions (DuckDB)"
    )

    con = duckdb.connect(DUCKDB_PATH)
    try:
        # Transaction explicite — SD7. Atomicité TRUNCATE+INSERT.
        con.execute("BEGIN")
        con.execute("TRUNCATE TABLE raw.owid_co2_emissions")
        con.execute(
            "INSERT INTO raw.owid_co2_emissions "
            "SELECT * FROM read_parquet("
            f"'{parquet_path.as_posix()}', hive_partitioning=false)"
        )
        con.execute("COMMIT")
    except Exception:
        con.execute("ROLLBACK")
        raise
    finally:
        # Compter les rows pour metadata + RESULT.md (capturé Mission F).
        row_count = con.execute(
            "SELECT COUNT(*) FROM raw.owid_co2_emissions"
        ).fetchone()[0]
        con.close()

    context.log.info(
        f"raw.owid_co2_emissions peuplée : {row_count} lignes "
        "(TRUNCATE+INSERT transactionnel)"
    )

    return Output(
        value=row_count,
        metadata={
            "row_count": row_count,
            "source_parquet": MetadataValue.path(str(parquet_path)),
            "duckdb_path": MetadataValue.path(DUCKDB_PATH),
        },
    )
