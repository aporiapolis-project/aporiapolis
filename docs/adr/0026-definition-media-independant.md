# ADR-0026 — Définition opérationnelle de « média indépendant »

**Date** : 2026-05-16
**Statut** : accepted
**Décideur(s)** : sam, validé après pré-relecture par personae IA (chercheuse-sic + journaliste-independant)
**Supersedes** : —
**Superseded by** : —

## Contexte

Le dossier *Médias français* contient une sous-question 5 « L'écosystème des médias indépendants : taille réelle, viabilité ». La pré-relecture par les personae a fait ressortir que le terme **« média indépendant » est un mot-valise** qui regroupe des structures aux modèles juridico-économiques et politiques très différents :

- Mediapart (SCOP depuis 2018, capital ouvert aux salariés, sans publicité, modèle abonnement uniquement) ;
- Reporterre (association puis SCIC, financement par dons et mécénat) ;
- StreetPress (association, financement mixte) ;
- Brut (capital privé classique, ayant reçu des investissements de Xavier Niel et Patrick Drahi à différents moments) ;
- Konbini (capital privé, modèle pub) ;
- Loopsider (capital privé) ;
- *La Lettre A* (capital privé propriétaire familial, modèle abonnement professionnel) ;
- *Politis* (SCIC depuis 2018).

Ces structures **ne sont pas dans le même camp économique ni politique**. Les regrouper sous le label « indépendant » suppose une définition implicite (généralement : « tous ceux qui ne sont pas dans les grands groupes Bolloré / LVMH / Niel / Drahi / Křetínský / Lagardère / Dassault »), définition négative qui n'est pas une catégorie analytique.

La persona chercheuse-sic a proposé d'adopter la **typologie Cagé-Hervé-Mazoyer** (*L'information à tout prix*, INA, 2017) qui distingue les modèles juridico-économiques des médias français de manière documentée. La persona journaliste-independant a confirmé la nécessité de désagréger et insisté sur le fait que les médias indépendants peuvent aussi avoir leurs propres biais (financement militant, choix éditoriaux orientés sans actionnaire, dépendance à un public fidèle).

Cette ADR fixe la **définition opérationnelle** que le dossier utilisera, ainsi que la typologie de classement.

## Options envisagées

### Option A — Définition binaire : indépendant vs grand groupe

Critère : le média est-il filiale d'un des grands groupes consolidés (Bolloré, LVMH, Niel/Le Monde Libre, Drahi/Altice, Křetínský/CMI, Lagardère, Dassault) ?

**Pour** : simplicité, opérationnel rapidement.

**Contre** : reproduit le mot-valise critiqué. Mediapart, Reporterre, *La Lettre A* et Loopsider se retrouvent dans le même camp alors que leurs modèles diffèrent radicalement. Indéfendable face à une relecture académique.

### Option B — Typologie purement juridique

Critère : forme juridique de l'entreprise éditrice (SA, SAS, SARL, association, SCOP, SCIC).

**Pour** : critère factuel et vérifiable (greffes).

**Contre** : ne capture pas la structure capitalistique (une SAS peut être 100 % filiale ou 100 % indépendante). Ne capture pas non plus le modèle économique (publicité, abonnement, mécénat).

### Option C — Typologie tri-dimensionnelle (Cagé-Hervé-Mazoyer adaptée)

Trois axes orthogonaux :

1. **Statut juridique** : SA / SAS / SARL / SCOP / SCIC / association.
2. **Structure capitalistique** : filiale d'un grand groupe consolidé / capital ouvert à des actionnaires institutionnels diversifiés / capital concentré (un actionnaire majoritaire, hors grand groupe consolidé) / capital coopératif (SCOP, SCIC) / capital associatif (à but non lucratif).
3. **Modèle de revenus dominant** : publicité majoritaire / abonnement majoritaire / mécénat-dons majoritaires / aides publiques majoritaires / mixte sans dominance (chaque source < 50 %).

Chaque média analysé est positionné sur ces trois axes. Le terme « indépendant » n'apparaît **pas dans la classification** : à la place, on parle de « médias à capital coopératif », « médias à modèle abonnement majoritaire », « médias non affiliés aux grands groupes consolidés », etc.

**Pour** : rigueur analytique, conformité littérature, désamorce les controverses sémantiques.

