import csv
from TikTokApi import TikTokApi

def fetch_tiktok_trends():
    # Create an instance of TikTokApi
    api = TikTokApi()

    # Fetch trending videos
    trending_videos = api.trending()

    # Extract relevant information from each video
    trends_data = []
    for video in trending_videos:
        video_data = {
            "id": video['id'],
            "author": video['author']['uniqueId'],
            "description": video['desc'],
            "likes": video['stats']['diggCount'],
            "shares": video['stats']['shareCount'],
            "comments": video['stats']['commentCount'],
            "views": video['stats']['playCount'],
        }
        trends_data.append(video_data)

    # Specify the field names for the CSV file
    field_names = ["id", "author", "description", "likes", "shares", "comments", "views"]

    # Create the CSV file
    file_path = "/home/choco/datalake/raw/youtube/trends.csv"
    with open(file_path, "w+", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)

        # Write the header
        writer.writeheader()

        # Write the data rows
        writer.writerows(trends_data)

    print("TikTok trends data has been saved to", file_path)

# Call the function to fetch and store TikTok trends
fetch_tiktok_trends()