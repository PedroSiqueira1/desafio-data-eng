import pandas as pd
from datetime import datetime
from prefect import task
import os

@task
def update_urls_csv(file_path='urls.csv'):
    '''
    Update the URLs in the csv file based on the last URL in the file.
    '''

    # Get environment variables
    update_url_flag = os.getenv('UPDATE_URLS')

    # Check if need to update the URLs
    if update_urls_csv == 'False':
        print('URLs are up to date.')
        return 0

    df = pd.read_csv(file_path)

    # Last row of the DataFrame
    last_row = df.tail(1).iloc[0]
    last_year = last_row['year']
    last_month = last_row['month']

    # Current year and month
    months = [1, 5, 9]
    current_year = datetime.now().year
    current_month = datetime.now().month

    # Generate the URL for a given year and month based of the last url template
    def generate_url(year, month):
        month_str = f"{month:02d}"
        return f"https://www.gov.br/cgu/pt-br/acesso-a-informacao/dados-abertos/arquivos/terceirizados/arquivos/terceirizados{year}{month_str}.xlsx"

    # Fill the DataFrame with the URLs to add
    urls_to_add = []
    for year in range(last_year, current_year + 1):
        for month in months:
            if (year < current_year) or (year == current_year and month <= current_month and month > last_month):
                url = generate_url(year, month)
                if url:
                    urls_to_add.append([year, month, url]) 

    new_df = pd.DataFrame(urls_to_add, columns=['year', 'month', 'url'])

    df = pd.concat([df, new_df], ignore_index=True)

    df['month'] = df['month'].apply(lambda x: f"{x:02d}")

    df.to_csv(file_path, index=False)

    print('URLs updated successfully.')
