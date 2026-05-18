# Source card — Our World in Data (OWID), dataset CO2 emissions

> **Statut** : carte source initiale créée le 2026-05-17 dans le cadre du brief B-8.0 (rebaselining doctrinaire pré-EPIC G). Validée Sam au merge de la PR `docs/rebaselining-doctrinaire-pre-b8`.
>
> **Référence doctrine** : `CLAUDE.md §1 Gate 2 — Source contract`. Cette carte est le contrat préalable obligatoire à toute ingestion de la source OWID dans le DWH AporiaPolis.
>
> **Ingestion réalisée B-8.2** : pipeline Dagster `ingest_owid_climate` (story #46 [G.2]) — bronze parquet local (cf. ADR-0031), raw DuckDB `raw.owid_co2_emissions` miroir 1:1 (79 colonnes, 50 411 lignes).
> **Transformation réalisée B-8.3** : staging DuckDB `staging.stg_owid__co2_emissions` (projection contractuelle), mart DuckDB `marts.indicateur` (contrat figé, slug `fr-co2-total-annual`, 217 lignes France 1802-2024 dans le snapshot OWID courant), snapshot DuckDB `audit_log.snapshot_indicateur` (strategy `check`).

## 1. Identité de la source

- **Nom canonique** : Our World in Data (OWID).
- **Organisation** : Global Change Data Lab (UK registered charity, n° 1186433).
- **URL projet** : https://ourworldindata.org/
- **Repo de référence (datasets)** : https://github.com/owid/co2-data
- **Contact** : info@ourworldindata.org (mentions légales du site).

## 2. Dataset précis

- **Nom du dataset** : CO2 and Greenhouse Gas Emissions.
- **URL canonique CSV** : https://github.com/owid/co2-data/raw/master/owid-co2-data.csv
  - **À reconfirmer en Mission 0 de B-8.2** (l'URL peut bouger ; alternative possible `https://github.com/owid/co2-data/blob/master/owid-co2-data.csv?raw=true`).
- **Codebook officiel** : https://github.com/owid/co2-data/blob/master/owid-co2-codebook.csv
- **Format** : CSV UTF-8, séparateur virgule, header en première ligne.
- **Encoding attendu** : UTF-8 (ASCII pour la majorité des colonnes ; quelques accents possibles dans noms de pays type `Côte d'Ivoire`).

## 3. Auteur·rices et primary sources

OWID agrège plusieurs sources primaires. Pour le dataset CO2 :

- **Global Carbon Budget** (Friedlingstein et al., 2024) — émissions territoriales, méthodologie principale.
- **Energy Institute Statistical Review of World Energy** — consommation énergétique et émissions énergétiques.
- **Population** : OWID basé sur HYDE, Gapminder, et UN World Population Prospects.

L'attribution doit toujours pointer **vers les primary sources via OWID**, pas seulement vers OWID. AporiaPolis affichera typiquement « Source : OWID — Global Carbon Budget 2024 ».

## 4. Licence et conformité d'usage

- **Licence des données** : Creative Commons BY 4.0 (CC BY 4.0).
  - Texte officiel : https://creativecommons.org/licenses/by/4.0/
  - Confirmé sur https://ourworldindata.org/owid-faqs#how-is-our-work-copyrighted (consulté 2026-05-17).
- **Conditions d'usage** :
  - Attribution obligatoire : citer OWID + la source primaire (cf. §3).
  - Aucune restriction commerciale ou de redistribution.
  - Aucune restriction de modification (transformations dbt autorisées).
- **Conformité usage AporiaPolis** : compatible AGPL-3.0 du projet. Aucune contradiction avec ADR-0021 (audit personnel local-only), ADR-0022 (rétention presse), ADR-0023 (org publique), ADR-0029 (droit de réponse).
- **Mentions légales obligatoires côté AporiaPolis** :
  - Page méthodologie : citer OWID + Global Carbon Budget + lien CC BY 4.0.
  - Footer de la page démonstrateur (B-8.5) : mention courte « Source : OWID, CC BY 4.0 ».
  - Code source : commentaire `# Source: OWID (CC BY 4.0) — https://ourworldindata.org/co2-emissions` en tête des assets Dagster et modèles dbt qui consomment cette source.

## 5. Schéma attendu

Le CSV OWID contient ~70 colonnes (cf. codebook). Pour B-8 (slice CO2 emissions FR total annuel — slug `fr-co2-total-annual`), les colonnes utiles minimales :

| Colonne CSV | Type | Description |
|---|---|---|
| `country` | text | Nom du pays (canonique anglais — « France » pour FR). |
| `iso_code` | text | Code ISO-3166-1 alpha-3 (« FRA » pour France). Nullable pour les agrégats régionaux. |
| `year` | integer | Année (4 chiffres). Couverture observée : 1750 à année courante - 1 (typiquement 2024 en 2026). |
| `co2` | numeric | Émissions annuelles de CO2 (Mt). Inclut émissions énergétiques + ciment + flaring. Exclut LUCF. |
| `co2_per_capita` | numeric | Émissions de CO2 par habitant (tCO2/hab/an). |
| `population` | numeric | Population totale du pays année N. |
| `source` | (dérivée) | Pour AporiaPolis : « OWID/Global Carbon Budget 2024 » par défaut. |

**Schéma cible silver** (B-8.2 ingestion + B-8.3 staging) : conserver les colonnes ci-dessus + `_ingested_at` (timestamp d'ingestion) + `_source_url` (URL CSV au moment de l'ingestion). Renommage en snake_case standard.

**Schéma cible mart** (B-8.3 — implémenté, cf. ADR-0031 §"contrat dbt
staging+mart" + D6 brief B-8.3) :

```
marts.indicateur
├── slug         text     not null  -- ex: 'fr-co2-total-annual'
├── year         integer  not null
├── value        numeric  not null  -- valeur en unité indiquée par 'unit'
├── unit         text     not null  -- 'Mt CO2'
├── source       text     not null  -- 'OWID/Global Carbon Budget 2024'
├── country_iso  text               -- 'FRA' (nullable pour agrégats globaux)
└── PK (slug, year, country_iso)
```

Nom générique `indicateur` (singulier) — le mart accueillera plusieurs
slugs au fil des slices EPIC G futurs (un slug = une question
éditoriale instrumentée). En B-8.3, un seul slug
(`fr-co2-total-annual`), 217 lignes observées dans le snapshot OWID
courant (France 1802-2024).

Test composite unique `(slug, year, country_iso)` via test SQL custom
dbt natif (`dbt/tests/assert_indicateur_unique.sql`). D8 brief
B-8.3 — pas de dépendance `dbt-utils` pour un seul invariant.

## 6. Granularité, fraîcheur, fréquence

- **Granularité spatiale** : pays (`iso_code` ISO-3 ou agrégats régionaux/mondiaux nommés).
- **Granularité temporelle** : annuelle (`year` ; pas de précision intra-année).
- **Couverture France** : continue depuis 1750. Anomalies historiques connues pour les années pre-1900 (estimations).
- **Fraîcheur observée 2026-05-17** : dernière année avec données complètes = **2024** (l'année 2025 n'est en général publiée par Global Carbon Budget qu'en fin d'année 2025 / début 2026).
  - **À reconfirmer en Mission 0 de B-8.2** par lecture du CSV au moment de l'ingestion : `max(year)` côté `country='France'` doit être ≥ 2024.
- **Fréquence de mise à jour upstream** : OWID met à jour `owid-co2-data.csv` au gré des releases Global Carbon Budget (annuelles, généralement décembre).
- **Schedule d'ingestion AporiaPolis** : quotidien 02:00 UTC en config Dagster (cf. acceptance G.2 verbatim). En MVP local, le schedule est défini mais inactif (`dagster dev` à la main).

## 7. Conformité technique et juridique

### robots.txt et accès programmatique

- **GitHub raw URL** : pas de robots.txt restrictif applicable au téléchargement automatisé. Pas de rate limiting documenté pour les fichiers raw publics individuels.
  - À surveiller en pratique : un download quotidien d'un CSV ~7 Mo est largement sous tout seuil de rate limiting GitHub (5000 req/h non-authentifiés sur API ; bien plus pour les raw files).
- **Pas d'authentification requise** pour le téléchargement.
- **Pas de scraping** : on télécharge un fichier CSV publié, pas de parsing HTML.

### Mentions légales OWID

OWID demande l'attribution mais ne requiert pas d'enregistrement préalable. Aucune CLA ou TOS spécifique à signer.

### RGPD / données personnelles

- **Aucune donnée personnelle** dans le dataset CO2 (agrégats nationaux annuels).
- **Pas de DPIA** requise (cf. CLAUDE.md §3 footer `DPIA: oui` non applicable).
- Le footer de commit pour ingestion OWID restera `DPIA: non` (implicite, pas besoin de footer explicite).

### Stockage AporiaPolis

- **Bronze MVP local** : parquet horodaté dans `data/bronze/owid/co2_emissions/snapshot_date=YYYY-MM-DD/co2_emissions.parquet` (cf. ADR-0031).
- **Silver/Mart MVP local** : DuckDB `data/duckdb/aporiapolis.duckdb`.
- **Prod (EPIC B)** : JSON brut dans Object Storage Scaleway + Postgres managé, conformément à `CLAUDE.md §2` et à l'acceptance verbatim G.2 originale.
- **Rétention bronze** : tous les snapshots conservés en MVP (volume négligeable, ~7 Mo × 365 ≈ 2,5 Go/an). Politique de rétention à formaliser en EPIC B.

## 8. Risques et signaux à surveiller

- **Changement d'URL canonique** : OWID a déjà migré ses datasets (de `ourworldindata.org/grapher/...` vers le repo GitHub `owid/co2-data`). Une nouvelle migration n'est pas exclue. Mitigation : Mission 0 de toute ré-ingestion vérifie l'URL via une requête HEAD.
- **Changement de schéma CSV** : Global Carbon Budget peut ajouter/renommer/supprimer des colonnes. Le pipeline doit tester explicitement la présence des colonnes utiles (cf. §5) en début d'ingestion et fail-fast si schéma divergent.
- **Changement de licence** : peu probable (CC BY 4.0 est l'engagement OWID public depuis 2015+), mais à surveiller annuellement.
- **Erreurs upstream** : Global Carbon Budget publie occasionnellement des révisions de données historiques (recalculs méthodologiques). La fraîcheur d'une année déjà ingérée peut donc varier dans le temps. Mitigation : ingérer en plein chaque jour (pas d'incrémental sur cette source), accepter les révisions silencieuses.
- **Disponibilité GitHub** : pas de SLA contractuel sur les raw URL. Mitigation : retry exponentiel dans l'asset Dagster, alerte si plusieurs échecs consécutifs.

## 9. Cohérence doc ↔ config machine (test obligatoire)

Cette source card est la **doc publique humaine** (Markdown, lecture éditoriale, validée Sam). Le pipeline Dagster lit son URL et son schéma depuis une **config machine** distincte qui sera créée en B-8.2 :

- Path attendu : `dagster/aporiapolis/config/sources/owid.yaml` (ou équivalent).
- Sera référencé par `# ADR-0031` en commentaire.

**Test de cohérence** à créer en B-8.2 (`tests/test_sources_consistency.py` ou pre-commit hook) :

```python
def test_owid_doc_and_config_consistency():
    """L'URL canonique et la licence doivent être identiques côté doc publique
    et côté config machine."""
    doc = parse_source_card("docs/sources/owid.md")
    cfg = parse_source_config("dagster/aporiapolis/config/sources/owid.yaml")
    assert doc["canonical_url"] == cfg["url"]
    assert doc["license"] == cfg["license"]
```

Ce test garantit que la doc publique (ce fichier) et la config exécutée (yaml) ne dérivent jamais. Cf. correction Codex #3 : « ne fais pas de la source card un fichier de config runtime ».

## 10. Versionnement et révisions de cette carte

| Version | Date | Auteur | Modifications |
|---|---|---|---|
| v0.1 | 2026-05-17 | sam + cowork | Création initiale dans le cadre du brief B-8.0 (rebaselining doctrinaire pré-EPIC G). |
| v0.2 | 2026-05-18 | sam + cowork | B-8.3 — Alignement §5 sur le nom de mart effectivement implémenté : `marts.indicateur` (générique, plusieurs slugs) au lieu de l'ancien nom spécifique CO2. PK composite `(slug, year, country_iso)`. Test composite via SQL custom dbt natif (pas `dbt-utils`, D8). Count observé : 217 lignes France 1802-2024 pour le slug `fr-co2-total-annual`. |

Toute évolution future (URL changée, schéma divergent, licence évoluée) doit ajouter une ligne à ce tableau et un comment-trail sur l'issue de l'ingestion correspondante.

<!--
Conventions :
- Carte source créée pendant le brief B-8.0 (Rain Razor/briefs/2026-05-17-slice-owid-e2e-00-rebaselining-doctrinaire/).
- Référence Gate 2 doctrine (CLAUDE.md §1).
- À mettre à jour si OWID change d'URL, de schéma, ou de licence.
-->
