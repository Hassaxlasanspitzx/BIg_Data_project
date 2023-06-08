import csv
import os
from googleapiclient.discovery import build

# Set up the API client
api_key = "AIzaSyBIV9xNTxLQaqsGLgmyUoTh_JP5AFshqi4"  # Replace with your actual API key
youtube = build("youtube", "v3", developerKey=api_key)

# Specify the start and end dates for the desired period
start_date = "2023-01-01"
end_date = "2023-06-30"

# Perform the API request
request = youtube.search().list(
    part="snippet",
    q="future of cosmetics",  # Replace "product" with "cosmetics product review"
    type="video",
    order="viewCount",  # Add this line to sort the results by view count, i.e., popularity
    maxResults=10,
    publishedAfter=start_date + "T00:00:00Z",  # Limit results to videos published after the start date
    publishedBefore=end_date + "T23:59:59Z",  # Limit results to videos published before the end date
    regionCode="US"
)
response = request.execute()

# Process the API response
results = []
for item in response["items"]:
    video_title = item["snippet"]["title"]
    video_url = "https://www.youtube.com/watch?v=" + item["id"]["videoId"]
    results.append({"Title": video_title, "URL": video_url})

# Specify the output file path
directory_path = "/home/choco/datalake/raw/youtube/"  # Replace with the actual directory path
file_name = "cosmetics_results.csv"  # Change the file name to "cosmetics_results.csv"

# Ensure the directory exists
if not os.path.exists(directory_path):
    os.makedirs(directory_path)

# Write the results to a CSV file
file_path = os.path.join(directory_path, file_name)
fieldnames = ["Title", "URL"]

with open(file_path, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

print("Results saved to:", file_path)