**Contre** : plus complexe à présenter au lecteur. Mitigation : page pédagogique avec un exemple concret pour chaque combinaison.

### Option D — Renoncer à la sous-question 5

Supprimer la sous-question, traiter les médias non affiliés aux grands groupes dans la SQ1 et SQ2.

**Pour** : évite la difficulté conceptuelle.

**Contre** : la sous-question correspond à une attente réelle du public et à un objet sociologique légitime. Y renoncer est un appauvrissement.

## Décision

**Option C retenue.** Le dossier *Médias français* adopte la **typologie tri-dimensionnelle** ci-dessous pour positionner chaque média analysé.

### Trois axes de classement

**Axe 1 — Statut juridique** (catégories closes) :
- `SA` — Société anonyme classique
- `SAS` — Société par actions simplifiée
- `SARL` — Société à responsabilité limitée
- `SCOP` — Société coopérative et participative (capital majoritairement salarié)
- `SCIC` — Société coopérative d'intérêt collectif (capital partagé entre plusieurs catégories)
- `Association` — Association loi 1901 ou structure équivalente à but non lucratif
- `Fondation` — Structure de fondation reconnue d'utilité publique

**Axe 2 — Structure capitalistique** (catégories closes, basées sur les déclarations AMF et registres des sociétés) :
- `filiale-grand-groupe` — Filiale ou contrôlée par un des grands groupes consolidés (liste figée dans la source card du dossier)
- `capital-concentre-non-affilie` — Actionnaire majoritaire unique ou famille majoritaire, non affilié à un grand groupe consolidé (par exemple : *La Lettre A* / Indigo Publications, *Politis* avant 2018)
- `capital-disperse` — Capital réparti entre plusieurs actionnaires institutionnels diversifiés, aucun n'ayant le contrôle
- `cooperatif` — SCOP ou SCIC (capital majoritairement salarié ou multi-partite)
- `associatif` — Association à but non lucratif

**Axe 3 — Modèle de revenus dominant** (catégories closes, basées sur les comptes annuels ou déclarations publiques) :
- `publicite-majoritaire` — > 50 % du chiffre d'affaires en publicité
- `abonnement-majoritaire` — > 50 % en abonnements payants
- `mecenat-dons-majoritaire` — > 50 % en dons, mécénat, financement participatif
- `aides-publiques-majoritaires` — > 50 % en aides à la presse, contribution publique au service public, subventions
- `mixte` — Aucune source > 50 % (cas fréquent : pub 30 %, abonnement 30 %, aides 30 %, divers 10 %)

### Application aux médias français

Chaque média analysé dans le dossier est positionné sur les **trois axes** dans un tableau structuré (`dim_media_typologie`), avec sources documentées pour chaque attribut.

**Exemples illustratifs (à valider lors de la rédaction effective du dossier)** :

| Média | Statut juridique | Structure capital | Modèle revenus |
|---|---|---|---|
| Mediapart | SCOP | Coopératif | Abonnement majoritaire |
| Reporterre | SCIC | Coopératif | Mécénat-dons majoritaire |
| StreetPress | Association | Associatif | Mécénat-dons majoritaire |
| Brut | SAS | Capital concentré non affilié (ou filiale selon période — à dater précisément) | Publicité majoritaire |
| *La Lettre A* / Indigo Publications | SAS | Capital concentré non affilié | Abonnement majoritaire (modèle pro) |
| *Le Monde* | SA | Filiale Le Monde Libre (Niel/Bergé/Pigasse) | Mixte |
| TF1 | SA cotée | Filiale Bouygues | Publicité majoritaire |
| France Inter / Radio France | EPIC (établissement public) | Public | Aides publiques majoritaires |
| Mediapart international desk | Filiale Mediapart | Coopératif (par filiation) | Abonnement majoritaire (par filiation) |

### Reformulation de la sous-question 5

La sous-question 5 ne s'intitule plus « L'écosystème des médias indépendants » mais :

> **SQ5 reformulée : « Comment se structure l'écosystème des médias non affiliés aux grands groupes consolidés ? »**

Avec quatre sous-sections :
1. Cartographie par typologie (les trois axes appliqués aux médias non affiliés).
2. Taille réelle (audience, revenus, effectifs).
3. Viabilité économique par typologie (qui tient sur 5-10 ans, qui disparaît).
4. Logique de financement et conséquences éditoriales (avec caveat sur les biais propres : militantisme, dépendance au public fidèle, dépendance aux fondations).

