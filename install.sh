#!/bin/bash
# GhostCipher installer — installs the package locally for the current user

# Exit immediately if a command fails
set -e

echo "Cloning GhostCipher repository..."
git clone https://github.com/LesterDaPow/ghostcipher_mit.git ghostcipher

cd ghostcipher

echo "Installing GhostCipher..."
pip install --user -e .

echo "GhostCipher installed successfully!"
echo "You can test it with:"
echo "python -c 'import ghostcipher; print(ghostcipher.encode(\"meow\"))'"
