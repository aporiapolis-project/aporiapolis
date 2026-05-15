---
slug: relecture-strate-ia-cadrage-medias-sociologue-quanti
title: Pré-relecture IA strate 1 — Cadrage Médias français v0.1 (sociologue/politiste quantitatif·ve)
document_relu: dossiers/medias/cadrage.md
version_relue: v0.1
persona: sociologue-quantitatif (v1)
persona_path: docs/methodology/personae-ia/sociologue-quantitatif.md
session_date: 2026-05-16
auteur_session: sam
statut: brut (non arbitré)
---

# Pré-relecture *Cadrage du dossier Médias français v0.1* — Persona Sociologue/politiste quantitatif·ve

> **Statut** : retour brut de session IA, archivé avant arbitrage. Pipeline prévu en §12 du cadrage : strate 1 IA → arbitrage auteur → v0.2 → strate 2 comité humain.
>
> **Doctrine** : ADR-0024 (relecture deux strates).
>
> **Posture de la persona** : méthodologique avant tout. Demande systématique de la population, du n, du mode de collecte, de la formulation exacte des questions, des intervalles de confiance. Distingue rigoureusement descriptif / inférentiel, corrélation / causation.

## 1. Solide méthodologiquement

- La **distinction explicite entre « peut faire / ne peut pas faire »** (§1) est exactement la posture attendue d'un document quanti grand public. Refuser de trancher l'indépendance comme concept est sain : ce n'est pas une variable mesurable, c'est un construit théorique multidimensionnel.
- Le **double recours à plusieurs baromètres** sur la confiance (Reuters Institute *et* Kantar/La Croix, §2 SQ6) et la note explicite sur l'incomparabilité méthodologique (§4 test 3) montrent que l'auteur connaît le piège. Reste à exécuter (voir §3 ci-dessous).
- Les **scores RICE par sous-question** (§5) sont un bon outil d'arbitrage *interne*. La transparence du calcul est appréciée.
- L'arbitrage **report de la sous-question 8 (fact-checking)** au motif d'un Confidence faible est cohérent — c'est exactement le genre d'arbitrage que justifie le score.
- Le **registre prudent du test 8** (« présentation factuelle, pas conclusion partisane ») évite le piège de la sociologie scandaleuse.

## 2. Limites méthodologiques non signalées

### 2.1. Le chiffre « ~30 % en 2025 vs ~39 % en 2015 » (§1)

L'auteur écrit « à confirmer en source primaire ». Ce n'est pas suffisant. Trois caveats à ajouter dès que le chiffre est repris :

- **Évolution méthodologique du Reuters DNR lui-même** entre 2015 et 2025 (taille du panel France, pondérations, formulation traduite de la question « trust most of the news most of the time »). À documenter.
- **Nature du panel** : Reuters DNR est un panel auto-recruté en ligne quotaté (YouGov en France). Ce n'est *pas* un échantillon probabiliste représentatif au sens classique INSEE/INED. À mentionner explicitement quand le chiffre est présenté au grand public.
- **Intervalle de confiance** : avec n ≈ 2000 pour la France, l'IC à 95 % est de l'ordre de ± 2 points. Un écart de 9 points est statistiquement robuste, mais l'IC ou l'erreur-type doit être cité lors de la publication.

### 2.2. Concentration capitalistique — concentration de quoi exactement ? (§2 SQ1, §4 tests 1)

Le mot « concentration » regroupe plusieurs choses qui sont fusionnées dans la note :

