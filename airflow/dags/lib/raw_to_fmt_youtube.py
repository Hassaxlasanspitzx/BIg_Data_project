import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import os

# Specify the file path relative to the current script
file_path = '/home/choco/airflow/datalake/raw/youtube/cosmetics_results.csv'

# Read the CSV file
youtube_data = pd.read_csv(file_path)

# Specify the output directory path
output_directory = '/home/choco/airflow/datalake/formatted/youtube/'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Specify the output file path within the directory
output_file_youtube = os.path.join(output_directory, 'formatted_youtube_data.parquet')

# Convert the DataFrame to Parquet format and write to file
table = pa.Table.from_pandas(youtube_data)
pq.write_table(table, output_file_youtube)

print("YouTube data formatted and saved to:", output_file_youtube)