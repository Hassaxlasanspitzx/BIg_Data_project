import pandas as pd
import os

# Specify the file path relative to the current script
file_path = '/home/choco/datalake/raw/youtube/cosmetics_results.csv'

# Read the CSV file
youtube_data = pd.read_csv(file_path)

# Specify the output directory path
output_directory = '/home/choco/datalake/formatted/youtube/'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Specify the output file path within the directory
output_file_youtube = os.path.join(output_directory, 'formatted_youtube_data.parquet')

# Convert the dataframe to Parquet format
youtube_data.to_parquet(output_file_youtube, index=False)

print("YouTube data formatted and saved to:", output_file_youtube)