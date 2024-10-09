#!/bin/bash

# Get the terminal window ID
TERMINAL_WINDOW_ID=$(osascript -e 'tell application "Terminal" to id of front window')

# Change to the directory where the script is located
cd "$(dirname "$0")"

while true; do
    # Prompt for YouTube URL
    echo "Enter YouTube URL (or 'q' to quit):"
    read url

    # Check if user wants to quit
    if [ "$url" = "q" ]; then
        echo "Exiting..."
        # Close only this specific terminal window
        osascript -e "tell application \"Terminal\" to close (every window whose id is $TERMINAL_WINDOW_ID)" & exit 0
    fi

    # Validate URL
    if [[ $url =~ ^https?://(www\.)?youtube\.com/watch\?v=[a-zA-Z0-9_-]{11}$ ]] || [[ $url =~ ^https?://youtu\.be/[a-zA-Z0-9_-]{11}$ ]]; then
        echo "Valid YouTube URL. Downloading thumbnail..."
        
        # Download thumbnail to the current directory
        yt-dlp --write-thumbnail --skip-download --convert-thumbnails png "$url" -o "%(title)s.%(ext)s"
        
        if [ $? -eq 0 ]; then
            echo "Thumbnail downloaded successfully to: $(pwd)"
            echo "Press Enter to continue or 'q' to quit..."
            read choice
            if [ "$choice" = "q" ]; then
                echo "Exiting..."
                # Close only this specific terminal window
                osascript -e "tell application \"Terminal\" to close (every window whose id is $TERMINAL_WINDOW_ID)" & exit 0
            fi
        else
            echo "Error downloading thumbnail. Please try again."
        fi
    else
        echo "Invalid YouTube URL. Please try again."
    fi

    echo ""
done