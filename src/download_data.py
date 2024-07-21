import os
import requests
import polars as pl

def download_data(csv_file='urls.csv', raw_data_path='./data/raw_data', retries=5):
    """
    Download data from the urls in the csv file and save it to the raw_data_path directory.
    """

    # Read urls csv file
    df_url = pl.read_csv(csv_file)

    # Create the directory if it does not exist
    if not os.path.exists(raw_data_path):
        os.makedirs(raw_data_path)

    # Iterate over the rows of the dataframe
    for row in df_url.rows():
        year = row[0]
        month = row[1]
        url = row[2]

        print(f"Downloading file for {year}-{month}")

        attempt = 0
        success = False

        while attempt < retries and not success:

            attempt += 1
            print(f"Attempt {attempt} of {retries}...")

            try:
                r = requests.get(url, allow_redirects=True)
                r.raise_for_status()  # Check for HTTP request errors

                file_extension = url.split('.')[-1] # Get the file extension

                path = f"{raw_data_path}/{year}_{month}.{file_extension}" 

                # Save the content to disk
                with open(path, 'wb') as f:
                    f.write(r.content)

                print(f"Downloaded {year}_{month}.{file_extension}")
                success = True

            except requests.exceptions.HTTPError as http_err:
                print(f"HTTP error occurred: {http_err}")
            except Exception as err:
                print(f"Other error occurred: {err}")
            
            

        if not success:
            print(f"Failed to download file for {year}-{month} after {retries} attempts.")

download_data()
