---
slug: medias
title: Médias français
status: draft-v0.2
version: v0.2
authors: [sam]
created: 2026-05-XX
last_updated: 2026-05-16
supersedes: v0.1 (2026-05-XX)
strate_1_relecture: dossiers/medias/relecture/strate-ia-cadrage-2026-05-16-*.md
---

# Cadrage du dossier *Médias français* — v0.2

> **Statut** : pré-note v0.2, intégrant les retours de la **strate 1** (pré-relecture par 5 personae IA documentées le 2026-05-16, voir [ADR-0024](../../docs/adr/0024-doctrine-relecture-deux-strates.md)). À soumettre à la **strate 2** (comité humain pluraliste) avant publication. Toutes les formulations restent ouvertes à arbitrage par le comité humain.
>
> **Versions précédentes** : v0.1 archivée dans Git history. Diff principal v0.1 → v0.2 résumé en §14.

## Historique de production de cette version

- **v0.1** rédigée le 2026-05-XX (cadrage initial).
- **Pré-relecture strate 1** le 2026-05-16 par 5 personae IA (chercheuse-sic, journaliste-independant, sociologue-quantitatif, lecteur-profane, data-engineer-senior). Retours archivés dans `dossiers/medias/relecture/`.
- **Arbitrage auteur** : 15 actions de modification retenues, validées par Sam, intégrées dans cette v0.2.
- **3 ADR émergentes** produites en parallèle : [ADR-0025](../../docs/adr/0025-mesure-concentration-mediatique.md) (concentration), [ADR-0026](../../docs/adr/0026-definition-media-independant.md) (média indépendant), [ADR-0029](../../docs/adr/0029-doctrine-droit-de-reponse.md) (droit de réponse).

---

## 1. Question principale et contexte

### 1.1. La question

**Le paysage médiatique français permet-il aujourd'hui un débat public pluraliste et informé ?**

### 1.2. Notre posture épistémique

Avant tout : **nous ne prétendons pas à la neutralité**, ce qui serait une posture intenable au sens où Bourdieu (*Méditations pascaliennes*, 1997) et Lemieux (*La sociologie sur le vif*, 2018) la critiquent. Nous adoptons une **éthique de production** :

- **Rigueur méthodologique publique** : chaque chiffre est sourcé, chaque indicateur est documenté, chaque arbitrage est tracé.
- **Auto-réflexivité explicite** : nous documentons notre propre positionnement (cf. §11bis « Conflits d'intérêts de l'auteur »).
- **Pluralité organisée** : la doctrine de relecture en deux strates ([ADR-0024](../../docs/adr/0024-doctrine-relecture-deux-strates.md)) garantit qu'aucune analyse ne sort sans être passée par cinq perspectives critiques différentes.
- **Refus de la fausse symétrie** : exposer plusieurs angles de lecture ne signifie pas leur accorder le même poids académique. Quand un angle est marginal dans la littérature, c'est dit.

Le choix de ne pas trancher la question principale est donc **un acte positionné, pas une évidence méthodologique**. Il coûte (risque de fausse symétrie, plafonnement de la portée critique) et il est assumé comme tel.

### 1.3. Pourquoi cette question maintenant

- **Sujet structurant** : les médias façonnent une grande partie du débat public dont AporiaPolis veut être un complément critique. Commencer par eux est méta-cohérent.
- **Inquiétude documentée** : la confiance déclarée des Français dans leurs médias se situe à un niveau bas sur la période documentée. Selon le **Reuters Institute Digital News Report 2025** (panel YouGov auto-recruté en ligne, n ≈ 2 000 pour la France), le taux est de ~30 % en 2025 contre ~39 % en 2015 (chiffres à confirmer en source primaire, lien à ajouter en v0.3). Le **baromètre Kantar Public pour *La Croix*** (annuel face-à-face) fournit une seconde série, non comparable méthodologiquement, à présenter séparément (cf. SQ6).
- **Concentration capitalistique accélérée** : depuis ~10 ans, plusieurs titres majeurs ont changé d'actionnaire de contrôle :
  - Vivendi (groupe Bolloré) prend le contrôle de Lagardère en 2023.
  - Xavier Niel détient des participations significatives dans Le Monde Libre depuis 2010.
  - Patrick Drahi acquiert Libération en 2014 (passage en SCIC en 2020).
  - Daniel Křetínský acquiert Marianne en 2018 via CMI France.
  - LVMH (Bernard Arnault) détient Les Échos depuis 2007 et Le Parisien depuis 2015.

  Chaque acquisition doit être sourcée précisément dans le dossier (déclarations AMF, enquêtes économiques tierces). Liste indicative, à compléter exhaustivement en source card `docs/sources/grands-groupes-mediatiques.md`.

- **Régulation en évolution** :
  - **ARCOM** (Autorité de régulation de la communication audiovisuelle et numérique, fusion CSA + HADOPI par la loi du 25 octobre 2021, entrée en vigueur le 1ᵉʳ janvier 2022).
  - **Droit voisin des éditeurs de presse** (transposition de la directive UE 2019/790, codifié article L218-2 CPI).
  - **AI Act européen** (adopté en mars 2024, mise en application progressive 2025-2027).
  - **EMFA** (European Media Freedom Act, adopté en avril 2024, applicable août 2025) — texte structurant pour le pluralisme et l'indépendance éditoriale à l'échelle UE.
  - **DSA** (Digital Services Act, applicable depuis 2024) — restructure les obligations des plateformes.
  - **Suppression de la contribution à l'audiovisuel public (CAP)** en 2022, substitution par fraction de TVA affectée.

- **Calendrier électoral** : présidentielle d'avril 2027. Un dossier publié en novembre 2026 offre 5 mois de circulation avant le premier tour, pertinent pour structurer un débat éclairé sans paraître publication de campagne.

### 1.4. Ce que la data peut faire / ne peut pas faire

