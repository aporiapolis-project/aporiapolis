-- Migration 002 — Création de raw.owid_co2_emissions
-- B-8.2 — Refs #46
--
-- Cette table est un MIROIR 1:1 du bronze OWID CO2 emissions,
-- conformément à la doctrine B-8.1 (docs/dwh/modelisation.md :
-- raw = miroir du bronze, projection contractuelle en staging).
--
-- Types : mapping vers types SQL portables DuckDB↔Postgres pour
-- préserver la trajectoire ADR-0031 (DuckDB en MVP local,
-- Postgres en prod cible) sans réécriture future.
--
-- Idempotent : instruction `CREATE ... IF NOT EXISTS`. La migration peut être
-- ré-exécutée sans erreur (cf. test idempotence B-8.1 RESULT
-- Mission F).
--
-- Source of truth des noms de colonnes : dagster/aporiapolis/config/
-- sources/owid.yaml (expected_source_header). Le test
-- test_owid_header_contract.py cas (c) vérifie l'alignement.
--
-- IMPORTANT — figeage Mission 0 B-8.2 :
-- La liste de colonnes ci-dessous est un point de départ basé sur
-- le codebook OWID 2024-2025. L'agent qui exécute B-8.2 DOIT en
-- Mission 0 ajuster cette migration pour qu'elle reflète strictement
-- le header CSV téléchargé (curl -fsSL "$OWID_URL" | head -n 1) et
-- la liste figée dans owid.yaml. En cas de divergence, le YAML fait
-- foi.

CREATE TABLE IF NOT EXISTS raw.owid_co2_emissions (
    country                              VARCHAR,
    year                                 INTEGER,
    iso_code                             VARCHAR,
    population                           BIGINT,
    gdp                                  DOUBLE PRECISION,
    cement_co2                           DOUBLE PRECISION,
    cement_co2_per_capita                DOUBLE PRECISION,
    co2                                  DOUBLE PRECISION,
    co2_growth_abs                       DOUBLE PRECISION,
    co2_growth_prct                      DOUBLE PRECISION,
    co2_including_luc                    DOUBLE PRECISION,
    co2_including_luc_growth_abs         DOUBLE PRECISION,
    co2_including_luc_growth_prct        DOUBLE PRECISION,
    co2_including_luc_per_capita         DOUBLE PRECISION,
    co2_including_luc_per_gdp            DOUBLE PRECISION,
    co2_including_luc_per_unit_energy    DOUBLE PRECISION,
    co2_per_capita                       DOUBLE PRECISION,
    co2_per_gdp                          DOUBLE PRECISION,
    co2_per_unit_energy                  DOUBLE PRECISION,
    coal_co2                             DOUBLE PRECISION,
    coal_co2_per_capita                  DOUBLE PRECISION,
    consumption_co2                      DOUBLE PRECISION,
    consumption_co2_per_capita           DOUBLE PRECISION,
    consumption_co2_per_gdp              DOUBLE PRECISION,
    cumulative_cement_co2                DOUBLE PRECISION,
    cumulative_co2                       DOUBLE PRECISION,
    cumulative_co2_including_luc         DOUBLE PRECISION,
    cumulative_coal_co2                  DOUBLE PRECISION,
    cumulative_flaring_co2               DOUBLE PRECISION,
    cumulative_gas_co2                   DOUBLE PRECISION,
    cumulative_luc_co2                   DOUBLE PRECISION,
    cumulative_oil_co2                   DOUBLE PRECISION,
    cumulative_other_co2                 DOUBLE PRECISION,
    energy_per_capita                    DOUBLE PRECISION,
    energy_per_gdp                       DOUBLE PRECISION,
    flaring_co2                          DOUBLE PRECISION,
    flaring_co2_per_capita               DOUBLE PRECISION,
    gas_co2                              DOUBLE PRECISION,
    gas_co2_per_capita                   DOUBLE PRECISION,
    ghg_excluding_lucf_per_capita        DOUBLE PRECISION,
    ghg_per_capita                       DOUBLE PRECISION,
    land_use_change_co2                  DOUBLE PRECISION,
    land_use_change_co2_per_capita       DOUBLE PRECISION,
    methane                              DOUBLE PRECISION,
    methane_per_capita                   DOUBLE PRECISION,
    nitrous_oxide                        DOUBLE PRECISION,
    nitrous_oxide_per_capita             DOUBLE PRECISION,
    oil_co2                              DOUBLE PRECISION,
    oil_co2_per_capita                   DOUBLE PRECISION,
    other_co2_per_capita                 DOUBLE PRECISION,
    other_industry_co2                   DOUBLE PRECISION,
    primary_energy_consumption           DOUBLE PRECISION,
    share_global_cement_co2              DOUBLE PRECISION,
    share_global_co2                     DOUBLE PRECISION,
    share_global_co2_including_luc       DOUBLE PRECISION,
    share_global_coal_co2                DOUBLE PRECISION,
    share_global_cumulative_cement_co2   DOUBLE PRECISION,
    share_global_cumulative_co2          DOUBLE PRECISION,
    share_global_cumulative_co2_including_luc DOUBLE PRECISION,
    share_global_cumulative_coal_co2     DOUBLE PRECISION,
    share_global_cumulative_flaring_co2  DOUBLE PRECISION,
    share_global_cumulative_gas_co2      DOUBLE PRECISION,
    share_global_cumulative_luc_co2      DOUBLE PRECISION,
    share_global_cumulative_oil_co2      DOUBLE PRECISION,
    share_global_cumulative_other_co2    DOUBLE PRECISION,
    share_global_flaring_co2             DOUBLE PRECISION,
    share_global_gas_co2                 DOUBLE PRECISION,
    share_global_luc_co2                 DOUBLE PRECISION,
    share_global_oil_co2                 DOUBLE PRECISION,
    share_global_other_co2               DOUBLE PRECISION,
    share_of_temperature_change_from_ghg DOUBLE PRECISION,
    temperature_change_from_ch4          DOUBLE PRECISION,
    temperature_change_from_co2          DOUBLE PRECISION,
    temperature_change_from_ghg          DOUBLE PRECISION,
    temperature_change_from_n2o          DOUBLE PRECISION,
    total_ghg                            DOUBLE PRECISION,
    total_ghg_excluding_lucf             DOUBLE PRECISION,
    trade_co2                            DOUBLE PRECISION,
    trade_co2_share                      DOUBLE PRECISION
);
