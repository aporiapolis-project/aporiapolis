# ADR-0030 — Doctrine de release pre-MVP

**Date** : 2026-05-16
**Statut** : accepted
**Décideur(s)** : sam
**Supersedes** : —
**Superseded by** : —

## Contexte

Au 16 mai 2026, le workflow `Release` du repo est rouge depuis le bootstrap :

- l'ancien workflow fondé sur `semantic-release` tente de pousser directement sur `main`, mais la branche est protégée et exige une PR avec le check `Validate commit messages`. Le push est rejeté par `GH006: Protected branch update failed for refs/heads/main` — cause confirmée par le log du run `25959757458` (audit du 16 mai 2026).
- Plus profondément, `semantic-release` veut produire `v1.0.0` à partir de l'historique actuel — qui contient déjà plusieurs commits `feat:` du bootstrap (`feat(dossier-medias): add framing note v0.2 [...]`, etc.) — alors que le repo se déclare `pre-mvp` et qu'aucun livrable n'est encore disponible publiquement.

Le problème n'est donc pas seulement technique (un workflow à patcher), il est **sémantique** : qu'est-ce qu'une release pour AporiaPolis tant qu'aucun artefact n'est publiable ? La présente ADR acte la doctrine de release pour la phase pre-MVP — c'est-à-dire jusqu'au premier slice E2E livrable du dossier Médias (brief B-8 du plan post-audit). Elle prépare l'implémentation par le brief B-1.

## Options envisagées

### Option A — `release-please` (Google)

Action `googleapis/release-please-action` qui maintient ouverte une PR « Release X.Y.Z » à jour à chaque push sur `main`. La release Git/GitHub (tag + release notes + CHANGELOG) n'est créée qu'au moment où un humain merge cette PR. Compatible avec `main` protégée sans bypass ; un token dédié à portée limitée est utilisé pour que les PRs générées déclenchent les checks attendus. Permet de différer le premier tag jusqu'à un moment choisi.

**Pour** :
- Compatibilité branch protection native (la release PR passe les mêmes checks que toute autre PR).
- Pas de risque de `v1.0.0` surprise : `initial-version: 0.1.0` + `bump-minor-pre-major: true` rendent la première release `v0.1.0` au moment où sam le décide.
- Réversibilité élevée : retirer le workflow + le manifest suffit à débrancher l'outil.
- Cohérent avec le principe doctrinaire 1 (ne pas rendre vert ce qui ment encore) : la mécanique est en place mais ne déclenche rien tant qu'on ne le veut pas.

