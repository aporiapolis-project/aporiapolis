/**
 * commitlint.config.mjs — AporiaPolis
 *
 * Enforces Conventional Commits with the scope list of the project.
 * Triggered by:
 *   - pre-commit hook (conventional-pre-commit on commit-msg stage)
 *   - GitHub Actions workflow (.github/workflows/commitlint.yml) on PRs.
 *
 * Adding a new scope? Update both this file and CLAUDE.md / 10_conventions.md.
 */

export default {
  extends: ['@commitlint/config-conventional'],
  rules: {
    'type-enum': [
      2,
      'always',
      [
        'feat',
        'fix',
        'perf',
        'refactor',
        'docs',
        'test',
        'chore',
        'ci',
        'build',
        'style',
        'revert',
      ],
    ],
    'scope-enum': [
      2,
      'always',
      [
        // Transverse
        'adr',
        'infra',
        'api',
        'mcp',
        'front-public',
        'front-audit',
        'datadeck',
        'dwh',
        'graph',
        'audit',
        'methodo',
        'auto-observation',
        'deps',
        'repo',
        'release',

        // Ingestion par source (élargir au fur et à mesure)
        'ingestion-owid',
        'ingestion-cc',
        'ingestion-hatvp',
        'ingestion-agora',
        'ingestion-arcom',
        'ingestion-insee',
        'ingestion-legifrance',
        'ingestion-assemblee',

        // DWH par dossier
        'dwh-medias',
        'dwh-dette',
        'dwh-climat',

        // Dossiers éditoriaux
        'dossier-medias',
        'dossier-dette',
        'dossier-climat',
        'dossier-meta-ia',
      ],
    ],
    'scope-empty': [2, 'never'],
    'subject-case': [
      2,
      'never',
      ['start-case', 'pascal-case', 'upper-case'],
    ],
    'subject-empty': [2, 'never'],
    'subject-full-stop': [2, 'never', '.'],
    'header-max-length': [2, 'always', 80],
    'body-leading-blank': [1, 'always'],
    'footer-leading-blank': [1, 'always'],
  },
};
