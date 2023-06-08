import pandas as pd

# Read the CSV file for top topics
df_top = pd.read_csv('google-data-top.csv')

# Perform any data manipulation or analysis if needed
# ...

# Convert to Parquet format
df_top.to_parquet('google-data-top.parquet', index=False)

# Read the CSV file for rising topics
df_rising = pd.read_csv('google-data-rising.csv')

# Perform any data manipulation or analysis if needed
# ...

# Convert to Parquet format
df_rising.to_parquet('google-data-rising.parquet', index=False)