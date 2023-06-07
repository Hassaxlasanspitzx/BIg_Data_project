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


def  store_google_data(trends):
    current_day = date.today().strftime("%Y%m%d")
    TARGET_PATH = "/home/choco/datalake/raw/google_trends/" + current_day + "/"
    if not os.path.exists(TARGET_PATH):
        os.makedirs(TARGET_PATH)
    print("Writing here: ", TARGET_PATH)

    # Extract the data from the dictionary
    data = trends['Cosmetics']

    # Specify the field names for the CSV file
    field_names = data[0].keys()

    # Create the CSV file
    file_path = TARGET_PATH + "google-data.csv"
    with open(file_path, "w+", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)

        # Write the header
        writer.writeheader()

        # Write the data rows
        writer.writerows(data)

    # Call the function
keyword = 'Cosmetics'
fetch_data_from_google(keyword)