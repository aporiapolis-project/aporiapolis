# ADR-0024 — Doctrine de relecture en deux strates

**Date** : 2026-05-XX (à la création dans le repo)
**Statut** : accepted
**Décideur(s)** : sam
**Supersedes** : —
**Superseded by** : —

## Contexte

Le projet AporiaPolis est conçu pour résister à ses propres conclusions par construction. Cette résistance s'appuie en grande partie sur une **relecture pluraliste** : un comité humain de profils variés (chercheur·euses, journalistes, lecteur·rice·s profanes, etc.) qui examine chaque dossier avant publication et qui valide publiquement la méthodologie.

Cependant, ce comité humain a deux limites pratiques :

1. **Temps long de constitution** : recruter, engager et coordonner 3-5 personnes pluralistes prend des semaines à des mois. Le calendrier de certification Simplon (publication Médias visée fin T2 / début T3, soit novembre 2026) impose un démarrage en parallèle de la rédaction.

2. **Capacité de traitement modeste** : un comité bénévole peut absorber ~10-20 heures de relecture par an et par membre. Sur la durée du projet, cela ne couvre que les publications majeures. Les itérations intermédiaires (révision d'une sous-question, ajustement méthodologique, mise à jour trimestrielle d'un dossier vivant) ne peuvent pas toutes passer par le comité humain.

L'arrivée à maturité des modèles d'IA générative (Cowork / Claude / autres) crée une opportunité méthodologique nouvelle : **utiliser des personae IA comme première strate de relecture critique**. Ces personae, instanciées par des prompts structurés simulant des profils-types, peuvent fournir une critique dense et rapide d'un dossier ou d'une note, en quelques minutes.

Cette ADR fixe la doctrine pour intégrer cette strate sans trahir la posture épistémique du projet.

## Options envisagées

### Option A — Comité humain seul

Tout relire est fait par le comité humain. Aucune relecture IA.

**Pour** : pureté méthodologique. Pas d'ambiguïté sur ce qui valide quoi.

**Contre** : ralentit l'itération. Bloque la production tant que le comité humain n'est pas constitué. Empêche les stress-tests intermédiaires entre deux relectures officielles.

### Option B — IA seule (sans comité humain)

Le projet s'appuie uniquement sur des personae IA pour la relecture, pas de comité humain.

**Pour** : rapidité maximale. Pas de coordination humaine.

**Contre** : trahison totale de la posture du projet. Aucun gage de pluralité épistémique réelle. Risque de convergence des biais IA. Pas de légitimité publique. Cette option est **rejetée d'emblée**.

### Option C — IA en pré-relecture, comité humain en validation finale

Deux strates clairement distinctes :

- **Strate 1 — Pré-relecture par personae IA** : exécutée par l'auteur (Sam) à plusieurs reprises pendant la rédaction d'un dossier. Critiques denses, rapides, multiples. Usage interne.
- **Strate 2 — Validation par comité humain pluraliste** : exécutée avant chaque publication majeure (version `X.0.0` ou `X.Y.0`). Trace publique. Comité de 3-5 personnes humaines réelles, identifiées (avec leur accord) sur la page « Qui parle ? ».

Les deux strates sont **complémentaires** : la pré-relecture IA stress-teste le matériau avant qu'il atteigne le comité humain, ce qui augmente la qualité de la critique humaine (elle ne perd plus de temps sur des défauts faciles) et la rentabilité du temps bénévole. Les retours IA sont *traités* par l'auteur, dont les arbitrages sont visibles publiquement. Les retours humains sont *intégrés ou réfutés publiquement avec justification*.

**Pour** : combine vélocité et pluralité humaine réelle. Permet d'avancer pendant la constitution du comité. Crée un processus mature et défendable.

**Contre** : complexifie le processus de production. Demande de la discipline pour ne pas faire passer une relecture IA pour une validation comité.

## Décision

**Option C** retenue.

Le projet AporiaPolis adopte une **relecture en deux strates clairement distinguées** :

### Strate 1 — Pré-relecture par personae IA (usage interne)

