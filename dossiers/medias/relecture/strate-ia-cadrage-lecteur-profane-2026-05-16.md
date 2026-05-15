---
slug: relecture-strate-ia-cadrage-medias-lecteur-profane
title: Pré-relecture IA strate 1 — Cadrage Médias français v0.1
document_relu: dossiers/medias/cadrage.md
version_relue: v0.1
persona: lecteur-profane (v1)
persona_path: docs/methodology/personae-ia/lecteur-profane.md
session_date: 2026-05-16
auteur_session: sam
statut: brut (non arbitré)
---

# Pré-relecture *Cadrage du dossier Médias français v0.1* — Persona Lecteur·rice profane

> **Statut** : retour brut de session IA, archivé avant arbitrage. Pipeline prévu en §12 du cadrage : strate 1 IA → arbitrage auteur → v0.2 → strate 2 comité humain.
>
> **Doctrine** : ADR-0024 (relecture deux strates).
>
> **Complémentarité** : retour à lire en regard de `strate-ia-cadrage-2026-05-16.md` (persona chercheuse-sic), qui porte sur la rigueur conceptuelle. Le présent retour porte sur l'**accessibilité** pour un·e lecteur·rice extérieur·e au projet.

## 1. Compris facilement

- **La question principale** (§1) : *« Le paysage médiatique français permet-il aujourd'hui un débat public pluraliste et informé ? »* — limpide, l'enjeu se saisit tout de suite. Bonne entrée, pas de jargon en ouverture.
- **« Pourquoi cette question maintenant »** (§1) : les cinq puces sont efficaces. Les exemples concrets « Bolloré → Vivendi puis Lagardère, Niel → Le Monde, Drahi → Libération… » ancrent dans du tangible.
- **« Peut faire / Ne peut pas faire »** (§1) : énorme point fort. Vous annoncez d'avance ce que vous ne prétendez pas faire. Ça met en confiance.
- **La phrase « Nous ne tranchons pas la question principale »** (§1 *in fine*) : très claire, très honnête. C'est rare et ça accroche.
- **Sous-question 1 (Qui possède les médias)** : concrète, immédiatement compréhensible. La distinction « capital de propriété vs capital de contrôle » se devine sans qu'on connaisse le vocabulaire.
- **Tableau RICE** (§5) : la conclusion verbale (« 1, 6, 3 sortent en tête ») suffit à comprendre le verdict sans avoir à décortiquer la formule.

## 2. Compris avec effort

### 2.1. « strate 1 / strate 2 » (intro)

Relu deux fois avant de comprendre que « strate 1 = IA » et « strate 2 = humain ». À la première lecture, j'imaginais des niveaux de profondeur.

**Reformulation possible** : *« pré-relecture par 5 personae IA (1ʳᵉ couche, automatique), puis validation par le comité humain (2ᵉ couche, finale) »*.

### 2.2. « 3/9 » (sous-question 3)

*« les obligations ARCOM (3/9 pour la TV, principes équivalents en radio) »* — « 3/9 », c'est trois tiers ? Neuf catégories ? Inconnu pour qui ne suit pas le sujet.

**Reformulation** : ajouter une note explicative à la première occurrence (un tiers gouvernement, un tiers majorité, un tiers oppositions, avec pondération).

### 2.3. « Test de réalité »

Vous l'utilisez 15+ fois sans le définir formellement. On finit par comprendre que c'est *« une hypothèse qu'on va tester sur les chiffres »*, mais une définition d'une ligne à la première occurrence éviterait la déduction silencieuse.

### 2.4. Tableau RICE — l'échelle

*« Score = (Reach × Impact × Confidence) / Effort »*. OK pour la formule, mais « Reach 8 » : sur quelle échelle ? 1-10 ? On suppose mais ce n'est pas dit.

**Reformulation** : mentionner explicitement *« notation 1-10 attribuée par l'auteur »*.

## 3. Pas compris du tout

### 3.1. ADR et EPIC — opacité forte

*« [ADR-0024] »* (intro), *« ADR-0022 »*, *« EPIC J »*, *« EPIC L »*, *« EPIC M »*, *« EPIC N »*, *« EPIC Q »*, *« EPIC R »*, *« EPIC F.6 »*. Aucune définition pour le lecteur extérieur. On devine « décision d'architecture » et « grand lot de travail » mais c'est de la pure inférence.

