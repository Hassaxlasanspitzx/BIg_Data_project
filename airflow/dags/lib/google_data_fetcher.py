from pytrends.request import TrendReq
import os
import csv
from datetime import date

def fetch_data_from_google(keyword):
    trends = visualize_related_topics_from_google(keyword)
    store_google_data(trends)

def visualize_related_topics_from_google(keyword):
    # Initialize pytrends
    pytrend = TrendReq()

    # Build the search query
    pytrend.build_payload(kw_list=[keyword], timeframe='2023-01-01 2023-06-30')

    # Get related topics
    related_topic = pytrend.related_topics()

    return related_topic

def store_google_data(trends):
    current_day = date.today().strftime("%Y%m%d")
    TARGET_PATH = "/home/choco/airflow/datalake/raw/google_trends/" + current_day + "/"
    if not os.path.exists(TARGET_PATH):
        os.makedirs(TARGET_PATH)
    print("Writing here: ", TARGET_PATH)

    # Extract the data from the dictionary
    data_top = trends['Cosmetics']['top'].iloc[1:]
    data_rising = trends['Cosmetics']['rising'].iloc[1:]

    # Select the desired columns
    data_top = data_top[['value', 'formattedValue', 'link', 'topic_mid', 'topic_title']]
    data_rising = data_rising[['value', 'formattedValue', 'link', 'topic_mid', 'topic_title']]

    # Save the DataFrame to CSV file
    file_path_top = TARGET_PATH + "google-data-top.csv"
    data_top.head(10).to_csv(file_path_top)

    file_path_rising = TARGET_PATH + "google-data-rising.csv"
    data_rising.head(10).to_csv(file_path_rising)

# Call the function
keyword = 'Cosmetics'
fetch_data_from_google(keyword)