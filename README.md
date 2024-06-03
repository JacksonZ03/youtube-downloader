# YouTube Video Downloader
Uses [YT-DLP](https://github.com/yt-dlp/yt-dlp) under the hood.
Just enter in a YouTube video URL and download it.

Allows you to select the resolution and codec you want to download. (If unsure, just press enter to default to best quality).

Downloads in mp4 format to the same directory as the script.

# Requirements
Install Anaconda to run this script: https://docs.anaconda.com/anaconda/install/

# Quick Start
## Mac OS
1. Install Anaconda: https://docs.anaconda.com/anaconda/install/
2. Double click `run.command` file to run the python script

## Linux
1. Install Anaconda: https://docs.anaconda.com/anaconda/install/
2. Run `chmod +x run.sh` to make the shell script executable
3. Run `run.sh` to execute the python script

# Codecs

AVC1 (aka. H.264) - Low Efficiency, Highest Bitrate

VP9 - Average Efficiency, Average Bitrate (20-35% more efficient than AVC1)

AV01 - High Efficiency, Lowest Bitrate (20% more efficient than VP9)