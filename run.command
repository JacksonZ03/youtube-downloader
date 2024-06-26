#!/bin/bash

# Get the terminal window ID
TERMINAL_WINDOW_ID=$(osascript -e 'tell application "Terminal" to id of front window')

set -e # Exit if anything fails

# Change working directory to the directory where the script is located
cd "$(dirname "$0")"

## Conda setup
# Path to your .conda environment folder (assuming it's in the same directory as this script)
CONDA_ENV_PATH="./.conda"

# Add conda-forge channel to the conda environment if not already present
if ! conda config --show channels | grep -q "conda-forge"; then
    # Add the conda-forge channel
    conda config --add channels conda-forge
    echo "The conda-forge channel has been added."
fi

# Activate the conda environment
if [ ! -d "./.conda" ]; then
    conda env create --prefix ./.conda --file ./src/environment.yml
    echo "*" >> ./.conda/.gitignore # Add "*" to .gitignore so it doesn't mess up source control in vscode
fi

source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate "$CONDA_ENV_PATH"


# Prompt the user for audio or video download
echo "Select download option:"
echo "1. Audio"
echo "2. Video (default)"
read -p "Enter 1 or 2: " -r
DOWNLOAD_OPTION=${REPLY:-2}

# Determine which Python script to run based on the user's choice
if [ "$DOWNLOAD_OPTION" == "1" ]; then
    PYTHON_SCRIPT="./src/audio-download.py"
elif [ "$DOWNLOAD_OPTION" == "2" ]; then
    PYTHON_SCRIPT="./src/video-download.py"
else
    echo "Invalid option. Exiting..."
    osascript -e "tell application \"Terminal\" to close (every window whose id is $TERMINAL_WINDOW_ID)" & exit 1
fi

# Run the Python script
python "$PYTHON_SCRIPT" < /dev/tty

# Deactivate the conda environment
conda deactivate

# Indicate script completion and wait for user to press Enter to exit
echo "Script completed. Press Enter to exit."
read -r

# Close the Terminal after pressing Enter
osascript -e "tell application \"Terminal\" to close (every window whose id is $TERMINAL_WINDOW_ID)" & exit 0
