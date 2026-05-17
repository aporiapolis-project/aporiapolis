# CLAUDE.md — conventions et contexte pour les agents IA

> Ce fichier sert de référence à tout agent IA travaillant sur ce repo. Il fixe le contexte, les conventions, les règles d'engagement IA et les anti-patterns. **Toute IA contribuant au repo respecte ce document.** Aucun outil IA spécifique n'est prescrit ; le nom du fichier est une convention de portabilité.

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

> **Déviations MVP local actées** : voir [ADR-0031](docs/adr/0031-strategie-stockage-mvp.md) (stack hybride DuckDB+parquet en MVP local, Postgres+Object Storage en prod) et [ADR-0032](docs/adr/0032-mode-consommation-page-api.md) (mode de consommation page → API en CSR via islands Svelte 5). Ces déviations n'invalident pas le tableau ci-dessus pour la cible prod ; elles documentent la couche MVP local qui n'est pas couverte verbatim par ce tableau.

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
IA-assistance: <outil-utilisé|none>
Validation: sam
```

Le footer `IA-assistance:` documente l'origine de l'édition et alimentera à terme un mécanisme d'auto-observation. Utiliser un identifiant court pour l'outil réellement employé, ou `none` si le commit est strictement manuel. **Convention recommandée, non bloquante en pre-MVP** : aucun hook ne rejette aujourd'hui un commit sans ces footers. L'enforcement (hook commit-msg dédié) est prévu post-MVP — voir issue tech-debt `[tech-debt] Enforcer footers IA-assistance/Validation via hook commit-msg`.

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

Voir [ADR-0030](docs/adr/0030-doctrine-release-pre-mvp.md). En pre-MVP : `release-please` ouvre et maintient une PR `chore(release): release aporiapolis X.Y.Z` sur `main`. Le merge de cette PR crée le tag + la GitHub Release. La PR reste ouverte jusqu'à publication d'un premier artefact MVP (post-EPIC G slice OWID). Pas de bump major automatique tant que `version < 1.0.0`.

## 9. Documents de référence

- Conventions complètes : voir `CONTRIBUTING.md`, `commitlint.config.mjs` et `docs/adr/`.
- Décisions structurantes récentes : [ADR-0024 — Doctrine de relecture en deux strates](docs/adr/0024-doctrine-relecture-deux-strates.md), [ADR-0030 — Doctrine de release pre-MVP](docs/adr/0030-doctrine-release-pre-mvp.md).
- Backlog v2 : géré dans GitHub Issues + Project public. Source d'autorité : les issues, pas un fichier markdown.
- Méthodologie publique : `docs/methodology/` (en cours).
- Sources : `docs/sources/<slug>.md`, une carte par source ingérée.

## 10. Quand poser une question vs avancer

- **Avance** : la convention est claire, la story est cadrée, les tests passent, aucune décision juridique n'est touchée.
- **Demande** : la story est sous gate, plusieurs interprétations sont possibles, un fichier hors scope serait modifié, une dépendance externe doit être ajoutée.

En cas de doute : ouvre une issue `tech-debt` qui documente la question et continue avec ton meilleur jugement plutôt que de bloquer.

## 11. Doctrine AporiaPolis

Cette section codifie les principes directeurs pour tout agent IA contribuant à ce repo, indépendamment de l'outil utilisé ou de son contexte d'exécution. Référence externe pour les principes 5-8 : https://github.com/multica-ai/andrej-karpathy-skills.

Ces principes biaisent vers **prudence > vitesse**. Pour les tâches triviales (correction de typo, one-liner évident), l'agent peut juger que la rigueur complète n'est pas requise. Le but est de réduire les erreurs coûteuses sur le travail non-trivial, pas de ralentir les tâches simples.

### 11.1 Gouvernance (principes 1-4)

Issus de la relecture du plan de remédiation post-audit (16 mai 2026), à appliquer à toute future remédiation ou mise en conformité du repo.

**Principe 1 — Ne pas rendre vert ce qui ment encore.** Avant de réparer un mécanisme cassé, décider d'abord ce qu'il doit vraiment faire. Refuser le fix qui fabrique de la fausse santé. Cas typiques : workflow CI rouge dont la sémantique est questionnable, doc qui promet ce qui n'est pas enforced, channel mail annoncé mais inexistant. Trancher la sémantique avant le technique.

**Principe 2 — Les checks requis en branch protection sont des PR gates uniquement.** Les workflows post-merge (release, deploy, notify, publish) n'appartiennent jamais aux required status checks. Pattern adopté : un job final `ci-gate` qui dépend de lint/test/security/dep-review, et qui devient le check requis avec `Validate commit messages`. Les noms à exiger sont les **display names** des jobs (clé `name:` YAML), pas les workflow names ni les job_ids.

**Principe 3 — La fermeture d'items Project v2 est acceptance-based, jamais bulk.** Aucun item ne se ferme « parce qu'il fait partie d'un livrable » — chaque item ne se ferme que quand son acceptance criteria explicite est atteint, idéalement vérifié contre le réel (état repo, CI, code). Corriger un board qui ment en fermant tout en bloc ne corrige pas — ça lui demande de mentir dans l'autre sens.

**Principe 4 — Le premier livrable exécutable utilise l'architecture décidée.** Le but de la première tranche verticale n'est pas de « livrer un truc rapide » ; c'est de **prouver que l'architecture décidée fonctionne**. Tout shortcut prouve seulement le shortcut. Question d'arbitrage : est-ce que je prouve l'architecture décidée, ou est-ce que je contourne une partie d'elle ?

### 11.2 Discipline de coding (principes 5-8, actifs dès B-8)

Issus des observations Andrej Karpathy sur les pièges récurrents des LLMs en coding (cf. https://github.com/multica-ai/andrej-karpathy-skills). Reformulés de manière tool-agnostic.

**Déclenchement : à partir de B-8** (premier code applicatif AporiaPolis, slice OWID E2E via EPIC G). Avant B-8, le repo est doc + ADR + config CI sans fichier de code applicatif — ces principes n'ont pas de cible.

**Principe 5 — Penser avant de coder.** Avant la première ligne de code, expliciter les hypothèses, présenter les interprétations alternatives quand le BRIEF est ambigu, identifier les tradeoffs des options envisagées. Aucune lecture ambiguë ne se résout silencieusement. Comportements à tenir : énoncer les hypothèses, présenter les lectures alternatives, pousser un retour si une approche plus simple existe, stopper face à la confusion. Critère de revue : un PR review ne doit pas révéler d'hypothèse implicite non documentée.

**Principe 6 — Simplicité d'abord.** Le code livré est le minimum nécessaire pour satisfaire l'acceptance criteria du BRIEF. Pas de feature non demandée, pas d'abstraction (factory, plugin, registry) avant le deuxième cas d'usage concret, pas de « flexibilité » ou de « configurabilité » non listée, pas d'error handling pour scénarios impossibles. Test : un ingénieur senior dirait-il que ce code est sur-compliqué ? Si oui, réécrire. Si 200 lignes pourraient être 50, c'est une violation. Note : la simplicité n'autorise pas le sous-engineering — le minimum nécessaire inclut la robustesse demandée par l'acceptance criteria et les tests qu'elle exige.

**Principe 7 — Modifications chirurgicales.** Ne toucher que ce qui est strictement nécessaire à la mission. Pas d'« amélioration » de code adjacent (style, commentaires, formatting) non demandée. Pas de refactor de code qui marche. Style existant respecté tel quel, même si l'agent ferait autrement. Le dead-code orphelin pré-existant est **mentionné** (RESULT.md ou issue tech-debt), pas supprimé dans la PR courante. Quand le changement crée des orphelins (imports, variables, fonctions devenus inutilisés **par ce changement précis**) : les nettoyer. Test de trace : chaque ligne du diff doit tracer à un item de l'acceptance criteria.

**Principe 8 — Exécution guidée par le critère de succès.** Toute tâche impérative est reformulée en critère de succès vérifiable avant d'écrire du code. Exemples : « ajouter la validation » → « écrire les tests sur les entrées invalides, puis les faire passer » ; « corriger le bug » → « écrire un test qui reproduit le bug, puis le faire passer » ; « refactorer X » → « tests passent avant ET après ». Pour les multi-étapes, plan court avec check par étape :

```
1. [Étape] → vérifier : [check]
2. [Étape] → vérifier : [check]
3. [Étape] → vérifier : [check]
```

Patterns de vérification adaptés à AporiaPolis (non exhaustifs) : tests `pytest` sur un service Python, tests `dbt test` sur un modèle dbt, acceptance criteria d'une issue Project v2, `make demo` qui tourne d'une commande, validation visuelle sur API ou page web. Critère de succès fort = l'agent boucle indépendamment vers la solution. Critère faible (« make it work ») = aller-retours coûteux. Toujours pousser pour le critère le plus précis vérifiable de bout en bout.

**Lien explicite Principe 8 ↔ Principe 3** : le critère de succès du Principe 8 est l'acceptance criteria du Principe 3, à deux échelles différentes (item Project v2 = échelle gouvernance, tâche de la mission = échelle coding). Les deux se renforcent.

### 11.3 Sources

- https://github.com/multica-ai/andrej-karpathy-skills — origine des principes 5-8 (fork miroir de `forrestchang/andrej-karpathy-skills`, dérivé d'observations d'Andrej Karpathy sur les pièges LLM coding).
- ADR-0030 doctrine release pre-MVP — exemple d'application du Principe 1.
