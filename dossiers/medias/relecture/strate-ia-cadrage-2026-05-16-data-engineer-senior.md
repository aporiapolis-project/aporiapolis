---
slug: relecture-strate-ia-cadrage-medias-data-engineer-senior
title: Pré-relecture IA strate 1 — Cadrage Médias français v0.1 (Data Engineer senior)
document_relu: dossiers/medias/cadrage.md
version_relue: v0.1
persona: data-engineer-senior (v1)
persona_path: docs/methodology/personae-ia/data-engineer-senior.md
session_date: 2026-05-16
auteur_session: sam
statut: brut (non arbitré)
---

# Pré-relecture *Cadrage du dossier Médias français v0.1* — Persona Data Engineer senior

> **Statut** : retour brut de session IA, archivé avant arbitrage. Pipeline prévu en §12 du cadrage : strate 1 IA → arbitrage auteur → v0.2 → strate 2 comité humain.
>
> **Doctrine** : ADR-0024 (relecture deux strates).
>
> **Posture de la persona** : pragmatique, MVP solo, 12 mois, budget contraint. Évaluation centrée sur faisabilité data, rigueur d'ingénierie, risques d'exécution. Pas de jugement sur la pertinence éditoriale (hors champ).

---

## 1. Solide techniquement

- **Cadrage source / aval bien distingué**. La section 7 sépare correctement les sources structurées (API/fichier), les scrapings, et les sources qualitatives à citer mais non ingérer. C'est exactement le bon réflexe pour éviter de bricoler un pipeline sur ce qui devrait rester une note de bas de page.
- **Posture méthodologique « ne pas trancher »** (section 1) : sain. En data, refuser de conclure quand la donnée ne le permet pas évite 80 % des bashings post-publication. Ça correspond aussi à la doctrine de tests de réalité avec issue « non concluant » (section 4, test 10).
- **Reportage de la sous-question 8 en V2 via score RICE** (section 5) : c'est exactement le type d'arbitrage qu'on aimerait voir plus souvent. Confidence faible × Effort fort → reporter. Bien.
- **Limites assumées explicites** (section 8) : la mention « Common Crawl bloqué par gate juridique ADR-0022 » montre que la dépendance entre éditorial et infra est tracée. C'est ce qu'on cherche.
- **Risques propres au dossier listés** (section 10) : la mitigation « Validation par persona journaliste avant publication » est concrète. Pas du blabla.

## 2. À tester / observer avant production

- **Test de réalité 7 (« financement audiovisuel public FR vs voisins »)** : tu écris « réfuté probablement (...) À sourcer précisément ». Ne publie pas sans avoir résolu ce point. Si la conclusion par défaut surprend, c'est qu'il y a une variable cachée (périmètre du périmètre public ? avant/après réforme CAP en 2022 ?). À tester sur **deux sources indépendantes minimum** avant d'écrire quoi que ce soit.
- **Test de réalité 3 (« confiance des Français »)** : tu mentionnes que Reuters et Kantar utilisent des modes de collecte différents (online auto-recruté vs face-à-face). C'est un bug méthodologique connu sur ce genre de longitudinal. À traiter dans un script de transformation dbt qui **conserve les deux séries en parallèle**, avec un mart `mart_confiance_medias` qui matérialise les deux et un test `accepted_values` sur la colonne `source_enquete`. Ne jamais consolider en moyenne pondérée — ce serait une fausse précision.
- **Reproductibilité « clone fresh + `make reproduce` »** (section 6) : objectif bien posé. À tester réellement au moins une fois par mois sur une VM fraîche dès T2. Sinon, c'est une promesse sur le papier qui se brisera silencieusement.
- **Couverture des sources critiques** : pour ARCOM, ACPM, DGMIC, prévoir un test dbt `freshness` (warn si > 7 jours pour ARCOM hebdo, > 90 jours pour DGMIC annuel). Sinon tu publieras avec des données périmées sans le savoir.

## 3. Over-engineering détecté

