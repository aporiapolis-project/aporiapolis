{{
  config(
    materialized='view',
    schema='staging'
  )
}}

-- B-8.3 — G.3 #47 — Modèle staging stg_owid__co2_emissions
--
-- Projection contractuelle 6 colonnes utiles depuis le miroir raw 1:1
-- OWID CO2 emissions (raw.owid_co2_emissions, B-8.2). La colonne
-- 'source' est dérivée littérale (constante éditoriale).
--
-- Doctrine B-8.1 (docs/dwh/modelisation.md) : raw = miroir bronze,
-- staging = projection contractuelle figée. Les 73 colonnes raw non
-- projetées ici restent disponibles pour de futurs marts.
--
-- Source: OWID (CC BY 4.0) — https://ourworldindata.org/co2-emissions
-- ADR-0031 — DuckDB+parquet local MVP

SELECT
    country,
    iso_code,
    year,
    co2,
    co2_per_capita,
    population,
    CAST('OWID/Global Carbon Budget 2024' AS VARCHAR) AS source
FROM {{ source('raw', 'owid_co2_emissions') }}
WHERE
    year IS NOT NULL
    AND country IS NOT NULL
