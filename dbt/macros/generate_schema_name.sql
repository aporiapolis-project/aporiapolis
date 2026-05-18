-- B-8.3 — Keep dbt custom schemas literal on DuckDB.
--
-- dbt's default macro prefixes custom schemas with target.schema
-- (for example `main_staging`). AporiaPolis already creates the
-- DuckDB schemas `staging`, `marts`, and `audit_log` explicitly via
-- migrations, so B-8.3 must materialize into those exact schemas.

{% macro generate_schema_name(custom_schema_name, node) -%}
    {%- if custom_schema_name is none -%}
        {{ target.schema }}
    {%- else -%}
        {{ custom_schema_name | trim }}
    {%- endif -%}
{%- endmacro %}
