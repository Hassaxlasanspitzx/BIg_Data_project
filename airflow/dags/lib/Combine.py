from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder \
    .appName("Data Analysis") \
    .getOrCreate()

# Read the Google data from Parquet file
google_data = spark.read.parquet('/home/choco/airflow/datalake/formatted/google_trends/formatted_google_data_rising.parquet')

# Read the YouTube data from Parquet file
youtube_data = spark.read.parquet('/home/choco/airflow/datalake/formatted/youtube/formatted_youtube_data.parquet')

# Check the column names in both DataFrames
print("Google Data Columns:")
google_data.printSchema()

print("YouTube Data Columns:")
youtube_data.printSchema()

# Perform data analysis using Spark operations
# Example analysis: Count the number of records in each DataFrame
google_count = google_data.count()
youtube_count = youtube_data.count()

# Example analysis: Calculate the average of a numeric column
average_value_google = google_data.selectExpr("avg(numeric_column)").collect()[0][0]
average_value_youtube = youtube_data.selectExpr("avg(numeric_column)").collect()[0][0]

# Save the analyzed data as new Parquet files
google_data.write.parquet('/home/choco/airflow/datalake/usages/combined_google_data.parquet')
youtube_data.write.parquet('/home/choco/airflow/datalake/usages/combined_youtube_data.parquet')

# Stop the SparkSession
spark.stop()

print("Google Data Count:", google_count)
print("YouTube Data Count:", youtube_count)
print("Average Value (Google Data):", average_value_google)
print("Average Value (YouTube Data):", average_value_youtube)