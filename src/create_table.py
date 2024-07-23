from sqlalchemy import create_engine, Table, Column, String, Float, DateTime, MetaData, func
import os
import datetime
def create_table(engine):
    metadata = MetaData()

    clean_data_table = Table(
        'orcamento_contratos_terceirizados', metadata,
        Column('id_terc', String, primary_key=True),
        Column('sg_orgao_sup_tabela_ug', String),
        Column('cd_ug_gestora', String),
        Column('nm_ug_tabela_ug', String),
        Column('sg_ug_gestora', String),
        Column('nr_contrato', String),
        Column('nr_cnpj', String),
        Column('nm_razao_social', String),
        Column('nr_cpf', String),
        Column('nm_terceirizado', String),
        Column('nm_categoria_profissional', String),
        Column('nm_escolaridade', String),
        Column('nr_jornada', String),
        Column('nm_unidade_prestacao', String),
        Column('vl_mensal_salario', Float),
        Column('vl_mensal_custo', Float),
        Column('nr_mes_carga', String),
        Column('nm_mes_carga', String),
        Column('nr_ano_carga', String),
        Column('sg_orgao', String),
        Column('nm_orgao', String),
        Column('cd_orgao_siafi', String),
        Column('cd_orgao_siape', String),
        Column('created_at', DateTime, server_default=func.now()),
        Column('updated_at', DateTime, server_default=func.now(), server_onupdate=func.now())
    )

    metadata.create_all(engine)

# Get the environment variables
username = os.getenv('USER')
password = os.getenv('PASSWORD')
host = os.getenv('HOST')
port = os.getenv('PORT')
database = os.getenv('DATABASE')

# Connect to the database
db_string = f'postgresql://{username}:{password}@{host}:{port}/{database}'
engine = create_engine(db_string)
create_table(engine)
