# Politique de sécurité

## Versions supportées

Le projet est en phase pre-MVP. La seule version supportée est la branche `main`. Une fois la V1 publiée, les politiques de maintenance LTS seront documentées ici.

| Version | Supportée |
|---|---|
| `main` (HEAD) | ✅ |
| Tags antérieurs à `v1.0.0` | ❌ (non recommandé pour usage en production) |

## Signaler une vulnérabilité

> **Ne pas ouvrir d'issue publique pour une vulnérabilité de sécurité.** Préférer le canal privé ci-dessous.

Envoyer un email à `security@aporiapolis.org` (à activer dès le déploiement de l'infrastructure).

Inclure dans le signalement :

- Type de vulnérabilité (RCE, XSS, SQLi, IDOR, exposition de données, etc.).
- Composant concerné (service, endpoint, fichier).
- Étapes de reproduction.
- Impact estimé.
- Conditions préalables (utilisateur authentifié, configuration spécifique, etc.).
- Vous-même : pseudonyme ou nom pour reconnaissance, anonymat respecté sur demande.

## Engagements

- **Accusé de réception** sous 5 jours ouvrés.
- **Première évaluation** sous 14 jours.
- **Correction** : selon la sévérité (CVSS), de 7 jours (critique) à 90 jours (basse).
- **Divulgation responsable** : nous publions une *advisory* après correction, avec crédit au rapporteur (sauf demande contraire), via le mécanisme GitHub Security Advisories.

## Hors périmètre

Les éléments suivants sont *hors* périmètre du signalement de sécurité :

- Faux positifs des scanners automatisés sans démonstration d'impact.
- Manque d'en-têtes HTTP non liés à un risque concret démontré.
- Vulnérabilités sur des services tiers (Cloudflare, Scaleway, GitHub) — signaler directement au fournisseur.
- Phishing ou ingénierie sociale ciblant les contributeurs.
- Issues de confidentialité résolues par l'architecture **local-only** du module audit personnel (voir [ADR-0021](docs/adr/0021-audit-personnel-architecture.md)).

## Pas de bug bounty

Ce projet est porté en solo sur fonds propres et certifié par un dispositif de formation. **Il n'y a pas de bug bounty financier.** La reconnaissance se fait par :

- Crédit dans la *Security Advisory* publique (avec consentement).
- Mention dans une page « Remerciements sécurité » sur le site (à venir).
- Recommandation publique sur LinkedIn / Mastodon / Bluesky si pertinent.

## Bonnes pratiques attendues des contributeurs

- Pas de secret en clair dans le repo, jamais — même pour un test (`sops` + `age` pour les configurations sensibles).
- Toute dépendance externe ajoutée doit être vérifiée (`pip-audit`, `npm audit`, `trivy`).
- Les commits touchant aux données personnelles incluent le footer `DPIA: oui` et déclenchent une revue manuelle.
- L'architecture **local-only** du module audit personnel (ADR-0021) ne peut être contournée même temporairement pour un debug — tout calcul reste côté navigateur, aucune réponse Likert ne transite vers le serveur.

## Contact

`security@aporiapolis.org` (à activer).

Clé PGP : à publier ici une fois générée et déposée sur un keyserver public.
