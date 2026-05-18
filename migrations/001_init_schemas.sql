-- migration 001 — init 6 schémas DuckDB
--
-- Contexte : ADR-0031 (stack hybride MVP local DuckDB+parquet / prod
-- Postgres+Object Storage). En MVP local, les 6 couches sémantiques de
-- l'architecture AporiaPolis sont matérialisées comme schémas DuckDB
-- séparés. Cette migration est SQL standard portable Postgres↔DuckDB
-- afin que la migration EPIC B (vers Postgres managé Scaleway) puisse
-- la rejouer sans réécriture.
--
-- Refs : #45 [G.1], ADR-0031, docs/dwh/modelisation.md
--
-- Idempotence : `CREATE SCHEMA IF NOT EXISTS` est supporté nativement
-- par DuckDB et Postgres. Cette migration est rejouable sur env
-- existant sans erreur. La création des tables est laissée aux
-- migrations ultérieures (ajoutées par briefs B-8.2 et au-delà).

-- Schéma app : référentiels métier transverses
-- (acteur, parti, dossier, sous_question — gérés par processus éditorial,
-- peu volumineux, transverses à tous les dossiers AporiaPolis).
CREATE SCHEMA IF NOT EXISTS app;

-- Schéma raw : tables miroirs des sources brutes ingérées
-- (1:1 avec les fichiers parquet bronze stockés dans data/bronze/...
-- — voir ADR-0031 §Précisions techniques point 1).
CREATE SCHEMA IF NOT EXISTS raw;

-- Schéma staging : sortie dbt couche staging
-- (typage strict, normalisation des noms de colonnes, sans agrégation).
CREATE SCHEMA IF NOT EXISTS staging;

-- Schéma intermediate : sortie dbt couche intermediate
-- (jointures et logique partagée entre plusieurs marts).
CREATE SCHEMA IF NOT EXISTS intermediate;

-- Schéma marts : sortie dbt couche marts
-- (tables prêtes à consommation API + front, dont la table publique
-- `indicateur` avec contrat figé en B-8.3 : slug, year, value, unit,
-- source, country_iso).
CREATE SCHEMA IF NOT EXISTS marts;

-- Schéma audit_log : journal d'audit
-- (qui a modifié quoi, quand, motif — tables à implémenter par briefs
-- ultérieurs lorsque l'API mutante apparaîtra).
CREATE SCHEMA IF NOT EXISTS audit_log;
