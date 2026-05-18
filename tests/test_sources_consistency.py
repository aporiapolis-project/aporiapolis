"""Test de cohérence source card (doc humaine) ↔ YAML config (machine).

Compare uniquement les **champs publics communs** :

- URL canonique du téléchargement
- Licence

Les SLOs HTTP (timeout, retry) restent machine-only dans le YAML et
ne sont **pas** comparés ici (corrigé v2.2 après audit Sam : la source
card n'a pas de valeurs SLOs exactes — comparer aurait fait mentir
le test).

Les colonnes contractuelles ne sont pas comparées ici non plus : la
source card liste des colonnes utiles silver (cibles staging B-8.3),
le YAML liste expected_source_header (contrat raw miroir). Deux choses
différentes. La projection contractuelle silver apparaîtra en B-8.3.
"""

from __future__ import annotations

import re
from importlib.resources import files
from pathlib import Path

import pytest
import yaml


SOURCE_CARD_PATH = Path("docs/sources/owid.md")


def _load_yaml_config() -> dict:
    resource = files("aporiapolis.config.sources").joinpath("owid.yaml")
    return yaml.safe_load(resource.read_text(encoding="utf-8"))


def _extract_field_from_source_card(field: str) -> str | None:
    """Extrait un champ depuis docs/sources/owid.md.

    Convention de parsing (à ajuster Mission 0 si format diffère) :

    - Champ inline ``- **URL** : <value>`` ou ``URL : <value>``
    - Champ inline ``- **Licence** : <value>`` ou ``Licence : <value>``

    Retourne None si introuvable.
    """
    if not SOURCE_CARD_PATH.exists():
        return None

    text = SOURCE_CARD_PATH.read_text(encoding="utf-8")

    # Cherche `**<field>**` ou `<field> :` (case-insensitive)
    patterns = [
        rf"\*\*{re.escape(field)}\*\*\s*[:\-]?\s*(.+?)$",
        rf"^{re.escape(field)}\s*:\s*(.+?)$",
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.MULTILINE | re.IGNORECASE)
        if match:
            return match.group(1).strip()
    return None


@pytest.fixture
def yaml_config() -> dict:
    return _load_yaml_config()


@pytest.fixture
def source_card_text() -> str:
    if not SOURCE_CARD_PATH.exists():
        pytest.skip(f"Source card absente : {SOURCE_CARD_PATH}")
    return SOURCE_CARD_PATH.read_text(encoding="utf-8")


def test_yaml_config_loads(yaml_config: dict) -> None:
    """Sanity : le YAML est parsable et a les champs requis."""
    assert "url" in yaml_config, "YAML doit déclarer 'url'"
    assert "licence" in yaml_config, "YAML doit déclarer 'licence'"
    assert "expected_source_header" in yaml_config, (
        "YAML doit déclarer 'expected_source_header'"
    )
    assert len(yaml_config["expected_source_header"]) > 50, (
        "expected_source_header doit lister ~70 colonnes OWID"
    )


def test_url_consistent_card_to_yaml(
    yaml_config: dict, source_card_text: str
) -> None:
    """L'URL canonique du YAML doit apparaître dans la source card."""
    yaml_url = yaml_config["url"]
    assert yaml_url in source_card_text, (
        f"URL YAML ({yaml_url}) introuvable dans {SOURCE_CARD_PATH}. "
        "Drift entre la doc humaine et la config machine."
    )


def test_licence_consistent_card_to_yaml(
    yaml_config: dict, source_card_text: str
) -> None:
    """La licence du YAML doit apparaître dans la source card.

    Comparaison textuelle insensible à la casse (CC BY 4.0 vs cc by 4.0).
    """
    yaml_licence = yaml_config["licence"]
    assert yaml_licence.lower() in source_card_text.lower(), (
        f"Licence YAML ({yaml_licence}) introuvable dans "
        f"{SOURCE_CARD_PATH}. Drift entre la doc humaine et la config "
        "machine."
    )
