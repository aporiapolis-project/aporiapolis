-- B-8.3 — G.4 #48 — Premier dbt-snapshot effectif AporiaPolis
--
-- Strategy 'check' sur (value, unit, source) — OWID n'expose pas de
-- timestamp upstream (D5 acté). Snapshote les révisions de Global
-- Carbon Budget sur le mart contractuel publié.
--
-- target_schema 'audit_log' — cohérent MERISE B-8.1.
--
-- ADR-0033 — concurrency=1 enforced via Dagster tag_concurrency_limits
-- (dagster.yaml, key 'dagster/dbt_snapshot' limit 1). Voir dagster.yaml
-- + dagster/aporiapolis/__init__.py (define_asset_job run_tags).

{% snapshot snapshot_indicateur %}

    {{
        config(
          target_schema='audit_log',
          unique_key="slug || '|' || CAST(year AS VARCHAR) || '|' || COALESCE(country_iso, 'NULL')",
          strategy='check',
          check_cols=['value', 'unit', 'source']
        )
    }}

    SELECT
        slug,
        year,
        value,
        unit,
        source,
        country_iso
    FROM {{ ref('indicateur') }}

{% endsnapshot %}
