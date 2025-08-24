#!/bin/bash
set -e

if [ -d "ghostcipher" ]; then
    echo "Updating existing GhostCipher repository..."
    cd ghostcipher
    git pull origin master
    cd ..  # go back to repo root
else
    echo "Cloning GhostCipher repository..."
    git clone https://github.com/LesterDaPow/ghostcipher_mit.git ghostcipher
fi

echo "Installing GhostCipher..."
pip install --user -e ./ghostcipher  # <-- install from repo root

echo "GhostCipher installed/updated successfully!"
