# ADR-0021 — Architecture autorisée pour l'audit personnel

**Date** : 2026-05-XX (à la création du repo)
**Statut** : accepted
**Décideur(s)** : sam, comité de relecture (consultatif)
**Supersedes** : —
**Superseded by** : —

## Contexte

Le module *audit personnel* d'AporiaPolis permet à un·e utilisateur·rice de déclarer ses positions sur les sous-questions des dossiers publiés, et de recevoir en retour :
- un score de cohérence interne,
- un alignement chiffré avec les programmes des principaux partis,
- une détection automatique des contradictions logiques cross-dossiers via parcours du graphe de connaissances,
- la possibilité de partager une « carte de cohérence » synthétique.

Les positions politiques (favorables, défavorables, neutres sur des questions politiques contestées) constituent des **catégories particulières de données** au sens de l'**article 9 RGPD**. Leur traitement est interdit par principe, sauf exception strictement encadrée (consentement explicite, données manifestement rendues publiques par la personne, etc.).

La CNIL impose qu'une **Analyse d'Impact relative à la Protection des Données (AIPD)** soit menée **avant la mise en œuvre** de tout traitement à risque élevé. Les opinions politiques + le profilage potentiel (le système produit une « caractérisation » de l'utilisateur·rice) cumulent les critères qui en font un traitement à risque élevé sans ambiguïté.

Cette ADR fixe l'**architecture autorisée** du module avant toute story d'implémentation. Tant qu'elle n'est pas signée, l'EPIC N du backlog v2 reste en statut `blocked-by-design`.

## Options envisagées

### Option A — Architecture serveur avec persistance durable

Sessions utilisateur stockées en base, réponses Likert conservées, calculs côté serveur, possibilité de « reprendre mon audit » entre appareils, statistiques d'usage agrégées, partage de la carte de cohérence via lien public.

**Pour** : flexibilité maximale, fonctionnalités riches (reprise multi-appareils, statistiques publiques, communauté).

**Contre** :
- Traitement de données sensibles au sens article 9 par AporiaPolis comme responsable de traitement.
- AIPD complète obligatoire avant lancement, avec consultation potentielle de la CNIL si risque résiduel élevé.
- Base de licéité étroite : seul l'article 9.2.a (consentement explicite, libre, spécifique, éclairé, univoque) est applicable raisonnablement. Ce consentement doit pouvoir être retiré à tout moment.
- Architecture de minimisation contraignante (pas de logs IP en clair, durées de conservation courtes documentées, anonymisation rapide).
- Sécurité renforcée nécessaire : chiffrement at-rest, audit log, MFA admin obligatoire, pen test régulier.
- Vulnérabilité réputationnelle : une fuite de positions politiques utilisateurs serait catastrophique pour la confiance dans le projet.
- Surface d'attaque non négligeable pour un projet à l'audience civique potentiellement visée par des acteurs adverses.

### Option B — Architecture serveur éphémère (≤ 24 h)

Sessions stockées le temps de la complétion (max 24 h), purgées automatiquement, calculs côté serveur, partage par export uniquement.

**Pour** : compromis entre confort utilisateur (reprise courte) et minimisation.

**Contre** :
- Reste un traitement de données sensibles par le responsable → AIPD obligatoire, même si plus légère.
- Audit log toujours nécessaire.
- Implémentation à peine plus simple que l'option A.
- Bénéfice fonctionnel mince (reprise sur 24 h, peu d'intérêt réel).

### Option C — Architecture local-only (calcul côté navigateur)

Les données du graphe (dossiers, sous-questions, positions des partis, indicateurs) sont chargées en lecture depuis l'API publique. L'utilisateur·rice répond dans le navigateur. Les calculs (cohérence, alignement, contradictions) sont effectués en JavaScript dans le navigateur. La session est stockée dans `localStorage` (machine de l'utilisateur, jamais transmise au serveur). Le partage se fait par export JSON volontaire (téléchargement local que l'utilisateur·rice peut diffuser elle/lui-même).

**Pour** :
- AporiaPolis ne traite *aucune donnée personnelle sensible*. Le serveur ne voit jamais les réponses.
- Privacy by design absolu : la donnée ne quitte jamais l'appareil sans action explicite de l'utilisateur·rice.
- Pas de DPIA exhaustive nécessaire pour ce module (notice de confidentialité suffit, expliquant que le calcul est local).
- Surface d'attaque réduite à zéro pour la donnée sensible.
- Aligned avec la sobriété éco-responsable du projet : pas de calcul serveur, pas de stockage, pas de transfert.
- Plus rapide à implémenter en V1.

**Contre** :
- Pas de « reprise d'audit sur un autre appareil ». La perte de `localStorage` (vidage manuel, navigation privée, changement de machine) entraîne la perte de la session.
- Pas de statistiques d'usage côté projet (combien d'audits réalisés, sur quels dossiers, etc.).
- Pas de carte sharable hébergée sur nos serveurs. L'utilisateur·rice exporte sa carte (JSON ou image générée localement), libre à elle/lui de la diffuser.
- Volume du graphe à charger côté client : à dimensionner soigneusement pour rester sobre.

### Option D — Renoncer au module audit personnel

**Pour** : zéro risque juridique. Allègement du périmètre projet.

**Contre** : perte de la fonctionnalité différenciante la plus virale et la plus pédagogique du projet. Atrophie significative de la proposition de valeur.

## Décision

**Option C — Architecture local-only** pour la V1 du module audit personnel.

Le module est implémenté entièrement côté client. Aucune donnée d'utilisateur·rice (réponses Likert, scores, alignements, contradictions) ne transite ni n'est stockée sur les serveurs AporiaPolis. Le serveur sert uniquement des données métier publiques en lecture (graphe, positions des partis, indicateurs) via l'API REST.

## Conséquences

### Positives

- AporiaPolis n'est **pas responsable de traitement** au sens RGPD pour les positions politiques saisies par les utilisateur·rice·s. Le projet est responsable de traitement uniquement pour les éventuelles traces serveur (logs anonymisés, métriques d'audience site général via Plausible), qui restent dans le périmètre habituel d'un site public.
- Pas de DPIA spécifique au module audit obligatoire. La mention dans la notice de confidentialité globale suffit.
- Surface d'attaque pour données sensibles : nulle côté serveur.
- Cohérence éthique : le projet *démontre par son architecture* qu'il prend la protection des données politiques au sérieux. Argument fort éditorialement et pédagogiquement.
- Implémentation V1 plus rapide et plus simple.
- Sobriété énergétique : le serveur ne calcule rien pour le module audit.

