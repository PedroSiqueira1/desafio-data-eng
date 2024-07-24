import os
from sqlalchemy import create_engine

# Get the environment variables
username = os.getenv('USER')
password = os.getenv('PASSWORD')
host = os.getenv('HOST')
port = os.getenv('PORT')
database = os.getenv('DATABASE')

# Connect to the database
db_string = f'postgresql://{username}:{password}@{host}:{port}/{database}'
engine = create_engine(db_string)