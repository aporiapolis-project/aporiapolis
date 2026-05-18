-- B-8.3 — G.3 #47 — Test SQL custom dbt natif
-- Asserte l'unicité composite (slug, year, country_iso) sur marts.indicateur.
--
-- D8 acté B-8.3 : test SQL custom plutôt que dépendance dbt-utils
-- (P6 — règle des 2 cas d'usage : un seul invariant composite ne
-- justifie pas une dépendance entière).
--
-- Convention dbt : un test "singular" retourne 0 ligne quand le test
-- passe, ≥ 1 ligne quand il échoue (les lignes retournées sont les
-- violations).

SELECT
    slug,
    year,
    country_iso,
    COUNT(*) AS occurrences
FROM {{ ref('indicateur') }}
GROUP BY slug, year, country_iso
HAVING COUNT(*) > 1
