# YT2MP3

YouTube to MP3 Converter

YT2MP3.py is a Python script that allows you to convert YouTube videos to MP3 audio format. It utilizes the YouTube to MP3 conversion API from [RapidAPI](https://rapidapi.com) to perform the conversion. Simply provide a list of YouTube video URLs in a text file, and the script will automatically download the corresponding MP3 files to a specified download path.

## Prerequisites

- [Python](https://www.python.org/downloads/) installed on your system.
- An API key from RapidAPI that grants you access to the [YouTube to MP3 conversion API](https://rapidapi.com/ytjar/api/youtube-mp36).

## How to Use

Follow these steps to use the script:

- Clone or download this repository to your local machine.
- Install the required dependencies by running the following command in your terminal:

```bash
pip install requests
```

Prepare a text file (youtubeURLs.txt) containing the YouTube video URLs, one URL per line. Ensure that you place this file in the same directory as the script.

Open the script (YT2MP3.py) and modify the following variables:

- URLS_FILE_PATH: The file path of the text file containing the YouTube video URLs (default: "youtubeURLs.txt").
- DOWNLOAD_PATH: The directory where you want the downloaded MP3 files to be saved. Replace {YOUR_DOWNLOAD_PATH} with your desired path.
- Insert your RapidAPI key into the HEADERS dictionary by replacing {YOUR_RAPID_API_KEY} with your actual API key.

## Run

Run the script by executing the following command in your terminal or command prompt:

```bash
python YT2MP3.py
```

The script will read the list of YouTube video URLs from the text file, convert each video to MP3, and save the resulting MP3 files in the specified download path.

Please be aware that downloading copyrighted material from YouTube may infringe upon YouTube's terms of service or copyright laws in your country. Ensure that you have the necessary permissions to download and use the content legally.

### Disclaimer

This script is intended for educational and personal use only. The authors are not responsible for any misuse of this script or violations of YouTube's terms of service or copyright laws. Always use this tool responsibly and respect the rights of content creators.
