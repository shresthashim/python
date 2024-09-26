#!/bin/bash

# Check if at least one package name is provided
if [ $# -eq 0 ]; then
    echo "No package name provided. Usage: ./uninstall_and_update.sh package_name1 package_name2 ..."
    exit 1
fi

# Uninstall the packages
for package in "$@"; do
    pip uninstall -y "$package"  # '-y' option automatically confirms uninstallation
done

# Update requirements.txt
pip freeze > requirements.txt

echo "Uninstalled packages and updated requirements.txt"
