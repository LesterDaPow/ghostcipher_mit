#!/bin/bash
set -e

if [ -d "ghostcipher" ]; then
    echo "Updating existing GhostCipher repository..."
    cd ghostcipher
    git pull origin master
else
    echo "Cloning GhostCipher repository..."
    git clone https://github.com/LesterDaPow/ghostcipher_mit.git ~/ghostcipher
    cd ~/ghostcipher
fi

echo "Installing GhostCipher..."
pip install --user -e .

echo "GhostCipher installed/updated successfully!"