- **47 sources tracées** (section 6, mesurable) : ce chiffre semble venir d'un comptage exhaustif et non d'un arbitrage. Un dossier MVP solo peut largement tenir avec **20-25 sources primaires bien instrumentées** plutôt que 47 traitées en surface. Risque : tu vas passer T2 à instrumenter au lieu de rédiger. Ré-arbitrer : combien de sources sont *load-bearing* pour les tests de réalité retenus ? Le reste devient *citation*, pas *ingestion*.
- **Cartographie 12 partis × 2-3 versions historiques** (section 7, scrapings) : 24-36 documents à scraper, à classifier, à versionner. Sur un MVP solo, c'est probablement le scope le plus gourmand en temps caché. Si l'analyse sert uniquement la sous-question 4 et un encart de critique de cohérence, **8-10 partis × version actuelle uniquement** suffit en V1. Versions historiques en V2.
- **« Classification d'angles via NLP » sur Common Crawl V2** (section 1) : bien que reporté V2, garde l'arbitrage en tête. Si tu envisages ça avec un LLM en prod, tu auras besoin d'un pipeline d'évaluation (échantillon labellisé, accord inter-annotateurs, métriques type F1). Ça veut dire 200-400 heures de travail caché en plus, **avant** d'avoir le moindre résultat publiable. À sortir du périmètre publicly-claimed tant que ce n'est pas chiffré.

## 4. Under-engineering détecté

- **Pas de mention de schéma source / staging / marts** dans la note. Tu cites les sources mais pas leur destination dans le warehouse. Sur un dossier qui croise ARCOM + ACPM + DGMIC + Reuters + RSF, le risque de drift de schémas et de **mauvaises jointures sur des clés naturelles non normalisées** (un groupe média « Vivendi » vs « Vivendi SE » vs « Bolloré » selon la source) est élevé. À traiter par un mart `dim_groupe_media` avec table de correspondance versionnée. À documenter dans une ADR avant que les pipelines tapent dedans.
- **Pas de stratégie d'idempotence sur les ingestions**. ARCOM publie hebdomadairement, ACPM trimestriellement, DGMIC annuellement. Que se passe-t-il si tu rejoues l'ingestion de mars 2026 en juin 2026 et que la source a corrigé un chiffre rétroactivement ? Pas adressé. À cadrer : politique de re-ingestion, snapshot dbt sur les tables où la rétro-correction est probable.
- **Pas de mention de tests dbt sur les marts du dossier**. La section 6 cite Lighthouse et axe-core (côté front), pas de cible côté data. Au minimum : `not_null` sur les colonnes pivot des marts publiés, `unique` sur les clés naturelles, `relationships` entre marts liés, `accepted_range` sur les % et les comptes. Sinon, premier samedi après publication à corriger des NULL ou des divisions par zéro.
- **Pas de gestion explicite des sources qui changent de méthodologie en cours de projet** (mentionné en section 10 mais sans mitigation technique). Solution : matérialiser une colonne `methodology_version` ou `source_version` dans le staging, et **bloquer la promotion en mart** si elle change sans validation manuelle. Sinon, série temporelle silencieusement cassée.
- **Aucune mention du droit de réponse côté technique**. La section 10 mentionne « Droit de réponse mentionné » comme mitigation du risque diffamation. Mais quel mécanisme ? Un changelog public versionné par dossier ? Une page `/droit-de-reponse/` ? Une procédure éditoriale ? À documenter avant publication, pas après le premier contentieux.

## 5. Dette technique acceptable vs critique

**Acceptable (laisser en V2)** :

- L'analyse Common Crawl est reportée — bien.
- L'audit personnel multi-dossiers reporté — bien.
- Le MCP server `mcp-data` reporté — bien.
- Sous-question 8 (fact-checking) reportée — bien.

**Critique (bloquant MVP)** :

- L'absence de `dim_groupe_media` et de table de correspondance des entités (cf §4). Sans ça, les jointures vont produire des résultats faux silencieusement. À traiter en T1 ou tôt T2.
- L'absence de tests dbt sur les marts publiés. À traiter en même temps que la rédaction des pipelines.
- La résolution du test de réalité 7 (financement audiovisuel public). Si tu publies avec une conclusion fausse, c'est l'angle d'attaque idéal pour discréditer le dossier entier. Priorité.
- L'absence d'une politique d'idempotence et de snapshots sur les sources sujettes à rétro-correction. Au minimum un ADR.

## 6. Coût opérationnel à chiffrer

- **Scraping des programmes des partis** : combien d'heures de maintenance par version ? Les sites des partis changent de structure régulièrement. Prévoir un budget de maintenance trimestriel, ou réduire le périmètre.
- **Veille sur les changements de méthodologie ARCOM/ACPM/DGMIC** : qui regarde, à quelle fréquence ? Si c'est toi seul, c'est ~2-4 heures par trimestre. Acceptable, mais à budgéter.
- **Hébergement des données** : 47 sources × histo annuel × marts → on parle probablement de < 10 Go. Postgres + objet froid (Scaleway / S3 équivalent) suffit largement pour < 5 €/mois. Pas un sujet de coût matériel, mais coût de **temps d'exploitation** sur l'année : prévoir 2-3 heures/mois en MVP, 4-6 heures/mois après publication (alertes, corrections).
- **Pré-relecture IA strate 1 par 5 personae sur dossier complet** (semaine 43) : prévoir le temps d'arbitrage post-IA. 5 personae × ~1500 mots de retour = 7500 mots à digérer. Compte 1-2 jours pleins, pas une demi-journée.