### Négatives

- Pas de reprise de session entre appareils. L'utilisateur·rice qui change de machine ou de navigateur perd son audit en cours. **Atténuation** : possibilité d'export volontaire au fil de l'eau, l'utilisateur·rice peut sauvegarder son JSON et le ré-importer ailleurs.
- Pas de carte partagée hébergée. **Atténuation** : génération d'une image carrée 1080×1080 côté client à partir du JSON, l'utilisateur·rice télécharge et publie où il/elle veut (Twitter, Bluesky, Mastodon, etc.).
- Pas de statistiques d'usage côté projet. **Atténuation acceptable** : c'est le prix de la confidentialité totale. Si une mesure agrégée d'usage devient nécessaire, elle se fera via une télémétrie *opt-in* et *anonyme* (ex. nombre d'audits commencés/complétés sans aucune trace du contenu), à formaliser dans une ADR ultérieure.
- Le poids du graphe chargé côté client doit rester maîtrisé. **Atténuation** : ne charger en client que les structures du graphe utiles à l'audit (un sous-ensemble agrégé), pas l'intégralité des données du DWH.

### Conditions de révision

Cette ADR peut être révisée et superseded par une ADR ultérieure si :

1. Un cas d'usage massif émerge nécessitant une persistance serveur (par exemple : intégration avec un partenariat de recherche académique encadré, étude longitudinale formalisée).
2. Une AIPD complète est conduite selon méthodologie CNIL, validée par un·e DPO certifié·e externe, et publiée publiquement.
3. Un module de consentement explicite RGPD article 9.2.a est implémenté avec interface UX maquettée, possibilité de retrait à tout moment, durée de conservation explicitement choisie, doctrine de minimisation documentée, et audit log immuable.
4. Le comité de relecture pluraliste donne un avis favorable explicite à la bascule.

Sans la conjonction de ces quatre conditions, cette ADR reste en vigueur et l'architecture serveur reste interdite.

## Spécifications techniques minimales (pour l'implémentation V1)

### Front

- Framework : Svelte 5 + TypeScript (SPA).
- Routing : SvelteKit ou file-based router compatible Svelte 5.
- État : Svelte stores (réactifs), pas de Redux ni équivalent.
- Calculs : modules TypeScript purs, testables unitairement.
- Persistance : `localStorage` du navigateur uniquement. Pas d'IndexedDB côté projet (peut être utilisé si volumétrie justifie, mais reste local).
- Pas de service worker pour persistence offline (V2 si pertinent).

