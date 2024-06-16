# YouTube Downloader
Uses [YT-DLP](https://github.com/yt-dlp/yt-dlp) under the hood to download any YouTube videos in both mp3 and mp4 format.

Allows you to select the resolution and codec you want to download. (If unsure, just press enter to default to best quality).

Downloads the video files to the same directory as the script.

# Requirements
Install Anaconda to run this script: https://docs.anaconda.com/anaconda/install/

# Quick Start
## Mac OS
1. Install Anaconda: https://docs.anaconda.com/anaconda/install/
2. Double click `run.command` file to run the python script
3. Pick either "1. Audio" or "2. Video"
4. Enter in the YouTube video URL to download

## Linux
1. Install Anaconda: https://docs.anaconda.com/anaconda/install/
2. Run `chmod +x run.sh` to make the shell script executable
3. Run `run.sh` to execute the python script
4. Pick either "1. Audio" or "2. Video"
5. Enter in the YouTube video URL to download

# Codecs

AVC1 (aka. H.264) - Low Efficiency, Highest Bitrate

VP9 - Execelent Efficiency, Average Bitrate (20-35% more efficient than AVC1) - Recommended

AV01 - High Efficiency, Lowest Bitrate (20% more efficient than VP9)

---

Selecting audio downloads to mp3 format at the highest quality.
