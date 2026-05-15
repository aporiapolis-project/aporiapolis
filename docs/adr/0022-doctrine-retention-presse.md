# ADR-0022 — Doctrine de rétention des corpus de presse et procédure Common Crawl

**Date** : 2026-05-XX (à la création du repo)
**Statut** : accepted
**Décideur(s)** : sam, comité de relecture (consultatif)
**Supersedes** : —
**Superseded by** : —

## Contexte

Pour certains dossiers d'AporiaPolis — notamment le dossier *Médias* et un éventuel dossier *Méta-IA dans le débat public* — il pourrait être pertinent d'analyser la couverture médiatique d'un sujet sur plusieurs années. Common Crawl est la principale source publique permettant ce type d'analyse à grande échelle.

Cependant, le droit français encadre strictement ces traitements :

1. **Article L122-5-3 I du Code de la propriété intellectuelle** (exception générale de fouille de textes et de données) autorise toute personne à effectuer des copies sur des œuvres licitement accessibles, *sauf opposition appropriée* (notamment lisible par machine pour les contenus en ligne), et impose la **destruction des copies à l'issue de la fouille**.

2. **Article L122-5-3 II du même code** (régime de recherche scientifique) permet la *conservation* des copies pour la vérification des résultats, mais est réservé à des **acteurs limitativement énumérés** : organismes de recherche, bibliothèques accessibles au public, musées, services d'archives, institutions dépositaires du patrimoine cinématographique, audiovisuel ou sonore — ou aux personnes agissant **pour leur compte et à leur demande** dans un partenariat sans but lucratif.

3. **Article L218-2** instaure le **droit voisin des éditeurs de publications de presse** : l'autorisation de l'éditeur ou de l'agence de presse est requise pour toute reproduction ou communication publique, totale ou partielle, de publications de presse sous forme numérique par un service de communication au public en ligne.

Le backlog v2 d'AporiaPolis a tracé la nécessité d'un gate juridique strict avant tout pilote Common Crawl. Cette ADR fixe la doctrine.

## Options envisagées

### Option A — Common Crawl massif en zone bronze persistante

Ingestion à large échelle (5-50 To) sur 10 ans de presse française, stockage durable, indexation, classification automatique d'angles.

**Pour** : analyse longitudinale en profondeur possible, démonstration de la pile big data du projet, source de matière unique.

**Contre** : juridiquement incompatible. Le régime L122-5-3 I impose la destruction post-fouille — incompatible avec un stockage persistant. Le régime L122-5-3 II exige un acteur éligible ou un partenariat formalisé, qu'AporiaPolis n'a pas. L218-2 interdirait toute republication ou citation longue.

### Option B — Common Crawl restreint avec destruction post-fouille (régime L122-5-3 I)

Ingestion ciblée (par exemple sous-corpus News, 200-500 Go), exécution d'analyses agrégées (classification d'angles, comptage par média / période / thème), destruction des copies à l'issue de chaque exécution, conservation uniquement des agrégats statistiques.

**Pour** : juridiquement compatible avec l'exception générale de fouille. Permet une analyse pertinente de la couverture médiatique sans stocker durablement les contenus.

