<!--
PR Template — AporiaPolis.
Le titre de la PR doit suivre Conventional Commits (ex : feat(api): add cursor pagination).
Le commit final après squash & merge sera ce titre + le corps ci-dessous.
-->

## Pourquoi

<!-- Brève explication du besoin métier ou technique (2-4 lignes max). -->

## Quoi

<!-- 3-5 puces : ce qui change. Pas de "what" du code, le diff parle. Ce qui est intéressant : le scope, les fichiers structurants. -->

-
-

## Comment vérifier

<!-- Étapes pour valider en local ou en staging. Inclure les commandes exactes si pertinent. -->

```bash

```

## Impact

- [ ] Breaking change ? Si oui, le commit final contient `BREAKING CHANGE:` détaillé.
- [ ] Modifie le schéma BDD / DWH ? Migration fournie et testée à blanc.
- [ ] Modifie une API publique ? OpenAPI à jour et changelog API noté.
- [ ] Touche aux données personnelles ? Footer `DPIA: oui` sur le commit final et DPIA mise à jour si nécessaire.
- [ ] Affecte la méthodologie publique (`docs/methodology/`) ? Changelog méthodo publié, comité de relecture saisi.
- [ ] Affecte l'accessibilité ? Tests axe-core passés, vérification manuelle NVDA documentée si page critique.
- [ ] Touche au module audit personnel ? Architecture local-only **non contournée** (cf. [ADR-0021](docs/adr/0021-audit-personnel-architecture.md)).
- [ ] Ingère / stocke du contenu de presse ? Doctrine de rétention respectée (cf. [ADR-0022](docs/adr/0022-doctrine-retention-presse.md)).

## Trace IA

Indiquer l'assistance réellement utilisée. Le commit final doit refléter ce choix dans son footer `IA-assistance:`.

- Assistance IA : <!-- outil(s) utilisé(s), rôle, ou « aucune » -->

## Tests

- [ ] Tests unitaires ajoutés ou modifiés (`pytest` / `vitest`).
- [ ] Tests dbt passants (`dbt test`).
- [ ] Tests d'intégration mis à jour si pertinent.
- [ ] Tests e2e Playwright si front impacté.
- [ ] Linters (`ruff`, `sqlfluff`, `mypy`, `prettier`) verts en local.

## Documentation

- [ ] `README.md` / `CLAUDE.md` à jour si pertinent.
- [ ] ADR ajoutée si décision structurante (numérotation continue).
- [ ] Source card mise à jour si ingestion impactée.
- [ ] Page du dossier impactée mise à jour.
- [ ] Changelog éditorial du dossier (`dossiers/<slug>/CHANGELOG.md`) si modification publique du dossier.

## Issues liées

Closes #
Refs #

<!--
Footer recommandé à inclure dans le commit final (squash) :

  IA-assistance: <outil-utilisé|none>
  Validation: <pseudo, par défaut sam>
-->
