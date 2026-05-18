"""B-8.3 — G.4 #48 — Tests pytest config Dagster concurrency.

Garantit que :
- dagster.yaml existe + contient run_queue + tag_concurrency_limits key
  'dagster/dbt_snapshot' limit=1.
- defs.resolve_job_def('snapshot_indicateur_job').run_tags ==
  {'dagster/dbt_snapshot': ''} (D9, H10 — pas op_tags asset).
- Le job run_dbt_models_job n'a PAS de run_tag (preuve de
  non-régression sur les jobs libres).

Ces tests sont STATIQUES (config + résolution de Definitions). La
preuve de sérialisation effective via daemon vit dans
scripts/test_concurrency.sh + RESULT.md Mission K (D9 — preuve post-hoc).
Tech-debt P3 ouverte pour upgrade pytest e2e quand 2e snapshot existera.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]

DBT_SNAPSHOT_TAG_KEY = "dagster/dbt_snapshot"


def test_dagster_yaml_present() -> None:
    """dagster.yaml existe à la racine du repo (D7)."""
    path = REPO_ROOT / "dagster.yaml"
    assert path.exists(), f"{path} absent"


def test_dagster_yaml_has_run_queue_and_tag_concurrency_limits() -> None:
    """dagster.yaml contient run_queue + tag_concurrency_limits clé+limit (D9, SD6)."""
    path = REPO_ROOT / "dagster.yaml"
    with path.open() as f:
        cfg = yaml.safe_load(f)

    # (1) run_queue: {} — active QueuedRunCoordinator par raccourci.
    assert "run_queue" in cfg, "run_queue manquant dans dagster.yaml"
    assert cfg["run_queue"], (
        "run_queue ne doit pas être vide : Dagster 1.13.5 teste ce bloc "
        "par truthiness avant d'instancier QueuedRunCoordinator."
    )

    # (2) concurrency.runs.tag_concurrency_limits avec key + limit.
    concurrency = cfg.get("concurrency") or {}
    runs_concurrency = concurrency.get("runs") or {}
    limits = runs_concurrency.get("tag_concurrency_limits") or []

    matching = [
        lim
        for lim in limits
        if lim.get("key") == DBT_SNAPSHOT_TAG_KEY
    ]
    assert matching, (
        f"tag_concurrency_limits key={DBT_SNAPSHOT_TAG_KEY!r} manquant."
    )
    assert matching[0].get("limit") == 1, (
        f"limit attendu=1, observé={matching[0].get('limit')}"
    )


def test_snapshot_job_has_run_tags() -> None:
    """run_tags du job snapshot_indicateur_job verbatim (D9, H10)."""
    # Import diff�r� pour �viter de planter le test suite si Definitions
    # casse — meilleur message d'erreur en cas de drift.
    from aporiapolis import defs

    job = defs.resolve_job_def("snapshot_indicateur_job")
    run_tags = dict(job.run_tags)
    assert run_tags == {DBT_SNAPSHOT_TAG_KEY: ""}, (
        f"run_tags attendu={{{DBT_SNAPSHOT_TAG_KEY!r}: ''}}, "
        f"observé={run_tags}"
    )
    assert dict(job.tags) == {DBT_SNAPSHOT_TAG_KEY: ""}, (
        "Dagster 1.13.5 `dagster job launch` propage `tags` dans les "
        f"runs ; attendu={{{DBT_SNAPSHOT_TAG_KEY!r}: ''}}, "
        f"observé={dict(job.tags)}"
    )


def test_run_dbt_models_job_has_no_concurrency_tag() -> None:
    """run_dbt_models_job ne porte PAS le tag dbt_snapshot (non-régression)."""
    from aporiapolis import defs

    job = defs.resolve_job_def("run_dbt_models_job")
    run_tags = dict(job.run_tags)
    assert DBT_SNAPSHOT_TAG_KEY not in run_tags, (
        f"run_dbt_models_job NE doit PAS porter {DBT_SNAPSHOT_TAG_KEY!r} "
        f"(observé : {run_tags})"
    )


def test_definitions_contain_dbt_assets() -> None:
    """Les 2 nouveaux assets sont enregistrés dans Definitions."""
    from aporiapolis import defs

    asset_keys = {
        str(k) for k in defs.resolve_asset_graph().get_all_asset_keys()
    }
    # On vérifie la présence des deux nouvelles clés sans figer le
    # format exact d'AssetKey (qui peut varier selon les versions
    # Dagster).
    has_dbt_run = any("dbt_run_models" in k for k in asset_keys)
    has_dbt_snapshot = any("dbt_snapshot_indicateur" in k for k in asset_keys)
    assert has_dbt_run, f"asset dbt_run_models manquant. Keys: {asset_keys}"
    assert has_dbt_snapshot, (
        f"asset dbt_snapshot_indicateur manquant. Keys: {asset_keys}"
    )


def test_instance_uses_queued_run_coordinator(monkeypatch: pytest.MonkeyPatch) -> None:
    """DAGSTER_HOME repo root instancie bien QueuedRunCoordinator (preuve #48)."""
    from dagster import DagsterInstance

    monkeypatch.setenv("DAGSTER_HOME", str(REPO_ROOT))
    inst = DagsterInstance.get()
    assert type(inst.run_coordinator).__name__ == "QueuedRunCoordinator"