## Conséquences

### Positives

- **Désamorçage de la controverse sémantique** sur « indépendant ». Le mot disparaît de la classification.
- **Rigueur analytique conforme à la littérature** (Cagé, Hervé, Mazoyer).
- **Possibilité de comparaisons précises** : on ne compare plus « Brut et Mediapart » (incomparables en fait), mais « les SAS à capital concentré non affilié à modèle pub majoritaire » entre elles.
- **Anticipation de la critique « les médias indé ont aussi des biais »** : la SQ5 sous-section 4 le traite explicitement, sans en faire un point caché.
- **Données objectives et vérifiables** : les trois axes sont basés sur des déclarations publiques (greffes, AMF, comptes annuels).

### Négatives

- **Complexité pédagogique** : trois axes au lieu d'un label binaire. Mitigation : tableau visuel avec exemples concrets, glossaire des cinq catégories par axe.
- **Coût de classement** : chaque média analysé doit être positionné sur les trois axes, avec sources. Au démarrage, c'est ~20-30 médias à classer.
- **Risque de « catégorisation contestée »** : un média peut contester sa classification (par exemple, un média en `capital-concentre-non-affilie` peut se présenter comme indépendant et contester l'analyse). Mitigation : tout classement est sourcé, la procédure de contestation passe par le droit de réponse (ADR-0029).

### Conditions de révision

Cette ADR peut être révisée si :

1. La littérature académique converge sur une typologie différente.
2. Une régulation française ou européenne (EMFA notamment) impose une typologie standard.
3. Des cas concrets de classement révèlent que les trois axes proposés ne suffisent pas à distinguer des situations significativement différentes (signal : plus de 20 % des médias se retrouvent dans la même cellule de la matrice).

## Mise en œuvre opérationnelle

### Modèles dbt

- `dim_media_typologie` : table dimensionnelle avec les trois axes par média, en SCD type 2 (un média peut changer de typologie au cours du temps — par exemple Mediapart est passé de SAS à SCOP en 2018).
- Tests dbt :
  - `accepted_values` sur chaque axe (limité aux catégories closes définies ci-dessus).
  - `not_null` sur la clé naturelle (media_id × date_effective).
  - `unique` sur la version courante par média.

### Source cards à enrichir

- `docs/sources/amf.md` : pour les déclarations actionnariat des groupes cotés et participations significatives.
- `docs/sources/societes-greffes.md` : pour les statuts juridiques.
- `docs/sources/dgmic.md` : déjà prévu, pour les aides publiques par bénéficiaire (axe 3).

### Page dossier

La SQ5 inclut :
1. Page principale : présentation pédagogique de la typologie tri-dimensionnelle, schéma visuel.
2. Tableau interactif (ou statique en V1) avec les ~20-30 médias retenus pour le dossier, positionnés sur les trois axes.
3. Sous-section « Viabilité par typologie » : courbes de longévité, taux de survie à 5 ans, etc.
4. Sous-section « Logique de financement et biais propres » : examen équilibré des biais possibles dans chaque typologie (pas seulement dans les filiales grand groupe).

### Glossaire à intégrer dans la page « Méthodologie » du site

Définitions courtes et accessibles des cinq catégories par axe, pour le lecteur grand public.

## Notes pour les implémenteurs

- **La liste des « grands groupes consolidés »** doit être figée dans une source card publique (`docs/sources/grands-groupes-mediatiques.md`), avec sources pour chaque groupe (qui contrôle, depuis quand). Cette liste évolue (par exemple, le rachat de Lagardère par Vivendi/Bolloré en 2023 modifie le périmètre).
- **Pour Brut et autres pure players à actionnariat évolutif**, dater précisément les changements de typologie. Le SCD type 2 sur `dim_media_typologie` est conçu pour ça.
- **La distinction filiale-grand-groupe vs capital-concentre-non-affilie** est juridiquement précise mais peut être contestée par les acteurs. La défense méthodologique est : critère = contrôle effectif documenté, pas appartenance déclarée.
- **Pour les médias publics** (France TV, Radio France, INA, Arte, etc.), la classification est `EPIC` côté statut juridique mais l'axe « structure capitalistique » est inapplicable au sens strict ; utiliser une catégorie spéciale `public-EPIC` dans la table avec note.
