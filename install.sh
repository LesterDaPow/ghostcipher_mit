#!/bin/bash
# GhostCipher installer — updates or installs locally in editable mode
# Professional version, safe for repeated runs

set -e  # Exit immediately if a command fails

REPO_URL="https://github.com/LesterDaPow/ghostcipher_mit.git"
INSTALL_DIR="ghostcipher"

if [ -d "$INSTALL_DIR" ]; then
    echo "Updating existing GhostCipher repository..."
    cd "$INSTALL_DIR"
    git pull origin master
    cd ..
else
    echo "Cloning GhostCipher repository..."
    git clone "$REPO_URL" "$INSTALL_DIR"
fi

echo "Installing GhostCipher in editable mode..."
pip install --user -e "./$INSTALL_DIR"

echo "GhostCipher installed/updated successfully!"
echo "Test it in Python with:"
echo "python -c 'import ghostcipher; print(ghostcipher.encode(\"meow\"))'"
