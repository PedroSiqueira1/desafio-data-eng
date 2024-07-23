import os
import polars as pl


def transform_data(clean_data_path='./data/clean_data', raw_data_path='./data/raw_data'):
    """
    Transform the data in the raw_data_path directory and save it to the clean_data_path directory.
    """

    # Create the directory if it does not exist
    if not os.path.exists(clean_data_path):
        os.makedirs(clean_data_path)

    # List all files in the raw_data_path directory
    files = os.listdir(raw_data_path)


    schema_columns = [  'id_terc',
                        'sg_orgao_sup_tabela_ug',
                        'cd_ug_gestora',
                        'nm_ug_tabela_ug',
                        'sg_ug_gestora',
                        'nr_contrato',
                        'nr_cnpj',
                        'nm_razao_social',
                        'nr_cpf',
                        'nm_terceirizado',
                        'nm_categoria_profissional',
                        'nm_escolaridade',
                        'nr_jornada',
                        'nm_unidade_prestacao',
                        'vl_mensal_salario',
                        'vl_mensal_custo',
                        'nr_mes_carga',
                        'nm_mes_carga',
                        'nr_ano_carga',
                        'sg_orgao',
                        'nm_orgao',
                        'cd_orgao_siafi',
                        'cd_orgao_siape'
                        ]
    
    def clean_and_save(df, file):
        """
        Clean the dataframe and save it to a csv file.
        """
        df.columns = schema_columns

        year = file.split('_')[0]
        year_column = pl.Series("nr_ano_carga", [year for _ in range(len(df))])

        month_number = file.split('_')[1].split('.')[0]
        month_number_column = pl.Series("nr_mes_carga", [month_number for _ in range(len(df))])

        months = {
            '1': 'JANEIRO',
            '5': 'MAIO',
            '9': 'SETEMBRO',
        }
        months_column = pl.Series("nm_mes_carga", [months[month_number] for _ in range(len(df))])

        df = df.with_columns([
            pl.col('vl_mensal_salario').str.replace(',', '.'),
            pl.col('vl_mensal_custo').str.replace(',', '.'),
        ])

        df = df.replace_column(df.columns.index("nr_mes_carga"), month_number_column)
        df = df.replace_column(df.columns.index("nm_mes_carga"), months_column)
        df = df.replace_column(df.columns.index("nr_ano_carga"), year_column)

        df.write_csv(f"{clean_data_path}/{file}")
    for file in files:
        print(f"Cleaning file {file}...")

        file_path = f"{raw_data_path}/{file}"
        file_extension = file.split('.')[-1]

        if file == '2019_1.csv':
            df = pl.read_csv(file_path, has_header=False, separator=';', encoding='utf8')
        elif file_extension == 'xlsx':
            df = pl.read_excel(file_path)
        else:
            df = pl.read_csv(file_path, has_header=True, separator=';', encoding='latin1')

        clean_and_save(df, file)
        print(f"{file} file saved in clean_data folder")

transform_data()