### Données chargées depuis le serveur (lecture seule, anonymes)

- Liste des dossiers publiés (slug, titre, version).
- Liste des sous-questions par dossier (avec les 3 propositions Likert).
- Positions des partis par sous-question (SCD2, version courante par défaut, historique disponible si l'utilisateur·rice le demande).
- Indicateurs et tests de réalité (pour informer l'utilisateur·rice pendant le questionnaire).
- Graphe simplifié des liens entre sous-questions (pour détecter les contradictions cross-dossiers).

Ces données sont **publiques**, déjà servies par l'API REST pour le site public. Pas de surcharge data ni de stockage spécifique au module audit.

### Calculs effectués localement

- Score de cohérence interne : agrégation pondérée des positions sur les sous-questions × propositions.
- Alignement par parti : produit scalaire entre vecteur utilisateur·rice et vecteur parti, normalisé.
- Détection de contradictions : parcours du graphe simplifié, identification des paires de positions logiquement tendues.
- Génération de la carte de cohérence : visualisation SVG inline, exportable en PNG via Canvas.

### Sortie / partage

- Export JSON : structure de la session (réponses Likert, scores calculés, version méthodologique utilisée). Téléchargement local.
- Export PNG : carte de cohérence visuelle 1080×1080 générée localement via Canvas.
- Pas de bouton « publier sur X » ou équivalent natif côté projet. L'utilisateur·rice utilise ses propres outils pour partager où il/elle veut.

### Communication réseau

- Lecture seule depuis l'API publique d'AporiaPolis pour charger les données du graphe (mises en cache côté navigateur via headers HTTP standards).
- **Aucun POST contenant des données d'utilisateur·rice** vers les serveurs AporiaPolis.
- Pas de pixels tiers, pas de tracking, pas d'analytics spécifique au module.

### Télémétrie

- **Interdite** pour le module audit personnel V1.
- Plausible (analytics du site général) ne place pas de cookies et n'individualise pas les visites. Acceptable au niveau du site, mais aucun event spécifique à l'audit ne doit être envoyé.
- Si à terme un comptage agrégé du nombre d'audits réalisés est souhaité, il devra faire l'objet d'une ADR de révision et d'une implémentation strictement anonyme et opt-in.

## Synthèse à publier sur `/legal/audit-personnel`

Texte à publier sur le site, à valider par le comité de relecture avant publication :

> **Comment fonctionne l'audit personnel — protection de vos données.**
>
> AporiaPolis a fait un choix radical : **vos réponses ne quittent jamais votre navigateur**. L'intégralité du module d'audit personnel — questionnaire, calculs de cohérence, alignements avec les partis, détection de tensions logiques — est exécutée localement sur votre appareil.
>
> Concrètement, cela signifie que :
>
> - Nous ne collectons aucune de vos réponses sur nos serveurs.
> - Nous ne stockons aucun résultat associé à votre identité.
> - Nous ne savons pas combien de personnes ont fait l'audit ni quels résultats elles ont obtenus.
> - Vous restez maître de votre carte de cohérence : vous pouvez la télécharger (JSON ou image), la partager où vous voulez, ou ne rien en faire.
>
> Cette architecture découle d'un choix éthique assumé : les opinions politiques sont des données particulièrement sensibles au regard du RGPD, et le seul moyen de garantir leur protection est de ne *jamais* les transmettre. Le coût de ce choix est que vous ne pouvez pas reprendre un audit entamé sur un autre appareil. Nous estimons que ce coût est largement préférable au risque qu'une fuite de positions politiques agglomérées ferait peser sur la communauté.
>
> Cette doctrine est formalisée dans notre ADR-0021, publique et révisable uniquement par décision documentée. Vous pouvez consulter l'ADR ici : [lien].

## Notes pour les implémenteurs

- Les tests d'intégrité de l'algorithme de calcul doivent être *publics* (suite pytest ou vitest dans le repo, exécutable depuis un clone fresh) pour permettre à n'importe qui de vérifier que les scores sont reproductibles.
- La documentation méthodologique (`/methodologie/audit-personnel`) doit expliciter chaque formule de calcul, chaque pondération, chaque biais connu — c'est la *garantie* qui remplace l'audit DPO.
- Le code du module doit éviter toute dépendance npm tierce non auditée et non essentielle (réduire les risques chaîne d'approvisionnement).
