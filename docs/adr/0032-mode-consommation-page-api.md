# ADR-0032 — Mode de consommation page → API en MVP : CSR via islands Svelte 5

**Date** : 2026-05-17
**Statut** : accepted
**Décideur(s)** : sam
**Supersedes** : aucune
**Superseded by** : aucune

## Contexte

Issue #50 (G.6) acceptance verbatim :

> Test scripté : commit Python sur le pipeline → push → Dagster reload → re-matérialisation → API renvoie la nouvelle valeur → **page web l'affiche**.

Cette acceptance impose que **la page reflète une nouvelle valeur sans intervention humaine** entre la rematérialisation et l'affichage. Le mode de rendu de la page (SSG / SSR / CSR) n'est pas libre : il détermine si l'acceptance est tenable verbatim ou s'il faut la rebaseliner.

`CLAUDE.md §2` fige le front public sur Astro 5 + Svelte 5. Aucune contrainte sur le mode de rendu : Astro supporte SSG (par défaut), SSR (output: 'server'), et les islands client-side (CSR partiel via composants Svelte 5 avec directive `client:load` / `client:idle` / `client:visible`).

Trois signaux ont rendu cette ADR nécessaire au moment où B-8 démarrait :

1. **G.6 acceptance verbatim** comme rappelé ci-dessus.
2. **Critique Codex 17 mai 2026** : « SSG et G.6 verbatim sont en tension directe. G.6 dit : rematérialisation → API nouvelle valeur → page web l'affiche. En SSG, la page ne change pas sans rebuild. L'ADR-0032 est utile justement pour trancher cette vérité-là ; elle n'est pas un simple choix front. »
3. **Principe 1 doctrine** : si on choisit SSG silencieusement et qu'on prétend ensuite « G.6 verifiée », on fait mentir l'acceptance. Si on rebaseliner G.6 pour inclure un rebuild, c'est une décision qui doit être actée explicitement, pas glissée dans un brief technique.

## Options envisagées

### Option A — SSG (Static Site Generation, défaut Astro)

La page est générée au build (`astro build`). Le HTML est figé avec la valeur au moment du build. Toute nouvelle valeur (rematérialisation Dagster → nouvelle valeur API) ne se reflète pas sans un nouveau `astro build` + redéploiement.

**Pour** :
- Performance maximale au runtime : HTML pré-rendu servi directement par CDN.
- Plus simple infrastructure : pas de serveur Astro à faire tourner, pas de Node en prod.
- Aligné avec Cloudflare Pages (déploiement statique simple, déjà cible EPIC H.4).
- Le HTML est cacheable agressivement.
- Conforme à la posture éditoriale « publication exemplaire » : chaque publication = un build daté reproductible.

