import os
import requests

URLS_FILE_PATH = "youtubeURLs.txt"
DOWNLOAD_PATH = "{YOUR_DOWNLOAD_PATH}"

API_URL = "https://youtube-mp36.p.rapidapi.com/dl"

HEADERS = {
    "X-RapidAPI-Key": "{YOUR_RAPID_API_KEY}",
    "X-RapidAPI-Host": "youtube-mp36.p.rapidapi.com"
}

def read_file_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def download_mp3(video_id):
    querystring = {"id": video_id}
    response = requests.get(API_URL, headers=HEADERS, params=querystring)

    print(response.json())

    json_response = response.json()

    if 'link' in json_response:
        download_link = json_response['link']

        response = requests.get(download_link)

        if response.status_code == 200:
            file_name = f"{json_response['title']}.mp3"
            file_path = os.path.join(DOWNLOAD_PATH, file_name)
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded MP3 for video ID {video_id} and saved as {file_name}.")
        else:
            print(f"Failed to download the MP3 for video ID {video_id}.")
    else:
        print(f"Failed to get the download link for video ID {video_id}. Error: {json_response.get('error')}")

# Create the target directory if it does not exist
if not os.path.exists(DOWNLOAD_PATH):
    os.makedirs(DOWNLOAD_PATH)

lines_list = read_file_lines(URLS_FILE_PATH)
video_ids = [url.split('v=')[1].strip() for url in lines_list]

for video_id in video_ids:
    download_mp3(video_id)
