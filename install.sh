#!/usr/bin/env bash

# Create a virtual environment and install the requirements
python3 -m venv venv


# Check the platform
OS="$(uname -s)"

# If we're on Windows
if [[  $OS =~ MINGW.* || $OS =~ CYGWIN.* ]]; then
    # Activate the environment
    exec ./venv/Scripts/activate
    # Install the packages
    exec ./venv/bin/pip3 install -r requirements.txt
else
    # Activate the environment
    source ./venv/bin/activate

    # Install the packages
    ./venv/bin/pip3 install -r requirements.txt
fi


