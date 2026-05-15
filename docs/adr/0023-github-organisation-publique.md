# ADR-0023 — Configuration GitHub publique du projet

**Date** : 2026-05-XX (à la création du repo)
**Statut** : accepted
**Décideur(s)** : sam
**Supersedes** : —
**Superseded by** : —

## Contexte

Le projet AporiaPolis se veut **open source** et **pilotage transparent** dès le jour 1. Le dépôt de code et l'instance de gestion de projet doivent vivre publiquement, accessibles à tout contributeur ou observateur.

GitHub offre plusieurs mécanismes complémentaires pour structurer cela : *issue types*, *issue forms*, *Projects*, *project custom fields*, *organization issue fields*, *labels*, *milestones*, *workflows*. Toutes ces briques ne se valent pas en termes de disponibilité, de scope (dépôt / organisation), de compatibilité avec un pilotage public, ou de maturité (certaines sont en preview).

Cette ADR fixe la **configuration GitHub** retenue pour AporiaPolis, et explicite pourquoi.

## Contraintes documentées par GitHub

1. **Issue types** sont un mécanisme **d'organisation**, pas de dépôt. Ils sont gérés au niveau de l'organisation GitHub et appliqués aux issues des dépôts de cette organisation. Lorsqu'un dépôt est transféré d'une organisation vers un compte personnel, les issue types sont **retirés** des issues existantes.

2. **Issue forms YAML** sont actuellement en **public preview** chez GitHub. Leur format peut évoluer. Elles permettent d'auto-assigner un `type`, des `labels`, des `assignees`, et un `projects` — mais la clé `projects:` exige que **la personne qui ouvre l'issue ait des droits d'écriture** sur le Project ciblé. Pour les issues ouvertes par des contributeurs externes (cas standard d'un projet open source), cette clé échoue silencieusement, et l'issue n'est pas ajoutée au Project.

3. **Project custom fields** (notamment de type single-select) sont disponibles dans les *Projects*, qu'ils soient publics ou privés. Ils sont l'outil de structuration recommandé par GitHub pour une *single source of truth* dans Projects.

4. **Organization issue fields** (les vrais champs synchronisés sur les issues au niveau organisation) sont en **preview** et **uniquement supportés dans les Projects privés**. Ils ne sont donc *pas adaptés* à un pilotage public.

5. **Comptes personnels** offrent seulement deux niveaux de permissions : `owner` et `collaborator`. Les organisations offrent des rôles plus granulaires (admin, maintainer, write, triage, read) et la gestion par équipes.

## Décision

### Hébergement

- **Création d'une organisation GitHub** `aporiapolis-project` (ou nom équivalent disponible) **avant** tout dépôt.
- Le dépôt `aporiapolis` est créé *à l'intérieur* de cette organisation, public, branche `main` protégée (PR requise, signatures vérifiées si possible).
- Le compte personnel de Sam reste éventuellement utilisé pour son journal d'apprentissage personnel ou ses contributions externes, mais **ne contient pas le projet AporiaPolis**.

### Issue types (au niveau organisation)

Cinq types autorisés :

- `epic` — chantier majeur, regroupe plusieurs stories.
- `story` — livrable concret, valeur utilisateur ou technique identifiable.
- `bug` — défaut à corriger.
- `docs` — documentation seule.
- `tech-debt` — dette technique à résorber.

Pas plus. Si un nouveau type apparaît nécessaire, ADR de révision obligatoire.

### Issue forms YAML

Localisation : `.github/ISSUE_TEMPLATE/` du dépôt.

Templates initiaux :

- `epic.yml` — saisie d'un epic (objectif, critère de succès global, stories liées, dépendances, risques).
- `story.yml` — saisie d'une story (pourquoi, acceptance, tasks, gate, stream, priorité, effort, IA-trace).
- `bug.yml` — saisie d'un bug (reproduction, attendu, observé, environnement).
- `methodology_concern.yml` — pour signaler un biais ou une erreur factuelle (template ouvert au public).
- `source_proposal.yml` — pour suggérer une nouvelle source ou sous-question.
- `accessibility_issue.yml` — pour signaler un défaut RGAA.

Chaque form auto-assigne :
- `type:` (issue type org-level approprié).
- `labels:` (par exemple `scope:audit`, `accessibility`, etc.).

**Ne pas utiliser la clé `projects:`** dans les forms. À la place, un *auto-add workflow* côté Project ajoute toute nouvelle issue du dépôt au Project (voir section workflows).

### Project

- Un seul Project public, lié au dépôt `aporiapolis`.
- Custom fields configurés :
  - `stream` (single-select) : `product` / `cert` / `compliance` / `rd`.
  - `priority` (single-select) : `P0` / `P1` / `P2` / `P3`.
  - `phase` (single-select) : `t1` / `t2` / `t3` / `t4` / `bonus` / `parking`.
  - `risk` (single-select) : `low` / `medium` / `high` / `critical`.
  - `effort` (number) : heures estimées.
  - `dossier` (single-select) : `medias` / `dette` / `meta-ia` / `none` (étendu au fur et à mesure).
  - `gate` (single-select) : `juridique` / `source` / `publication` / `none`.

Vues du Project initialement :