- Activée à plusieurs étapes de la production d'un dossier (cadrage, après analyse, avant remise au comité humain, après intégration des retours comité).
- Réalisée via 5 personae IA documentées dans `docs/methodology/personae-ia/` : chercheur·euse SIC, journaliste indépendant·e, sociologue quantitatif·ve, lecteur·rice profane, Data Engineer senior.
- Chaque persona a sa fiche publique (profil, références, style de critique, biais déclarés, garde-fous, prompt-type).
- Les retours IA et les arbitrages de l'auteur sont **versionnés dans le repo** (`dossiers/<slug>/relecture/strate-ia-<date>.md`).
- **Non substituable à la strate 2** : aucun dossier ne peut être publié sans validation de strate 2.

### Strate 2 — Validation par comité humain pluraliste (légitimation publique)

- Activée avant chaque publication majeure d'un dossier (version `X.0.0` ou `X.Y.0`).
- Réalisée par un comité de 3 à 5 personnes humaines réelles, identifiées avec leur accord sur la page « Qui parle ? ».
- Profils-cibles : chercheur·euse SIC, journaliste exerçant·e, lecteur·rice profane, sociologue ou politiste, Data Engineer senior (peut être atteint progressivement, pas tous obligatoirement en place pour le premier dossier).
- Les retours sont intégrés ou réfutés publiquement avec justification, dans `dossiers/<slug>/relecture/strate-comite-<date>.md`.
- **Seule strate 2 légitime la mention « projet relu par un comité pluraliste »** sur le site public et dans la documentation.

### Transparence éditoriale obligatoire

Sur chaque page de dossier publiée, l'encart « Production de cette page » mentionne explicitement les deux strates avec leurs trace publiques :

> *Cette page a été pré-relue par 5 personae IA documentées ([voir les retours](./relecture/strate-ia-YYYY-MM-DD.md)) puis validée par le comité humain pluraliste ([voir les retours](./relecture/strate-comite-YYYY-MM-DD.md)). Cette doctrine est décrite dans [ADR-0024](docs/adr/0024-doctrine-relecture-deux-strates.md).*

### Distinction sémantique stricte

- « Pré-relue par IA » : strate 1 uniquement, **jamais** dit « relue par un comité » sur cette base.
- « Relue par un comité » : strate 2 uniquement, après validation humaine effective.
- « Pré-publié » ou « brouillon » : si seule strate 1 est passée, le statut public reste *non publié*. Le brouillon peut être consultable sur le repo mais pas accessible depuis la home du site.

## Conséquences

### Positives

