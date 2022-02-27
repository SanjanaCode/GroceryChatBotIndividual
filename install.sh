#!/usr/bin/env bash

# Create a virtual environment and install the requirements
python3 -m venv venv

# Activate the environment
source ./venv/bin/activate

# Install the packages
./venv/bin/pip3 install -r requirements.txt