**Contre** : nécessite de relancer les pipelines si on veut réanalyser le corpus, donc coût Athena répétitif. Limite à des analyses agrégées (pas de drill-down vers l'article individuel pour le public). Demande un respect strict de l'opt-out machine-lisible (robots.txt, ai.txt, meta tags).

### Option C — Partenariat formalisé avec acteur éligible au régime II

Convention sans but lucratif avec un organisme de recherche universitaire, une bibliothèque accessible au public, ou une institution patrimoniale, permettant à AporiaPolis d'agir pour son compte et à sa demande dans le cadre du régime de recherche scientifique. Permet la conservation des copies pour vérification des résultats.

**Pour** : permet la conservation durable du corpus dans un cadre juridique sécurisé. Ouvre la voie à des analyses approfondies et reproductibles.

**Contre** : demande un effort externe significatif (identifier un partenaire, formaliser une convention, garantir le caractère scientifique du partenariat). Pas garanti d'aboutir dans le timing du projet de certification. Risque de devenir un projet dans le projet.

### Option D — Renoncer entièrement à Common Crawl

Le dossier Médias V1 se construit uniquement sur les sources structurées officielles (ARCOM, ACPM, INA, INSEE, Cour des comptes, Médiamétrie, baromètres Reuters/Sciences Po, etc.).

**Pour** : sécurité juridique maximale. Source d'agrégation simple. Pas de dépendance Common Crawl ni AWS Athena.

**Contre** : perte de la dimension « analyse longitudinale du discours médiatique » qui serait pertinente pour le dossier Médias et le dossier Méta-IA.

## Décision

**Phasage strict en trois temps :**

### Phase MVP (T1-T2)
**Option D appliquée.** Aucun corpus de presse stocké persistement. Le dossier Médias V1 se construit exclusivement sur les sources officielles structurées. Common Crawl est en parking lot `blocked-by-design`.

### Phase V2 (T3-T4)
**Option B sous gate juridique strict.** Pilote Common Crawl restreint *uniquement* après validation de cette ADR par le comité de relecture, et sous les conditions opérationnelles ci-dessous.

### Phase V3 ou post-cert
**Option C en exploration ouverte.** Si une analyse approfondie reproductible devient un besoin produit confirmé, exploration d'un partenariat formalisé avec un acteur éligible. Cette option n'est pas critique pour la certification.

## Conditions opérationnelles du pilote V2 (Option B)

Si le pilote Common Crawl V2 est lancé, il respecte impérativement :

### Volume et coût

- Volume max scanné via AWS Athena : **50 Go** par exécution. Au-delà, validation explicite requise.
- Budget cap mensuel : **30 €** d'Athena (correspond à ~6 To scannés au tarif 5 $/To, soit largement le volume autorisé).
- Athena column index utilisé en priorité (corpus News uniquement, pas l'index principal massif).

### Rétention

- **Aucune conservation des copies** des contenus de presse au-delà de la durée stricte d'exécution du pipeline.
- Pipelines conçus pour : lire depuis S3 Common Crawl → extraire les métadonnées et agrégats → écrire les agrégats dans le DWH → détruire toute donnée intermédiaire.
- Zones bronze interdites pour le contenu de presse. Si une zone bronze est créée pour des raisons techniques, elle est purgée par script automatique à la fin de chaque exécution (TTL 1 heure max).
- Documentation publique de cette doctrine sur `/methodologie/dossier/medias` et `/legal/doctrine-presse`.

### Sorties publiques

- **Aucune republication** d'extraits, même courts, sans autorisation explicite et écrite de l'éditeur concerné.
- **Aucune citation longue**. Seules les citations très courtes (< 100 caractères) sont admises et uniquement dans un contexte critique au sens du droit de citation (L122-5 3° du CPI), avec mention de l'auteur et de la source.
- **Sorties autorisées** : agrégats statistiques uniquement (nombre d'articles sur une thématique par média, par période ; distribution d'angles classifiés automatiquement ; co-occurrences thématiques ; évolution temporelle des volumes). Ces agrégats ne reproduisent ni ne communiquent les œuvres au public, ils décrivent un phénomène mesurable.
- Pour chaque visualisation publique issue de Common Crawl, mention obligatoire : « Données dérivées de Common Crawl (filtre presse française, période X-Y). Méthodologie et code disponibles. Le contenu source n'est pas reproduit. »

### Opt-out

- Respect strict des **robots.txt**, **ai.txt**, et meta tags `noai` / `noimageai` / `noindex` à la *date d'analyse*. Implémentation explicite dans le pipeline d'ingestion.
- Si un éditeur exprime son opposition après la fin de la fouille (par exemple via courriel à l'adresse DPO), les agrégats statistiques le concernant sont supprimés du DWH et des publications, et l'éditeur est ajouté à une liste d'exclusion permanente. Cette liste est versionnée publiquement dans `docs/methodology/opt-out-presse.md`.

### Documentation publique

- Page `/methodologie/doctrine-presse` publie cette ADR et son application opérationnelle.
- Page `/legal/doctrine-presse` publie le résumé juridique destiné aux éditeurs (contact, droit de réponse, opt-out, garanties).
- Adresse DPO active pour les demandes d'éditeurs.

## Conditions de bascule vers Option C (partenariat scientifique)

Si Option C devient pertinente en V3 ou post-cert, conditions strictes :

1. Partenariat formalisé par convention écrite avec un acteur éligible au L122-5-3 II.
2. Convention sans but lucratif (l'analyse scientifique est le but premier).
3. AporiaPolis agit « pour le compte et à la demande » du partenaire — formalisation écrite explicite de cette relation.
4. Le partenariat doit produire des artefacts à finalité scientifique reconnaissable (papers, datasets de recherche, contributions à la communauté académique).
5. Une ADR superseding la présente est rédigée pour formaliser le passage Option B → Option C.

## Conséquences

### Positives

- Sécurité juridique inattaquable pour le MVP.
- Force des sources alternatives plus structurées, plus fiables, mieux documentées (gain qualité pour le dossier Médias).
- Démontre une posture de respect du droit voisin des éditeurs — atout réputationnel.
- Limite la dépendance à AWS pour la première publication.
- Cohérence avec la posture méthodologique du projet (transparence sur les limites).

### Négatives

- Le dossier Médias V1 perd la dimension « analyse longitudinale du discours sur 10 ans ». Compromis assumé pour le MVP.
- Si le pilote V2 est lancé, complexité opérationnelle non triviale : gestion de la destruction post-fouille, respect dynamique des opt-out, etc.
- Le partenariat Option C, s'il devient nécessaire, est un projet externe à part entière qui peut décaler le calendrier.

### Conditions de révision

- Évolution législative ou jurisprudentielle significative sur le régime TDM ou le droit voisin presse.
- Conclusion d'un partenariat éligible au régime II (déclenche superseding par nouvelle ADR).
- Décision documentée de renoncer définitivement à Common Crawl pour le projet.

## Notes pour les implémenteurs

- Aucune story `ingestion-cc` ne peut être démarrée avant la signature de cette ADR par le comité de relecture.
- Le script de pipeline Common Crawl V2 doit avoir un *test de non-rétention* dans sa CI : exécution → vérification qu'aucun fichier brut n'a été conservé en dehors de la fenêtre TTL → échec sinon.
- L'adresse `dpo@aporiapolis.org` (ou équivalent) doit être active *avant* le premier lancement du pilote, pour permettre les demandes d'opt-out d'éditeurs.
- La liste d'exclusion permanente (`docs/methodology/opt-out-presse.md`) doit être consultée par chaque exécution du pipeline et appliquée comme filtre.
- Toute violation détectée de cette doctrine (par exemple : un fichier de presse trouvé en zone bronze après une fenêtre TTL) déclenche une alerte critique au sens du monitoring, et une remédiation manuelle documentée.
