# ADR-0029 — Doctrine du droit de réponse

**Date** : 2026-05-16
**Statut** : accepted
**Décideur(s)** : sam, validé après pré-relecture par personae IA (journaliste-independant + data-engineer-senior)
**Supersedes** : —
**Superseded by** : —

## Contexte

AporiaPolis publie des dossiers analytiques sur des controverses politiques françaises, notamment le dossier *Médias français* qui mentionne explicitement des **groupes économiques, des personnalités politiques, et des médias nommés**. Toute publication française à destination du public est soumise à la **loi du 29 juillet 1881** sur la liberté de la presse, qui ouvre un **droit de réponse** opposable, ainsi qu'au **décret n° 2007-1527** du 24 octobre 2007 qui en précise les modalités pour les services de communication en ligne.

La pré-relecture du cadrage Médias par les personae IA a fait apparaître que :

- Le cadrage v0.1 mentionne « droit de réponse mentionné » comme mitigation du risque diffamation (§10) mais **sans dispositif concret** : pas d'adresse, pas de procédure, pas de délai, pas de format.
- La persona `journaliste-independant` rappelle qu'un projet civic-tech à enjeu juridique sans procédure formalisée s'expose à des contentieux disproportionnés au premier signalement.
- La persona `data-engineer-senior` rappelle qu'un mécanisme technique de gestion du droit de réponse est nécessaire (page dédiée, changelog, traçabilité, lien depuis les pages de dossier) — ce mécanisme n'est pas adressé.

Cette ADR fixe la doctrine du droit de réponse côté **éditorial** (procédure, format, garanties) et côté **technique** (page, changelog, instrumentation).

## Cadre légal de référence

### Loi du 29 juillet 1881, article 13 (droit de réponse)

> *« Le directeur de la publication sera tenu d'insérer dans les trois jours de leur réception, les réponses de toute personne nommée ou désignée dans le journal ou écrit périodique, sous peine d'une amende […]. »*

Pour la presse périodique imprimée, le délai de publication est de 3 jours pour les quotidiens, l'insertion à la prochaine édition pour les autres périodicités.

### Décret n° 2007-1527 du 24 octobre 2007 (services de communication en ligne)

Adapte le droit de réponse aux services en ligne. Délai d'exercice du droit : **3 mois suivant la mise en ligne du contenu** mis en cause. Délai d'insertion : **3 jours à compter de la réception** de la demande conforme.

Format de la demande : doit être adressée par écrit (papier ou voie électronique) au directeur de publication, comporter les mentions du contenu mis en cause, l'identité et la signature du demandeur. La réponse doit être inférieure ou égale à 200 lignes pour un demandeur dont l'article ou la mention ne dépassait pas cette limite.

### Article 13-1 de la loi 1881 (anonymat des sources)

À ne pas confondre avec le droit de réponse, mais pertinent en pratique : si un demandeur exerce son droit de réponse à un contenu basé sur une source anonyme, le droit de réponse s'exerce **sans obliger le publicateur à divulguer sa source**.

### Article 226-10 du Code pénal (dénonciation calomnieuse)

Pertinent en arrière-plan : la responsabilité pénale du publicateur peut être engagée en cas de dénonciation calomnieuse, indépendamment de la procédure de droit de réponse.

## Décision

AporiaPolis met en place une **procédure formalisée de droit de réponse** conforme au cadre légal, avec instrumentation technique permettant la traçabilité publique.

### Composantes éditoriales

1. **Page publique dédiée** : `/legal/droit-de-reponse` sur le site, accessible depuis le footer et depuis chaque page de dossier.
2. **Adresse de réception unique** : `droit-de-reponse@aporiapolis.org` (à activer dès le domaine en ligne), avec accusé de réception automatique sous 24 heures.
3. **Adresse postale de secours** : nom et adresse postale du directeur de publication, publiée dans les mentions légales, conforme à l'obligation légale.
4. **Délais respectés** :
   - Recevabilité examinée sous 24-48 heures.
   - Insertion sous 3 jours ouvrés à compter de la réception conforme (cohérent avec décret 2007-1527).
   - Sauf en cas de demande non conforme, où une réponse motivée de non-recevabilité est envoyée dans le même délai.
5. **Format d'insertion** : la réponse exercée est publiée :
   - sur la page du dossier mis en cause (encart « Droit de réponse » daté, en haut de page si récent, intégré au flux après 30 jours) ;
   - dans le changelog public du dossier (`dossiers/<slug>/CHANGELOG.md`) avec mention « Droit de réponse exercé par X le YYYY-MM-DD » ;
   - sur une page de récapitulatif annuel `/legal/droit-de-reponse/historique` ;
   - dans le commit Git correspondant, avec tag spécial `droit-de-reponse-YYYY-NN`.