## 7. ADR manquantes

Décisions structurantes que je vois prises ou implicites dans le cadrage, sans ADR référencée :

- **ADR sur la doctrine de mesure de la concentration capitalistique** : audience cumulée, part de diffusion, part de revenus, part de contrôle... lequel est l'indicateur canonique du dossier ? Décision à figer avant l'ingestion, sinon ré-arbitrage tard dans le projet.
- **ADR sur la définition opérationnelle de « média indépendant »** (sous-question 5). Périmètre flou, contesté. Sans définition figée et versionnée, le test de réalité 2 est ininterprétable.
- **ADR sur la politique de snapshots et de rétro-corrections des sources** (cf §4).
- **ADR sur la table de correspondance des entités groupe / titre / média** (`dim_groupe_media`).
- **ADR sur la doctrine du droit de réponse** côté technique et éditorial (cité en section 10 sans procédure).

ADR-0021 (audit personnel), 0022 (rétention presse), 0023 (organisation GitHub), 0024 (deux strates de relecture) sont citées et bien intégrées — c'est cohérent. Mais les 5 décisions ci-dessus émergent de ce cadrage et n'ont pas leur ADR.

## 8. Biais de ma critique

- **Pragmatisme orienté production** : je vais minimiser la valeur pédagogique de certains choix (scraper 12 partis × 3 versions est probablement aussi un exercice de démonstration de compétences pour la certif, pas seulement de la livraison MVP). Garde la décision finale au niveau certif, pas au niveau ROI ingénierie pur.
- **Aversion à l'over-engineering** : ma proposition de « 20-25 sources au lieu de 47 » est instinctive. C'est peut-être faux pour ce dossier précis si la rigueur méthodologique exige cette couverture. Re-challenger : combien sont *load-bearing* pour les tests de réalité retenus ? Si c'est > 35, garde tout.
- **Standardisme** : je propose dbt tests, snapshots, ADR par défaut. C'est ma norme de scaleup, pas forcément ce qui est rentable sur un projet solo. Mais sur les marts publiés au public, je tiens : pas de tests = bug en production garanti.
- **Indifférence au métier** : je n'ai rien dit sur la pertinence éditoriale de la sous-question 7 (comparaison internationale) ou sur la question principale. Pas mon champ premier. Garde à l'esprit qu'un dossier techniquement parfait sur la mauvaise question reste un mauvais dossier.

---

## Synthèse en une ligne

La pré-note est solide sur la posture méthodologique et les arbitrages explicites (RICE, V1/V2, limites assumées). Les angles morts sont côté pipeline data : modélisation des entités, tests qualité, idempotence, et 5 ADR émergentes. Le périmètre semble légèrement sur-dimensionné (47 sources, 36 documents partis) pour un MVP solo sur 6 mois.

---

## Annexe — Points à arbitrer pour la v0.2

Liste actionnable que l'auteur peut reprendre après synthèse des 5 personae :

1. Ré-arbitrer le périmètre des sources (47 → cible *load-bearing* uniquement).
2. Ré-arbitrer le périmètre des programmes scrapés (12 × 3 versions → 8-10 × version actuelle pour V1).
3. Créer 5 ADR émergentes (concentration, média indépendant, snapshots, dim_groupe_media, droit de réponse).
4. Ajouter une section « Cible data quality » au paragraphe 6 (tests dbt, freshness, snapshots) à côté des cibles front (Lighthouse, axe-core).
5. Résoudre en priorité le test de réalité 7 (financement audiovisuel public) avec 2 sources indépendantes avant rédaction.
6. Documenter le mécanisme technique du droit de réponse (page, changelog, procédure).

---

## Métadonnées de session

- **Date** : 2026-05-16
- **Persona** : `data-engineer-senior` v1
- **Document relu** : `dossiers/medias/cadrage.md` v0.1
- **Mode** : conversation Cowork unique, retour direct (pas d'allers-retours)
- **Prochaine étape (auteur)** : arbitrer les remarques (accepter / rejeter / différer avec motif) et produire `cadrage.md` v0.2. Croiser avec les 4 autres retours de personae IA (`chercheuse-sic` déjà archivé sous `strate-ia-cadrage-2026-05-16.md`, restent `journaliste-independant`, `sociologue-quantitatif`, `lecteur-profane`) avant de soumettre la v0.2 au comité humain.
