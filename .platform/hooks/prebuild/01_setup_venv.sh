#!/bin/bash

# Log the start of the script
echo "Starting virtual environment setup..."

# Ensure Python3 is available
if ! command -v python3 &> /dev/null; then
    echo "Error: Python3 is not installed."
    exit 1
fi

# Create a virtual environment if it doesn't exist
if [ ! -d "/var/app/staging/venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv /var/app/staging/venv
else
    echo "Virtual environment already exists."
fi

# Upgrade pip to the latest version
echo "Upgrading pip..."
/var/app/staging/venv/bin/pip install --upgrade pip

# Install dependencies
if [ -f "/var/app/staging/requirements.txt" ]; then
    echo "Installing dependencies from requirements.txt..."
    /var/app/staging/venv/bin/pip install -r /var/app/staging/requirements.txt
else
    echo "Error: requirements.txt not found in /var/app/staging/"
    exit 1
fi

# Log the completion
echo "Virtual environment setup completed successfully."


