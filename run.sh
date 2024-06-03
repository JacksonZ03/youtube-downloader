#!/bin/bash

set -e # Exit if anything fails

# Change working directory to the directory where the script is located
cd "$(dirname "$0")"

# Path to your Python script
PYTHON_SCRIPT="./download.py"

# Path to your .conda environment folder (assuming it's in the same directory as this script)
CONDA_ENV_PATH="./.conda"

# Activate the conda environment
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate "$CONDA_ENV_PATH"

# Run the Python script
python "$PYTHON_SCRIPT"

# Deactivate the conda environment
conda deactivate