**Contre** :
- Dépendance à un outil tiers maintenu par Google ; en cas d'abandon, migration nécessaire.
- Ajoute deux fichiers à la racine (`release-please-config.json`, `.release-please-manifest.json`).
- La release PR peut accumuler des commits en attente pendant des semaines (jusqu'à B-8) — légère charge cognitive dans l'onglet Pull Requests.

### Option B — `semantic-release` PR-mode

Conservation de `semantic-release` mais reconfiguration pour ouvrir une PR au lieu de pousser sur `main`. Nécessite typiquement un plugin custom ou une combinaison `@semantic-release/git` + un workflow qui crée la PR via `gh` après push sur une branche temporaire.

**Pour** :
- Pas de changement d'outil — l'écosystème de plugins est connu.

**Contre** :
- Plus de plomberie que A pour un bénéfice équivalent ; documentation moins claire pour ce pattern.
- Le risque sémantique du `v1.0.0` automatique sur historique existant subsiste : il faut soit forcer un point de départ `0.0.0`, soit nettoyer l'historique des commits `feat:` du bootstrap — l'un comme l'autre est plus invasif que les réglages natifs de release-please.
- Réversibilité moyenne (plusieurs fichiers à toucher pour rebrancher autre chose).

### Option C — Désactivation jusqu'au premier artefact publiable

Suppression du workflow `release.yml` et de l'ancienne configuration `semantic-release`. Pas d'automatisation tant qu'il n'y a rien de réellement publiable (probablement après B-8). Une issue tech-debt acte la condition de réactivation.

**Pour** :
- Cohérence doctrinaire maximale : on ne fait pas semblant d'avoir une chaîne de release tant qu'il n'y a rien à releaser.
- Coût minimal (un commit suppression + une issue tech-debt).
- Réversibilité triviale.

**Contre** :
- Reporte la décision : il faudra rouvrir cette ADR au moment du premier slice E2E.
- Aucun mécanisme en place pour générer le premier tag — un humain devra y penser.
- Pas de signal automatique de « ce qu'il y a sur main depuis la dernière release » (utile pour la communication même en pre-MVP).

## Décision

Adoption de l'**Option A — `release-please`** (Google) comme système d'automatisation de la release pour la phase pre-MVP et au-delà.

Motivation principale : préparer la mécanique de release sans mentir aujourd'hui. La release PR maintenue par l'action ne déclenche aucune publication tant que sam ne la merge pas. La première release effective (`v0.1.0`) sera produite lorsque le premier slice E2E (B-8) sera livré, par un acte humain explicite — pas par accumulation silencieuse de commits `feat:` du bootstrap.

### Spécification d'implémentation (pour B-1)

- **Workflow** : `.github/workflows/release-please.yml` utilisant `googleapis/release-please-action@v4` (ou la dernière version stable au moment de l'exécution de B-1, à pinner explicitement).
- **Config** : `release-please-config.json` à la racine, avec :
  - `release-type: simple` (mode single package, pas de monorepo).
  - `package-name: aporiapolis`.
  - `initial-version: 0.1.0`.
  - `bump-minor-pre-major: true` (les commits `feat:` produisent des bumps `minor` tant que la version reste en `0.x.y`, jamais un bump `major` automatique vers `1.0.0`).
  - `group-pull-request-title-pattern: "chore(release): release${component} ${version}"` afin que la PR groupée reste compatible avec commitlint tout en gardant le composant visible.
- **Manifest** : `.release-please-manifest.json` à la racine, contenu initial `{".": "0.0.0"}`.
- **Suppression** : l'ancien workflow `.github/workflows/release.yml` est retiré dans la même PR de B-1, pour éviter toute coexistence ambiguë.
- **Permissions du workflow** : `contents: write`, `pull-requests: write`. Le secret `RELEASE_PLEASE_TOKEN` porte un token dédié à portée limitée ; il permet aux PRs générées de déclencher les workflows habituels sans contourner la branch protection.
- **Comportement attendu après B-1** :
  - À chaque push sur `main`, release-please crée ou met à jour une PR intitulée `chore(release): release aporiapolis X.Y.Z` avec changelog généré et bump du manifest.
  - Tant que la PR n'est pas mergée, aucun tag, aucune release GitHub, aucun changelog publié.
  - Le premier merge d'une telle PR (probablement déclenché manuellement par sam après B-8) crée le tag `v0.1.0`, la release GitHub correspondante, et le `CHANGELOG.md` initial.
- **Conventions de commit** : le filtre de types reste celui de Conventional Commits (cf. `CLAUDE.md` §3). `feat:` → bump `minor`, `fix:` → bump `patch`, `docs:`/`chore:`/`ci:`/etc. → pas de bump. À documenter dans `release-please-config.json` via `changelog-sections` pour aligner le rendu attendu (Features, Bug Fixes, Performance, Refactoring, Documentation).

## Conséquences

### Positives
- **Cohérence doctrinaire** : aucun mensonge dans la chaîne CI — le workflow Release ne tournera plus à vide en boucle d'échec dès lors que B-1 sera mergé.
- **Pas de release surprise** : le premier `v0.1.0` sera produit par un acte humain conscient, après B-8.
- **Branch protection respectée** : la release PR passe par les mêmes checks que n'importe quelle PR ; aucun bypass n'est nécessaire.
- **Réversibilité** : la chaîne `release-please` peut être démontée avec un commit (3 fichiers à retirer) si une autre stratégie devient préférable.

### Négatives
- **Dépendance à un outil tiers** : si Google abandonne `release-please-action` (faible probabilité, l'outil est utilisé largement par googleapis/), une migration sera nécessaire.
- **Bruit visuel** : une PR « release » restera ouverte en permanence dans l'onglet Pull Requests entre deux releases ; en pre-MVP, ce sera la PR la plus visible avant la première vraie release.
- **Couplage Conventional Commits** : la qualité du changelog dépend de la discipline des commits ; un commit mal scopé ou mal typé pollue durablement les release notes. Le hook commitlint et la validation `sam` sur chaque commit IA mitigent ce risque mais ne l'éliminent pas.

### Conditions de révision

Cette ADR sera revisitée :
- À la **fin de B-8** (premier slice OWID E2E livré), pour acter la transition pre-MVP → MVP et pour décider du déclenchement de `v0.1.0` (qui peut soit advenir par merge de la release PR maintenue par l'outil, soit demander une intervention manuelle si la doctrine évolue).
- Si la **stratégie de versionnement éditorial** impose un découplage avec le versionnement code — par exemple si on adopte un versionnement double `code-vMAJOR.MINOR / dossier-medias-vYYYY-MM` qui ne s'accommoderait pas du modèle single-package de release-please.
- Si une **faille de sécurité** ou un **changement de licence** affectent `release-please-action` au point d'imposer un retrait de l'outil.
- Si la **doctrine de branch protection** évolue (par exemple en supprimant le check requis sur `main`, scénario peu probable mais pas exclu).

## Notes pour les implémenteurs

Quelques points à vérifier au moment de B-1 :

- L'historique actuel contient plusieurs commits `feat(dossier-medias): ...` du bootstrap. Avec `initial-version: 0.1.0` + `bump-minor-pre-major: true`, release-please ne déclenchera pas un saut vers `v1.0.0` — il produira une release PR proposant `v0.1.0`. Vérifier la PR créée par release-please dès le premier push post-merge B-1 pour confirmer ce comportement.
- Le `CHANGELOG.md` n'existe pas encore dans le repo. release-please le crée à la première release. Pas de pré-création nécessaire.
- Ne **pas** ajouter le workflow `release-please` aux checks requis en branch protection — c'est un workflow post-merge, par construction il s'exécute *après* le merge. Cf. principe doctrinaire 2 (pré-vol §7).
- Le footer `IA-assistance:` du commit de release auto sera `none` (généré par bot), avec `Validation:` à formuler — point à trancher dans B-1 (probablement `Validation: sam` au moment du merge manuel de la release PR, suffisant comme traçabilité).

## Refs

- Audit du 16 mai 2026 (findings P0 sur CI rouge).
- Mise en conformité end-to-end C-1 (17 mai 2026) : PRs #116, #118, #120 ; PR release-please conforme #121.
- Documentation release-please : <https://github.com/googleapis/release-please>.
- Run en échec du workflow Release actuel : <https://github.com/aporiapolis-project/aporiapolis/actions/runs/25959757458>.
