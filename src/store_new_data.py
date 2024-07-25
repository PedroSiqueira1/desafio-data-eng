import utils.create_table
import utils.load_to_database
import utils.transform_data
import utils.download_data
from utils.db import engine
from prefect import flow

@flow(log_prints=True)
def store_new_data():

    utils.update_urls.update_urls_csv(file_path='urls.csv')
    utils.download_data.download_data(csv_file='urls.csv', raw_data_path='./data/raw_data', retries=5)
    utils.transform_data.transform_data(clean_data_path='./data/clean_data', raw_data_path='./data/raw_data')
    utils.load_to_database.load_to_database(engine,clean_data_path='./data/clean_data')


if __name__ == '__main__':
    store_new_data()