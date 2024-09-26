#!/bin/bash

# Check if at least one package name is provided
if [ $# -eq 0 ]; then
    echo "No package name provided. Usage: ./install_and_update.sh package_name1 package_name2 ..."
    exit 1
fi

# Install the packages
for package in "$@"; do
    pip install "$package"
done

# Update requirements.txt
pip freeze > requirements.txt

echo "Installed packages and updated requirements.txt"
