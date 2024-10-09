# Download thumbnails from the list of YouTube videos specified in videos.txt to the current directory

#!/bin/bash

yt-dlp --write-thumbnail --skip-download --convert-thumbnails png -a videos.txt -o "%(title)s.%(ext)s"
