# AporiaPolis

> Outil de réflexion individuelle assistée par la data sur les controverses politiques françaises — méthodologie publique, code ouvert.

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](LICENSE)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org)

## Pitch

AporiaPolis produit des **dossiers thématiques** sur les controverses politiques françaises (médias, dette publique, etc.) construits sur des sources publiques traçables. Chaque dossier expose les sous-questions structurantes, les angles de lecture, les **tests de réalité** (confirmé / partiel / réfuté / non concluant) et les positions historisées des partis. Un module d'**audit personnel** (architecture local-only, calcul côté navigateur, aucune donnée transmise au serveur) permet à chacun·e de confronter ses propres positions au paysage politique.

Le projet est **open source** (AGPL-3.0), **piloté publiquement** (issues, Project, ADR visibles), et **méthodologiquement défendable** : comité de relecture pluraliste, sources versionnées en SCD2, accessibilité RGAA AA dès la conception, reproductibilité bout en bout (`make reproduce` régénère 100 % des chiffres publiés).

## Statut

`pre-mvp` · phase **T1 (Fondations)** · première publication cible **fin T2 / début T3** (dossier *Médias*).

## Architecture résumée

- **MVP local (T1-T2 2026)** : DuckDB + parquet local, Dagster,
  modèles dbt, FastAPI, Svelte 5 en CSR islands. Voir ADR-0031
  (stratégie stockage MVP) et ADR-0032 (mode rendu CSR).
- **Prod cible (V2+)** : Postgres + Object Storage (Scaleway),
  même surface applicative, migration sans réécriture grâce aux
  types SQL portables. Voir ADR-0031 et EPIC B (infrastructure).
- **Ingestion** : Dagster orchestre les pipelines bronze → raw →
  staging/marts via dbt.
- **DWH** : DuckDB en MVP local, Postgres managé Scaleway en prod cible,
  modélisation dimensionnelle avec SCD2 pour les positions partis et acteurs.
- **API** : FastAPI publique read-only, OpenAPI 3.1 auto.
- **Front public** : Astro 5, accessibility-first (axe-core 0 défaut niveau A).
- **Audit personnel** : SPA Svelte, *calcul intégralement côté navigateur*, aucune persistance serveur.
- **Hébergement** : Scaleway (DEV1-M + Postgres managé), Cloudflare en front, Caddy reverse proxy.

## Décisions structurantes (ADR)

- [ADR-0021 — Architecture autorisée pour l'audit personnel](docs/adr/0021-audit-personnel-architecture.md) · local-only, aucune donnée article 9 RGPD traitée par le projet.
- [ADR-0022 — Doctrine de rétention des corpus de presse et procédure Common Crawl](docs/adr/0022-doctrine-retention-presse.md) · destruction post-fouille, aucun bronze persistant pour la presse.
- [ADR-0023 — Configuration GitHub publique](docs/adr/0023-github-organisation-publique.md) · organisation publique, issue types, Project public, labels réduits.
- [ADR-0024 — Doctrine de relecture en deux strates](docs/adr/0024-doctrine-relecture-deux-strates.md) · strate 1 IA personae (interne), strate 2 comité humain (publique).
- [ADR-0030 — Doctrine de release pre-MVP](docs/adr/0030-doctrine-release-pre-mvp.md) · `release-please` avec PR ouverte sur `main`, premier tag différé jusqu'au premier artefact MVP.
- [ADR-0031 — Stratégie stockage MVP (DuckDB+parquet local / Postgres prod)](docs/adr/0031-strategie-stockage-mvp.md)
- [ADR-0032 — Mode rendu CSR islands Svelte 5](docs/adr/0032-csr-islands-svelte5.md)
- [ADR-0033 — Concurrency des dbt-snapshots dans Dagster](docs/adr/0033-concurrency-dbt-snapshots.md)

## Démarrer

Voir le [backlog](https://github.com/aporiapolis-project/aporiapolis/issues?q=is%3Aopen+label%3Aepic) pour suivre l'avancement.

### Ingestion (état post-B-8.2)

Premier pipeline d'ingestion implémenté : **OWID CO2 emissions**.

- **Asset bronze** `owid_co2_emissions_bronze` : télécharge le CSV
  OWID complet (79 colonnes), valide le header contre un contrat
  YAML (fail-fast sur drift), écrit un parquet horodaté à
  `data/bronze/owid/co2_emissions/snapshot_date=YYYY-MM-DD/co2_emissions.parquet`.
- **Asset raw** `raw_owid_co2_emissions` : charge le parquet dans
  la table DuckDB `raw.owid_co2_emissions` (miroir 1:1).
- **Job nommé** `ingest_owid_climate` matérialise les 2 assets.
- **Schedule déclaratif** `daily_ingest_owid` (02:00 UTC,
  `default_status=STOPPED`) — déclaratif, non actif sans
  `dagster-daemon` lancé.

Démonstration end-to-end (env frais) :

```bash
rm -rf data/duckdb data/bronze .venv && make demo-ingest
```

Voir `docs/sources/owid.md` (source card humaine),
`dagster/aporiapolis/config/sources/owid.yaml` (config machine),
et ADR-0031 / ADR-0033.

## Contribuer

Lire [CONTRIBUTING.md](CONTRIBUTING.md), puis ouvrir une issue avant de coder. Tout commit doit respecter [Conventional Commits](https://www.conventionalcommits.org/). Les footers `IA-assistance:` et `Validation:` sont recommandés (convention de traçabilité, enforcement prévu post-MVP).

## Code de conduite

Voir [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Le désaccord politique de fond est bienvenu s'il est argumenté.

## Sécurité

Voir [SECURITY.md](SECURITY.md) — divulgation responsable via un **GitHub Security Advisory privé**.

## Licence

[AGPL-3.0](LICENSE) — usage libre, modifications redistribuées sous la même licence, y compris pour les usages en service réseau.