**Peut faire** : mesurer la **concentration capitalistique et d'audience** (HHI, C5, parts cumulées, cf. [ADR-0025](../../docs/adr/0025-mesure-concentration-mediatique.md)), tracer l'évolution de la confiance dans les médias (baromètres longitudinaux séparés), comparer aux pays voisins (Reuters Institute, Eurobaromètre), analyser la production éditoriale (Common Crawl en V2 sous gate juridique [ADR-0022](../../docs/adr/0022-doctrine-retention-presse.md), classification d'angles via traitement automatique du langage), tracer l'évolution des positions des partis sur la régulation des médias (programmes scrapés, votes parlementaires), positionner chaque média sur une typologie juridico-économique tri-dimensionnelle (cf. [ADR-0026](../../docs/adr/0026-definition-media-independant.md)).

**Ne peut pas faire** : trancher la **« concentration éditoriale »** comme score unique (cf. ADR-0025, c'est une cartographie qualitative documentée, pas un chiffre), trancher l'« indépendance » d'un média (notion floue, contestée, multidimensionnelle), valider qu'une rédaction « manipule » l'opinion (relève du droit, pas de la data), définir ce qu'est un « bon » journalisme (jugement de valeur).

---

## 1bis. Cadre intellectuel mobilisé

Le dossier s'appuie sur la littérature académique suivante. Liste non exhaustive, à enrichir au fil de la rédaction.

### Cadre comparatif international

- **Hallin, D. & Mancini, P.** (2004). *Comparing Media Systems: Three Models of Media and Politics*. Cambridge University Press. — Cadre canonique de comparaison des systèmes médiatiques. La France appartient au modèle « pluraliste polarisé » (avec Italie, Espagne, Grèce), distinct du modèle « libéral » (US, UK, Canada, Irlande) et du modèle « démocratique corporatiste » (Allemagne, pays nordiques, Pays-Bas).
- **Brüggemann, M., et al.** (2014). *Hallin and Mancini Revisited: Four Empirical Types of Western Media Systems*. Journal of Communication, 64(6). — Actualisation empirique d'Hallin & Mancini.

### Sociologie du champ journalistique

- **Bourdieu, P.** (1996). *Sur la télévision*. Liber. — Théorie du champ journalistique appliquée à la TV.
- **Bourdieu, P.** (1997). *Méditations pascaliennes*. Seuil. — Notamment sur la « neutralité » comme posture positionnée.
- **Champagne, P.** (1990). *Faire l'opinion*. Minuit. — Sociologie de la production de l'opinion publique.
- **Champagne, P.** (2016, posthume). *La double dépendance*. Raisons d'agir.
- **Lemieux, C.** (2000). *Mauvaise presse. Une sociologie compréhensive du travail journalistique*. Métailié.
- **Lemieux, C.** (2018). *La sociologie sur le vif*. PSL/EHESS.
- **Neveu, E.** (2019, dernière éd.). *Sociologie du journalisme*. La Découverte, coll. *Repères*. — Manuel de référence francophone.
- **Schudson, M.** (1978). *Discovering the News*. Basic Books. — Histoire de l'objectivité journalistique.

### Économie politique des médias

- **Schiller, D.** (1989). *Beyond the Sociology of Knowledge*. — Référence ancienne sur la concentration médiatique, structurante pour distinguer les niveaux capitalistique / éditorial / audience.
- **Cagé, J.** (2015). *Sauver les médias*. Seuil/République des idées. — Cadre français de référence sur l'économie de la presse, distinction capital de propriété vs capital de contrôle.
- **Cagé, J., Hervé, N. & Mazoyer, B.** (2017). *L'information à tout prix*. INA Éditions. — Typologie juridico-économique des médias français, base de l'[ADR-0026](../../docs/adr/0026-definition-media-independant.md).
- **Méadel, C.** (2010). *Quantifier le public. Histoire des mesures d'audience de la radio et de la télévision*. Economica. — La mesure d'audience comme construit social, à mobiliser pour caveat Médiamétrie.

### Théorie de l'agenda et pluralisme

- **McCombs, M. & Shaw, D.** (1972). *The Agenda-Setting Function of Mass Media*. — Théorie de l'agenda-setting.
- **Charron, J. & de Bonville, J.** (différents ouvrages). — Application francophone de l'agenda-setting.

### Fact-checking

- **Graves, L.** (2016). *Deciding What's True: The Rise of Political Fact-Checking in American Journalism*. Columbia University Press. — Ouvrage de référence sur le mouvement fact-checking.
- **Bigot, J.-M. & Vauchez, A.** (2017-2023). Différents articles sur le fact-checking en France.

### Confiance dans les médias

- **Hardin, R.** (2002). *Trust and Trustworthiness*. Russell Sage Foundation. — Théorie de la confiance institutionnelle.
- **Baumard, N.** (différents travaux). — Sur la confiance et son évolution.

### Sources institutionnelles

- **Reuters Institute Digital News Report**, annuel (Oxford). — Référence pour les comparaisons internationales de consommation et de confiance.
- **Reporters sans frontières (RSF)**, Index annuel de la liberté de la presse. — Indice composite (5 sous-indicateurs), méthodologie refondue en 2022, à mentionner.

### Sources critiques militantes

À mobiliser comme sources situées, **pas comme observatoires neutres** :

- **Acrimed** (Action-Critique-Médias). Association militante engagée, ligne éditoriale assumée. Cf. note méthodologique dans la source card `docs/sources/acrimed.md`.
- **La Revue des Médias** (INA). Plus institutionnelle, à utiliser comme source de référence sur l'histoire du paysage.

---

## 2. Sous-questions retenues (7 pour la V1 + 1 reportée V2)

### Sous-question 1 — Qui possède et qui contrôle les médias français, et quelle relation avec la diversité éditoriale ?

**Angle** : économie politique, conformément au cadre conceptuel de l'[ADR-0025](../../docs/adr/0025-mesure-concentration-mediatique.md) qui ventile la « concentration » en **quatre niveaux distincts** :

1. **Concentration capitalistique** (qui détient le capital) : indicateur canonique HHI sur les parts de capital par marché, indicateurs complémentaires C5 et C10.
2. **Concentration de contrôle** (qui décide stratégiquement) : cartographie nominative des entités de contrôle + mécanismes (pactes d'actionnaires, droits de vote multiples, etc.), C5 de contrôle.
3. **Concentration éditoriale** (combien d'entités produisent réellement des contenus distincts) : cartographie qualitative documentée, **pas un score unique** (cf. ADR-0025).
4. **Concentration d'audience** (qui est effectivement consommé) : HHI sur parts d'audience Médiamétrie / ACPM, avec caveat permanent Médiamétrie GIE.

**Périmètre inclut explicitement** : presse écrite nationale, presse écrite régionale (PQR), télévision gratuite, télévision payante, radio (privée + service public), pure players web, médias indépendants (typologie ADR-0026), **et audiovisuel public** (France Télévisions, Radio France, INA, Arte France, France Médias Monde, TV5 Monde). L'audiovisuel public est traité avec ses spécificités (gouvernance ARCOM, financement TVA affectée post-2022, indépendance vis-à-vis du pouvoir politique).

**Sources** : ARCOM, ACPM, Médiamétrie (agrégats publics), AMF (déclarations actionnariat groupes cotés), greffes des tribunaux de commerce (non cotés), rapports Cour des comptes (audiovisuel public), rapport Assouline du Sénat (2022) sur la concentration médiatique, enquêtes économiques tierces.

**Tests de réalité candidats** : HHI capitalistique sur 20 ans, HHI d'audience sur 10 ans (caveat ACPM 2014), discordances observées entre les 4 niveaux (cas où concentration capitalistique forte coexiste avec diversité éditoriale, et inversement).

### Sous-question 2 — Quels modèles économiques tiennent ?

**Angle** : viabilité économique. Distinguer modèles dominants (publicité, abonnement, mécénat, aides publiques, **financement public TVA pour l'audiovisuel public**) par segment.

**Périmètre étendu** : inclut explicitement l'**audiovisuel public** (France TV + Radio France + INA + Arte France + France Médias Monde + TV5 Monde) avec son régime de financement spécifique post-2022 (suppression CAP, TVA affectée). La suppression de la redevance en 2022 a complexifié la lecture longitudinale du financement audiovisuel public.

**Sources** : DGMIC (aides à la presse), comptes annuels des groupes cotés, OJD/ACPM (diffusion), Médiamétrie (audience), ARCOM (rapports financiers TV/radio), Cour des comptes (audiovisuel public), rapports EBU (Funding of Public Service Media) pour les comparaisons internationales.

**Tests de réalité candidats** : rentabilité comparée des modèles, dépendance publicitaire par segment, évolution des aides publiques, viabilité des pure players par typologie (cf. ADR-0026), comparaison du financement audiovisuel public par habitant avec matrice de périmètres comparables (cf. test refondé en §4).

### Sous-question 3 — Le pluralisme à l'antenne (formel) est-il respecté ?

**Angle** : régulation et obligation légale. La sous-question traite explicitement le **pluralisme formel partisan** mesuré par les obligations ARCOM (règle dite des 3/9 pour la TV — un tiers gouvernement, un tiers majorité, un tiers oppositions ; principes équivalents en radio).

**Caveat majeur** : la mesure ARCOM mesure le **pluralisme formel d'expression politique partisane**, pas le pluralisme effectif. La littérature (McCombs & Shaw 1972 sur l'agenda-setting, Charron & de Bonville côté francophone) distingue trois niveaux qui ne sont pas équivalents :
- Pluralisme **structurel** (combien d'entités produisent ?) — traité dans SQ1.
- Pluralisme **éditorial** (combien d'angles différents sur le même événement ?) — non traité en V1 (Common Crawl bloqué par ADR-0022).
- Pluralisme **d'agenda** (les mêmes sujets sont-ils traités partout ?) — non traité en V1.

La SQ3 ne traite que le **premier niveau du pluralisme formel** — partage du temps de parole partisan à l'antenne. Cette limitation est assumée explicitement.

**Périmètre inclut explicitement l'audiovisuel public** (France TV, France Inter, etc.) avec ses obligations spécifiques.

**Sources** : ARCOM données ouvertes hebdomadaires sur le pluralisme politique, AGORA (lobbying médias — voir la source card HATVP RRI), CSA archives historiques.

**Tests de réalité candidats** : respect des obligations en moyenne sur 12 mois glissants (caveat période électorale / hors campagne), comparaison TV / radio, comparaison public / privé.

### Sous-question 4 — Indépendance éditoriale : cas documentés, mécanismes, garanties, **et contre-exemples**

**Angle** : sociologie des organisations journalistiques. Cas documentés de pressions éditoriales (départs publiquement annoncés via communiqués SDJ, conflits éditoriaux ayant donné lieu à enquêtes publiées par des médias tiers, refus de publication ayant fait l'objet d'un constat écrit en interne et rendu public). Garanties existantes (chartes éditoriales contraignantes, sociétés de journalistes, statuts coopératifs).

**Apport majeur v0.2** : la SQ4 inclut désormais une **section dédiée aux contre-exemples** : rédactions ayant résisté à des pressions documentées (avec sources), SDJ ayant obtenu des chartes contraignantes, départs collectifs ayant abouti à la fondation de nouveaux médias (Disclose, Reporterre, Politis, StreetPress — origine et trajectoire). Sans ces contre-exemples, la SQ4 serait unidimensionnelle et attaquable comme « unilatérale ».

**Cadre juridique** : conformité stricte à la **loi du 29 juillet 1881** (notamment articles 13 sur droit de réponse et 35bis sur la diffamation). Toute mention nominative d'un groupe associée à « pressions éditoriales » doit :
1. S'appuyer sur une enquête tierce publiée, non rétractée, **et non condamnée en diffamation**.
2. Mentionner la position du groupe mis en cause (droit de réponse anticipé : ont-ils répondu publiquement à l'accusation ? Quelle est leur position ?).
3. Distinguer la responsabilité juridique de l'actionnaire et celle du média (la jurisprudence française est claire : on ne peut pas imputer à un actionnaire les décisions éditoriales sans démonstration d'intervention directe).
4. Procédure de droit de réponse formalisée disponible (cf. [ADR-0029](../../docs/adr/0029-doctrine-droit-de-reponse.md)).

**Sources** : enquêtes Mediapart, Acrimed, *La Lettre A*, communiqués SDJ datés, codes éditoriaux publics des médias.

**Tests de réalité candidats (qualitatifs assumés)** :
- Densité comparée de cas documentés par groupe sur 10 ans (avec critère de sélection explicite : cas avec source primaire publique non rétractée et non condamnée en diffamation).
- Présence ou absence de SDJ avec pouvoir contraignant.
- Statut juridique des rédactions et présence de chartes éditoriales contraignantes.

### Sous-question 5 — Comment se structure l'écosystème des médias non affiliés aux grands groupes consolidés ?

**Reformulation v0.2** : la sous-question s'intitule désormais « non affiliés aux grands groupes consolidés » plutôt que « indépendants », pour éviter le mot-valise. Suit la **typologie tri-dimensionnelle** définie dans l'[ADR-0026](../../docs/adr/0026-definition-media-independant.md) :

1. **Statut juridique** (SA, SAS, SARL, SCOP, SCIC, association, fondation).
2. **Structure capitalistique** (filiale grand groupe, capital concentré non affilié, capital dispersé, coopératif, associatif).
3. **Modèle de revenus dominant** (publicité, abonnement, mécénat-dons, aides publiques, mixte).

Quatre sous-sections :
1. **Cartographie par typologie** : positionner ~20-30 médias sur les trois axes.
2. **Taille réelle** : audience, revenus, effectifs.
3. **Viabilité économique par typologie** : qui tient sur 5-10 ans, qui disparaît.
4. **Logique de financement et conséquences éditoriales** : examen équilibré des biais possibles dans **chaque typologie**, y compris dans les médias non affiliés (militantisme, dépendance au public fidèle, dépendance aux fondations). Pas de présomption que « non affilié = neutre ».

**Sources** : ACPM, déclarations publiques d'abonnés (Mediapart, *La Lettre A*), API publiques YouTube pour les créateurs civiques, observatoire Acrimed (source située), greffes pour les statuts juridiques.

**Tests de réalité candidats** : part d'audience info des médias non affiliés (vs établis), évolution 2015-2025 avec caveat mesure web (cookies / mobile / paywalls), longévité comparée par typologie.

### Sous-question 6 — La confiance des Français dans les médias : évolution et facteurs

**Angle** : sociologie de la réception, avec caveats méthodologiques majeurs.

**Caveat méthodologique central** : « confiance dans les médias » est un construit polysémique. Le Reuters Institute pose la question *« How much do you trust most news most of the time? »* (panel YouGov auto-recruté en ligne). Le baromètre Kantar Public pour *La Croix* pose *« À propos de ce que disent les médias, vous-même, diriez-vous que les choses se sont passées vraiment ou à peu près comme ils le racontent ? »* (face-à-face). **Ce n'est pas la même mesure conceptuelle**. Présentation systématique des deux séries séparément. Aucune consolidation en moyenne pondérée.

**Identification des effets sur les facteurs corrélés** : génération, niveau de diplôme, orientation politique, média principal consommé. Caveat de désirabilité sociale (déclarer une faible confiance dans les médias est socialement valorisé dans certains segments). Microdonnées : Reuters DNR et Kantar/La Croix publient les agrégats, pas les microdonnées en libre accès. Pour faire des régressions multivariées contrôlant les corrélations entre facteurs, recourir à ELIPSS / European Social Survey (modules « media trust ») qui ont des microdonnées publiques.

**Dimension générationnelle explicite** : les 18-25 ans et les 60+ ont des consommations médiatiques radicalement divergentes. Cette dimension est traitée explicitement.

**Sources** : Reuters Institute Digital News Report (annuel), baromètre Kantar Public pour *La Croix* (annuel), Eurobaromètre Média, European Social Survey.

**Tests de réalité candidats** :
- Évolution longitudinale par enquête, présentée séparément.
- Comparaison France vs Allemagne / Royaume-Uni / Suède / Danemark via Reuters DNR (méthodologie identique entre pays).
- Corrélations sociologiques (avec caveat sur la nature corrélationnelle, pas causale).

### Sous-question 7 — Comment les médias internationaux nous regardent (et inversement)

**Angle** : comparaison internationale, **dans le cadre Hallin & Mancini** (2004). La France appartient au modèle « pluraliste polarisé » (avec Italie, Espagne, Grèce), ce qui a des implications fortes :
- Forte politisation historique des médias.
- Intervention étatique substantielle (aides à la presse).
- Faible autonomisation du champ journalistique par rapport au champ politique.

**Comparer FR à BBC / DR / PBS sans rappeler ce cadre conduit à des conclusions trompeuses**. La sous-question s'ouvre par une note de cadrage Hallin & Mancini, puis dialoguer avec les actualisations récentes (Brüggemann *et al.* 2014 sur la convergence des modèles).

**Pays retenus pour la comparaison** : Allemagne (modèle démocratique corporatiste), Royaume-Uni (modèle libéral), Suède + Danemark (modèles démocratiques corporatistes nord-européens), États-Unis (modèle libéral pur). Liste pouvant être enrichie selon disponibilité des données.

**Sources** : Reporters sans frontières (Index annuel, avec caveat refonte méthodologique 2022), Reuters Institute DNR (comparable entre pays), OCDE statistics on culture/media, rapports EBU.

**Tests de réalité candidats** :
- Position FR au classement RSF sur 10 ans, avec caveat rupture méthodologique 2022 (présenter score brut et rang séparément).
- Financement audiovisuel public par habitant comparé, avec **matrice de périmètres comparables** (cf. test refondé §4 test 7).
- Indépendance de la régulation comparée (mode de nomination ARCOM vs Ofcom vs FCC, etc.).

### Sous-question 8 — Convergence presse / fact-checking : reportée V2

**Statut v0.2** : confirmation du report en V2, score RICE faible mais raisons mieux fondées après mobilisation de la littérature.

**Justification du report** : la sous-question demande un travail méthodologique substantiel (typologie des cellules de fact-checking, échantillonnage probabiliste de leur production, accord inter-annotateurs sur le classement). En V1, présenter des études existantes (Graves 2016, Bigot & Vauchez) plutôt que mesurer nous-mêmes.

**Reformulation à anticiper V2** : *« Existence d'une charte d'indépendance vis-à-vis de la maison-mère ; signature des principes IFCN ; traitement de cas où la maison-mère a été publiquement contestée sur un fait »*, plutôt que la mesure du « taux de fact-checks portant sur la maison-mère » (mesure piégeuse : une cellule de fact-checking se déclenche sur des affirmations publiquement contestées ou virales, pas sur sa propre rédaction qui n'émet pas d'affirmations factuelles au même rythme).

---

## 3. Angles de lecture présents dans le débat (à exposer, pas à trancher)

Pour chaque sous-question, plusieurs angles cohabitent. Quelques exemples emblématiques, reformulés en v0.2 pour éviter les caricatures.

### Sous-question 1 (propriété et contrôle)

- **Angle libéral / concurrentiel** : la diversité des titres et la concurrence sur le marché de l'attention garantissent à elles seules le pluralisme ; les régulations supplémentaires créent plus de risques (capture du régulateur, barrière à l'entrée) qu'elles n'en règlent. **Contre-arguments empiriques à prendre en compte** : cas de marchés concentrés sans diversité éditoriale documentée.
- **Angle structuraliste** : la concentration capitalistique est une menace pour le pluralisme indépendamment du comportement vertueux des propriétaires (Schiller, Cagé). **Contre-arguments empiriques à prendre en compte** : cas de groupes concentrés avec rédactions documentées comme indépendantes.
- **Angle réformiste** : il faut des garanties d'indépendance éditoriale dans les statuts (chartes contraignantes, SDJ avec pouvoir, SCIC), sans nécessairement remettre en cause la propriété privée. **Cadre légal pertinent** : loi Bloche/Cagé 2017 et 2021 sur le statut juridique des médias d'information.

### Sous-question 2 (modèles éco)

- **Angle marché** : la publicité finance la qualité, les modèles sans publicité ont leurs propres biais (militants, dépendants du public fidèle).
- **Angle service public** : la publicité corrompt structurellement la presse, le financement public neutre (modèle BBC, modèle EBU démocratique corporatiste) est la solution.
- **Angle hybride** : diversification des sources de financement (pub + abonnement + mécénat + aides publiques) pour réduire les dépendances singulières.

### Sous-question 3 (pluralisme à l'antenne)

- **Angle légaliste** : le pluralisme formel ARCOM (règle 3/9) est suffisant comme garantie démocratique.
- **Angle exigeant** : le pluralisme formel est nécessaire mais pas suffisant ; le pluralisme éditorial (angles différents) et d'agenda (sujets traités) ne sont pas mesurés et probablement défaillants.
- **Angle critique** : la mesure ARCOM elle-même est insuffisante (parler 10 minutes en plateau à 23h ≠ 10 minutes en JT de 20h).

### Sous-question 4 (indépendance éditoriale)

- **Angle déontologique** : la profession se régule via chartes, SDJ, ordre professionnel ; les garanties sont en place.
- **Angle structurel** : seules les coopératives ou la diversification de propriété garantissent l'indépendance ; les chartes sans contrainte juridique sont du wishful thinking.
- **Angle libéral** : le marché et le droit à la réputation suffisent, pas besoin de garanties spéciales.
- **Angle « médias militants assumés »** (ajouté v0.2 — angle émergent peu pris en compte) : certains médias se revendiquent explicitement engagés (presse militante anarchiste, certains pure players) et tiennent que la transparence sur le positionnement est plus honnête que la prétention à la neutralité. Cet angle a sa cohérence et mérite d'être exposé.

### Sous-questions 5, 6, 7

Angles à enrichir lors de la rédaction effective du dossier, selon le même principe : présenter pluralement, ne pas pondérer comme équivalents quand un angle est marginal dans la littérature.

---

## 4. Tests de réalité candidats

Format pour chaque test : **hypothèse prédictive → mesure → conclusion attendue selon les issues** (confirmé / partiel / réfuté / non concluant).

**Distinction explicite v0.2** : tests **quantitatifs** (mesure chiffrée robuste) vs **qualitatifs** (cartographie documentée d'événements ou de cas, sans agrégation chiffrée). Les tests qualitatifs sont assumés comme tels, **pas maquillés en quanti**.

### Tests quantitatifs

**Test 1 — Concentration de propriété sur 20 ans** : HHI capitalistique sur le marché presse écrite nationale, à différentes dates (2004, 2014, 2024). Caveat : l'indicateur ACPM a évolué en 2014, donc retraitement ou présentation des deux séries 2004-2014 et 2014-2024 séparément. → confirmé / réfuté / non concluant selon retraitement.

**Test 2 — Audience cumulée des médias non affiliés (typologie ADR-0026)** : ACPM + déclarations publiques d'abonnés (Mediapart, *La Lettre A*) + audiences web médias non affiliés. Caveat : la mesure d'audience web 2015 n'est pas comparable à 2025 (cookies, mobile, paywalls). Reformuler en « audience déclarée par les médias non affiliés eux-mêmes » et signaler la nature auto-déclarative. → confirmé partiel ou non concluant selon segment.

**Test 3 — Confiance des Français 2015-2025** : Reuters DNR (panel YouGov en ligne) ET Kantar Public pour *La Croix* (face-à-face), **deux séries présentées séparément** (incomparabilité méthodologique). Pour Reuters DNR : IC à 95 % ≈ ± 2 points avec n ≈ 2 000. Un écart de 9 points est statistiquement robuste pour cette enquête. **Ne jamais consolider en moyenne pondérée**. → confirmé pour Reuters DNR, à vérifier pour Kantar/La Croix.

**Test 5 — Pluralisme formel ARCOM (règle 3/9)** : données ARCOM publiques hebdomadaires, moyenne sur 12 mois glissants. Caveat : la mesure ne capture que le pluralisme partisan formel, pas le pluralisme éditorial ni d'agenda. → confirmé / réfuté selon période.

**Test 6 — Poids des aides publiques dans les comptes des bénéficiaires** : DGMIC (aides nominatives) × comptes annuels des groupes cotés bénéficiaires. Caveat : les groupes diversifiés agrègent presse + autres, ratio à recalculer sur périmètre presse seule. → confirmé partiel selon segment.

**Test 7 — Financement audiovisuel public FR vs voisins (test refondé v0.2)** :

*v0.1 affirmait à tort « probablement réfuté » sans matrice de périmètres. La v0.2 refonde entièrement.*

**Hypothèse** : « Le financement de l'audiovisuel public français est comparable à celui de nos voisins européens. »

**Matrice de périmètres requise** :
| Pays | Acteurs cœur | Acteurs périphériques optionnels | Source budgétaire principale |
|---|---|---|---|
| France | France TV + Radio France + INA + Arte-France | France Médias Monde, TV5 Monde, TOCE | Fraction TVA depuis 2022 (avant : CAP) |
| Allemagne | ARD + ZDF + Deutschlandradio | Deutsche Welle | Rundfunkbeitrag |
| Royaume-Uni | BBC | World Service | Licence Fee + dotation Foreign Office (World Service) |

**Sources primaires** : PLF France (mission Médias), Bundeshaushalt Allemagne, BBC Annual Report, rapports EBU Funding of Public Service Media.

**Conclusion attendue à élaborer** : présentation par périmètre comparable (cœur audiovisuel public hors externalités), pas d'affirmation unique. Le chiffre par habitant change du simple au double selon le périmètre choisi — affirmation à éviter sans cadrage.

**Test 9 — Position FR au classement RSF sur 10 ans** : RSF Index, en présentant **score brut** et **rang** séparément (le rang est artefactuel, dépend des autres pays). Caveat : refonte méthodologique 2022 du classement. → factuel sur la donnée brute, à interpréter avec caveat.

### Tests qualitatifs (assumés comme tels, v0.2)

**Test 4 — Concordances/discordances entre les 4 niveaux de concentration** : étude de cas documentés où concentration capitalistique forte coexiste avec diversité éditoriale (et inversement). Critère de sélection des cas : groupes représentant > 10 % d'un marché médiatique français. Présenté comme **cartographie qualitative**, pas comme score.

**Test 8 — Cartographie des cas documentés de pressions éditoriales par groupe** : enquêtes publiées par médias tiers, non rétractées et non condamnées en diffamation, sur 10 ans glissants. **Critère de sélection explicite** : cas avec source primaire publique citable, mention de la position du groupe mis en cause (droit de réponse anticipé). Cartographie qualitative documentée, pas score chiffré ni « densité comparée ». Comprendre les contre-exemples (rédactions ayant résisté à des pressions) avec la même rigueur que les cas où la pression a abouti.

**Test 10 — Doctrine d'indépendance des cellules fact-checking de la maison-mère** (reporté V2 mais cadré v0.2) : présence d'une charte d'indépendance signée, signature des principes IFCN, traitement de cas où la maison-mère a été publiquement contestée sur un fait. **Pas la mesure piégeuse du « taux de fact-checks portant sur la maison-mère »**. Si conservé, échantillonnage probabiliste ou exhaustif explicite.

### Tests à compléter en v0.3 (post-arbitrage comité)

Tests 11-15 à formaliser après pré-relecture par comité humain (strate 2). Pistes en réserve :
- Mesure de la mutualisation des rédactions au sein des groupes (fait référence à concentration éditoriale, niveau 3 de ADR-0025).
- Évolution de la précarité dans la profession journalistique (CSP, pigistes, intermittents) — peut nourrir SQ4.
- Mesure de la couverture des sujets internationaux par segment de média français (test annexe SQ7).

---

## 5. Analyse RICE des sous-questions

**Caveat méthodologique v0.2** : le score RICE (Reach × Impact × Confidence / Effort) est un **outil d'arbitrage de production**, pas un jugement sur la **valeur intellectuelle** des sous-questions. Une sous-question peut être structurellement importante avec un mauvais score RICE (par exemple à cause d'un Effort élevé). Le score sert à arbitrer le **rythme de production** dans un MVP solo sur 12 mois, pas à hiérarchiser l'importance des questions du paysage médiatique.

**Échelle** : notation 1-10 attribuée par l'auteur, comparative entre sous-questions du dossier.

| Sous-question | Reach (audience potentielle) | Impact (force du résultat) | Confidence (data disponible) | Effort (temps de production) | Score RICE |
|---|---|---|---|---|---|
| 1 — Propriété + 4 niveaux | 9 | 9 | 8 | 6 | 108 |
| 2 — Modèles éco + audiovisuel public | 7 | 7 | 7 | 5 | 69 |
| 3 — Pluralisme formel ARCOM | 6 | 6 | 9 | 3 | 108 |
| 4 — Indépendance + contre-exemples | 9 | 8 | 6 | 7 | 62 |
| 5 — Médias non affiliés + typologie | 7 | 7 | 6 | 4 | 74 |
| 6 — Confiance + dimension générationnelle | 8 | 7 | 7 | 4 | 98 |
| 7 — International dans cadre H&M | 6 | 7 | 7 | 4 | 74 |
| 8 — Fact-checking | reportée V2 | | | | |

Score = (Reach × Impact × Confidence) / Effort.

**Lecture v0.2** : sous-questions 1, 3, 6 sortent en tête. SQ4 reste prioritaire malgré son score plus bas en raison de son importance structurelle (le projet ne peut pas faire l'économie de la SQ4 même si elle est plus coûteuse). SQ8 reportée V2 confirmée.

---

## 6. Objectifs SMART et cibles qualité

### 6.1. Objectifs éditoriaux et techniques

- **Spécifique** : publier le dossier *Médias français* en 7 sous-questions (V1), sur le site `aporiapolis.org`, avec méthodologie complète versionnée.
- **Mesurable** : voir cibles ci-dessous (front, méthodo, data quality).
- **Atteignable** : à partir des sources structurées identifiées (ARCOM, ACPM, DGMIC, Médiamétrie, Reuters Institute, Reporters sans frontières, INSEE, AFP, Cour des comptes, rapport Assouline) sans recours à Common Crawl V1 (bloqué par ADR-0022). Charge estimée : ~250-350 heures cumulées sur T2.
- **Réaliste** : aligné sur les ressources disponibles (Sam solo, comité de relecture en cours de constitution, budget MVP) et sur la stack figée (Postgres + dbt + FastAPI + Astro 5 + Svelte 5).
- **Temporellement défini** : publication officielle version 1.0.0 le 18 novembre 2026 (semaine 47). Dépôt des contenus pré-publication au comité humain : 1ᵉʳ novembre 2026 (semaine 44). Pré-relecture IA strate 1 sur dossier complet : 25 octobre 2026 (semaine 43).

### 6.2. Cibles front et accessibilité

- **Lighthouse Performance** > 95 sur toutes les pages publiques du dossier.
- **Lighthouse Accessibility** > 95 sur toutes les pages.
- **axe-core** : 0 défaut niveau A, ≤ 5 défauts niveau AA.
- **Tests manuels NVDA** sur 3 pages clés du dossier (page d'accueil dossier, SQ1, SQ4).
- **Pas de tracking tiers** : analytics Plausible self-hosted uniquement.

Note pour lecteur·rice profane : ces cibles techniques signifient que le site doit être **rapide à charger**, **accessible aux personnes en situation de handicap** selon les standards web reconnus (équivalent norme RGAA AA), et **respectueux de la vie privée**.

### 6.3. Cibles data quality (nouveau v0.2)

Aux côtés des cibles front, le dossier respecte des cibles qualité côté data :

- **Tests dbt** systématiques sur les marts publiés :
  - `not_null` sur toutes les colonnes pivot.
  - `unique` sur les clés naturelles.
  - `relationships` entre marts liés.
  - `accepted_range` sur les pourcentages (0-100) et les comptes (≥ 0).
  - `accepted_values` sur les colonnes catégorielles (typologie ADR-0026 par exemple).
- **Freshness** : alertes si données plus anciennes que :
  - 7 jours pour ARCOM (publication hebdomadaire).
  - 30 jours pour ACPM (mises à jour mensuelles).
  - 90 jours pour DGMIC (publication trimestrielle ou annuelle selon source).
- **Snapshots SCD type 2** sur les sources sujettes à rétro-correction (sources où une publication antérieure peut être corrigée après-coup) : ARCOM, ACPM, DGMIC. ADR-0027 dédiée à venir (cf. parking lot data engineer).
- **Reproductibilité** : `make reproduce` sur clone fresh régénère 100 % des chiffres publiés. Test mensuel sur VM fraîche dès T2.
- **Concurrency=1** sur les dbt snapshots (cf. doc 09 méthode de travail, contrainte Dagster connue).

### 6.4. Cibles méthodologiques

- **Sources tracées** : ~20-25 sources **load-bearing** ingérées (utilisées pour produire les chiffres du dossier) + ~30-40 sources **citées** dans le cadre intellectuel (références bibliographiques, sans ingestion). Volumes ajustés par rapport à v0.1 (47 « tracées ») suite à retour data-engineer pour éviter dispersion T2.
- **Source cards** : une par source ingérée, complète (gate 2 du backlog v2 cf. doc 13 et conventions doc 10).
- **Reproductibilité** : tout chiffre publié doit être régénérable depuis le repo public. Audit avant publication.
- **Tests de réalité** : conclusion explicite par test (confirmé / partiel / réfuté / non concluant), avec critères de sélection documentés pour les tests qualitatifs.

---

## 7. Sources préliminaires identifiées

### 7.1. Sources load-bearing (ingérées) — cible ~20-25

Listées par sous-question pour visibilité.

**Pour SQ1 (concentration)** :
- ARCOM (rapports financiers, pluralisme) → `docs/sources/arcom.md`.
- ACPM (diffusion presse écrite, audience web) → `docs/sources/acpm.md`.
- Médiamétrie (audience TV/radio, agrégats publics) → `docs/sources/mediametrie.md` (avec caveat GIE).
- AMF (déclarations actionnariat groupes cotés) → `docs/sources/amf.md`.
- Greffes des tribunaux de commerce (non cotés) → `docs/sources/societes-greffes.md`.
- Rapport Assouline du Sénat (2022) sur la concentration médiatique → source citée.

**Pour SQ2 (modèles éco)** :
- DGMIC (aides à la presse, nominatives) → `docs/sources/dgmic.md`.
- Comptes annuels groupes cotés (AMF) → mutualisé avec SQ1.
- Cour des comptes (rapports annuels audiovisuel public) → `docs/sources/cour-des-comptes.md`.
- EBU Funding of Public Service Media → `docs/sources/ebu.md`.

**Pour SQ3 (pluralisme à l'antenne)** :
- ARCOM données ouvertes hebdomadaires → mutualisé.
- AGORA (Représentants d'intérêts HATVP) → `docs/sources/hatvp-rri.md`.

**Pour SQ4 (indépendance)** :
- Source qualitative : enquêtes Mediapart, *La Lettre A*, Acrimed (sources situées) → `docs/sources/acrimed.md`, `docs/sources/mediapart-enquetes.md`.
- Codes éditoriaux publics des médias et chartes éditoriales → source par média.

**Pour SQ5 (médias non affiliés)** :
- ACPM affichées des médias indépendants → mutualisé.
- Déclarations publiques d'abonnés (Mediapart, La Lettre A) → source citée.
- API publique YouTube (créateurs civiques) → `docs/sources/youtube-api.md`.
- Statuts juridiques (greffes) → mutualisé.

**Pour SQ6 (confiance)** :
- Reuters Institute Digital News Report → `docs/sources/reuters-institute.md`.
- Baromètre Kantar Public pour *La Croix* → `docs/sources/kantar-la-croix.md`.
- European Social Survey modules trust → `docs/sources/ess.md`.
- Eurobaromètre Média → `docs/sources/eurobarometre-media.md`.

**Pour SQ7 (international)** :
- Reporters sans frontières (Index annuel) → `docs/sources/rsf.md`.
- OCDE statistics on culture/media → `docs/sources/ocde.md`.
- BBC Annual Report → source citée.
- Bundeshaushalt Allemagne → source citée.

**Transverse** :
- HATVP RRI (lobbying médias) → mutualisé avec autres dossiers, déjà prévue dans backlog v2.
- INSEE (statistiques contextuelles) → source partagée multi-dossiers.

Total estimé load-bearing : ~22-25 sources ingérées.

### 7.2. Sources citées (bibliographie académique) — cible ~30-40

Voir §1bis « Cadre intellectuel mobilisé » pour la liste de référence. À compléter au fil de la rédaction effective. Format : citations standard dans les pages de dossier, sans ingestion technique.

### 7.3. Périmètre des programmes scrapés (réduction v0.2)

**v0.1** prévoyait 12 partis × 2-3 versions historiques = 24-36 documents.

**v0.2** : 8-10 partis × **version actuelle (2027)** + version 2022 pour les partis dont l'évolution est centrale. Versions historiques plus anciennes reportées V2 (SCD2 prévu mais alimentation simplifiée en V1, voir parking lot data engineer dans la doctrine v0.2).

Justification : retour data-engineer-senior — scraper 36 documents est probablement le scope le plus gourmand en temps caché. Sur un MVP solo, prioriser la qualité actuelle vs l'historicité.

---

## 8. Périmètre et angles morts assumés V1

### 8.1. Inclus dans la V1

- Mesure quantitative des 4 niveaux de concentration (capitalistique, contrôle, éditoriale qualitatif, audience) sur les principaux marchés français.
- Mesure des modèles économiques par segment, y compris audiovisuel public post-réforme CAP 2022.
- Mesure du pluralisme formel ARCOM (caveat : niveau 1 seulement du pluralisme).
- Synthèse qualitative des cas documentés d'indépendance éditoriale et **contre-exemples de résistance documentés**.
- Cartographie des médias non affiliés selon typologie tri-dimensionnelle (ADR-0026).
- Mesure de la confiance par enquête séparée (Reuters DNR et Kantar/La Croix).
- Comparaisons internationales dans le cadre Hallin & Mancini.
- Cartographie des positions des 8-10 partis principaux sur la régulation des médias (version actuelle + version 2022 si pertinent).
- Critique de cohérence : positions × votes effectifs des élus (Députoscope filtré dossier Médias).
- Doctrine droit de réponse opérationnelle (ADR-0029) avant première publication.

### 8.2. Exclus en V1, reportés V2 ou V3

- Analyse Common Crawl de la couverture médiatique sur 10 ans (bloqué par ADR-0022, régime de rétention).
- Sous-question 8 (fact-checking) — reportée V2 avec reformulation.
- Module audit personnel multi-dossiers (V2, EPIC Q).
- MCP server `mcp-data` exposant ce dossier en lecture (V2, EPIC R).
- Versions historiques anciennes des programmes (> 2017) — reportées V2.

### 8.3. Angles morts assumés explicitement V1

Sept sujets que la V1 **ne traite pas** et qui méritent un dossier dédié ou intégration V2 :

1. **Sociologie des journalistes eux-mêmes** : CSP, évolution de la précarité (pigistes, intermittents, CDD), formation (écoles reconnues vs autres parcours), distribution géographique. La V1 ne dispose pas du temps pour traiter cette dimension (sources principales : Devillard *et al.* Panthéon-Assas, travaux Marchetti et Ruellan). Sans cette dimension, l'« indépendance éditoriale » de la SQ4 est traitée hors-sol — limite assumée.

2. **Question du genre dans le journalisme** : composition genrée des rédactions et son évolution, indicateur structurel du pluralisme effectif. Travaux : Coulomb-Gully, Damian-Gaillard. Reportée V2 ou dossier dédié.

3. **Algorithmes des réseaux sociaux et économie de l'attention** : adaptation des médias aux logiques algorithmiques (titres SEO, vidéos courtes, formats TikTok). Travaux : Mercier & Pignard-Cheynel, Smyrnaios. Sujet immense qui mériterait un dossier dédié. V1 ne le traite pas.

4. **Médias régionaux / presse quotidienne régionale (PQR)** : Ouest-France est le premier quotidien français en diffusion, et la PQR a ses logiques propres (capitalisme familial, mutuelles, groupes régionaux, dépendance aux annonces publiques). V1 mentionne la PQR dans SQ1 mais ne lui consacre pas l'analyse de fond qu'elle mérite. Dossier dédié futur.

5. **Consommation directe de médias étrangers par les Français** : *Courrier International*, *Guardian*, *FT*, *NYT*, *Spiegel*… frange du public à profil sociologique distinct (CSP+ urbaines). Déversoir significatif du marché informationnel haut-de-gamme. V1 mentionne mais ne quantifie pas. V2.

6. **Structure de propriété des annonceurs** : chevauchements actionnariat médias / annonceurs (notamment LVMH / Bouygues / Bolloré). Indicateur de dépendance publicitaire indirecte. Travaux : Acrimed, Reporterre. V1 ne le traite pas. V2.

7. **Économie de l'attention et adaptation des médias aux plateformes** : transformation du métier journalistique sous contrainte algorithmique. Recouvre partiellement le point 3. V2.

Mention explicite de ces 7 angles morts dans la page d'accueil du dossier publié — la transparence sur les limites est partie intégrante de la posture méthodologique.

---

## 9. Calendrier détaillé du dossier

Inchangé par rapport à v0.1.

- **Mi-juillet 2026** : note de cadrage v1.0 validée par comité humain (cette note actuellement en v0.2 doit progresser vers v0.3 après comité humain).
- **Août 2026** : démarrage des ingestions sources structurées (EPIC J : ARCOM, ACPM, DGMIC, Médiamétrie, AMF, etc.).
- **Septembre 2026** : ingestion scraping (8-10 programmes partis version actuelle, sites institutionnels). Analyse et tests de réalité (EPIC L).
- **Octobre 2026** : rédaction (EPIC M). Pré-relecture IA strate 1 sur le contenu rédigé (semaine 43).
- **1ᵉʳ novembre 2026** : remise au comité humain pour relecture strate 2.
- **18 novembre 2026** : publication officielle v1.0.0.

---

## 10. Risques propres à ce dossier

| Risque | Probabilité | Gravité | Mitigation |
|---|---|---|---|
| Mise en cause juridique sur SQ4 (indépendance) | moyenne | élevée | Validation par persona journaliste-independant avant publication. Formulations strictement factuelles avec sources primaires non rétractées. **Doctrine droit de réponse formalisée [ADR-0029]**. |
| Mauvaise interprétation du dossier (« attaque politique des médias ») | élevée | moyenne | Encart pédagogique en intro. Section §1.2 « Notre posture épistémique » exposée. Inclusion équitable des contre-arguments dans tous les angles de lecture. Comité de relecture pluraliste publiquement identifié. |
| Données ARCOM ou ACPM en rupture (changement de méthodologie pendant le projet) | faible | moyenne | Choix conscient des indicateurs longitudinaux les plus stables. Mention explicite des changements méthodologiques quand ils existent. **ADR-0027 (snapshots) à venir pour gérer les rétro-corrections**. |
| Cas documentés sur SQ4 datés ou contestés depuis publication originale | moyenne | moyenne | Limitation aux cas avec source primaire publique non rétractée **et non condamnée en diffamation**. Mise à jour trimestrielle si évolution. |
| Dossier perçu comme militant par les défenseurs des médias mainstream | élevée | faible | Page « Production de cette page » détaillant le double processus de relecture (ADR-0024). Comité pluraliste publiquement identifié. **Conflits d'intérêts de l'auteur déclarés** (cf. §11bis). |
| Indicateur de concentration mal interprété (« HHI au-dessus de 2 500 = illégal ») | moyenne | moyenne | Caveat permanent : les seuils HHI de la DG Comp sont des seuils pour les *concentrations* (fusions), pas des seuils prescriptifs pour le pluralisme. Pédagogie explicite. |
| Médiamétrie GIE — mesure d'audience non indépendante | structurel | moyenne | Caveat permanent dans toute citation de données Médiamétrie. Source card avec mention explicite. |
| Mauvaise comparabilité internationale (Hallin & Mancini ignoré) | faible | moyenne (v0.1) → faible (v0.2) | Cadre Hallin & Mancini intégré explicitement en intro SQ7 (v0.2). |
| Risque d'instrumentalisation du droit de réponse | moyenne | faible | Procédure stricte (cf. ADR-0029) : recevabilité formelle, longueur ≤ contenu initial, pas de droit de réponse à la réponse. |

---

## 11. Questions ouvertes à arbitrer par le comité humain (strate 2)

Questions résiduelles après strate 1 et arbitrage auteur :

- Faut-il inclure ou non un audit personnel V1 sur ce dossier (lié à EPIC N) ? Avantage : booste l'engagement. Risque : disperse le focus, et N dépend du gate juridique de l'audit personnel (cf. doc 13 backlog v2 §EPIC N). **Position de défaut** : audit V1 inclus si EPIC N est passé, sinon report sur le 2e dossier.

- Doit-on traiter les **créateurs civiques sur Twitch/YouTube** dans la SQ5 (intégration à la typologie ADR-0026) ou en sous-question dédiée ? Argument pour intégration : cohérence avec la typologie. Argument pour dédié : c'est l'évolution la plus rapide et mériterait un traitement à part. **Position de défaut v0.2** : intégration à SQ5 avec encart méthodologique sur les difficultés de mesure (audience cumulée vs vues vidéo, comparabilité avec médias traditionnels).

- Faut-il une **section dédiée Algorithmes des réseaux sociaux** dans le dossier Médias V1, ou cela mérite-t-il un dossier propre ? **Position de défaut v0.2** : angle mort assumé V1 (cf. §8.3 point 3), dossier dédié futur.

- Comment équilibrer la cartographie qualitative des **cas documentés de pressions éditoriales** (SQ4) avec les **contre-exemples de résistance** ? Risque de fausse symétrie si on présente 5 cas de pressions et 5 cas de résistance comme équivalents alors que la littérature ne les présente pas comme tels. **Position de défaut v0.2** : présenter selon la pondération que la littérature accorde, avec section explicite « État de la recherche ».

- La sous-question 5 (médias non affiliés) doit-elle inclure les **médias militants assumés** (presse anarchiste, presse syndicale, presse engagée auto-déclarée) ? **Position de défaut v0.2** : oui, en sous-section de la typologie ADR-0026 avec mention explicite « médias se revendiquant engagés ».

- Faut-il intégrer une analyse de la **consommation directe de médias étrangers par les Français** dans SQ6 (confiance) ? Argument pour : cette frange du public influence le débat (CSP+). Argument contre : disperse SQ6. **Position de défaut v0.2** : mention en angle mort assumé (cf. §8.3 point 5), pas d'analyse de fond V1.

---

## 11bis. Transparence éditoriale

### 11bis.1. Conflits d'intérêts de l'auteur

Conformément aux bonnes pratiques de la presse indépendante et à l'esprit de la posture épistémique du projet (§1.2), l'auteur du dossier déclare publiquement :

**Statut professionnel actuel** : Sam exerce comme **métreur**, **OPC (Ordonnancement-Pilotage-Coordination)**, **suivi financier DET (Direction de l'Exécution des Travaux)** et **créateur de software interne** dans une agence d'**architecture du patrimoine**. En parallèle, en **alternance**, il suit la formation **Data Engineer (niveau 7) chez Simplon** — projet AporiaPolis dont fait partie le présent dossier.

**Trajectoire professionnelle antérieure** :
- **12 ans** comme coach et manager dans l'**esport** ;
- **4 ans** à la création d'une **ferme pédagogique en permaculture** ;
- **12 ans** comme chef de service puis directeur de **centre de loisirs (périscolaire, 0-25 ans)** ;
- Formation initiale en **prépa ingénieur système électronique et traitement de l'information**.

Cette trajectoire multi-secteurs (éducation, agriculture, esport, patrimoine architectural, data engineering) est mentionnée pour transparence, sans prétendre qu'elle constitue une expertise spécifique sur le secteur médiatique français — c'est précisément l'inverse qui est utile au projet : l'auteur n'a pas de capital social ni intellectuel préinvesti dans le champ journalistique français, ce qui réduit certains conflits d'intérêts évidents mais peut aussi être une limite (extériorité au milieu).

**Conflits d'intérêts déclarés** : aucun lien financier avec les groupes médiatiques étudiés dans ce dossier à la date de la v0.2. L'employeur actuel (agence d'architecture du patrimoine) n'a pas de lien direct avec le secteur médiatique français. Aucune participation, contrat, mandat, ou rémunération dans le secteur médiatique français.

**Consommation médiatique personnelle déclarée** :
- **Presse écrite** : abonnement au *Monde Diplomatique* (mensuel, presse critique engagée).
- **Flux numériques** : YouTube et Twitter / X comme canaux quotidiens.
- **Pas d'abonnement** à la presse quotidienne nationale (Le Monde, Libération, Le Figaro, Les Échos).
- **Peu d'exposition quotidienne à l'audiovisuel public** (France Inter, France TV, etc.).

Cette consommation oriente nécessairement la perception du paysage médiatique : sensibilité forte à la **critique structurelle** des médias (héritage *Diplo*), exposition aux **flux courts et algorithmes des plateformes** (YouTube, X), **faible exposition aux médias mainstream du quotidien**. Limite assumée explicitement — c'est précisément l'écart de cette consommation à la moyenne du public français qui rend le dossier nécessaire pour l'auteur (volonté de comprendre rigoureusement ce qu'il consomme peu), et c'est aussi pour cela que la **relecture pluraliste par le comité humain** (strate 2) est essentielle : compenser cette limite par des perspectives ancrées dans d'autres pratiques de consommation.

**Positionnement politique** : **matérialisme historique assumé**, déjà déclaré sur la page « Qui parle ? » du site (héritage critique du marxisme français, sans appartenance partisane déclarée). Cette posture intellectuelle est rendue publique précisément pour que les lecteur·rice·s puissent en tenir compte dans leur lecture du dossier. Conformément à la posture épistémique du projet (§1.2), elle est **assumée comme positionnée**, pas dissimulée derrière une fausse neutralité.

**Audience préexistante** : l'auteur dispose d'une audience préexistante sur Twitter / X (~25 k abonnés), constituée principalement autour de l'**esport** et non du sujet politique du présent dossier. Doctrine de diffusion : **compte AporiaPolis projet dédié** pour la communication éditoriale, **compte personnel pour disclosure sobre uniquement** (mention du projet sans relais éditorial direct, pour ne pas instrumentaliser une audience constituée sur un autre objet).

**Engagement temporel** : ce projet est le projet de fin de **certification Simplon Data Engineer niveau 7**. Le calendrier (publication V1 visée mi-novembre 2026) est contraint par cette double exigence : qualité éditoriale du dossier et exigences de la certification. Cet engagement explique les arbitrages de périmètre (**MVP solo sur 12 mois**) ainsi que les angles morts assumés V1 listés en §8.3.

### 11bis.2. Composition prévue du comité humain de relecture (strate 2)

Au moment de cette v0.2, le comité humain est en cours de constitution (EPIC D du backlog v2). Profils visés (3-5 personnes, avec leur accord pour mention publique) :

1. **Chercheur·euse en sciences de l'information et de la communication** (SIC) — pour la rigueur conceptuelle (cadre Hallin & Mancini, Champagne, Cagé).
2. **Journaliste exerçant·e** (carte de presse) — pour la déontologie et l'anticipation des risques juridiques.
3. **Sociologue ou politiste quantitatif·ve** — pour la méthodologie des tests de réalité.
4. **Lecteur·rice profane curieux·se** — pour l'accessibilité grand public.
5. **Data Engineer senior** — pour la rigueur technique (optionnel V1).

Cette composition reflète celle des 5 personae IA (strate 1) mais avec des humains réels. Les personae IA ne remplacent jamais le comité humain (cf. ADR-0024) : elles préparent la matière pour que le temps bénévole du comité soit dédié aux questions les plus structurantes.

**Mandat du comité** : 10-20 heures par an et par membre, avis sur note de cadrage + relecture du dossier final pré-publication. Mention publique avec accord, sinon anonyme. Voir `docs/methodology/comite.md` (à produire dans EPIC D).

### 11bis.3. Trace IA dans la production de cette note

Conformément à l'ADR-0024 et à la doctrine d'AporiaPolis sur la transparence éditoriale :

- **Rédaction initiale** (v0.1) : assistance Cowork (Claude) pour la structuration et la rédaction première version, validation humaine systématique (Sam).
- **Pré-relecture strate 1** : 5 personae IA documentées dans `docs/methodology/personae-ia/`, retours archivés dans `dossiers/medias/relecture/strate-ia-cadrage-2026-05-16-*.md`.
- **Arbitrage et production v0.2** : assistance Cowork (Claude) pour la production de cette v0.2 intégrant les retours strate 1, sous la supervision de Sam qui a validé chaque action d'arbitrage en bloc.
- **Strate 2 (à venir)** : validation par le comité humain pluraliste sans assistance IA.

Toute publication finale du dossier (v1.0) intégrera l'encart « Production de cette page » conformément à l'ADR-0024.

---

## 12. Tableau de bord de production de ce cadrage

| Étape | Statut | Date prévue / réalisée |
|---|---|---|
| Pré-note v0.1 rédigée | ✅ | 2026-05-XX |
| Pré-relecture IA strate 1 (5 personae) | ✅ | 2026-05-16 |
| Arbitrage auteur post-IA + production v0.2 | ✅ | 2026-05-16 |
| 3 ADR émergentes produites (0025, 0026, 0029) | ✅ | 2026-05-16 |
| Recrutement comité humain (3 contacts engagés) | ⏳ | 2026-06-30 (cible) |
| Soumission v0.2 au comité humain | ⏳ | 2026-07-XX |
| Retours comité strate 2 archivés | ⏳ | 2026-07-XX |
| Arbitrage post-comité → v1.0 | ⏳ | 2026-07-31 (cible) |
| Stockage v1.0 final dans le repo | ⏳ | post-validation comité |
| Démarrage rédaction du dossier (EPIC M) | ⏳ | 2026-10-XX (après validation v1.0) |
| Publication officielle dossier v1.0.0 | ⏳ | 2026-11-18 (cible) |

---

## 13. Diff résumé v0.1 → v0.2

Pour suivi méthodologique :

**Ajouté en v0.2** :
- §1.2 « Notre posture épistémique » (auto-réflexivité explicite).
- §1.3 EMFA et DSA dans le contexte réglementaire.
- §1bis « Cadre intellectuel mobilisé » avec ~15 références bibliographiques.
- SQ1 restructurée en 4 niveaux de concentration (référence ADR-0025).
- SQ2 et SQ3 intègrent explicitement l'audiovisuel public.
- SQ4 inclut une section « contre-exemples » de résistance documentée.
- SQ5 reformulée et adoptant la typologie tri-dimensionnelle (ADR-0026).
- SQ6 explicite la dimension générationnelle.
- SQ7 intègre le cadre Hallin & Mancini.
- §3 — Angle de lecture « médias militants assumés » ajouté à SQ4.
- §4 — Test 7 (financement audiovisuel public) entièrement refondé avec matrice de périmètres.
- §4 — Tests 8 et 10 explicitement qualitatifs, pas maquillés en quanti.
- §5 — Caveat sur le score RICE.
- §6.3 « Cibles data quality » (tests dbt, freshness, snapshots).
- §8.3 « Angles morts assumés V1 » : 7 sujets explicités.
- §10 — Risques avec doctrine droit de réponse (ADR-0029) et caveat HHI.
- §11bis « Transparence éditoriale » : conflits d'intérêts auteur, composition comité humain, trace IA.

**Réduit ou modifié en v0.2** :
- Sources tracées : 47 → ~22-25 load-bearing + ~30-40 citées (distinction explicite).
- Programmes scrapés : 12 × 2-3 versions → 8-10 × version actuelle (+ 2022 si pertinent).
- Énumération nominative des propriétaires (§1.3) : datée et sourcée précisément.
- Citation « ~30 % en 2025 vs ~39 % en 2015 » : sourcée Reuters DNR avec caveats méthodologiques.
- Acronymes : développés à leur première occurrence + glossaire en §14.
- Mots « strate 1 / strate 2 » : remplacés par « pré-relecture IA / validation comité humain » dans les sections grand public.
- Angle libéral reformulé (était caricaturé en v0.1).

**Inchangé** :
- Question principale.
- Calendrier de production.
- Périmètre macro (7 sous-questions V1, SQ8 reportée V2).

---

## 14. Glossaire

| Acronyme | Développement | Domaine |
|---|---|---|
| **ACPM** | Alliance pour les Chiffres de la Presse et des Médias | Mesure d'audience presse + web FR |
| **ADR** | Architecture Decision Record (note de décision d'architecture du projet) | Méthodologie projet |
| **AGORA** | Logiciel/téléservice de la HATVP pour le Répertoire des Représentants d'Intérêts | Lobbying |
| **AI Act** | Règlement européen sur l'intelligence artificielle (mars 2024) | Droit UE |
| **AMF** | Autorité des Marchés Financiers | Régulation financière FR |
| **ARCOM** | Autorité de Régulation de la Communication Audiovisuelle et Numérique (fusion CSA/HADOPI, 2022) | Régulation médias FR |
| **CAP** | Contribution à l'Audiovisuel Public (ex-redevance, supprimée en 2022) | Financement audiovisuel public |
| **C5 / C10** | Concentration ratio à 5 (resp. 10) acteurs : part cumulée des 5 (10) premiers | Mesure concentration |
| **CSP** | Catégorie Socio-Professionnelle | Sociologie |
| **DGMIC** | Direction Générale des Médias et des Industries Culturelles (Ministère de la Culture) | Tutelle médias FR |
| **DSA** | Digital Services Act (règlement UE applicable depuis 2024) | Droit UE |
| **EBU** | European Broadcasting Union (Union européenne de radio-télévision) | Audiovisuel public européen |
| **EMFA** | European Media Freedom Act (avril 2024, applicable août 2025) | Droit UE médias |
| **EPIC** | Lot de travail majeur dans la roadmap projet (sur GitHub Project) | Méthodologie projet |
| **ESS** | European Social Survey | Enquête sociologique européenne |
| **GIE** | Groupement d'Intérêt Économique | Statut juridique |
| **HATVP** | Haute Autorité pour la Transparence de la Vie Publique | Régulation FR |
| **HHI** | Herfindahl-Hirschman Index | Indicateur de concentration standardisé |
| **IFCN** | International Fact-Checking Network | Fact-checking |
| **INA** | Institut National de l'Audiovisuel | Audiovisuel public FR |
| **MVP** | Minimum Viable Product (version V1 d'AporiaPolis dans le contexte du projet) | Méthodologie projet |
| **NLP** | Natural Language Processing (traitement automatique du langage) | Technique IA |
| **PQR** | Presse Quotidienne Régionale | Médias FR |
| **PSM** | Public Service Media (médias de service public) | International |
| **RICE** | Reach × Impact × Confidence / Effort (méthode de priorisation) | Méthodologie projet |
| **RGAA** | Référentiel Général d'Amélioration de l'Accessibilité | Accessibilité web FR |
| **RGPD** | Règlement Général sur la Protection des Données | Droit UE protection données |
| **RRI** | Répertoire des Représentants d'Intérêts (HATVP) | Lobbying |
| **RSF** | Reporters sans frontières | ONG liberté de la presse |
| **SA / SAS / SARL** | Société Anonyme / par Actions Simplifiée / À Responsabilité Limitée | Statuts juridiques FR |
| **SCD** | Slowly Changing Dimension (gestion historicisation des dimensions, type 1/2/3 selon Kimball) | Data engineering |
| **SCOP** | Société Coopérative et Participative | Statut juridique FR |
| **SCIC** | Société Coopérative d'Intérêt Collectif | Statut juridique FR |
| **SDJ** | Société des Journalistes (forme collective interne à une rédaction) | Profession journalistique |
| **SIC** | Sciences de l'Information et de la Communication | Discipline universitaire |
| **SMART** | Spécifique, Mesurable, Atteignable, Réaliste, Temporellement défini (objectifs) | Méthodologie projet |
| **T1 / T2 / T3 / T4** | Trimestres du projet AporiaPolis (T1 mai-juillet 2026, T2 août-octobre, etc.) | Méthodologie projet |
| **TOCE** | Taxe sur les Opérateurs de Communications Électroniques (finance partiellement l'audiovisuel public FR) | Financement audiovisuel public |
| **V1 / V2 / V3** | Versions successives d'AporiaPolis dans la roadmap | Méthodologie projet |

---

**Prochaine action de l'auteur (Sam)** : démarrer le recrutement du comité humain (EPIC D du backlog v2), avec cette v0.2 comme matière concrète à présenter aux candidat·es. Une fois 3 contacts engagés et la composition stabilisée, soumettre la v0.2 pour relecture strate 2. Intégrer les retours du comité humain dans une v1.0 stabilisée avant le démarrage de la production effective du dossier (EPIC J ingestion sources structurées, en août 2026).
