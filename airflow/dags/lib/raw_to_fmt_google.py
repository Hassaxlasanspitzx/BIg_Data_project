import pandas as pd
import os

# Specify the file path relative to the current script
file_path_rising = '/home/choco/airflow/datalake/raw/google_trends/20230608/google-data-rising.csv'

# Read the CSV file
google_data_rising = pd.read_csv(file_path_rising)

# Select the desired columns
columns = ['value', 'formattedValue', 'link', 'topic_mid', 'topic_title']
google_data_rising_formatted = google_data_rising[columns]

# Specify the output directory path
output_directory = '/home/choco/airflow/datalake/formatted/google_trends/'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Specify the output file path within the directory
output_file_google_rising = os.path.join(output_directory, 'formatted_google_data_rising.parquet')

# Convert the dataframe to Parquet format
google_data_rising_formatted.to_parquet(output_file_google_rising, index=False)

print("Google data (rising) formatted and saved to:", output_file_google_rising)