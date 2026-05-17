# ADR-0031 — Stratégie de stockage et exécution dbt en MVP : DuckDB+parquet local, Postgres+Object Storage en prod

**Date** : 2026-05-17
**Statut** : accepted
**Décideur(s)** : sam
**Supersedes** : aucune (extension non-conflictuelle de CLAUDE.md §2 pour la couche MVP local)
**Superseded by** : aucune

## Contexte

Le repo AporiaPolis fige sa stack en `CLAUDE.md §2` avec, pour la couche transformation et DWH :

- Transformation : `dbt-core sur Postgres`.
- DWH / BDD : `Postgres managé Scaleway`.
- Hébergement : `Scaleway VPS + Postgres managé + Object Storage, Caddy reverse proxy, Cloudflare front`.

Cette cible est honorée pour la production. Mais le slice B-8 (premier code applicatif, EPIC G stories #45/#46/#47/#49/#50) doit pouvoir tourner localement sur la machine d'un contributeur unique sans dépendre d'un Postgres managé Scaleway (qui n'existe pas encore — EPIC B infra n'est pas démarrée) ni d'un Object Storage Scaleway (idem).

Trois signaux ont rendu cette ADR nécessaire au moment où B-8 démarrait :

1. **Acceptance #46 (G.2)** demande verbatim « bronze JSON brut horodaté en **Object Storage Scaleway** » et « silver table **Postgres** `stg_owid__co2_emissions` ». Sans ADR, soit on attend l'infra Scaleway pour ingérer une seule source publique bénigne (overkill), soit on contourne silencieusement et CLAUDE.md §2 ment.
2. **Principe 1 doctrine** (CLAUDE.md §11.1) : « ne pas rendre vert ce qui ment encore ». Implémenter DuckDB localement *sans* le dire ferait fonctionner le slice et mentir la stack officielle simultanément.
3. **Principe 4 doctrine** : « le premier livrable utilise l'architecture décidée ». Le but de B-8 est de prouver la chaîne Dagster → bronze → dbt → API → page. Cette chaîne *décidée* n'impose pas Postgres en MVP local ; elle impose Postgres en prod. La distinction est utile, à condition de l'écrire.

Le repo Karpathy (https://github.com/multica-ai/andrej-karpathy-skills) ajoute le principe 5 « penser avant de coder » : avant la première ligne d'asset Dagster, expliciter les hypothèses et les tradeoffs. C'est ce que fait cette ADR.

## Options envisagées

### Option A — Postgres local en Docker + MinIO local en S3-compat

Postgres local dans un service Docker (`docker compose up postgres`), MinIO local pour le bronze en S3 protocol (`mc cp …`). Code dbt-postgres + code Python qui parle S3 SDK comme en prod.

**Pour** :
- Fidélité absolue à `CLAUDE.md §2` (aucune déviation, aucune ADR n'aurait été nécessaire).
- Code MVP local = code prod : ce qui marche en B-8 marchera en EPIC B sans réécriture.
- Permet de tester dès maintenant des features Postgres-spécifiques (CTE matérialisées, types JSONB, extensions).
- Aucun risque de drift dbt-duckdb vs dbt-postgres (SQL pas toujours portable malgré l'effort).

**Contre** :
- 2 services Docker à lancer / maintenir en local. Friction quotidienne pour Sam + premier vrai onboarding contributeur extérieur.
- Postgres + MinIO ajoutent ~500-700 Mo d'images Docker + RAM résidente.
- Slow loop de feedback en dev : `psql` plus lourd que `duckdb`, MinIO SDK plus verbeux que `pd.read_parquet`.
- L'« infra prod » que ça simule n'existe pas encore (EPIC B). On paie un tribut à une cible future qui n'a pas encore son ADR ni sa première brique provisionnée.

### Option B — DuckDB+parquet local en MVP, Postgres+Object Storage en prod (ADR hybride)

DuckDB comme moteur SQL local (target dbt `duckdb`), parquet local horodaté pour le bronze (`data/bronze/<source>/<entity>/snapshot_date=YYYY-MM-DD/`). Prod Scaleway reste sur `CLAUDE.md §2` : Postgres + Object Storage. Le code SQL dbt est écrit en standard portable raisonnable mais on n'investit pas dans la portabilité absolue (pas de Jinja conditionnel `target.adapter` partout). Le seam MVP→prod sera retravaillé en EPIC B selon ce que dira l'expérience.

**Pour** :
- Boucle de feedback locale très courte : `dbt run --target duckdb` ~secondes sur un dataset OWID.
- Aucune infra Docker requise pour B-8 (DuckDB = librairie embarquée).
- Parquet local lisible directement par DuckDB sans intermédiaire (`read_parquet('data/bronze/...')`).
- Le seam MVP→prod est explicite (cette ADR) et documenté, donc CLAUDE.md §2 ne ment pas — il prescrit la prod, cette ADR prescrit le MVP local.
- Principe 6 doctrine respecté : minimum nécessaire en MVP, pas de tribut à une prod qui n'existe pas encore.

**Contre** :
- Le code MVP local ≠ code prod : la migration EPIC B aura un coût non nul (réécriture des connexions, du IO bronze, peut-être de quelques modèles dbt si syntaxe SQL diverge).
- Risque de drift dans les modèles dbt si on écrit du SQL DuckDB-natif (fonctions, types, syntaxe spécifique) qui ne portera pas tel quel sur Postgres.
- Première vraie migration en EPIC B sera un sujet propre (ADR future), pas un copier-coller.

### Option C — Pivot full DuckDB (MVP et prod)

DuckDB partout, abandon de Postgres comme cible prod. Supersede explicitement `CLAUDE.md §2`. Migration vers Postgres reportée à un déclencheur de croissance (volume, concurrence, multi-tenancy) qui justifierait l'effort.

**Pour** :
- Le plus simple techniquement : un seul moteur, aucune migration future à prévoir.
- DuckDB en 2026 supporte concurrence read-only + tables persistantes ; viable pour MVP + V2 + V3 sur volumes AporiaPolis envisagés.
- Réduit la surface de doctrine à maintenir.

**Contre** :
- Pivot stratégique majeur — supersede `CLAUDE.md §2` qui était la décision fondatrice de novembre 2025 (stack bootstrap).
- DuckDB en prod web reste un pari : moins d'écosystème (pas de Scaleway managé), opérations différentes (sauvegardes, monitoring, scaling), peu d'expérience publique d'hébergement production multi-utilisateur.
- Engagement Sam sur une stack non standard qu'il faudra défendre auprès du comité de relecture et auprès du jury Simplon (Postgres reste la stack canonique enseignée).
- Aucun bénéfice immédiat par rapport à Option B — le pivot est rentable seulement si la prod est imminente, ce qui n'est pas le cas.

## Décision

**Option B retenue.**

MVP local utilise **DuckDB + parquet** ; prod (déclenchée par EPIC B) conservera **Postgres + Object Storage** tel que `CLAUDE.md §2` le prescrit. Cette ADR ne supersede pas `CLAUDE.md §2` — elle l'étend pour la couche MVP local.

### Précisions techniques actées

1. **Bronze MVP local** : fichiers parquet horodatés dans `data/bronze/<source>/<entity>/snapshot_date=YYYY-MM-DD/<entity>.parquet`. Dossier `data/` exclu de `.gitignore` (à confirmer en B-8.1 — exception `.gitkeep` ou bootstrap script). Schéma de partition `snapshot_date=YYYY-MM-DD` (équivalent Hive-style) cohérent avec ce que DuckDB et S3 parlent nativement.
2. **Silver/intermediate/marts MVP local** : tables DuckDB dans `data/duckdb/aporiapolis.duckdb` (fichier unique, gitignored). Profile dbt `profiles.example.yml` ne mentionne que la target `duckdb` ; aucun profile Postgres stub en B-8 (cf. correction Codex « pas de dual-stack actif »).
3. **Layout package Python pour l'API** : repo conserve `services/api-rest/` (path historique) ; package Python interne s'appelle `api_rest/` (underscore) pour être importable. `pyproject.toml` côté `services/api-rest/`. Run : `uvicorn api_rest.main:app` après `cd services/api-rest && pip install -e .`.
4. **Schéma de modélisation MERISE (G.1)** : 6 schémas séparés DuckDB (`app`, `raw`, `staging`, `intermediate`, `marts`, `audit_log`) conformes à l'acceptance G.1 rebaselinée. DuckDB supporte les schémas via `CREATE SCHEMA` standard SQL.
5. **Code SQL dbt** : SQL standard suffisamment portable pour ne pas peindre dans le coin (pas de fonction DuckDB-only sans nécessité). Pas de Jinja conditionnel `target.adapter` à ce stade — la portabilité sera retravaillée en EPIC B.
6. **Tests dbt** : `not_null`, `unique`, `accepted_values` standard. Tests dbt portables Postgres↔DuckDB sans modification.
7. **Concurrence dbt snapshots (G.4)** : `tag_concurrency_limits` Dagster reste applicable indépendamment du moteur — la contrainte est sur l'orchestration, pas sur le SQL. ADR-0033 dédiée à créer en B-8.2.

### Précisions méthodologiques actées

- Aucune ligne de code MVP local ne sera réécrite « pour la prod » avant EPIC B. Le coût de migration est accepté et documenté ici.
- Une ADR future (EPIC B) bouclera la stratégie de migration concrète (probablement : dual-write transitoire, ou cutover unique, ou expansion DuckDB en prod si l'expérience MVP le justifie).
- `docs/sources/<slug>.md` (Gate 2 doctrine §1) reste obligatoire avant toute ingestion. Cette ADR n'assouplit pas le Gate 2.

## Conséquences

### Positives

- B-8 peut démarrer sans dépendance infra externe.
- Doctrine 1 préservée : `CLAUDE.md §2` documente la prod (vrai), cette ADR documente le MVP local (vrai), aucun mensonge.
- Boucle de feedback dev courte (DuckDB embarqué).
- Coût de migration EPIC B identifié explicitement, pas latent.
- Comité de relecture peut comprendre la déviation sans archéologie Git.

### Négatives

- Le code MVP local ≠ code prod. La migration EPIC B sera un sujet propre à instrumenter (tests d'équivalence Postgres↔DuckDB sur les marts critiques, ou réécriture ciblée).
- Risque résiduel de drift SQL DuckDB-natif si un contributeur oublie la portabilité. Mitigation : revue de code (Principe 7 — modifications chirurgicales) + tests dbt portables.
- Le moteur Postgres ne sera testé qu'au moment de la migration. Tout problème spécifique Postgres (types JSONB, extensions, comportement de transaction) sera découvert tard.

### Conditions de révision

Cette ADR devrait être revisitée si :

- **EPIC B démarre** : créer une ADR de migration concrète (cutover, dual-write transitoire, ou expansion DuckDB). La présente ADR n'est pas dépréciée mais étendue.
- **DuckDB se révèle inadapté au MVP local** : volumes inattendus, dépendance dbt qui casse, friction outillage. Auquel cas Option A (Postgres+MinIO Docker) redevient candidate ; cette ADR serait superseded.
- **AporiaPolis atteint un volume où le pivot Option C devient rentable** : si la prod ne démarre jamais et DuckDB tient en V3 / présidentielle, on peut envisager d'étendre DuckDB en prod légère. Auquel cas pivot full DuckDB se déclenche par ADR de superseding de `CLAUDE.md §2` *et* de cette ADR.
- **Une décision juridique nouvelle change la cible d'hébergement** : ex. obligation de stocker en France métropolitaine, contrainte RGPD spécifique qui exclut un fournisseur, etc. Auquel cas la cible prod elle-même bouge, et cette ADR doit suivre.

## Notes pour les implémenteurs

- Le code Dagster qui ingère OWID (B-8.2) lit son URL depuis une **config machine** (`dagster/aporiapolis/config/sources/owid.yaml` ou équivalent), pas depuis `docs/sources/owid.md` (qui est une doc publique humaine). Un test de cohérence (`tests/test_sources_consistency.py`) vérifiera que doc et config restent alignées sur l'URL et la licence.
- Le `dbt/profiles.example.yml` ne mentionne que `target: duckdb`. Pas de stub Postgres en B-8 (déclencherait du dead code que `dbt run --target postgres` n'utilise pas — Principe 6).
- Le `dbt_project.yml` peut spécifier `materialized: table` ou `materialized: view` selon le besoin ; pas de spécificité Postgres ni DuckDB requise au démarrage.
- Pour le `make demo` (B-8.6), la chaîne de bout en bout tourne en local sans infra externe :
  ```
  make demo → dagster asset materialize → dbt run → dbt test → astro build → smoke test sur page buildée → exit 0
  ```
- Référencer cette ADR depuis le code via un commentaire `# ADR-0031` sur le bloc concerné (ex. au début de `dagster/aporiapolis/assets/ingest_owid_climate.py` et au début de `dbt/profiles.example.yml`).

<!--
Conventions :
- ADR créée pendant le brief B-8.0 (Rain Razor/briefs/2026-05-17-slice-owid-e2e-00-rebaselining-doctrinaire/).
- Numérotation à 4 chiffres : 0031 confirmé libre (trous 0027/0028 réservés pour snapshots historiques et dim_groupe_media selon project_rain_razor mémoire Cowork ; 0010 sera utilisé par ADR-0033 G.4 concurrency snapshots).
- Cette ADR n'est jamais modifiée après acceptation : si DuckDB se révèle inadapté, créer une ADR de superseding.
-->
