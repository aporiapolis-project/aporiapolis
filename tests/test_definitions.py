"""Test des Definitions Dagster AporiaPolis.

Vérifie l'acceptance G.2 #46 verbatim :

- Job nommé ``ingest_owid_climate`` existe.
- ``ScheduleDefinition`` ``daily_ingest_owid`` existe avec
  ``cron_schedule="0 2 * * *"`` et ``execution_timezone="UTC"``.
- Les 2 assets bronze et raw sont déclarés.

Ne lance pas d'exécution. Ne nécessite pas Internet.
"""

from __future__ import annotations

import pytest


@pytest.fixture
def defs():
    """Charge les Definitions du module aporiapolis."""
    from aporiapolis import defs as aporiapolis_defs

    return aporiapolis_defs


def test_job_ingest_owid_climate_exists(defs) -> None:
    """Acceptance G.2 #46 — job nommé ingest_owid_climate."""
    job = defs.get_job_def("ingest_owid_climate")
    assert job is not None, "Job 'ingest_owid_climate' doit exister"
    assert job.name == "ingest_owid_climate"


def test_schedule_daily_ingest_owid_exists(defs) -> None:
    """Acceptance G.2 #46 — schedule quotidien 02:00 UTC."""
    schedule = defs.get_schedule_def("daily_ingest_owid")
    assert schedule is not None, "Schedule 'daily_ingest_owid' doit exister"


def test_schedule_cron_and_timezone(defs) -> None:
    """Le cron est bien 02:00 UTC tous les jours."""
    schedule = defs.get_schedule_def("daily_ingest_owid")
    assert schedule.cron_schedule == "0 2 * * *", (
        f"Cron attendu '0 2 * * *', reçu {schedule.cron_schedule!r}"
    )
    assert schedule.execution_timezone == "UTC", (
        f"Timezone attendu 'UTC', reçu {schedule.execution_timezone!r}"
    )


def test_schedule_default_status_stopped(defs) -> None:
    """Le schedule est déclaré STOPPED par défaut (D5 + doctrine MVP
    « fraîcheur prouvée nécessaire »)."""
    from dagster import DefaultScheduleStatus

    schedule = defs.get_schedule_def("daily_ingest_owid")
    assert schedule.default_status == DefaultScheduleStatus.STOPPED, (
        "Schedule doit être STOPPED par défaut (MVP B-8.2)"
    )


def test_bronze_and_raw_assets_declared(defs) -> None:
    """Les 2 assets chaînés (D1) sont déclarés."""
    asset_graph = defs.resolve_asset_graph()
    asset_keys = {key.to_user_string() for key in asset_graph.get_all_asset_keys()}
    assert "owid_co2_emissions_bronze" in asset_keys, "Asset bronze doit être déclaré"
    assert "raw_owid_co2_emissions" in asset_keys, "Asset raw doit être déclaré"


def test_no_tag_concurrency_limits_in_definitions(defs) -> None:
    """SD6 — aucune trace de tag_concurrency_limits dans Definitions.

    tag_concurrency_limits vit dans dagster.yaml (instance), pas
    dans Python Definitions. Cf. ADR-0033.
    """
    import inspect

    import aporiapolis

    source = inspect.getsource(aporiapolis)
    assert "tag_concurrency_limits" not in source, (
        "Definitions ne doivent pas contenir tag_concurrency_limits "
        "(SD6 + ADR-0033 — config d'instance, pas Definitions)"
    )
