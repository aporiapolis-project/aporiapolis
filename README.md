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

- **Ingestion** : Dagster orchestre les pipelines vers Postgres (bronze → silver → gold via dbt).
- **DWH** : Postgres managé Scaleway, modélisation dimensionnelle avec SCD2 pour les positions partis et acteurs.
- **API** : FastAPI publique read-only, OpenAPI 3.1 auto.
- **Front public** : Astro 5, accessibility-first (axe-core 0 défaut niveau A).
- **Audit personnel** : SPA Svelte, *calcul intégralement côté navigateur*, aucune persistance serveur.
- **Hébergement** : Scaleway (DEV1-M + Postgres managé), Cloudflare en front, Caddy reverse proxy.

## Décisions structurantes (ADR)

- [ADR-0021 — Architecture autorisée pour l'audit personnel](docs/adr/0021-audit-personnel-architecture.md) · local-only, aucune donnée article 9 RGPD traitée par le projet.
- [ADR-0022 — Doctrine de rétention des corpus de presse et procédure Common Crawl](docs/adr/0022-doctrine-retention-presse.md) · destruction post-fouille, aucun bronze persistant pour la presse.
- [ADR-0023 — Configuration GitHub publique](docs/adr/0023-github-organisation-publique.md) · organisation publique, issue types, Project public, labels réduits.

## Démarrer

> Le squelette de services est posé mais les pipelines ne sont pas encore implémentés. Voir le [backlog](https://github.com/aporiapolis-project/aporiapolis/issues?q=is%3Aopen+label%3Aepic) pour suivre l'avancement.

## Contribuer

Lire [CONTRIBUTING.md](CONTRIBUTING.md), puis ouvrir une issue avant de coder. Tout commit doit respecter [Conventional Commits](https://www.conventionalcommits.org/) et inclure les footers `IA-assistance:` et `Validation:`.

## Code de conduite

Voir [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Le désaccord politique de fond est bienvenu s'il est argumenté.

## Sécurité

Voir [SECURITY.md](SECURITY.md) — divulgation responsable à `security@aporiapolis.org`.

## Licence

[AGPL-3.0](LICENSE) — usage libre, modifications redistribuées sous la même licence, y compris pour les usages en service réseau.
