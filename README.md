# YouTube Downloader
Uses [YT-DLP](https://github.com/yt-dlp/yt-dlp) under the hood to download any YouTube videos in both mp3 and mp4 format.

Allows you to select the resolution and codec you want to download. (If unsure, just press enter to default to best quality).

The python scripts will create a `download` folder (if it doesn't already exist) and save the media files there.

# Requirements
[Install Miniconda](https://docs.anaconda.com/free/miniconda/miniconda-install/) to run this script.

> *This script will add conda-forge channel to your Miniconda installation if it doesn't already exist. The script will not re-order existing conda-forge channel if it already exists.*

# Quick Start
## Mac OS
1. [Install Miniconda](https://docs.anaconda.com/free/miniconda/miniconda-install/)
2. Double click `run.command` file to run the python script
3. Pick either `1. Audio`[^1] or `2. Video`
4. Enter in the YouTube video URL to download

## Linux
1. [Install Miniconda](https://docs.anaconda.com/free/miniconda/miniconda-install/)
2. Run `chmod +x run.sh` to make the shell script executable
3. Run `run.sh` to execute the python script
4. Pick either `1. Audio`[^1] or `2. Video`
5. Enter in the YouTube video URL to download


# Codecs

|    Video Codec    | Efficiency   | Bitrate                                   |
| ----------------- | ------------ | ----------------------------------------- |
| AVC1 (aka. H.264) | Low          | Highest                                   |
| VP9 (Recommended) | Excellent    | Average (20-35% more efficient than AVC1) |
| AV01              | High         | Lowest (20% more efficient than VP9)      |


[^1]: Selecting `1. Audio` downloads to mp3 format at the highest quality.
