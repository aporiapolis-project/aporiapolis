# Personae IA — strate 1 de relecture

Ce dossier contient les fiches des **personae IA** utilisées pour la pré-relecture (strate 1) des dossiers d'AporiaPolis, conformément à [ADR-0024](../../adr/0024-doctrine-relecture-deux-strates.md).

## Liste des personae

| Slug | Profil | Usage typique |
|---|---|---|
| `chercheuse-sic` | Chercheur·euse en sciences de l'information et de la communication | Critique méthodologique sur les médias, sources académiques |
| `journaliste-independant` | Journaliste exerçant·e en presse indépendante | Vérification factuelle, déontologie, anticipation des réactions presse |
| `sociologue-quantitatif` | Sociologue ou politiste orienté·e quanti | Rigueur des indicateurs, biais de sondages, méthodes d'enquête |
| `lecteur-profane` | Lecteur·rice curieux·se non spécialiste | Test de clarté, repérage du jargon, accessibilité conceptuelle |
| `data-engineer-senior` | Data Engineer expérimenté·e | Rigueur technique, reproductibilité, choix d'architecture |

## Comment utiliser une persona

Chaque fiche contient un **prompt-type** prêt à coller dans l'outil IA de votre choix. Le pattern est toujours le même :

1. Ouvrez une nouvelle conversation (séparée de la session de production en cours).
2. Collez le prompt-type complet de la persona en début de conversation.
3. Ajoutez le contenu à relire (note de cadrage, page de dossier, méthodologie, etc.) — soit en fichier joint, soit en copier-coller.
4. Demandez : *« Selon ta perspective, donne-moi ton retour structuré sur ce document : ce qui est solide, ce qui pose problème, ce qui mérite clarification, ce qui te manque. »*
5. Récupérez le retour, archivez-le dans le repo : `dossiers/<slug>/relecture/strate-ia-<date>.md`, section « Persona : <slug-persona> ».

Faites passer **les 5 personae sur le même document**, dans des conversations séparées (sinon les retours convergent par contamination du contexte).

## Versionnement des personae

Chaque fiche porte un numéro de version (`v1`, `v2`, etc.) dans son frontmatter. Le numéro utilisé pour une session de relecture doit être noté dans l'archive de retour.

Toute évolution structurante d'une persona (changement de profil, modification du prompt-type, ajout de garde-fou) passe par une PR dans le repo et incrémente la version. Les contributeurs externes peuvent proposer des évolutions ou de nouvelles personae.

## Garde-fous généraux (applicables à toutes les personae)

Tous les prompts-types incluent les instructions suivantes :

- **Tu n'es pas une personne réelle.** Tu simules un profil-type. Tu ne dois pas usurper l'identité d'une personne nommée existante. Tu peux mentionner les chercheur·euse·s, journalistes ou auteur·rice·s dont les idées influencent ta perspective, mais sans prétendre être eux/elles.
- **Tu peux dire « je n'ai pas de retour pertinent ».** Si un point sort de ton champ de compétence, signale-le explicitement plutôt que d'inventer.
- **Tu critiques constructivement.** Pour chaque problème signalé, propose si possible une piste de reformulation, une source à consulter, ou une question à creuser.
- **Tu déclares tes biais.** En fin de retour, identifie les biais de ta perspective qui ont pu colorer ta critique. Ne fais pas semblant d'être neutre.

## Anti-patterns

- **Faire passer un retour IA pour humain** : interdit par ADR-0024.
- **Faire converger les personae avant arbitrage** : chaque retour est récolté indépendamment.
- **« Améliorer » un retour IA dans le repo sans trace** : la trace publique est partie intégrante du processus.
- **Sauter la strate 2** : aucune publication sans validation comité humain, quelle que soit la qualité de la strate 1.

## Évolutions futures

Cette liste de 5 personae correspond au dossier *Médias français* (premier dossier MVP). Pour les dossiers suivants, d'autres personae spécialisées pourraient être ajoutées :

- Dossier *Climat-énergie* : climatologue, économiste de la transition, ingénieur·e énergie.
- Dossier *Dette publique* : économiste mainstream, économiste hétérodoxe, fiscaliste.
- Dossier *Immigration* : démographe, sociologue des migrations, juriste droit des étrangers.
- etc.

À chaque nouveau dossier, l'auteur évalue si les personae existantes suffisent ou s'il faut en ajouter. Les ajouts sont documentés par PR et ADR si structurants.
