
{{ config(materialized='table') }}


WITH filtered_data AS (
    SELECT
        id_terc,
        nm_terceirizado,
        nr_cnpj,
        nm_razao_social,
        nm_categoria_profissional,
        nm_escolaridade,
        nr_jornada,
        nm_unidade_prestacao,
        vl_mensal_custo,
        nm_ug_tabela_ug
    FROM orcamento_contratos_terceirizados
    WHERE vl_mensal_custo > 15000
    AND nm_ug_tabela_ug = 'DEPARTAMENTO DE POLICIA RODOVIARIA FEDERAL'
)

SELECT
    id_terc,
    nm_terceirizado,
    nr_cnpj,
    nm_razao_social,
    nm_categoria_profissional,
    nm_escolaridade,
    nr_jornada,
    nm_unidade_prestacao,
    vl_mensal_custo,
    nm_ug_tabela_ug
FROM filtered_data
