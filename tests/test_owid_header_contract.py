"""Test du contrat header CSV OWID ↔ YAML expected_source_header.

Trois cas couverts :

(a) mock CSV avec colonne **manquante** → asset bronze raise
    ``OwidHeaderDriftError``
(b) mock CSV avec colonne **ajoutée** → asset bronze raise
    ``OwidHeaderDriftError``
(c) **alignement source of truth** : la migration 002 SQL contient
    les mêmes colonnes que ``expected_source_header`` du YAML
    (pas de drift entre les deux miroirs du contrat).

Le YAML est la source of truth ; la migration SQL et le test
dérivent.
"""

from __future__ import annotations

import re
from importlib.resources import files
from pathlib import Path

import pytest
import yaml


MIGRATION_PATH = Path("migrations/002_create_raw_owid_co2_emissions.sql")


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def expected_columns() -> list[str]:
    """Charge expected_source_header depuis le YAML (source of truth)."""
    resource = files("aporiapolis.config.sources").joinpath("owid.yaml")
    data = yaml.safe_load(resource.read_text(encoding="utf-8"))
    return list(data["expected_source_header"])


@pytest.fixture
def validator():
    """Importe le validateur de header depuis le module assets."""
    from aporiapolis.assets.owid_co2_emissions import (
        OwidHeaderDriftError,
        _validate_header,
    )

    return _validate_header, OwidHeaderDriftError


# ---------------------------------------------------------------------------
# Cas (a) — colonne contractuelle manquante
# ---------------------------------------------------------------------------


def test_missing_column_raises(validator, expected_columns: list[str]) -> None:
    _validate_header, OwidHeaderDriftError = validator

    # Header avec la dernière colonne retirée → manquante
    actual = expected_columns[:-1]

    with pytest.raises(OwidHeaderDriftError) as exc_info:
        _validate_header(actual, expected_columns)

    assert "manquantes" in str(exc_info.value).lower(), (
        "Le message d'erreur doit mentionner les colonnes manquantes"
    )


# ---------------------------------------------------------------------------
# Cas (b) — colonne non contractuelle ajoutée
# ---------------------------------------------------------------------------


def test_added_column_raises(validator, expected_columns: list[str]) -> None:
    _validate_header, OwidHeaderDriftError = validator

    # Header avec une colonne supplémentaire non attendue
    actual = list(expected_columns) + ["new_owid_column_2026"]

    with pytest.raises(OwidHeaderDriftError) as exc_info:
        _validate_header(actual, expected_columns)

    assert "ajoutées" in str(exc_info.value).lower(), (
        "Le message d'erreur doit mentionner les colonnes ajoutées"
    )


def test_exact_match_passes(validator, expected_columns: list[str]) -> None:
    _validate_header, OwidHeaderDriftError = validator

    # Identique → ne raise pas
    _validate_header(list(expected_columns), expected_columns)


# ---------------------------------------------------------------------------
# Cas (c) — alignement migration 002 SQL ↔ YAML
# ---------------------------------------------------------------------------


def _extract_sql_columns(sql_text: str) -> list[str]:
    """Extrait les noms de colonnes d'un CREATE TABLE basique.

    Heuristique : lignes du type ``    column_name TYPE`` à
    l'intérieur du bloc ``CREATE TABLE ... (...)``. Ignore les lignes
    commentaires et la ligne de fermeture ``)``.
    """
    # Isoler le bloc entre ( et );
    match = re.search(r"CREATE\s+TABLE[^(]*\((.*?)\);", sql_text, re.S | re.I)
    if not match:
        return []
    body = match.group(1)

    columns = []
    for raw_line in body.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("--"):
            continue
        # Première occurrence d'un identifiant Python-style
        col_match = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)", line)
        if col_match:
            columns.append(col_match.group(1))
    return columns


def test_migration_columns_match_yaml(
    expected_columns: list[str],
) -> None:
    if not MIGRATION_PATH.exists():
        pytest.skip(f"Migration 002 absente : {MIGRATION_PATH}")

    sql_text = MIGRATION_PATH.read_text(encoding="utf-8")
    sql_columns = _extract_sql_columns(sql_text)

    sql_set = set(sql_columns)
    yaml_set = set(expected_columns)

    only_in_sql = sql_set - yaml_set
    only_in_yaml = yaml_set - sql_set

    assert not only_in_sql and not only_in_yaml, (
        "Drift entre migration 002 SQL et YAML "
        "expected_source_header.\n"
        f"  Colonnes uniquement dans SQL : {sorted(only_in_sql) or '(aucune)'}\n"
        f"  Colonnes uniquement dans YAML : {sorted(only_in_yaml) or '(aucune)'}\n"
        "Le YAML est la source of truth — corriger la migration SQL."
    )