6. **Anonymat possible du demandeur** sur demande motivée (par exemple : journaliste anonyme protégé par une rédaction). Décision du directeur de publication, motivée publiquement.
7. **Pas de modification du contenu original mis en cause** : la réponse s'ajoute, elle ne réécrit pas. Si le contenu original contenait une erreur factuelle, une correction séparée est publiée *en plus* de la réponse (workflow erratum, distinct du droit de réponse).

### Composantes techniques

1. **Page `/legal/droit-de-reponse`** :
   - Procédure expliquée en langage clair (cf. cadre légal résumé).
   - Formulaire ou indications pour adresser la demande (email + courrier postal).
   - Délais affichés clairement (3 mois pour exercer le droit, 3 jours pour insertion).
   - Lien vers la page historique des droits de réponse exercés (transparence totale).
2. **Page `/legal/droit-de-reponse/historique`** : liste chronologique de tous les droits de réponse exercés, avec date, nature de la demande, page du dossier concernée, réponse publiée. Garantit la transparence du processus.
3. **Encart « Droit de réponse » sur chaque page de dossier** : section dédiée en bas de page, affichée *même quand vide* avec mention « Aucun droit de réponse n'a été exercé sur ce dossier à ce jour. Vous pouvez exercer le vôtre en suivant la procédure. » Lien vers `/legal/droit-de-reponse`.
4. **Changelog par dossier** : chaque exercice de droit de réponse génère une entrée datée dans `dossiers/<slug>/CHANGELOG.md` (le projet a déjà un changelog par dossier, cf. doc 10 conventions).
5. **Workflow Git** : chaque exercice fait l'objet d'un commit avec :
   - message : `docs(dossier-<slug>): droit de réponse <demandeur ou anonyme> sur <sujet>`
   - footer : `Droit-de-reponse: YYYY-NN-<slug>` (référencé dans l'historique)
   - tag : `droit-de-reponse-YYYY-NN`
6. **Notification publique** : tout exercice de droit de réponse fait l'objet d'un thread sobre sur le compte Twitter / Bluesky / Mastodon projet (annonce + lien), pour ne pas « enterrer » le droit de réponse dans le silence.

### Composantes opérationnelles

1. **Boîte aux lettres email surveillée quotidiennement** par le directeur de publication (Sam initialement).
2. **Décision de recevabilité** : la demande doit être conforme aux critères du décret 2007-1527 (identité, contenu mis en cause précisément, signature). Si conforme : insertion sous 3 jours. Si non conforme : réponse motivée demandant complément.
3. **Pas de droit de réponse à une réponse** : conforme au droit, AporiaPolis n'est pas tenue de répondre à la réponse exercée. Mais une correction factuelle séparée peut être publiée si la réponse comporte elle-même une affirmation contestable.
4. **Conservation des correspondances** : toutes les demandes (acceptées ou refusées) sont archivées dans `docs/legal/droit-de-reponse-archive/` (privé sur le repo, accessible directeur de publication et comité de relecture en cas de litige).

### Articulation avec l'erratum

Le droit de réponse n'est **pas la même chose** qu'une correction factuelle. Pour clarifier :

- **Droit de réponse** : exercé par une personne nommée ou désignée. AporiaPolis publie sa réponse *sans modifier l'article original*. C'est le mis-en-cause qui exprime sa position.
- **Erratum / correction** : AporiaPolis constate une erreur factuelle dans son contenu (chiffre faux, citation déformée, date erronée). AporiaPolis corrige le contenu lui-même, avec mention visible (« version corrigée le YYYY-MM-DD, voir [diff] ») et entrée dans le changelog du dossier.

Les deux mécanismes coexistent :
- Si un mis-en-cause signale une erreur factuelle dans son cas : double action (erratum + droit de réponse).
- Si une erreur factuelle est signalée par un tiers : erratum seul.
- Si un mis-en-cause veut donner sa version sans qu'il y ait d'erreur factuelle : droit de réponse seul.

## Conséquences

### Positives

- **Conformité légale stricte** : la procédure est conforme à la loi 1881 et au décret 2007-1527, ce qui réduit fortement le risque de contentieux gagnable.
- **Argumentaire en cas de mise en cause** : disposer d'une procédure publiée et visible désamorce les attaques qui exploiteraient son absence (« le site ne propose même pas de droit de réponse »).
- **Discipline éditoriale** : oblige l'auteur·rice à anticiper la mise en cause au moment de la rédaction (« si X exerce son droit de réponse sur cette phrase, quelle est ma défense ? »). Améliore mécaniquement la qualité.
- **Transparence radicale** : la page `/historique` rend impossible le « droit de réponse enterré ». C'est une discipline cohérente avec la posture méthodologique du projet.
- **Cohérence avec la stratégie de communication** : annoncer publiquement chaque droit de réponse sur les réseaux est un acte d'humilité éditoriale qui renforce la crédibilité.

### Négatives

- **Coût de mise en place** : page dédiée, formulaire, encart sur chaque dossier, workflow Git, automatisations. Estimation : ~20-30 heures de développement pour V1.
- **Coût de fonctionnement** : surveillance quotidienne de la boîte de réception, décisions de recevabilité, insertion sous 3 jours = engagement de service permanent du directeur de publication.
- **Risque d'instrumentalisation** : un acteur peut exercer son droit de réponse pour des raisons stratégiques (saturer le dossier de contestations, retarder la publication, etc.). Mitigation : strict respect de la recevabilité formelle (réponse limitée à la longueur de la mention initiale, pas de droit de réponse à la réponse).
- **Charge mentale** : préparer chaque dossier à être contesté est cognitivement coûteux. C'est aussi son meilleur garde-fou.

### Conditions de révision

Cette ADR peut être révisée et superseded si :

1. La loi 1881 ou le décret 2007-1527 sont modifiés (peu probable dans la durée du projet, mais à surveiller).
2. Une jurisprudence récente fixe une interprétation contraignante (par exemple sur les délais, sur les obligations de format, sur l'anonymat des demandeurs).
3. L'expérience pratique du projet révèle des frictions opérationnelles non anticipées (par exemple : volume de demandes infondées noyant les recevables).
4. AporiaPolis prend une structure juridique différente (association loi 1901, structure éditoriale formelle) qui modifie le statut du directeur de publication.

## Mise en œuvre opérationnelle

### Avant la première publication d'un dossier

- [ ] Page `/legal/droit-de-reponse` rédigée et publiée.
- [ ] Page `/legal/droit-de-reponse/historique` créée (vide initialement, avec mention « Aucun droit de réponse exercé à ce jour »).
- [ ] Adresse email `droit-de-reponse@aporiapolis.org` active et surveillée.
- [ ] Mentions légales (`/legal/mentions`) incluent l'identité et l'adresse du directeur de publication, conformes à l'article 6 de la LCEN.
- [ ] Composant `<DroitDeReponseFooter>` dans le système de composants Astro, intégré à la page-template de chaque dossier.
- [ ] Procédure interne de traitement documentée dans `docs/runbooks/droit-de-reponse.md` (étapes, délais, modèles de réponse type).
- [ ] Workflow Git documenté dans `CONTRIBUTING.md` (commit footer `Droit-de-reponse:`, tag `droit-de-reponse-YYYY-NN`).

### En continu

- Boîte email vérifiée quotidiennement.
- Tableau de bord interne (Grafana ou simple page admin) suivant : nombre de demandes reçues, recevables, insérées, refusées, en cours.
- Revue trimestrielle de la procédure avec le comité de relecture : la procédure fonctionne-t-elle ? Des frictions ?

### En cas de mise en cause majeure ou de contentieux

- Procédure d'escalade : si une mise en cause apparaît susceptible de déboucher sur un contentieux (mise en demeure, recommandé d'un avocat, etc.), saisir le comité de relecture en urgence et consulter un·e juriste spécialisé·e en droit de la presse. Budget conseil juridique anticipé : 200-500 € en réserve pour ce cas (cf. doc 03 budget prévisionnel, ligne « Conseil juridique »).

## Notes pour les implémenteurs

- **Le statut du directeur de publication** doit être clarifié dans les mentions légales : tant qu'AporiaPolis reste un projet personnel (Sam initiateur), c'est Sam qui en assume la responsabilité juridique. Si une association loi 1901 est constituée plus tard, le directeur de publication peut changer — ADR de mise à jour dans ce cas.
- **Délai de 3 mois pour exercer le droit de réponse** : à compter de la mise en ligne. Pour les dossiers vivants (avec mises à jour trimestrielles), chaque mise à jour majeure déclenche un nouveau délai de 3 mois sur les passages modifiés. À documenter dans la procédure interne.
- **L'anonymat sur demande** est une faveur, pas un droit du demandeur. Doit être motivé. Décision du directeur de publication, motivée publiquement (par exemple : « anonymat accordé sur demande motivée du demandeur invoquant la protection des sources journalistiques »).
- **La page historique des droits de réponse** est un acte éditorial fort. Elle peut être contestée elle-même (un demandeur peut ne pas vouloir que sa demande figure dans l'historique). Mais la transparence du processus l'emporte sur la confidentialité de la demande : c'est aussi une garantie pour les autres demandeurs futurs.
