import os
import polars as pl
from sqlalchemy import create_engine

def load_to_database(engine, clean_data_path='./data/clean_data'):
    """
    Load the data in the clean_data_path directory to the database.
    """

    for file_name in os.listdir(clean_data_path):
        file_path = os.path.join(clean_data_path, file_name)
        
        df = pl.read_csv(file_path)
        
        # Insere os dados no banco de dados
        df.write_database('orcamento_contratos_terceirizados', connection=engine, if_table_exists='append')
        print(f"Loaded {file_name} into database.")


# Get the environment variables
username = os.getenv('USER')
password = os.getenv('PASSWORD')
host = os.getenv('HOST')
port = os.getenv('PORT')
database = os.getenv('DATABASE')

# Connect to the database
db_string = f'postgresql://{username}:{password}@{host}:{port}/{database}'
engine = create_engine(db_string)
load_to_database(engine)
