# CLAUDE.md — conventions et contexte pour les agents IA

> Ce fichier est chargé automatiquement par Claude Code et lu par tout agent IA travaillant sur ce repo (Codex CLI, Cursor, Cline, Aider, Continue, Claude Code, etc.). Il fixe le contexte, les conventions, les règles d'engagement IA et les anti-patterns. **Toute IA contribuant au repo respecte ce document.** Aucun outil IA spécifique n'est prescrit ; le nom du fichier est une convention de portabilité.

## 1. Contexte projet

AporiaPolis est un outil civic-tech open source produit en solo (sam), avec un comité de relecture pluraliste. La cible directrice est **la première publication exemplaire du dossier Médias (fin T2 / début T3)**. Tout ce qui ne contribue pas directement à cette cible est différé (voir backlog v2 et parking lot).

Trois gates transverses encadrent l'avancement :
- **Gate 1 — Juridique** : bloque toute story d'audit personnel. Voir [ADR-0021](docs/adr/0021-audit-personnel-architecture.md).
- **Gate 2 — Source contract** : bloque toute story d'ingestion. Une `docs/sources/<slug>.md` est obligatoire.
- **Gate 3 — Publication** : bloque toute mise en ligne publique (RGAA AA, reproductibilité, doctrine analytics, comité).

## 2. Stack figée

Ne pas dévier sans ADR superseding explicite.