- **Concentration de propriété** (qui possède le capital — variable d'actionnariat).
- **Concentration de contrôle** (qui décide — peut différer en cas de pacte, droits de vote double, golden share).
- **Concentration de l'audience** (parts cumulées — variable de marché).
- **Concentration éditoriale** (synergies de rédaction — variable organisationnelle).

Choisir l'indicateur et le nommer : ratio de concentration C5 ou C8, indice HHI (Herfindahl-Hirschman), indice de Gini. Le HHI est l'indicateur standard utilisé par les régulateurs concurrence (DG Comp européenne, FCC américaine). Préférable à la part top-5 cumulée parce qu'il intègre toute la distribution.

> **Note d'articulation avec le retour persona `chercheuse-sic`** : la chercheuse SIC propose la même ventilation à quatre niveaux (capitalistique / contrôle / éditoriale / audience). Convergence forte entre les deux personae sur ce point — c'est la correction de fond la plus prioritaire.

### 2.3. Sous-question 6 — facteurs corrélés à la confiance

L'auteur liste : « génération, niveau de diplôme, orientation politique, média consommé ». Bien. Mais :

- **Identification des effets** : ces variables sont fortement corrélées entre elles (niveau de diplôme × génération × orientation politique). Une simple corrélation bivariée induira en erreur. Il faut un modèle multivarié (régression linéaire ou logistique selon la variable dépendante).
- **Microdonnées requises** : le Reuters DNR publie les résultats agrégés et certains croisements, mais pas systématiquement les microdonnées en libre accès. Le baromètre Kantar/La Croix non plus. Pour faire des régressions, il faut soit acheter l'accès, soit utiliser ELIPSS / European Social Survey (modules « media trust ») qui ont des microdonnées publiques. À budgétiser ou à reporter en V2.
- **Désirabilité sociale** : déclarer une faible confiance dans les médias est aujourd'hui socialement valorisé dans certains segments (critique anti-médias mainstream). Biais à mentionner.

### 2.4. Test 7 — Financement audiovisuel public (§4)

L'auteur écrit : *« réfuté probablement (chiffres publics 2024 montrent un budget par habitant supérieur à l'Allemagne et largement supérieur au Royaume-Uni). »* Affirmation forte non sourcée. Et surtout, **incomparable selon le périmètre** :

- ARD + ZDF + Deutschlandradio en Allemagne sont financés par le *Rundfunkbeitrag* (~8,4 Mds€/an). France TV + Radio France + INA + ARTE-France + TV5 Monde ~ 3,8 Mds€/an post-réforme 2022 (suppression CAP, financement TVA). Allemagne ~ 100 €/habitant, France ~ 57 €/habitant.
- Mais : périmètre. Inclus-tu ARTE (binational) ? RFI/France 24 (audiovisuel extérieur, financements MEAE) ? La taxe sur les opérateurs télécoms (TOCE) ?
- Le chiffre **change du simple au double** selon le périmètre. À documenter avant de classer le test « réfuté ».

### 2.5. Sous-question 7 — Position au classement RSF

Le classement RSF est un **indice composite** (5 sous-indicateurs : contexte politique, cadre légal, contexte économique, contexte socioculturel, sécurité). Les pondérations et la méthodologie de calcul ont évolué (refonte majeure en 2022). La comparaison 2015 vs 2025 :

- En **score absolu** : la série n'est pas parfaitement comparable du fait de la refonte 2022.
- En **rang** : artefactuel, car le rang dépend autant des autres pays que de la France elle-même. Une France stable peut « monter » ou « descendre » uniquement parce qu'un autre pays a bougé.

Présenter les deux et expliciter la rupture méthodologique 2022.

### 2.6. Test 4 — « écart de traitement entre médias »

L'auteur reporte en V2 (Common Crawl). Bien. Mais en V1 il dit : « présenter des études existantes (Acrimed, Reuters Institute) ». Acrimed est une association militante avec ligne éditoriale assumée — c'est une source légitime mais à présenter comme une *perspective située*, pas comme un observatoire neutre. À cadrer dans la *source card*.

## 3. Confusions à clarifier

