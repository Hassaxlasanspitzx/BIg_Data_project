#def fetch_data_from_twitter(**kwargs):
    #print("We are getting data from ..")
    #print("...")
    #print("Done !");#
import csv
import os
from datetime import date
from pytrends.request import TrendReq

def fetch_data_from_google(keyword):
   trends = visualize_related_topics_from_google(keyword)
   store_google_data(trends)

def visualize_related_topics_from_google(keyword):
    # Initialize pytrends
    pytrend = TrendReq()

    # Build the search query
    pytrend.build_payload(kw_list=[keyword])

    # Get related topics
    related_topic = pytrend.related_topics()

    return related_topic

def store_google_data(trends):
        current_day = date.today().strftime("%Y%m%d")
        TARGET_PATH = "/home/choco/datalake/raw/google_trends/" + current_day + "/"
        if not os.path.exists(TARGET_PATH):
            os.makedirs(TARGET_PATH)
        print("Writing here: ", TARGET_PATH)

        # Extract the data from the dictionary
        data_top = trends['Cosmetics']['top']
        data_rising = trends['Cosmetics']['rising']

        # Save the DataFrame to CSV file
        file_path_top = TARGET_PATH + "google-data-top.csv"
        data_top.to_csv(file_path_top)

        file_path_rising = TARGET_PATH + "google-data-rising.csv"
        data_rising.to_csv(file_path_rising)

    # Call the function
keyword = 'Cosmetics'
fetch_data_from_google(keyword)