**Contre** :
- **Incompatible avec G.6 acceptance verbatim**. Pour refléter une nouvelle valeur, il faut un rebuild + redéploiement.
- Soit on rebaseliner G.6 pour inclure le rebuild dans la chaîne (« push → Dagster → re-matérialisation → trigger rebuild Astro → nouvelle page déployée → page web l'affiche »), ce qui ajoute une étape d'infrastructure de déploiement automatique. Soit on accepte que le test e2e ne soit pas verbatim.

### Option B — SSR (Server-Side Rendering, `output: 'server'`)

La page est rendue au runtime, à chaque requête, par un serveur Astro qui appelle l'API et compose le HTML. Nouvelle valeur API → première requête suivante affiche la nouvelle valeur.

**Pour** :
- Compatible G.6 verbatim sans rebaselining : la page reflète l'API à chaque requête.
- Plus simple côté Svelte : pas d'hydratation manuelle, pas de loading state à gérer.
- Permet des features serveur (auth, transformations, headers privés) si besoin futur.

**Contre** :
- Infrastructure plus lourde : serveur Astro Node qui tourne en prod. Conflict avec EPIC H.4 Cloudflare Pages (statique).
- Performance moins prévisible : chaque requête frappe l'API, latence en dépend.
- Couplage temporel : si l'API est down, la page Astro est down.
- Ajoute un point de monitoring + déploiement à maintenir, alors que B-8 vise un MVP local minimal.

### Option C — CSR via islands Svelte 5 (hydratation client)

La page Astro est servie en HTML statique avec un **island Svelte 5** (composant client-side) qui, au mount dans le navigateur, appelle l'API (`fetch('/api/v1/indicators/fr-co2-total-annual')`) et affiche la valeur. Le HTML initial contient un loading state (« Chargement… ») remplacé par la valeur dès que le fetch revient.

**Pour** :
- Compatible G.6 verbatim sans rebaselining : à chaque chargement de page (ou re-fetch via bouton), l'island appelle l'API et affiche la valeur courante.
- Infrastructure minimale : page Astro statique (Cloudflare Pages OK), serveur uniquement pour l'API (`services/api-rest/`). Pas de serveur Astro.
- Bien aligné avec Astro 5 + Svelte 5 — les islands sont la fonctionnalité phare du modèle Astro.
- Indépendance temporelle : si l'API est down, la page Astro charge mais l'island affiche un état d'erreur localisé, sans casser la navigation.
- Cohérent avec `CLAUDE.md §2` (Svelte 5 + Astro 5, calculs front-end).

**Contre** :
- Loading state initial : le visiteur voit « Chargement… » avant la valeur. UX moins propre qu'un HTML pré-rendu.
- Une partie de la page n'est pas indexable par les moteurs de recherche (le chiffre arrive après hydratation). Sensible si la page devient référence éditoriale ; non-bloquant pour un démonstrateur technique.
- Couple la page à un endpoint API public et stable. Si l'API change de contrat, la page casse côté client (mais c'est le contrat de G.5 — endpoints stables).
- Test e2e doit attendre l'hydratation (Playwright `await page.waitForSelector('[data-testid="indicator-value"]')`).

### Option non retenue — Combinaison SSG + ISR (Incremental Static Regeneration)

ISR au sens Next.js (régénération automatique périodique côté serveur) n'est pas une primitive Astro 5 native. Reportable mais non envisagée en MVP.

## Décision

**Option C retenue.**

La page démonstrateur consommant l'API indicateurs sera rendue en **CSR via island Svelte 5**, sur une page Astro 5 par ailleurs statique. La page initiale est SSG (rapide, cacheable) ; seul l'affichage du chiffre est délégué à un island client-side qui fetch l'API au mount.

### Précisions techniques actées

1. **Page Astro** : `front-public/src/pages/methodologie/premiere-chaine.astro` (URL `/methodologie/premiere-chaine`, cf. cadrage Cowork v3). Page mostly statique : titre, paragraphe d'introduction, mention de la source, lien méthodologie. Un island Svelte 5 pour le chiffre.
2. **Island Svelte 5** : `front-public/src/components/IndicatorValue.svelte`. Props : `slug` (par défaut `fr-co2-total-annual`), `apiBase` (par défaut `/api/v1`). Au `onMount` : `fetch(\`${apiBase}/indicators/${slug}\`)`. Trois états : loading, success, error. L'année et la valeur sont lues depuis la réponse (jamais hardcodées).
3. **Loading state** : skeleton ou texte « Chargement de la valeur… ». Pas plus.
4. **Error state** : message court qui invite à recharger (`Impossible de charger la valeur. Rechargez la page.`). Pas de stack trace côté utilisateur.
5. **Directive Astro** : `client:load` (hydratation immédiate au chargement de la page). Pas `client:visible` (le chiffre est above-the-fold) ni `client:idle` (latence inutile).
6. **Proxy dev** : Astro dev server proxify `/api/*` vers `http://localhost:8000/api/*` (le FastAPI en dev). Configuration dans `astro.config.mjs`.
7. **CORS prod** : l'API FastAPI configurera CORS pour autoriser le domaine front public. À acter en B-8.4 (G.5) avec un test pytest dédié.
8. **Build SSG** : `astro build` produit `dist/` statique. Cloudflare Pages servira `dist/` ; l'API tournera ailleurs (Scaleway VPS en EPIC B, localhost en dev). Pas de serveur Astro à déployer.

