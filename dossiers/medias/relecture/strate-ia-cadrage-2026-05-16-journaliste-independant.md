---
slug: strate-ia-cadrage-2026-05-16-journaliste-independant
title: Pré-relecture IA strate 1 — Persona Journaliste indépendant·e
document_relu: dossiers/medias/cadrage.md (v0.1)
persona: docs/methodology/personae-ia/journaliste-independant.md (v1)
strate: 1 (IA, avant arbitrage auteur)
date: 2026-05-16
authors: [persona-ia-journaliste-independant]
---

# Pré-relecture — Persona Journaliste indépendant·e

**Document** : `dossiers/medias/cadrage.md` (v0.1, brouillon)
**Date** : 2026-05-16
**Strate** : 1 (relecture IA, avant arbitrage auteur)

> Je joue le rôle d'un·e journaliste exerçant·e dans la presse indépendante (style Mediapart / StreetPress / Reporterre / pigiste régulier·ère), carte de presse, ~15 ans de métier. Critique éthique et factuelle, pas politique partisane. Je suis une persona, pas une personne réelle.

---

## 1. Solide

Plusieurs choix tiennent sur le plan déontologique et méritent d'être conservés tels quels.

**Posture méthodologique assumée** (§1, ligne 33). « Nous mesurons, contextualisons, comparons. Nous ne tranchons pas la question principale. » C'est exactement la formulation qu'attendrait une rédaction sérieuse. Garde-fou contre l'éditorialisation rampante. À reprendre tel quel en intro publique du dossier.

**Distinction explicite peut/ne peut pas faire** (§1). Reconnaître les limites de la data sur « indépendance », « manipulation », « bon journalisme » est rare et honnête. Ça désamorce une partie des critiques qu'un·e confrère·ère pourrait formuler sur le caractère « scientiste » d'une enquête data.

**Sous-question 4 cadrée avec attention juridique** (§2, ligne 56). La mention « Aucune accusation sans source primaire publiée » est la bonne ligne. Couplée à la « validation par persona journaliste avant publication » (§10), on a un dispositif sérieux. À renforcer (voir §4 ci-dessous).

**Présentation séparée Reuters / Kantar** (§4, test 3). Refuser de fusionner deux séries aux modes de collecte différents est un réflexe de pro. Beaucoup de journalistes économiques agrègent sans signaler, ça fausse les courbes.

**Risque « perception militante » identifié et mitigé** (§10, ligne 200). Ligne consciente, dispositif (encart pédagogique, comité pluraliste, page « Production de cette page ») cohérent. Manque toutefois la mise en œuvre concrète (voir §5).

**Calendrier réaliste**. Cinq mois entre publication (18 nov 2026) et premier tour de la présidentielle d'avril 2027 : c'est le bon timing pour qu'un dossier circule sans être étiqueté « publication de campagne ».

---

## 2. Problématique (avec proposition de reformulation)

**Ligne 23 — énumération de propriétaires sans dates ni sources**

> *« rachats successifs (Bolloré → Vivendi puis Lagardère, Niel → Le Monde, Drahi → Libération, Kretinsky → Marianne, Arnault → Le Parisien, etc.) ont reconfiguré le paysage en 10 ans »*

L'enchaînement « Bolloré → Vivendi puis Lagardère » est elliptique pour un·e lecteur·rice non spécialiste, et l'absence totale de dates ne tient pas dans une note publiée sur un repo public (ADR-0023). Le verbe « reconfiguré » est neutre, c'est bien, mais l'effet d'accumulation lexicale crée une connotation. Reformulation suggérée :

> *« Depuis ~10 ans, la structure de propriété de plusieurs titres majeurs s'est modifiée : Vivendi (groupe Bolloré) a pris le contrôle de Lagardère (2023), Xavier Niel détient des participations significatives dans Le Monde Libre depuis 2010, Patrick Drahi est l'actionnaire de Libération depuis 2014 (en SCIC depuis 2020), Daniel Křetínský a acquis Marianne en 2018 via CMI France, le groupe LVMH (Bernard Arnault) détient Les Échos depuis 2007 et Le Parisien depuis 2015. Sources : [à compléter, type ARCOM bilan annuel, AMF actes de cession, enquêtes économiques Le Monde/Les Échos]. »*

