"""B-8.3 — G.3 #47 — Tests config dbt statiques.

Garantit la non-régression de :
- dbt_project.yml présent + parseable
- profiles.yml présent + profile name aligné
- modèles staging + marts présents au filesystem
- snapshot snapshot_indicateur présent
- test custom assert_indicateur_unique.sql présent
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]


def test_dbt_project_yml_present_and_parseable() -> None:
    """dbt_project.yml existe à la racine et est parseable."""
    path = REPO_ROOT / "dbt_project.yml"
    assert path.exists(), f"{path} absent"
    with path.open() as f:
        cfg = yaml.safe_load(f)
    assert cfg.get("name") == "aporiapolis"
    assert cfg.get("profile") == "aporiapolis"


def test_dbt_profiles_yml_present_and_aligned() -> None:
    """dbt/profiles.yml existe, profile name = 'aporiapolis', target = 'dev'."""
    path = REPO_ROOT / "dbt" / "profiles.yml"
    assert path.exists(), f"{path} absent"
    with path.open() as f:
        cfg = yaml.safe_load(f)
    assert "aporiapolis" in cfg
    assert cfg["aporiapolis"].get("target") == "dev"
    assert "dev" in cfg["aporiapolis"]["outputs"]
    assert cfg["aporiapolis"]["outputs"]["dev"]["type"] == "duckdb"


def test_staging_model_present() -> None:
    """stg_owid__co2_emissions.sql présent."""
    path = REPO_ROOT / "dbt" / "models" / "staging" / "stg_owid__co2_emissions.sql"
    assert path.exists(), f"{path} absent"
    content = path.read_text()
    assert "raw" in content and "owid_co2_emissions" in content


def test_staging_schema_yml_present() -> None:
    """staging/_schema.yml présent + référence raw.owid_co2_emissions."""
    path = REPO_ROOT / "dbt" / "models" / "staging" / "_schema.yml"
    assert path.exists(), f"{path} absent"
    with path.open() as f:
        cfg = yaml.safe_load(f)
    sources = cfg.get("sources", [])
    assert any(s.get("name") == "raw" for s in sources)


def test_marts_indicateur_model_present() -> None:
    """marts/indicateur.sql présent + contient slug 'fr-co2-total-annual'."""
    path = REPO_ROOT / "dbt" / "models" / "marts" / "indicateur.sql"
    assert path.exists(), f"{path} absent"
    content = path.read_text()
    assert "fr-co2-total-annual" in content
    assert "country = 'France'" in content


def test_marts_schema_yml_present() -> None:
    """marts/_schema.yml présent."""
    path = REPO_ROOT / "dbt" / "models" / "marts" / "_schema.yml"
    assert path.exists(), f"{path} absent"


def test_snapshot_indicateur_present() -> None:
    """snapshots/snapshot_indicateur.sql présent + strategy check sur (value, unit, source)."""
    path = REPO_ROOT / "dbt" / "snapshots" / "snapshot_indicateur.sql"
    assert path.exists(), f"{path} absent"
    content = path.read_text()
    assert "strategy='check'" in content or "strategy=\"check\"" in content
    assert "value" in content and "unit" in content and "source" in content


def test_custom_composite_test_present() -> None:
    """dbt/tests/assert_indicateur_unique.sql présent (D8 — test SQL custom)."""
    path = REPO_ROOT / "dbt" / "tests" / "assert_indicateur_unique.sql"
    assert path.exists(), f"{path} absent"
    content = path.read_text()
    # Test attendu : GROUP BY (slug, year, country_iso) HAVING COUNT(*) > 1
    assert "GROUP BY" in content
    assert "HAVING COUNT(*) > 1" in content
    assert "slug" in content and "year" in content and "country_iso" in content


def test_generate_schema_name_macro_keeps_custom_schemas_literal() -> None:
    """Custom schemas must materialize as staging/marts, not main_staging/main_marts."""
    path = REPO_ROOT / "dbt" / "macros" / "generate_schema_name.sql"
    assert path.exists(), f"{path} absent"
    content = path.read_text()
    assert "custom_schema_name | trim" in content
    assert "target.schema ~" not in content


def test_no_dbt_utils_dependency() -> None:
    """D8 acté : pas de packages.yml avec dbt-utils en B-8.3."""
    pkg_path = REPO_ROOT / "packages.yml"
    if pkg_path.exists():
        with pkg_path.open() as f:
            cfg = yaml.safe_load(f) or {}
        pkgs = cfg.get("packages", [])
        for p in pkgs:
            assert "dbt-utils" not in (p.get("package") or "")
    # Si packages.yml absent : test passe trivialement.