### Précisions méthodologiques actées

- L'island Svelte 5 ne contient **aucun calcul métier**. Il transporte la valeur de l'API à l'écran. CLAUDE.md §5 Svelte autorise les calculs dans modules `.ts` purs ; ici aucun calcul, juste un fetch + affichage.
- Le test e2e (G.6) utilisera Playwright (`tests/e2e/test_chain.py` côté Python, Playwright Python bindings, ou alternatives à acter en B-8.6) avec un `waitForSelector` sur l'élément `[data-testid="indicator-value"]` rendu après hydratation.
- La page n'a pas vocation à être indexée comme dossier éditorial : `/methodologie/premiere-chaine` documente la chaîne technique. Le SEO est secondaire (pas de meta description riche, pas d'OpenGraph optimisé en B-8).

## Conséquences

### Positives

- G.6 acceptance tenable verbatim sans rebaselining.
- Infrastructure prod alignée avec EPIC H.4 (Cloudflare Pages statique).
- Robustesse temporelle : la page se charge même si l'API est lente ou down (état d'erreur localisé).
- Séparation des couches préservée : Astro = chrome + texte, Svelte island = consommation API, FastAPI = logique métier.
- Cohérent avec Principe 6 doctrine (minimum nécessaire) : pas de serveur Astro, pas d'ISR exotique.

### Négatives

- Loading state initial visible. Acceptable pour un démonstrateur technique, à reconsidérer si la page devient référence publique majeure.
- Indexabilité partielle du chiffre. Non-bloquant pour `/methodologie/premiere-chaine` ; à réévaluer pour les futurs dossiers éditoriaux (`/dossiers/<slug>/`) qui auront leur propre ADR si nécessaire.
- Couplage CORS à configurer correctement (B-8.4).
- Test e2e plus complexe (attendre l'hydratation) qu'un test purement statique.

### Conditions de révision

Cette ADR devrait être revisitée si :

- **Les dossiers éditoriaux** (`/dossiers/<slug>/`, EPIC M) demandent un mode de rendu différent (par exemple SSG pur pour SEO maximal). Auquel cas une ADR distincte par type de page peut être préférable à un unique mode global.
- **Astro 5 propose ISR ou un mode hybride** qui rendrait l'option non retenue compétitive. Auquel cas réévaluer.
- **Le test e2e G.6 se révèle systématiquement flaky** à cause de l'hydratation. Auquel cas envisager SSR pour la page démonstrateur.
- **Le volume d'API calls par page** devient un problème de coût ou de latence. Auquel cas envisager SSR avec cache côté serveur, ou ISR si dispo.

## Notes pour les implémenteurs

- Référencer cette ADR depuis le code via un commentaire `// ADR-0032` sur :
  - `front-public/src/components/IndicatorValue.svelte` (en-tête).
  - `front-public/src/pages/methodologie/premiere-chaine.astro` (en-tête).
  - `astro.config.mjs` (au niveau du proxy `/api/*`).
- Le `data-testid="indicator-value"` doit être posé sur l'élément qui contient la valeur affichée après hydratation. Le test e2e en B-8.6 dépend de ce hook.
- Les trois états (loading / success / error) doivent être atteignables par tests unitaires Svelte (vitest), au moins un test par état.
- L'API ne doit pas exposer le slug `fr-co2-total-annual` comme contrat magique côté front : passer le slug en prop de l'island depuis la page Astro permet de tester l'island avec d'autres slugs sans rebuild Astro.
- a11y AA : loading state lisible par lecteur d'écran (`aria-live="polite"` sur la zone qui change). À tester en B-8.4 avec axe-core.

<!--
Conventions :
- ADR créée pendant le brief B-8.0.
- Numérotation 0032 (libre, après 0031 stack hybride).
- Cohérente avec ADR-0031 sur le périmètre MVP local : pas de tribut payé à une infrastructure (serveur Astro SSR) qui n'existe pas encore.
-->