- **Vélocité préservée** : l'auteur peut itérer rapidement sur la qualité méthodologique sans bloquer sur l'agenda du comité humain.
- **Qualité augmentée du temps bénévole** : le comité humain reçoit un matériau déjà stress-testé.
- **Originalité méthodologique** : très peu de projets civic-tech français formalisent un tel processus. Devient un atout éditorial et un sujet de communication.
- **Cohérence avec la posture du projet** : transparence totale du processus, traçabilité publique des deux strates, distinction sémantique stricte.
- **Soutenable pour la durée du MVP** : permet la production du dossier Médias V1 pendant que le comité humain se constitue (D.1, D.2, D.3 de l'EPIC D).

### Négatives

- **Complexité accrue du processus** : 4-6 étapes de relecture par dossier au lieu de 1-2.
- **Discipline indispensable** : risque de glissement sémantique (« j'ai fait relire » sans préciser par qui) que la doctrine doit prévenir par sa rigueur.
- **Dépendance à la qualité des personae IA** : si une persona est mal cadrée, ses retours seront biaisés sans qu'on le sache forcément. Mitigation : versionnement public des personae, possibilité pour des contributeurs externes de proposer des évolutions via PR.
- **Coût IA** : usage de Cowork ou Claude.ai compris dans les abonnements déjà payés. Coût marginal nul pour le projet.

### Conditions de révision

Cette ADR peut être révisée et superseded si :

1. Une étude indépendante démontre que les personae IA produisent des biais systématiques non corrigeables, au point de fausser durablement les arbitrages.
2. Le comité humain atteint une capacité suffisante pour absorber toute la relecture (improbable à moins de plusieurs salariés dédiés).
3. Une jurisprudence ou doctrine publique (CNIL, AI Act, etc.) rend la pratique problématique en l'état.
4. Un partenariat scientifique reconnu permet de remplacer la strate 1 par une véritable revue par pairs académique sur certains dossiers (cas d'évolution positive vers une strate 1bis).

## Mise en œuvre opérationnelle

### Dossier `docs/methodology/personae-ia/`

Contient :
- `README.md` — index des personae, instructions d'usage, doctrine de mise à jour.
- `chercheuse-sic.md` — persona chercheur·euse en sciences de l'information et de la communication.
- `journaliste-independant.md` — persona journaliste exerçant·e dans la presse indépendante.
- `sociologue-quantitatif.md` — persona sociologue ou politiste orienté·e quanti.
- `lecteur-profane.md` — persona lecteur·rice curieux·se non spécialiste.
- `data-engineer-senior.md` — persona Data Engineer expérimenté·e (regard technique).

Chaque fiche contient : profil détaillé, références bibliographiques typiques, style de critique attendu, biais déclarés, garde-fous, prompt-type prêt à coller, exemples de critiques typiques.

### Workflow d'usage par dossier

À insérer dans `docs/methodology/workflow-relecture.md` :

1. Auteur rédige la note de cadrage du dossier.
2. **Pré-relecture IA strate 1 sur cadrage** : auteur fait passer la note par chaque persona. Retours versionnés dans `dossiers/<slug>/relecture/strate-ia-cadrage-<date>.md`. Auteur arbitre.
3. Auteur produit le dossier complet (sources, analyses, rédaction).
4. **Pré-relecture IA strate 1 sur dossier complet** : 5 personae lisent. Retours versionnés. Arbitrage.
5. **Validation strate 2 par comité humain** : envoi du dossier au comité. Retours collectés et versionnés dans `dossiers/<slug>/relecture/strate-comite-<date>.md`. Auteur arbitre publiquement.
6. Si retours du comité demandent des changements substantiels → boucle 4 (re-pré-relecture IA sur les sections modifiées) puis 5 (validation finale comité).
7. **Publication**.

### Encart sur chaque page de dossier publiée

Template à utiliser systématiquement dans l'encart « Production de cette page » :

```markdown
**Pré-relecture IA** (5 personae documentées, ADR-0024) :
[résumé court : N retours intégrés, M discutés, K rejetés avec justification].
[Lien vers la trace complète : `dossiers/<slug>/relecture/strate-ia-<date>.md`]

**Validation comité humain pluraliste** :
[liste des relecteur·rice·s avec leur accord, ou « comité élargi anonyme » si certain·e·s préfèrent].
[Lien vers la trace complète : `dossiers/<slug>/relecture/strate-comite-<date>.md`]
```

### Évolution des personae

- Toute évolution majeure d'une persona IA (changement de profil, ajout de garde-fou, modification du prompt-type) passe par PR dans le repo.
- Les contributions externes sont bienvenues (un·e contributeur·rice peut proposer une nouvelle persona ou critiquer une persona existante).
- Une version (v1, v2, etc.) est attachée à chaque persona. Le numéro de version utilisé pour relire un dossier est versionné dans `dossiers/<slug>/relecture/strate-ia-<date>.md`.

## Notes pour les implémenteurs

- Aucune persona ne doit usurper l'identité d'une personne réelle. Les références bibliographiques typiques sont OK (« Influencé par les travaux de Bourdieu et Champagne »), mais pas la simulation d'individus nommés (« Tu es Patrick Champagne »).
- Le prompt-type d'une persona doit explicitement inclure une instruction sur les biais à éviter et sur la possibilité de répondre « je n'ai pas de retour pertinent sur ce point ».
- En cas de désaccord majeur entre personae sur un point, c'est *le signal* qu'un dossier mérite arbitrage humain particulièrement attentif sur ce point — pas qu'il faut « moyenner » les retours.
- L'auteur garde la responsabilité finale des arbitrages. Les personae sont des outils, pas des décideurs.
