#!/bin/bash

# Create a virtual environment if it doesn't exist
if [ ! -d "/var/app/staging/venv" ]; then
    python3 -m venv /var/app/staging/venv
fi

# Install dependencies
/var/app/staging/venv/bin/pip install -r /var/app/staging/requirements.txt