**Reformulation** : à la première mention, ajouter *« ADR (Architecture Decision Record, note de décision d'architecture du projet — voir notre méthode) »* et *« EPIC (lot de travail dans notre roadmap, voir notre Project board) »*.

### 3.2. « gate juridique ADR-0022 »

Double opacité. C'est quoi un « gate juridique » ? Une vérification ? Un veto ? Un délai ?

Citation exacte : *« Analyse Common Crawl de la couverture médiatique sur 10 ans (bloqué par gate juridique ADR-0022). »*

**Reformulation** : *« reporté tant que la question juridique sur l'usage de Common Crawl n'est pas tranchée (voir ADR-0022) »*.

### 3.3. « Common Crawl en V2 sous gate juridique, classification d'angles via NLP »

Trois opacités enchaînées :

- **Common Crawl** : c'est quoi ? Une archive du web ? Jamais expliqué.
- **V2** : la deuxième version d'AporiaPolis, on suppose ?
- **NLP** : neuro-linguistic programming ? Non, sûrement *natural language processing*. Jamais explicité.

**Reformulation** : *« Common Crawl (immense archive publique du web) — utilisation prévue en V2 (deuxième version d'AporiaPolis), sous réserve de validation juridique. Permettra alors d'analyser automatiquement les angles éditoriaux par traitement automatique du langage (NLP). »*

### 3.4. Acronymes non développés

**DGMIC**, **OJD/ACPM**, **AGORA** (lobbying médias), **HATVP RRI**, **SDJ**, **GIE**, **PQR**, **IFCN** : aucun n'est développé à sa première occurrence. ACPM et ARCOM se devinent par contexte, les autres non.

**Reformulation** : glossaire en fin de note OU développement à la première mention. C'est probablement le défaut le plus fréquent du document.

### 3.5. Objectifs SMART (§6) — décrochage technique

*« score Lighthouse Accessibility > 95, axe-core 0 défaut niveau A, reproductibilité validée par audit (clone fresh + `make reproduce`) »* : décrochage complet. Lighthouse semble être un outil Google ? axe-core ? « clone fresh + make reproduce » = ligne de commande.

**Reformulation** : *« site accessible aux personnes en situation de handicap selon les standards web reconnus, et reproductible par un tiers technique »*. Les détails techniques peuvent rester dans une annexe technique, pas dans la note de cadrage.

### 3.6. « stack figée (Postgres + dbt + FastAPI + Astro) » (§6)

Inaccessible. On devine « outils techniques retenus ».

**Reformulation** : *« outils techniques retenus, voir [doc tech] »*. Le détail des noms n'apporte rien à un·e lecteur·rice profane.

## 4. Trop long ou hors sujet (pour un·e lecteur·rice profane)

- **§9 (Calendrier)** : utile pour l'auteur, pas pour le lecteur profane. Sautable.
- **§12 (Tableau de bord de production)** : méta-méta-production. Utile en interne, inutile pour un lecteur extérieur.
- **Toutes les mentions d'EPIC** dans §8 (V2/V3) : pas besoin de savoir que c'est l'EPIC Q ou R, juste *« reporté à la V2 »*.
- **Sous-question 8 (fact-checking)** : décrite en détail puis annoncée reportée. Compression possible : *« Sous-question candidate écartée du MVP (score RICE faible) : fact-checking. Reportée V2. »* — trois lignes au lieu de huit.

À l'inverse, rien d'essentiel ne paraît absent côté substance — voir §5.

## 5. Manquant

### 5.1. Encart « À qui parle ce dossier ? »

Une phrase d'ouverture identifierait le public visé : *« Ce dossier s'adresse à toute personne — citoyen·ne curieux·se, journaliste, chercheur·euse, élu·e — qui veut comprendre comment fonctionne le paysage médiatique français au-delà des polémiques. »* Aide à l'identification (ou non) du lecteur.

### 5.2. Schéma simple en §1

Une carte mentale avec la question principale au centre et les 8 sous-questions autour. Le tableau RICE arrive trop tard et n'est pas un schéma de structure.

### 5.3. Exemple concret en sous-question 4

*« cas documentés de pressions éditoriales »* — sans citer personne, *un* exemple historique consensuel (genre l'affaire *I-Télé* en 2016 ou un cas déjà jugé) ancrerait. Sinon ça reste abstrait.

### 5.4. Définition rapide de « concentration capitalistique » (sous-question 1)

Reprendre la formulation que la persona suggère elle-même : *« capital = qui détient les parts ; éditorial = qui décide vraiment de ce qui passe à l'antenne — pas toujours la même personne. »* Distinction-clé pour le lecteur.

### 5.5. Chiffres de confiance avec point de comparaison (sous-question 6)

*« ~30 % en 2025 vs ~39 % en 2015 »* est donné en intro. Le rappeler ici, et ajouter un point de comparaison : *« la moyenne européenne est à X % »*. Sans ça, on ne sait pas si 30 % est dramatique ou banal.

### 5.6. Angles de lecture (§3) — couverture partielle

Vous donnez trois angles pour les sous-questions 1, 2 et 4 — pas pour les autres. Soit c'est exhaustif et il faut le dire (*« nous illustrons sur 3 sous-questions, la méthode est la même pour les autres »*), soit c'est incomplet et ça déséquilibre.

## 6. Ton et accessibilité

- **Très peu condescendant** : vous parlez de « lecteur·rice », expliquez vos limites, n'écrasez pas. Point fort.
- **Effet « club initié »** par accumulation de jargon : ADR, EPIC, gate, MVP, V1/V2/V3, RICE, NLP, SMART. À force, le lecteur extérieur se sent spectateur d'une conversation interne, pas destinataire.
- **« Méta-cohérent »** (§1) : très bonne formulation, mais suppose qu'on sait déjà ce que veut faire le projet. Tombe à côté pour qui ne sait pas.
- **Aucune formulation séduisante-mais-creuse** détectée. Ton sobre, factuel, qui inspire confiance.
- **Détail mineur** : *« ~250-350 heures cumulées sur T2 »* (§6) — « T2 » = deuxième trimestre, à développer.

## 7. Parcours de lecture

- **§1 à §4** (question, sous-questions, angles, tests de réalité) : lu attentivement, tenu jusqu'au bout. ~1200 mots cumulés.
- **§5 (RICE)** : tableau survolé, conclusion lue. OK.
- **§6 (SMART)** : décrochage sur « Lighthouse / axe-core / make reproduce ». Sentiment : *« ça ne me concerne pas. »*
- **§7 (sources)** : parcouru en diagonale. Listes à puces avec acronymes peu accrocheuses.
- **§8 à §12** : lecture rapide, presque saute. Fatigue cognitive installée.

**Point de bascule clair** : §6, dès qu'arrivent les outils techniques. Avant : on est dedans. Après : on décolle.

**Si c'était un dossier publié** (et non une note de cadrage interne), le lecteur profane n'irait probablement pas jusqu'au bout. Pour une note interne, cette fatigue est moins grave.

## 8. Biais possibles de ma critique

- **Préférence pour le concret** : j'ai sous-évalué la rigueur méthodologique des sections 5, 6, 9, 12 (importantes même si pas faites pour moi).
- **Méfiance vis-à-vis de la complexité** : j'ai pu critiquer du jargon qui, dans certains cas, est le mot juste (« concentration capitalistique » a un sens précis en éco politique, contrairement à « concentration tout court »). Vous pouvez ne pas le simplifier, mais alors expliquez-le une fois.
- **Effet « cas personnel »** : j'ai jugé à l'aune de *« est-ce que moi, lecteur·rice profane, je comprends ? »* — légitime puisque c'est mon rôle, mais cette note est une *note de cadrage interne*. Si elle reste à usage strictement interne, certains points (acronymes EPIC/ADR notamment) sont peut-être justifiés tels quels.
- **Limite d'attention** : décrochage en §6. Un·e collègue plus patient·e aurait peut-être donné un retour différent sur les §8-12.
- **Sensibilité au ton** : globalement positive ici, donc pas de braquage. Pas d'opportunité de tester un passage où le ton aurait pu glisser.

---

## Recommandation globale

La note v0.1 est solide sur la substance et le cadrage intellectuel. Les frictions repérées portent principalement sur **l'accessibilité** :

1. **Passe glossaire systématique** : développer tous les acronymes (ADR, EPIC, ARCOM, ACPM, DGMIC, SDJ, GIE, PQR, IFCN, NLP, MVP, RICE, T2…) à leur première occurrence OU en annexe.
2. **Réécriture allégée des §6, §8 et §12** : si la note doit circuler au-delà du cercle projet (page « Production de cette page » par exemple), les passages purement techniques doivent être reformulés en français accessible ou renvoyés en annexe.
3. **Ajouter un schéma simple en §1** : carte des sous-questions, pour donner une vue d'ensemble avant l'entrée détaillée.

Si la note reste *strictement interne* (vous, le comité humain, les personae), ces remarques restent valables mais leur urgence diminue.

---

## Métadonnées de session

- **Date** : 2026-05-16
- **Persona** : `lecteur-profane` v1
- **Document relu** : `dossiers/medias/cadrage.md` v0.1
- **Mode** : conversation Cowork unique, retour direct (pas d'allers-retours)
- **Prochaine étape (auteur)** : arbitrer les remarques (accepter / rejeter / différer avec motif) et produire `cadrage.md` v0.2. Croiser avec les retours des autres personae IA (déjà archivé : chercheuse-sic ; à produire : 3 autres) avant de soumettre la v0.2 au comité humain.
