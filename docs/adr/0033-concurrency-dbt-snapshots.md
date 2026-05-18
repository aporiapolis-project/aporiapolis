# ADR-0033 — Concurrency des dbt-snapshots dans Dagster (AporiaPolis)

- **Statut** : accepted
- **Date** : 2026-05-18
- **Décideurs** : Sam (mainteneur unique pré-MVP)
- **Stories liées** : [G.4 #48](https://github.com/aporiapolis-project/aporiapolis/issues/48)
- **ADRs liées** : ADR-0031 (stratégie stockage MVP), ADR-0032 (CSR islands Svelte 5)

## Contexte

L'orchestrateur Dagster AporiaPolis (`dagster/aporiapolis/`) matérialise
des assets de plusieurs natures :

- **Assets d'ingestion bronze** (download d'une source externe vers
  parquet horodaté `data/bronze/<source>/<entity>/snapshot_date=YYYY-MM-DD/...`).
- **Assets raw** (charge parquet bronze vers une table `raw.<entity>`
  miroir 1:1 du bronze conformément ADR-0031 + doctrine
  `docs/dwh/modelisation.md`).
- **Modèles dbt staging / intermediate / marts** (transformations
  contractuelles consommant raw).
- **`dbt snapshot`** (capture évolutive de tables critiques au sens
  SCD2 — historisation type 2).

Les `dbt snapshot` posent un problème de concurrence spécifique : si
deux exécutions du même snapshot tournent en parallèle (par exemple
deux runs Dagster qui se déclenchent côte à côte parce qu'un schedule
et un trigger manuel coïncident), deux lignes contradictoires
peuvent être insérées dans la table de snapshot, corrompant la
chronologie SCD2. Ce risque est documenté par dbt et est
spécifiquement contre-intuitif quand on découvre l'outil.

Les autres types d'assets (ingestion bronze, modèles dbt non-snapshot)
ne portent pas ce risque-là. La concurrence par défaut de Dagster
(plusieurs runs en parallèle) reste acceptable pour eux.

## Décision

**Tous les `dbt snapshot` orchestrés via Dagster dans AporiaPolis
s'exécutent avec une concurrence maximale de 1 run à la fois,
strictement.**

Cette contrainte est implémentée via le mécanisme natif Dagster de
`tag_concurrency_limits` au niveau de la **configuration d'instance**
(`dagster.yaml`), pas au niveau des Definitions Python :

```yaml
# dagster.yaml (instance) — exemple cible
concurrency:
  runs:
    tag_concurrency_limits:
      - key: "dagster/dbt_snapshot"
        limit: 1
```

Les jobs / assets qui exécutent un `dbt snapshot` portent le tag
correspondant (`dagster/dbt_snapshot` ou équivalent à figer au
moment de l'implémentation effective).

## Conséquences

### Positives

- **Intégrité SCD2 garantie** sur tous les snapshots dbt
  d'AporiaPolis. Pas de risque de lignes contradictoires.
- **Pattern transverse cohérent** : toutes les futures sources qui
  utiliseront un dbt-snapshot hériteront automatiquement de la
  contrainte, sans configuration par-source.
- **Doctrine épistémique préservée** : la chronologie SCD2 est un
  contrat avec le lecteur. La sérialiser au niveau orchestrateur
  protège ce contrat contre les accidents de timing.

### Négatives / acceptées

- **Latence accrue** sur les pipelines qui chaînent plusieurs
  snapshots : ils s'exécuteront en série, pas en parallèle. Pour le
  MVP AporiaPolis (1 source ingérée en B-8, 2-3 en T2), ce coût
  est négligeable. À revoir si > 5 snapshots distincts coexistent.
- **Aucune protection** côté ingestion bronze ou modèles dbt non-snapshot.
  Si un risque de concurrence émerge ailleurs (ex. écrasement de
  parquet bronze par 2 ingestions parallèles de la même source), il
  fera l'objet d'un ADR séparé — pas une extension silencieuse
  d'ADR-0033.

## Mise en œuvre

**B-8.2 ne livre PAS d'implémentation effective de cet ADR.** Aucun
`dbt snapshot` n'existe encore dans le repo (ils seront introduits en
B-8.3+ avec les premiers modèles dbt). En conséquence, B-8.2 ne crée
pas non plus le fichier `dagster.yaml` d'instance — il sera créé au
moment où la contrainte devient effective.

**L'acceptance de l'issue G.4 #48** (« `tag_concurrency_limits`
effectif sur les dbt-snapshots ») **n'est donc pas atteinte par
B-8.2** — l'issue reste OPEN. Sa fermeture passera par le brief
(B-8.3+) qui :

1. Crée le premier dbt-snapshot effectif (fichier `.sql` dans
   `dbt/snapshots/`).
2. Crée `dagster.yaml` au niveau de l'instance Dagster avec la
   configuration `tag_concurrency_limits` ci-dessus.
3. Tag le job/asset Dagster qui exécute le snapshot.
4. Prouve la contrainte via un test (ex. lancer 2 runs concurrents
   et vérifier sérialisation effective).

## Alternatives écartées

### Alternative 1 — Sérialisation au niveau du job Dagster (`max_concurrency_per_job`)

Limite la concurrence par job, pas par tag transverse. Inadapté car
plusieurs snapshots peuvent coexister dans différents jobs et chacun
mérite la contrainte séparément.

### Alternative 2 — Sérialisation côté dbt (`thread_count: 1`)

Limite la concurrence à l'intérieur d'une exécution dbt, pas entre
deux exécutions Dagster concurrentes. Insuffisant pour le cas SCD2
qui nous concerne ici.

### Alternative 3 — Verrou applicatif côté DuckDB

Possible mais ajouterait une complexité custom non nécessaire. Le
mécanisme Dagster natif `tag_concurrency_limits` est plus simple,
plus visible, plus tooled.

## Lien doctrine 8 principes

- **Principe 1** (ne pas rendre vert ce qui ment) : cet ADR documente
  un pattern qui sera implémenté plus tard. Il ne prétend pas que la
  protection est en place ; l'issue #48 reste OPEN en conséquence.
- **Principe 4** (architecture décidée) : Dagster est choisi comme
  orchestrateur depuis le bootstrap. La concurrence par tag transverse
  est le mécanisme Dagster natif standard.
- **Principe 5** (penser avant de coder) : la contrainte SCD2 est
  explicitée AVANT que le premier snapshot soit écrit, pour éviter
  un correctif post-hoc après corruption.

## Références

- Dagster — Run tag concurrency limits :
  https://docs.dagster.io/guides/operate/managing-concurrency
- dbt — Snapshots (SCD2) :
  https://docs.getdbt.com/docs/build/snapshots
- ADR-0031 — Stratégie stockage MVP (DuckDB+parquet local / Postgres prod).
