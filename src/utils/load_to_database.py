import os
import polars as pl
from prefect import task

@task
def load_to_database(engine, clean_data_path='../data/clean_data'):
    """
    Load the data in the clean_data_path directory to the database.
    """

    for file_name in os.listdir(clean_data_path):
        file_path = os.path.join(clean_data_path, file_name)
        
        df = pl.read_csv(file_path)
        
        # Insere os dados no banco de dados
        df.write_database('orcamento_contratos_terceirizados', connection=engine, if_table_exists='append')
        print(f"Loaded {file_name} into database.")