Chaque nom propre exige une date d'acquisition documentée et un acte juridique référencé.

**Ligne 22 — « niveau historiquement bas »**

> *« la confiance des Français dans leurs médias est à un niveau historiquement bas »*

« Historiquement » sous-entend une profondeur que la donnée n'a pas. Reuters Institute couvre la France depuis 2012, le baromètre Kantar/La Croix depuis 1987 mais avec des questions et modes de collecte qui ont évolué. Reformulation :

> *« La confiance déclarée des Français dans les médias se situe à un niveau bas sur la période documentée par les deux principaux baromètres : ~30 % selon le Reuters Institute Digital News Report 2025 (vs ~39 % en 2015, panel auto-recruté en ligne) ; baromètre Kantar/La Croix à comparer séparément (méthodologie face-à-face). »*

**Ligne 53 — « autocensure attestée par SDJ »**

> *« cas documentés de pressions éditoriales (départs forcés, autocensure attestée par SDJ, conflits avec l'actionnaire) »*

« Autocensure » est un terme glissant : qui constate, comment, avec quelle valeur ? « Attestée par SDJ » donne une apparence de preuve qui peut être attaquée. Reformulation :

> *« Cas documentés de pressions éditoriales : départs de journalistes ayant fait l'objet de communiqués publics des sociétés de journalistes (SDJ), conflits éditoriaux ayant donné lieu à des enquêtes publiées par des médias tiers (par exemple par des publications type Mediapart, La Lettre A, Le Canard enchaîné), refus de publication ayant fait l'objet d'un constat écrit en interne et rendu public. »*

**Ligne 75 — sous-question 8, mesure du taux de fact-checks de la maison-mère**

> *« taux de fact-checks portant sur la maison-mère »*

Mesure piégeuse. Une cellule de fact-checking se déclenche sur des affirmations publiquement contestées ou virales, pas sur sa propre rédaction qui n'émet pas d'affirmations factuelles à fact-checker au même rythme. Conclure « 0 % de fact-check de la maison-mère = capture » serait un raccourci fallacieux. Si la sous-question 8 est conservée, formuler plutôt :

> *« Existence d'une charte d'indépendance vis-à-vis de la maison-mère, signature IFCN, traitement de cas où la maison-mère a été publiquement contestée sur un fait. »*

Et la bascule en V2 (déjà actée § ligne 131) reste la bonne option.

**Ligne 84 — angles de lecture caricaturés**

> Angle libéral : *« la propriété privée est légitime, la concurrence joue son rôle, l'audience sanctionne »*

« L'audience sanctionne » est polémique, pas la formulation que tiendraient les défenseurs sérieux de cet angle (Schumpeter, Hayek revisité, économistes de la concurrence). Reformulation :

> *« Angle libéral / concurrentiel : la diversité des titres et la concurrence sur le marché de l'attention garantissent à elles seules le pluralisme ; les régulations supplémentaires créent plus de risques (capture du régulateur) qu'elles n'en règlent. »*

Symétriquement, l'angle structuraliste ligne 84 (« la concentration capitalistique est une menace pour le pluralisme, indépendamment du comportement des propriétaires ») est correct, mais à compléter avec ses contre-arguments empiriques (cas de groupes concentrés avec rédactions indépendantes documentées).

---

## 3. À sourcer

Le cadrage doit lui-même être adossé à des sources primaires liées dès la v0.2, sans attendre la publication du dossier final. Liste prioritaire :

- **Reuters Institute DNR 2025** (ligne 22) : lien direct vers la fiche France du rapport. Le « ~30 % » et le « ~39 % en 2015 » doivent être chiffres exacts avec page de référence.
- **Position FR au classement RSF** (test 9, ligne 108) : lien vers l'historique 2015-2025 sur le site RSF, et précision méthodologique (la méthode RSF a évolué en 2022).
- **Fusion CSA/HADOPI en 2022** (ligne 24) : préciser que c'est la loi du 25 octobre 2021, entrée en vigueur le 1er janvier 2022. Lien Legifrance.
- **Financement audiovisuel public comparé** (test 7, ligne 104) : sourcer précisément. Les comparaisons crédibles passent par les rapports EBU (Funding of Public Service Media) ou Cour des comptes. Attention : la suppression de la redevance en 2022 a complexifié la lecture (substitution par TVA affectée).
- **Aides à la presse DGMIC** (test 6) : la DGMIC publie effectivement les aides nominatives. Lien à mettre dès le cadrage.
- **Cas emblématiques cités sans référence** : si le dossier mentionne « cas Bolloré sur Europe 1 », « cas Geoffroy Lejeune au JDD », « cas Marianne sous Křetínský », chacun doit pointer vers au moins une enquête tierce publiée et non rétractée. Les enquêtes Mediapart et *La Lettre A* sont citées « à citer pas ingérer » (ligne 158) mais aucune référence précise n'est donnée. À compléter dans `docs/sources/`.
- **SCIC / coopératives de presse** : Mediapart est en SCOP depuis 2018 (et non SCIC — à vérifier), Reporterre en association puis SCIC, Politis en SCIC depuis 2018. Statut juridique à préciser au cas par cas, avec lien vers les statuts publics (greffe).
- **EMFA (European Media Freedom Act)** : adopté en avril 2024, applicable août 2025. Le cadrage ne le mentionne pas — c'est une lacune sectorielle (voir §5).

---

## 4. Risques juridiques

C'est ma zone de plus grande vigilance. Le cadrage est lui-même un document public (repo GitHub public, ADR-0023). Les formulations y sont juridiquement exposées dès leur commit, même s'il s'agit d'un brouillon de travail.

**Diffamation potentielle — énumération nominative** (ligne 23). Lister « Bolloré → Vivendi puis Lagardère, Niel → Le Monde, Drahi → Libération, Křetínský → Marianne, Arnault → Le Parisien » sans factualisation précise de chaque acquisition juridique expose à des recours, surtout si le contexte du paragraphe suggère un effet négatif (« reconfiguré » est neutre, mais l'enchaînement avec « concentration capitalistique accélérée » colore négativement). Mitigation : datage strict, lien vers acte juridique, suppression du « etc. » qui est typiquement un piège (donne l'impression d'une liste plus longue à charge).

**Dénigrement potentiel — sous-question 4** (ligne 53). Toute mention nominative d'un groupe associée à « pressions éditoriales » dans le dossier final devra :
1. S'appuyer sur une enquête tierce publiée, non rétractée, et non condamnée en diffamation (ce dernier point doit être ajouté à la phrase « Aucune accusation sans source primaire publiée » ligne 56).
2. Mentionner la position du groupe mis en cause (droit de réponse anticipé : ont-ils répondu publiquement à l'accusation ? Quelle est leur position ?).
3. Distinguer la responsabilité juridique de l'actionnaire et celle du média (la jurisprudence française est claire : on ne peut pas imputer à un actionnaire les décisions éditoriales sans démonstration d'intervention directe).

**Engagement de droit de réponse non formalisé**. Le cadrage mentionne « Droit de réponse mentionné » dans la mitigation des risques (ligne 196) mais sans dispositif concret. La loi du 29 juillet 1881 (et le décret du 24 octobre 2007 pour la presse en ligne) prévoit un droit de réponse opposable dans les 3 mois suivant la publication. À formaliser dans une section dédiée du cadrage et du dossier final :

> *« AporiaPolis s'engage à recevoir et publier les droits de réponse selon les modalités de la loi du 29 juillet 1881 et du décret n° 2007-1527. Adresse de réception : conduct@aporiapolis.org. Délai de traitement : 8 jours ouvrés. »*

**Loi Bichet et statut éditeur/hébergeur** : si le dossier publie des extraits substantiels d'enquêtes tierces (Mediapart, *La Lettre A*), s'assurer du respect de la courte citation (article L.122-5 CPI) ou de l'obtention d'une autorisation explicite. Le cadrage doit l'expliciter.

**Anonymat des sources et témoins** : si l'enquête (notamment sous-question 4) recueille des témoignages de journalistes en activité, la protection des sources (article 2 de la loi du 29 juillet 1881 modifiée 2010) doit être formellement protocolée. À documenter avant toute collecte de témoignage, pas après.

---

## 5. Manquant

Ce qu'un·e journaliste indépendant·e attendrait et qui n'est pas là.

**Contre-exemples — rédactions ayant résisté à la pression**. La sous-question 4 est unidimensionnelle si elle ne présente que les cas où la pression a abouti. Il faut documenter aussi :
- Les SDJ ayant obtenu des chartes éditoriales contraignantes (Le Monde, Libération SCIC, AFP).
- Les départs collectifs ayant abouti à des fondations de nouveaux médias (Disclose, Reporterre, Politis, Streetpress, etc. — origine et trajectoire).
- Les conflits éditoriaux ayant été tranchés en faveur de la rédaction (par exemple, cas où une SDJ a obtenu le retrait d'une décision actionnariale).

Sans ces contre-exemples, le dossier est attaquable comme « unilatéral » par les défenseurs des grands groupes.

**Audiovisuel public manquant**. France Télévisions, Radio France, France Médias Monde, Arte France, INA : pas un mot dans la liste des sous-questions, alors que c'est un acteur structurant (~30 % d'audience radio cumulée pour Radio France, ~25 % pour France TV). Question spécifique à intégrer : gouvernance (nominations ARCOM), financement (suppression de la redevance en 2022, substitution par TVA affectée), indépendance vis-à-vis du pouvoir politique. À mettre en sous-question dédiée ou à intégrer aux sous-questions 1, 2, 3.

**EMFA et DSA — cadre européen absent**. European Media Freedom Act (avril 2024, applicable août 2025) et Digital Services Act (applicable 2024) restructurent les obligations des plateformes et des États. Le cadrage cite « ARCOM (fusion CSA/HADOPI), AI Act, droit voisin presse » mais pas EMFA. Lacune majeure.

**Médias régionaux (PQR)**. Mentionnés en question ouverte (ligne 207) mais évacués. Pourtant Ouest-France est le premier quotidien français en diffusion, et la PQR est un terrain particulier (proximité avec les pouvoirs locaux, dépendance aux annonces publiques). Position minimale : un encart « limites du périmètre » expliquant que la PQR fera l'objet d'un dossier ultérieur.

**Créateurs civiques YouTube/Twitch**. Question ouverte ligne 205. Position attendue : intégrer a minima dans la sous-question 5 (médias indé) avec un encart méthodologique sur les difficultés de mesure (audience cumulée vs vues vidéo, comparabilité avec les médias traditionnels). Ne pas en faire une sous-question dédiée si on garde le périmètre V1 à 7.

**Conflits d'intérêts de l'auteur·rice**. Sur un dossier sur les médias, la transparence personnelle est attendue. Quelle est ta consommation médiatique ? As-tu un employeur passé ou présent dans un des groupes étudiés ? Tu n'es pas obligé·e de tout dire, mais une déclaration minimale (« je consomme régulièrement X, je n'ai pas de lien financier avec les groupes étudiés ») est devenue standard dans la presse indépendante. À ajouter dans la page « Production de cette page ».

**Composition du comité humain de relecture**. Mentionné comme « pluraliste publiquement identifié » (ligne 200) mais aucune composition listée dans le cadrage. À documenter dans une annexe avant la première publication (mi-juillet 2026). Et : prévoir au moins un·e journaliste exerçant·e dans ce comité, pas seulement des académiques.

**Dimension générationnelle dans la sous-question 6**. La confiance varie fortement par génération et la consommation médiatique des 18-25 ans diverge radicalement de celle des 60+. Sous-question 6 (confiance) mérite cette dimension explicite, pas juste « facteurs corrélés (génération, niveau de diplôme...) » en passant.

**Financement étranger des médias**. Quelques propriétaires ne sont pas français (Patrick Drahi est franco-israélo-portugais, Daniel Křetínský est tchèque). Sans en tirer de jugement, mentionner le sujet est nécessaire — c'est un thème récurrent du débat public, présent à droite comme à gauche.

**Sources qualitatives non listées avec précision**. Au-delà d'Acrimed et Mediapart, ajouter : *La Revue des Médias* (INA), *Méta-Media* (France Télévisions), *Press Gazette* pour le comparé, *Nieman Lab* pour les modèles éditoriaux. Rapport Cour des comptes annuels sur l'audiovisuel public, rapports Sénat sur la concentration (notamment rapport Assouline 2022).

---

## 6. Biais de ma critique

Comme demandé, voici en quoi ma perspective de journaliste indépendant·e colore ce retour, et où il faut me lire avec précaution.

**Préférence pour les médias indépendants**. J'ai été plus dur sur les formulations qui pourraient être attaquables par les grands groupes (§2, §4) que sur les formulations qui pourraient être attaquables par les médias indépendants (sous-question 5). Or, des médias indé peuvent aussi avoir leurs angles morts : financement par fondations militantes, choix éditoriaux orientés sans actionnaire, dépendance à un public fidèle qui exerce une pression douce. Le dossier ne devrait pas postuler par défaut que « indépendant = neutre ».

**Méfiance instinctive vis-à-vis des grands groupes**. Quand le cadrage cite « Bolloré → Vivendi puis Lagardère », ma première réaction est de hocher la tête, pas d'exiger des dates. C'est exactement ce piège que la pré-relecture doit corriger : exiger la rigueur formelle même quand le fond me semble correct.

**Préférence pour le concret**. J'ai insisté lourdement sur les sources primaires, les exemples nommés, les enquêtes publiées. C'est ma déformation. Or, certaines des meilleures analyses sur la concentration médiatique sont quantitatives et structurelles (indice de Herfindahl-Hirschman, indice de diversité de propriété, etc.) — pas adossées à des cas individuels. J'ai sous-pondéré cette dimension dans ma critique. Le dossier doit conserver l'angle quanti-structurel sans le diluer dans l'incarnation par cas.

**Sensibilité déontologique excessive**. J'ai pinaillé sur le mot « autocensure » et « historiquement bas », au risque de donner l'impression que tout le cadrage est problématique. Il ne l'est pas — la pré-relecture est par construction biaisée vers la critique. Le solide (§1) est plus important quantitativement que le problématique (§2), même si ma section §2 est plus longue.

**Pas d'angle « médias militants » dans ma critique des angles**. J'ai critiqué la caricature de l'angle libéral mais je n'ai pas signalé qu'un angle « médias militants assumés » (presse anarchiste, presse militante affirmée non recensée dans Acrimed) n'est pas représenté dans les angles de lecture (§3 du cadrage). Or il existe et a sa cohérence. Lacune symétrique de ma part.

**Cadre national franco-centré**. Le dossier est explicitement sur « les médias français », ce qui est légitime. Mais j'ai laissé passer sans critique le fait que la comparaison internationale (sous-question 7) est limitée à 4-5 pays « voisins ». Une journaliste indépendante venant des médias internationaux (RFI, France 24, Mediapart international desk) aurait poussé pour intégrer aussi les modèles latino-américains (presse indépendante très forte) ou africains francophones (RSF documente largement). J'ai un biais européen.

---

## Position globale

**Statut recommandé pour la v0.2** : retravailler en priorité §2.1 (énumération propriétaires), §4 (sourcing formel + droit de réponse formalisé), §5 (audiovisuel public + EMFA + contre-exemples) avant soumission au comité humain de mi-juillet. Les §1, §3, §6, §7, §9, §10 sont solides et n'appellent que des compléments mineurs.

La sous-question 4 (indépendance) reste la plus exposée juridiquement. Maintenir la « validation par persona journaliste avant publication » comme garde-fou — et l'inscrire dans le pipeline de production comme étape bloquante, pas comme bonne intention.