| Couche | Choix |
|---|---|
| Langage principal | Python 3.12+ (uv + ruff) |
| Orchestration | Dagster |
| Transformation | dbt-core sur Postgres |
| DWH / BDD | Postgres managé Scaleway (pas de Neo4j en V1, pas de Redpanda en prod, pas d'OpenMetadata) |
| API publique | FastAPI (OpenAPI 3.1 auto, pagination cursor, erreurs RFC 7807) |
| MCP server | FastMCP — single server `mcp-data` read-only |
| Front public | Astro 5 + Svelte 5 (TypeScript), design tokens accessibles WCAG AA |
| Front audit | SvelteKit ou file-based router Svelte 5 — **calcul intégralement client**, `localStorage` uniquement |
| Scraping | Playwright dans un service dédié, respect robots.txt strict |
| CLI (post-MVP) | Go |
| Hébergement | Scaleway VPS + Postgres managé + Object Storage, Caddy reverse proxy, Cloudflare front |

## 3. Conventional Commits — obligatoire

Format :

```
<type>(<scope>): <subject>

[body : pourquoi, contexte, conséquences]

[footers]
```

Subject : ≤ 80 caractères, impératif présent, sans majuscule initiale, sans point final. (Enforced par `commitlint.config.mjs` `header-max-length: 80`.)

Types autorisés : `feat`, `fix`, `perf`, `refactor`, `docs`, `test`, `chore`, `ci`, `build`, `style`, `revert`. Breaking : `feat!` ou footer `BREAKING CHANGE:`.

Scopes autorisés : voir `commitlint.config.mjs`. Principaux : `infra`, `api`, `mcp`, `front-public`, `front-audit`, `dwh`, `graph`, `audit`, `methodo`, `repo`, `deps`, `release`, `adr`, `ingestion-<source>`, `dwh-<dossier>`, `dossier-<slug>`.

### Footers recommandés pour tout commit assisté par IA

```
IA-assistance: <claude-code|cowork|codex|none>
Validation: sam
```

Le footer `IA-assistance:` documente l'origine de l'édition et alimentera à terme un mécanisme d'auto-observation. **Convention recommandée, non bloquante en pre-MVP** : aucun hook ne rejette aujourd'hui un commit sans ces footers. L'enforcement (hook commit-msg dédié) est prévu post-MVP — voir issue tech-debt `[tech-debt] Enforcer footers IA-assistance/Validation via hook commit-msg`.

Le footer `Validation: sam` matérialise la relecture humaine systématique.

Footers complémentaires : `Refs: #123`, `Closes: #456`, `BREAKING CHANGE: ...`, `DPIA: oui` (commit touchant des données personnelles).

## 4. Règles d'engagement IA

### L'IA peut faire seule
- Refactoring local sans changement de comportement (couvert par tests).
- Ajout de tests sur du code existant.
- Mise en forme, lint, typage.
- Génération de boilerplate à partir d'un template existant (nouveau modèle dbt, nouveau scraper, nouveau endpoint FastAPI).
- Rédaction de docstrings et commentaires *uniquement quand le « pourquoi » est non-trivial*.
- Mise à jour de dépendances mineures (sans breaking).
- Réponse à une issue documentaire claire.

### L'IA propose, sam valide avant merge
- Tout changement de schéma BDD ou DWH (migration).
- Tout changement d'API publique (endpoint, paramètre, contrat).
- Toute nouvelle dépendance externe (npm, pip, dbt package).
- Toute story tagguée `gate:juridique`, `gate:source` ou `gate:publication`.
- Toute modification de la méthodologie publique (`docs/methodology/`).
- Tout changement structurant : ADR à créer.
- Tout commit touchant aux données personnelles (`DPIA: oui` requis).

### L'IA ne fait pas
- Création/suppression de branche distante, push --force, modification de branch protection.
- Merge de PR, fermeture d'issue sans validation explicite.
- Création de secret, modification de variable d'environnement de production.
- Implémentation de stories `gate:juridique` tant que l'ADR-0021 est en vigueur et que la décision de bascule n'a pas été superseded.
- Ingestion ou stockage de contenus de presse en zone bronze persistante (interdit par ADR-0022).
- Décision éditoriale : choix d'un angle, validation d'un test de réalité, classement d'une source.
- Modification de fichiers `dossiers/<slug>/*.mdx` sans demande explicite.

## 5. Style de code

### Python
- `ruff` pour lint + format (`ruff check . && ruff format .`).
- `mypy` sur `services/` (sans `--strict` en MVP — voir issue tech-debt `[tech-debt] Enforcer mypy --strict quand le code Python existera`).
- Typage explicite y compris pour les variables locales si non triviales.
- Pas de `from x import *`. Pas de `print()` en code de production (utiliser `logging`).
- Tests : `pytest`, fixtures factory-style, noms `test_<unité>_<comportement>`.

### SQL (dbt)
- `sqlfluff` pour lint et format.
- Modèles `snake_case` préfixés : `stg_<source>__<entity>`, `int_<theme>__<step>`, `fact_<grain>`, `dim_<entity>`.
- SCD2 systématique sur dimensions politiques (`dim_acteur`, `dim_parti`, `dim_programme`).
- Tests dbt nommés explicitement : `not_null_dim_acteur_id`, etc.
- Hook pre-commit `dbt-tests-on-modified` non-bloquant en MVP (`|| true`) tant qu'il n'y a pas de modèles. Retrait du `|| true` prévu post-premier modèle — voir issue tech-debt `[tech-debt] Enforcer dbt test après premier modèle dbt`.

### Svelte / TypeScript
- Composants en PascalCase, fichiers `<Composant>.svelte`.
- Stores Svelte natifs, pas de Redux ni équivalent.
- Calculs dans modules `.ts` purs, testables unitairement (vitest).
- Pas de dépendance npm tierce non auditée pour le module audit personnel (chaîne d'approvisionnement réduite).

### Go (post-MVP)
- `gofmt`, `staticcheck`.
- Packages cohésifs, pas de `internal/utils` fourre-tout.

## 6. Anti-patterns à éviter

- **Inventer un endpoint, une table ou un fichier qui n'existe pas.** Lire le code avant de proposer.
- **Modifier `dossiers/` sans validation éditoriale.** Le contenu éditorial n'est pas du code refactorisable.
- **Ajouter un mock à la place d'un test d'intégration sur les pipelines d'ingestion.** Préférer un fixture petit mais réel.
- **Persister des données utilisateur côté serveur pour le module audit.** Bloqué par ADR-0021.
- **Ingérer ou stocker du contenu de presse en bronze persistant.** Bloqué par ADR-0022.
- **Ajouter un commentaire qui décrit *ce que* fait le code.** Si nécessaire, expliquer *pourquoi*.
- **Créer un fichier `.md` de documentation que personne n'a demandé.** Préférer enrichir un fichier existant.
- **Référencer un ticket, une PR ou un commit dans un commentaire de code.** Ces références rotent — mettre l'info dans le commit / PR description.

## 7. Politique de merge

`squash` only. `merge commit` et `rebase merge` désactivés au niveau settings repo. Historique `main` linéaire, un commit par PR. Le titre du commit final = titre de la PR (Conventional Commits respecté).

## 8. Doctrine de release

Voir [ADR-0030](docs/adr/0030-doctrine-release-pre-mvp.md). En pre-MVP : `release-please` ouvre et maintient une PR `chore(main): release X.Y.Z` sur `main`. Le merge de cette PR crée le tag + la GitHub Release. La PR reste ouverte jusqu'à publication d'un premier artefact MVP (post-EPIC G slice OWID). Pas de bump major automatique tant que `version < 1.0.0`.

## 9. Documents de référence

- Conventions complètes : voir `docs/adr/` et le doc planning externe (`Rain Razor/10_conventions.md`).
- Décisions structurantes récentes : [ADR-0024 — Doctrine de relecture en deux strates](docs/adr/0024-doctrine-relecture-deux-strates.md), [ADR-0030 — Doctrine de release pre-MVP](docs/adr/0030-doctrine-release-pre-mvp.md).
- Backlog v2 : géré dans GitHub Issues + Project public. Source d'autorité : les issues, pas un fichier markdown.
- Méthodologie publique : `docs/methodology/` (en cours).
- Sources : `docs/sources/<slug>.md`, une carte par source ingérée.

## 10. Quand poser une question vs avancer

- **Avance** : la convention est claire, la story est cadrée, les tests passent, aucune décision juridique n'est touchée.
- **Demande** : la story est sous gate, plusieurs interprétations sont possibles, un fichier hors scope serait modifié, une dépendance externe doit être ajoutée.

En cas de doute : ouvre une issue `tech-debt` qui documente la question et continue avec ton meilleur jugement plutôt que de bloquer.