- **Test 3 (confiance)** : « présentation des deux séries séparément ». Bien. Mais ajouter explicitement : *« nous ne calculons pas de série combinée, et nous n'inférons pas une "tendance unique" à partir de deux séries non-comparables. »* Sans ça, le lecteur fera l'agrégat mentalement quand même.
- **§3 angles de lecture** : la distinction des angles est bien faite, mais attention à ne pas présenter trois angles « équipondérés » si l'un est marginal dans le débat académique. La pondération éditoriale doit être documentée (combien de papiers académiques défendent chaque position, par exemple).
- **Sous-question 4 — densité de cas documentés** : « densité de cas par groupe sur 10 ans ». Densité = nombre absolu ou normé par la taille du groupe (nombre de titres × nombre de salarié·e·s) ? La normalisation change beaucoup le résultat.
- **Concept d'« audience info »** (SQ5) — info comment ? Temps passé sur sections actu d'un site ? Reach d'articles politiques ? Définition opérationnelle à fixer.

## 4. Comparaisons à requalifier (mêmes méthodos, mêmes périodes)

| Comparaison annoncée | Risque d'incomparabilité | Action |
|---|---|---|
| Confiance médias FR 2015 vs 2025 | Méthodologie d'enquête | Une seule série par graphique. Deux séries présentées côte-à-côte avec caveat. |
| Concentration presse 2004 vs 2024 | Changement indicateur ACPM 2014 | Retraitement ou présentation des deux séries indicateurs |
| Position RSF 2015 vs 2025 | Refonte méthodologique 2022 | Mentionner la rupture |
| Financement audiovisuel public FR vs DE vs UK | Périmètre national différent | Tableau périmètres comparables (cœur audiovisuel public hors externalités) |
| Confiance France vs Allemagne vs UK | OK si Reuters DNR, méthodologie identique | Préciser que c'est Reuters DNR, mêmes vagues |
| Audience médias indé 2015 vs 2025 | Évolution mesures ACPM web | Indicateur stable à choisir et justifier |

## 5. Sources à vérifier en sources primaires

Chiffres ou affirmations qui demandent un lien vers la source primaire avant publication (et même avant la v0.2) :

- Le « ~30 % en 2025 vs ~39 % en 2015 » — Reuters DNR France 2015 + 2025, page exacte.
- Tous les pourcentages de financement public audiovisuel — chiffres budgétaires officiels (PLF France, Bundeshaushalt Allemagne, BBC Annual Report UK).
- Toute affirmation sur la concentration capitalistique — comptes annuels des groupes cotés (Bolloré, Vivendi, Lagardère, etc. déposés à l'AMF / Companies House).
- Toute citation de cas documentés en sous-question 4 — source primaire (communiqué SDJ daté, arrêt de justice, enquête sur média avec auteur identifié).

Pour chacune, créer ou compléter la *source card* avant que le chiffre apparaisse dans le dossier publié.

## 6. Tests de réalité — robustesse méthodologique

Classement des 10 tests (§4) selon leur défendabilité méthodologique :

**Robustes (publiables tels quels avec minor caveats) :**

- **Test 5 — Pluralisme 3/9** : données ARCOM publiques, méthodologie ARCOM stable, indicateurs clairs. Caveat sur la fenêtre temporelle choisie (période électorale vs hors campagne) à expliciter.
- **Test 9 — Rang RSF** : factuel sur la donnée brute. Caveat sur la rupture 2022.

**Robustes sous conditions de retraitement :**

- **Test 1 — Concentration presse** : retraitement de l'indicateur ACPM 2014 obligatoire. Sinon, présenter 2014-2024 plutôt que 2004-2024.
- **Test 3 — Confiance 2015-2025** : robuste *par enquête*, pas robuste *entre enquêtes*. Présenter deux séries.
- **Test 6 — Poids des aides publiques** : robuste si comptes annuels disponibles publiquement pour les bénéficiaires majeurs. Caveat : les groupes diversifiés agrègent presse + autres, ratio à recalculer périmètre presse seule.

**Fragiles méthodologiquement :**

- **Test 2 — Audience médias indé absolue 2015-2025** : la mesure d'audience web 2015 n'est pas comparable à 2025 (mesures cookies, mobile, paywalls). Reformuler en « audience déclarée par les médias indé eux-mêmes » et signaler la nature auto-déclarative.
- **Test 7 — Financement audiovisuel public** : voir §2.4 ci-dessus. **Test à reformuler complètement** avant la v0.2 : ne pas annoncer « probablement réfuté » sans la matrice de périmètres.
- **Test 8 — Concentration de cas documentés** : qualitatif déguisé en quanti. Le critère de sélection des cas est le levier méthodologique principal. Documenter explicitement (cas avec source primaire publique non rétractée, période X-Y, sélection sur quel critère). Sinon, le lecteur peut accuser de cherry-picking.
- **Test 10 — Fact-checking maison-mère** : pertinent mais l'échantillon doit être probabiliste (échantillon aléatoire d'articles sur la période) ou exhaustif (tous les articles). Sinon, biais de sélection.
- **Test 4 — Écart de traitement** : déjà reporté V2, OK.

