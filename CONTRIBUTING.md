# Contribuer à AporiaPolis

> Merci de vouloir contribuer. Ce projet est piloté publiquement et accueille les contributions de toute personne — codeuse, journaliste, chercheuse, étudiant·e ou citoyen·ne — qui partage l'exigence de **sourçage rigoureux**, de **méthodologie défendable** et de **respect du désaccord politique argumenté**.

## 1. Avant de coder : ouvrir une issue

Toute contribution non triviale (changement de comportement, ajout de fonctionnalité, refactor visible) commence par une **issue**, pas par une PR.

Les templates d'issue (`.github/ISSUE_TEMPLATE/`) couvrent :

- **Bug** — un défaut à reproduire et corriger.
- **Story** — un livrable concret, avec acceptance critères.
- **Epic** — un chantier majeur regroupant plusieurs stories.
- **Methodology concern** — pour signaler un biais, une erreur factuelle, ou une fragilité méthodologique. **Ouvert au public, attendu et bienvenu.**
- **Source proposal** — pour suggérer une nouvelle source ou une nouvelle sous-question.
- **Accessibility issue** — pour signaler un défaut RGAA.

Une fois l'issue ouverte et discutée, vous pouvez ouvrir une PR qui la référence.

## 2. Workflow de PR

### Branches

Format : `<type>/<scope>-<courte-description>`. Exemples : `feat/api-pagination-cursor`, `fix/dwh-medias-scd2-dim-parti`, `docs/adr-024-cache-strategy`.

### Conventional Commits — obligatoire

```
<type>(<scope>): <subject>

[body : pourquoi et conséquences]

IA-assistance: <claude-code|cowork|codex|none>
Validation: <pseudo>
```

- Types : `feat`, `fix`, `perf`, `refactor`, `docs`, `test`, `chore`, `ci`, `build`, `style`.
- Breaking change : `feat!` ou footer `BREAKING CHANGE:`.
- Scopes : voir `commitlint.config.js`.
- Subject : ≤ 50 caractères, mode impératif, sans majuscule initiale, sans point final.

### Trace IA obligatoire

Tout commit doit indiquer son niveau d'assistance IA :

- `IA-assistance: claude-code` — édition agentique via Claude Code.
- `IA-assistance: cowork` — alignement / rédaction assistés par Cowork.
- `IA-assistance: codex` — complétion via Codex.
- `IA-assistance: none` — strictement manuel.

Le footer `Validation:` indique l'humain ayant relu et validé. **Tous les commits sont relus**, même les commits IA, par sam ou par un·e contributeur·rice habilité·e.

### Squash & merge

Le commit final après squash respecte les Conventional Commits. Les commits intermédiaires sur la branche peuvent être plus bavards, ils sont écrasés.

### Taille de PR

> Une PR > 500 lignes est un signal de découpage trop tardif. Préférer 2-3 PR successives.

## 3. Domaines de contribution privilégiés

| Domaine | Niveau bienvenu |
|---|---|
| Ajout d'une source publique (avec source card) | **Très bienvenu** |
| Correction de chiffre, d'attribution, de citation | **Très bienvenu** |
| Signalement d'un biais méthodologique | **Très bienvenu**, via `methodology_concern.yml` |
| Amélioration d'accessibilité (RGAA AA) | **Très bienvenu** |
| Traduction / clarification de langage clair | **Bienvenu**, avec attention au respect du sens |
| Nouveau dossier complet | **Différé** post-MVP, discuter en amont via issue |
| Modification de la doctrine RGPD ou de l'architecture audit | **ADR requise**, validée par comité |

## 4. Comité de relecture pluraliste

Les changements suivants passent par le **comité de relecture** :

- Toute modification de `docs/methodology/`.
- Toute publication d'un dossier (`dossiers/<slug>/` avec status `published`).
- Toute ADR superseding une ADR existante.
- Toute modification du module audit personnel touchant l'expérience utilisateur·rice.

Les retours du comité sont **publics** : intégrés ou réfutés explicitement avec justification.

## 5. Reconnaissance

Toute contribution acceptée crédite l'auteur·e (Co-Authored-By dans le commit ou mention `Contributeurs et contributrices` sur le site). Anonymat possible sur demande.

## 6. Pre-commit hooks

Installer les hooks localement :

```bash
uv pip install pre-commit
pre-commit install --hook-type pre-commit --hook-type commit-msg
```

Les hooks lancent : `ruff`, `sqlfluff`, `prettier` (md/yaml/json), `conventional-pre-commit`, et `dbt test` sur les modèles modifiés.

## 7. Tests

| Type | Outil | Localisation |
|---|---|---|
| Unitaires Python | pytest | `services/<svc>/tests/` |
| Unitaires Svelte/TS | vitest | `front-*/src/**/__tests__/` |
| dbt | `dbt test` | `dbt/tests/` |
| Intégration | pytest + testcontainers | `tests/integration/` |
| E2E | Playwright | `tests/e2e/` |
| Accessibilité | axe-core | intégré aux tests E2E |

PR sans test associé est *refusée* sur tout changement de comportement.

## 8. Politique de désaccord

Ce projet a une opinion : *le doute peut être outillé, et la complexité du débat public mérite mieux que des slogans*. Cette opinion est argumentée publiquement dans la page « Qui parle ? » et dans la méthodologie.

Vous pouvez ne pas la partager. Vous pouvez la critiquer publiquement, dans les issues, ou ailleurs. Tant que la critique est **argumentée**, **sourcée**, et respectueuse des personnes, elle est bienvenue.

Voir [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) pour le cadre interpersonnel.

## 9. Contact

- Issues : <https://github.com/aporiapolis-project/aporiapolis/issues>.
- DPO / RGPD : `dpo@aporiapolis.org` (à activer).
- Sécurité : `security@aporiapolis.org` (à activer) — voir [SECURITY.md](SECURITY.md).
