# ADR-0025 — Mesure canonique de la concentration médiatique

**Date** : 2026-05-16
**Statut** : accepted
**Décideur(s)** : sam, validé après pré-relecture par personae IA (chercheuse-sic + sociologue-quantitatif)
**Supersedes** : —
**Superseded by** : —

## Contexte

Le dossier *Médias français* (premier dossier MVP d'AporiaPolis) doit mesurer la « concentration médiatique » comme objet central de la sous-question 1 (« Qui possède et qui contrôle les médias français ? ») et comme arrière-plan de plusieurs autres sous-questions.

La pré-relecture de la note de cadrage v0.1 par les personae IA (strate 1) a fait apparaître une **convergence forte de deux profils différents** (chercheuse en SIC, sociologue/politiste quantitatif·ve) sur un même point : le mot « concentration » regroupe en réalité plusieurs phénomènes distincts dans la littérature académique et dans les régulations, qui ne se recouvrent pas systématiquement et qui ne se mesurent pas de la même façon. Sans choix méthodologique explicite et figé, le dossier risque :

- des **confusions de niveaux d'analyse** (par exemple : prétendre mesurer la « concentration éditoriale » via la concentration capitalistique, ce que la littérature distingue depuis Schiller 1989 et que Cagé 2015 documente sur le cas français) ;
- des **comparaisons internationales fausses** (les régulateurs concurrence européens et américains utilisent HHI ; les commentateurs grand public utilisent souvent C5 ou C10 ; les agrégats sont incomparables) ;
- des **séries temporelles incomparables** (les indicateurs ACPM ont évolué en 2014 ; les mesures avant et après n'ont pas la même base) ;
- une **fragilité juridique** sur la sous-question 4 (toute affirmation portant sur la « concentration éditoriale » ou sur l'effet de la concentration capitalistique sur l'autonomie éditoriale doit être adossée à un indicateur précisément défini et défendable).

Cette ADR fixe la **doctrine de mesure** que le dossier appliquera.

## Options envisagées

### Option A — Indicateur unique (par exemple C5 : part cumulée des 5 premiers groupes)

Un seul indicateur, simple, lisible.

**Pour** : pédagogie maximale, comparabilité grand public.

**Contre** : perd toute la nuance des quatre niveaux. Reproduit les confusions de la littérature grand public. Indéfendable face à un comité de relecture exigeant.

### Option B — Matrice à 4 niveaux distincts, sans hiérarchie

Mesurer séparément les quatre niveaux (capitalistique, contrôle, éditoriale, audience) sans en privilégier un.

**Pour** : rigueur conceptuelle. Suit la littérature canonique.

**Contre** : produit 4 indicateurs sans hiérarchie d'importance, ce qui complique la lecture grand public et empêche les comparaisons internationales standardisées.

### Option C — Matrice à 4 niveaux + indicateur canonique HHI pour les comparaisons standardisées

Mesurer les quatre niveaux distinctement, **avec un indicateur canonique normé** par niveau (HHI Herfindahl-Hirschman par défaut pour les niveaux capitalistique et audience ; C5 + cartographie de contrôle pour le niveau contrôle ; indicateur composite pour le niveau éditorial).

**Pour** : combine rigueur conceptuelle et comparabilité internationale standardisée. HHI est l'indicateur utilisé par la DG Comp européenne, la FCC américaine, l'Autorité de la concurrence française, le rapport Assouline du Sénat (2022). Permet à la fois la lecture grand public (« 9 propriétaires contrôlent 81 % de la diffusion presse écrite ») et la défense méthodologique (« HHI de 2 380 sur la presse quotidienne nationale, ce qui dépasse le seuil de concentration élevée fixé à 2 000 par la DG Comp »).

**Contre** : plus complexe à expliquer initialement, exige une note méthodologique pédagogique en intro de la sous-question 1.

## Décision

**Option C retenue.** Le dossier *Médias français* mesure la concentration médiatique selon **quatre niveaux distincts**, chacun avec son indicateur canonique :

### Niveau 1 — Concentration capitalistique

**Définition** : qui détient le capital des entités médiatiques ?

**Indicateur canonique** : **HHI (Herfindahl-Hirschman Index)** sur les parts de capital, calculé séparément sur chaque marché pertinent (presse écrite nationale, presse écrite régionale, télévision gratuite, radio, etc.).

**Indicateurs complémentaires** : **C5** (part cumulée des 5 premiers propriétaires) pour la lecture grand public, **C10** pour les marchés plus fragmentés.

**Sources** : déclarations AMF pour les groupes cotés, registres des sociétés (greffes des tribunaux de commerce) pour les non cotés, rapports ARCOM annuels, rapport Assouline (Sénat, 2022).

**Seuils de référence** : HHI < 1 500 = peu concentré ; 1 500-2 500 = modérément concentré ; > 2 500 = très concentré (seuils de la DG Comp européenne, repris par l'Autorité de la concurrence française).

### Niveau 2 — Concentration de contrôle

**Définition** : qui prend effectivement les décisions stratégiques, indépendamment du capital ?

Cette dimension diverge de la concentration capitalistique dans plusieurs cas :
- droits de vote double ou multiple ;
- pactes d'actionnaires ;
- *golden shares* publiques (cas France TV vis-à-vis du Trésor) ;
- présence d'un actionnaire de contrôle minoritaire (cas Bolloré dans Vivendi à plusieurs moments) ;
- contrôle par holding interposé.

**Indicateur canonique** : **cartographie nominative** des entités de contrôle (qui contrôle qui via quel mécanisme), accompagnée d'un **C5 de contrôle** (combien d'entités de contrôle distinctes pour X % du marché).

**Sources** : pactes d'actionnaires déposés à l'AMF, statuts publics des sociétés, enquêtes économiques tierces (*Le Monde* business, *Les Échos*, *Mediapart*, *La Lettre A*), rapports ARCOM, audits de la Cour des comptes pour l'audiovisuel public.

### Niveau 3 — Concentration éditoriale

**Définition** : combien d'entités produisent réellement des contenus éditoriaux distincts ? Au-delà de la propriété, mesurer la mutualisation effective des rédactions, des contenus, des angles.

**Indicateur canonique** : indicateur composite combinant :
- nombre de rédactions distinctes maintenues par groupe propriétaire (vs mutualisation) ;
- existence et pouvoir des SDJ (sociétés de journalistes) — variable qualitative documentée ;
- présence d'une charte éditoriale contraignante avec valeur juridique.

**Sources** : statuts des médias, communiqués SDJ, chartes éditoriales publiques, enquêtes sociologiques (*Devillard et al.*, *Le Champion*, Acrimed).

**Note importante** : ce niveau **ne se quantifie pas en un score unique**. Il se mesure via une **cartographie qualitative documentée**, présentée comme telle. Toute tentation de le réduire à un chiffre serait méthodologiquement contestable et juridiquement exposée.

### Niveau 4 — Concentration d'audience

**Définition** : combien d'entités captent effectivement l'audience du public ? Indépendamment de la propriété et du contrôle.

**Indicateur canonique** : **HHI sur les parts d'audience** mesurées par Médiamétrie (TV/radio) ou ACPM (presse écrite, web).

**Indicateurs complémentaires** : **C5 d'audience** pour la lecture grand public, **temps quotidien moyen passé** par segment (Reuters Digital News Report).

**Sources** : Médiamétrie (agrégats publics, le détail n'est pas en open data), ACPM (Audience Internet et Diffusion presse), Reuters Institute DNR pour les comparaisons internationales.

**Caveat méthodologique majeur** : Médiamétrie est un GIE des chaînes et radios mesurées, ce qui pose une question d'indépendance des mesures elles-mêmes (cf. Méadel, *Quantifier le public*, 2010). À documenter dans la source card Médiamétrie et dans la doctrine d'usage de ces données.

## Articulation des quatre niveaux dans le dossier

Sous-question 1 du dossier *Médias français* (« Qui possède et qui contrôle les médias français ? ») se structure autour de ces quatre niveaux :

1. Page principale de la SQ1 : présentation pédagogique des quatre niveaux + leur articulation (un schéma le rend visible).
2. Quatre sous-sections de la SQ1 : une par niveau, avec son indicateur canonique mesuré sur les principaux marchés français.
3. Section transversale : **discordances observées** entre les quatre niveaux (cas où concentration capitalistique forte coexiste avec diversité éditoriale ; cas inverse), avec exemples documentés.

Les autres sous-questions du dossier (SQ2 modèles éco, SQ3 pluralisme à l'antenne, SQ4 indépendance, etc.) **référencent explicitement** le niveau de concentration concerné quand elles s'y rapportent, plutôt que d'utiliser « concentration » sans qualifier.

## Conséquences

### Positives

- **Rigueur conceptuelle** : aligne le dossier sur la littérature académique canonique (Schiller, Cagé, Hallin & Mancini).
- **Comparabilité internationale** : HHI est l'indicateur utilisé partout en Europe et aux US par les régulateurs.
- **Défense méthodologique** : tout contestataire devra contester un indicateur précisément défini, pas une notion floue.
- **Compatibilité avec les seuils réglementaires** : permet de raccrocher les résultats du dossier aux cadres légaux (concentration > 2 500 HHI déclenche un examen renforcé en droit européen de la concurrence).
- **Pédagogie possible** : C5 reste disponible comme outil de lecture grand public, mais comme indicateur *complémentaire* et non *canonique*.

### Négatives

- **Complexité accrue** de la sous-question 1, qui devient la plus dense du dossier. Mitigation : schéma pédagogique en intro, glossaire des indicateurs en annexe.
- **Coût de calcul** : HHI exige des données granulaires (parts détaillées par acteur), ce qui suppose une ingestion soignée. Implication pour la source card ACPM / Médiamétrie / ARCOM.
- **Concentration éditoriale qualitative** : pas de chiffre synthétique, ce qui peut frustrer les lecteurs en quête de comparaison immédiate. Mitigation : cartographie visuelle + tableau de scores qualitatifs documentés.

### Conditions de révision

Cette ADR peut être révisée et superseded si :

1. Une autorité de régulation française ou européenne (ARCOM, Autorité de la concurrence, DG Comp) publie une nouvelle doctrine de mesure qui s'impose comme nouveau standard.
2. La littérature académique converge sur un indicateur composite de la « concentration éditoriale » qui n'existe pas aujourd'hui.
3. Les sources publiques (ACPM, Médiamétrie) modifient leur méthodologie en cours de projet, exigeant une mise à jour de la doctrine de calcul.

## Mise en œuvre opérationnelle

### Modèles dbt à prévoir

- `mart_concentration_capitalistique` : HHI + C5 + C10 par marché, par année.
- `mart_concentration_audience` : HHI + C5 + temps d'écoute moyen par marché, par année.
- `dim_groupe_media` (cf. ADR-0028 à venir) : table de correspondance entités → groupe propriétaire effectif, avec SCD type 2 pour gérer les rachats.
- `fact_acquisition_mediatique` : événements de rachat/cession, datés, sourcés.

### Tests dbt obligatoires

- `not_null` sur les colonnes pivot (date, marché, indicateur).
- `accepted_range` : HHI entre 0 et 10 000 ; C5 entre 0 et 100.
- `relationships` entre `mart_concentration_*` et `dim_groupe_media`.
- `unique` sur la clé naturelle (date × marché × niveau).

### Page dossier

La page principale de la SQ1 inclut :
1. Schéma pédagogique des 4 niveaux.
2. Tableau de bord interactif (ou statique en V1) avec les 4 indicateurs canoniques sur les principaux marchés.
3. Section « Discordances observées » avec exemples documentés (par exemple : Bolloré dans Vivendi, où la concentration capitalistique est très forte mais où la SQ examine les implications éditoriales effectives).
4. Section « Limites » exposant les caveats Médiamétrie GIE et concentration éditoriale qualitative.

### Sources cards à créer ou enrichir

- `docs/sources/acpm.md` : ajout des indicateurs ACPM de diffusion par groupe propriétaire.
- `docs/sources/mediametrie.md` (à créer) : caveat GIE explicite.
- `docs/sources/amf.md` (à créer) : pour les déclarations actionnariat des groupes cotés.
- `docs/sources/sociétés-greffes.md` (à créer) : pour les non cotés.

## Notes pour les implémenteurs

- **Avant toute publication impliquant un chiffre HHI ou C5**, faire une revue rapide avec un·e économiste de la concurrence si possible (la persona `sociologue-quantitatif` peut faire cette revue en strate 1 ; le comité humain en strate 2 idéalement avec un·e économiste).
- **Les seuils HHI de la DG Comp** (1 500 / 2 500) sont des seuils pour les *concentrations* (fusions, acquisitions), pas des seuils prescriptifs pour le pluralisme médiatique. Les mentionner avec ce caveat : un HHI au-dessus de 2 500 n'est *pas* en soi illégal, c'est un signal qui justifie un examen.
- **Caveat permanent sur Médiamétrie GIE** : à inclure systématiquement quand des données d'audience TV/radio sont citées. C'est une discipline éditoriale.
