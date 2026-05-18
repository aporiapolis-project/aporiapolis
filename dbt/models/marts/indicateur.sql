{{
  config(
    materialized='table',
    schema='marts'
  )
}}

-- B-8.3 — G.3 #47 — Modèle marts indicateur (contrat figé)
--
-- Contrat éditorial canonique B-8 :
--   (slug, year, value, unit, source, country_iso)
--
-- Slug B-8 : 'fr-co2-total-annual' (Total annuel France Mt CO2)
-- Filtre : country = 'France' (ISO-3 'FRA')
-- Unit : 'Mt CO2' (constant pour ce slug)
--
-- ADR-0031 §"contrat dbt staging+mart" — D6 acté B-8.3 : nom de mart
-- 'indicateur' (générique, plusieurs slugs cohabiteront).
-- Source card OWID §5 patchée dans la même PR (M11).
--
-- Source: OWID (CC BY 4.0) — https://ourworldindata.org/co2-emissions

SELECT
    CAST('fr-co2-total-annual' AS VARCHAR) AS slug,
    year,
    CAST(co2 AS DOUBLE) AS value,  -- noqa: RF04
    CAST('Mt CO2' AS VARCHAR) AS unit,
    source,
    iso_code AS country_iso
FROM {{ ref('stg_owid__co2_emissions') }}
WHERE
    country = 'France'
    AND iso_code = 'FRA'
    AND co2 IS NOT NULL
    AND year IS NOT NULL
ORDER BY year