## 7. Biais possibles de cette critique

- **Méfiance vis-à-vis du qualitatif** : j'ai été dur sur les tests 8 et 10 qui mêlent compute et jugement éditorial. Pour un dossier grand public, une part de qualitatif est légitime et inévitable. Ne pas surcalibrer l'autocritique au point de ne plus rien dire.
- **Scepticisme paralysant** : j'ai listé 14 caveats. Si tous étaient appliqués strictement, le dossier deviendrait illisible. Hiérarchiser : caveats explicites en intro générale de méthodologie, caveats cachés dans des info-bulles sur les graphiques. Ne pas alourdir le corps de texte.
- **Préférence pour les grandes enquêtes officielles** : j'ai poussé Reuters DNR / ELIPSS / ESS. Mais le baromètre Kantar/La Croix face-à-face a aussi sa valeur (mode de collecte plus robuste pour les sujets sensibles). Et certaines données ARCOM/ACPM sont irremplaçables même si elles ne sont pas issues d'enquêtes probabilistes.
- **Conservatisme statistique grand public** : j'ai insisté sur les IC, mais le public n'est pas formé à les lire. Présenter « ~30 % (±2 points) » en survol et garder l'IC complet en source card / annexe méthodologique. Pas obligé de l'exposer en gros plan.
- **Manque d'attention au format média** : rien sur l'accessibilité, l'a11y, l'UX. C'est hors champ pour la persona. La persona *lecteur profane* aura un retour plus utile sur la lisibilité.

---

## Synthèse — top 3 actions prioritaires pour passer en v0.2

1. **Reformuler le test 7 (financement audiovisuel public)** avec une matrice de périmètres comparables avant toute conclusion. C'est la fragilité la plus exposée à une mise en cause facile.
2. **Spécifier l'indicateur de concentration** dans la sous-question 1 (HHI ou C5/C8) et reposer les tests 1 et 8 dessus. *(Converge avec le retour de la persona `chercheuse-sic`.)*
3. **Reprendre tous les chiffres mentionnés dans le cadrage** (Reuters DNR, RSF, etc.) avec liens vers sources primaires, avant la v0.2. Aucun chiffre orphelin de source.

Le reste peut être traité en arbitrage de fond sur la phase rédaction (octobre 2026). Le cadrage est solide dans l'intention, perfectible dans l'opérationnalisation. Bonne base pour la suite.

---

## Métadonnées de session

- **Date** : 2026-05-16
- **Persona** : `sociologue-quantitatif` v1
- **Document relu** : `dossiers/medias/cadrage.md` v0.1
- **Mode** : conversation Cowork unique, retour direct (pas d'allers-retours)
- **Prochaine étape (auteur)** : arbitrer les remarques (accepter / rejeter / différer avec motif) et croiser avec le retour `chercheuse-sic` déjà archivé + les 3 autres personae IA restantes (journaliste-independant, lecteur-profane, data-engineer-senior) avant de produire `cadrage.md` v0.2 et de soumettre au comité humain.