- **Maintenant** : filter `phase=t1 OR phase=t2`, group by `priority`, sort by `effort` asc.
- **Roadmap** : timeline view par milestone.
- **Par stream** : kanban groupé par `stream`.
- **Gates** : filter `gate != none`, group by `gate`.
- **Parking lot** : filter `phase=parking`.

### Workflows GitHub

- **Auto-add to project** : workflow standard fourni par GitHub, ajoute toute issue créée dans le dépôt au Project public. Préféré à la clé `projects:` des forms (compatible contributeurs externes).
- **Commitlint** : workflow GitHub Actions sur les PR pour valider les Conventional Commits.
- **Release** : workflow GitHub Actions sur push `main` pour déclencher semantic-release.
- **CI lint/test/security** : workflows séparés pour ruff, mypy, pytest, dbt tests, bandit, trivy.

### Labels (réduits)

Liste fermée :

- **Scopes techniques stables** : `scope:api`, `scope:mcp`, `scope:front-public`, `scope:front-audit`, `scope:dwh`, `scope:graph`, `scope:audit`, `scope:methodo`, `scope:infra`, `scope:repo`, `scope:deps`.
- **Sources actives uniquement** : `source:<slug>` créés au fur et à mesure des source cards (par exemple `source:arcom`, `source:hatvp-rri`, `source:legifrance`, etc.).
- **Communauté** : `good-first-issue`, `help-wanted`.
- **État spécial** : `wontfix`, `duplicate`, `blocked-by-design`.

**Pas de labels redondants avec les custom fields** : ne pas avoir à la fois `P0` en label et en field, par exemple. Le field prévaut.

### Milestones

Créés à la création du dépôt :

- `T1 · Fondations · juin-juillet 2026`.
- `T2 · Production dossier 1 · août-octobre 2026`.
- `T3 · Publication + V2 · novembre 2026-janvier 2027`.
- `T4 · V3 + finalisation · février-avril 2027`.
- `Bonus · mai 2027`.

### Branche main et protection

- Branche `main` protégée : PR obligatoire, au moins une revue (auto-review acceptée si check-list de PR cochée), tests CI passants requis, pas de force-push, pas de suppression.
- Signature des commits recommandée mais non bloquante (clé GPG ou SSH signing).
- Squash & merge par défaut.

### Rôles d'organisation initiaux

- `sam` : owner.
- Comité de relecture (3-5 personnes) : rôle `triage` ou `read` selon préférence personnelle, accès au Project en lecture.
- Contributeurs externes futurs : rôle `triage` à l'opportunité, `write` après contributions confirmées.

## Conséquences

### Positives

- Issue types disponibles et utilisables (impossible sur compte perso).
- Permissions granulaires.
- Single source of truth dans Projects.
- Pilotage public visible.
- Préparé pour l'arrivée de contributeurs externes sans refonte ultérieure.
- Cohérence avec la posture éthique du projet (transparence du pilotage).

### Négatives

- Création d'une organisation GitHub à faire avant tout autre travail GitHub. Petit délai initial (15-30 minutes).
- Les organization issue fields restent inaccessibles tant qu'ils ne sortent pas de leur preview privée. Adapté en restant sur project custom fields.
- Les issue forms sont en public preview ; un changement de format de GitHub pourrait casser les templates. **Atténuation** : la sémantique critique du backlog (acceptance, gate, stream, priority) est *aussi* présente dans le body de l'issue et dans les custom fields du Project, pas seulement dans la structure du form. Si les forms changent, le pilotage tient.

### Conditions de révision

- Sortie de preview des organization issue fields *et* support des Projects publics : envisager la migration des custom fields vers les issue fields pour bénéficier de leur synchronisation native.
- Sortie de preview des issue forms : enrichir éventuellement les templates si de nouvelles capacités sont publiées.
- Volume de contributions externes dépasse ce qu'un workflow auto-add gère bien : envisager des workflows plus sophistiqués.
- Décision documentée de migrer vers GitLab, Forgejo ou une autre plateforme : superseding par nouvelle ADR.

## Notes pour les implémenteurs

- L'organisation GitHub doit être créée par Sam avant tout autre travail GitHub. Le compte de facturation reste personnel pour le moment (plan gratuit suffisant).
- Les issue types sont créés depuis les paramètres de l'organisation, pas depuis le dépôt.
- Le Project est créé au niveau de l'organisation, puis lié au dépôt.
- L'auto-add workflow est configurable depuis l'interface Project (« Workflows → Auto-add to project »).
- Les premiers labels et milestones peuvent être créés par script via `gh label create` et `gh api`. Un script `infra/github-setup.sh` versionné dans le dépôt sera utile.
- Si le nom `aporiapolis-project` est pris, alternatives à essayer : `aporiapolis-org`, `aporiapolis-team`, `aporiapolis-civic`, `aporiapolis-data`. Documenter le choix final dans cette ADR par mise à jour explicite.

## Sources GitHub consultées

- [Issue types — Organization settings](https://docs.github.com/en/issues/tracking-your-work-with-issues/configuring-issues/managing-issue-types-in-an-organization).
- [Issue forms — Syntax for issue forms](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms).
- [Project custom fields — Adding fields](https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-fields).
- [Auto-add to project workflow — Setting up](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-built-in-automations).
