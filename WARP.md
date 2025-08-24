# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Overview

GhostCipher is a Unicode steganography library that encodes text into invisible Unicode characters. It enables hiding secrets in plain sight by converting text into sequences of zero-width/invisible Unicode glyphs that can be embedded in any document.

## Installation & Setup

### Development Installation (Editable Mode)
```bash
pip install -e .
```

### Using Installation Scripts
```bash
# GUI installer (Tkinter-based)
python3 GUI_Installer.py

# Shell installer  
chmod +x install.sh
./install.sh

# Shell wrapper for GUI
./gui_wrapper
```

The installers clone/update from the upstream GitHub repository and install in editable mode with `--user` flag.

## Development Commands

### Testing the Library
```bash
# Quick functionality test
python3 -c "import ghostcipher; print(repr(ghostcipher.encode('test')))"

# Test encode/decode cycle
python3 -c "import ghostcipher; s='hello'; print(ghostcipher.decode(ghostcipher.encode(s)) == s)"

# Test steganography functions
python3 -c "import ghostcipher; hidden=ghostcipher.hide_in_text('visible', 'secret'); print(ghostcipher.reveal_from_text(hidden, 6))"
```

### Building & Distribution
```bash
# Build package
python3 setup.py sdist bdist_wheel

# Clean build artifacts
rm -rf build/ dist/ *.egg-info/
```

### Code Quality (Recommended)
```bash
# Install development tools
pip install flake8 black pytest

# Linting
flake8 ghostcipher/

# Code formatting
black ghostcipher/

# Run tests (when test suite is added)
pytest
```

## Architecture

### Core Encoding Algorithm
GhostCipher uses a base-16 encoding scheme mapping each character to exactly 2 invisible Unicode characters:

1. **Character Mapping**: Each ASCII/Unicode character is converted to its ordinal value
2. **Base-16 Split**: The ordinal is split into high nibble (`n // 16`) and low nibble (`n % 16`)
3. **Unicode Mapping**: Each nibble maps to one of 16 predefined invisible Unicode characters
4. **Steganography**: Encoded strings can be appended to visible text invisibly

### Unicode Character Table
The library uses 16 invisible Unicode characters as "digits":
- Zero Width Space (`\u200B`)
- Zero Width Non-Joiner (`\u200C`) 
- Zero Width Joiner (`\u200D`)
- Word Joiner (`\u2060`)
- Function Application (`\u2061-\u2064`)
- Various format controls (`\u206A-\u206F`)
- Zero Width No-Break Space (`\uFEFF`)
- Interlinear Annotation Anchor (`\uFFF9`)

### Steganography Model
- **Hide**: Visible text + invisible encoded secret → Combined text
- **Reveal**: Extract last `N*2` characters where `N` is the secret length
- **Limitation**: Requires knowing the secret length for extraction

## Project Structure

```
ghostcipher_mit/
├── ghostcipher/           # Core Python package
│   └── __init__.py       # Main API (encode, decode, hide_in_text, reveal_from_text)
├── GUI_Installer.py      # Tkinter-based installer GUI
├── install.sh           # Shell-based installer script
├── gui_wrapper          # Shell wrapper for GUI installer
├── setup.py            # Python package configuration
├── README.md          # User documentation
└── LICENSE           # MIT license
```

## Key Components

### Core API (`ghostcipher/__init__.py`)
- `encode(text: str) -> str`: Convert text to invisible characters
- `decode(invisible: str) -> str`: Convert invisible characters back to text
- `hide_in_text(text: str, secret: str) -> str`: Hide secret in visible text
- `reveal_from_text(text: str, secret_length: int) -> str`: Extract hidden secret

### Installation Tools
- **GUI_Installer.py**: Threaded Tkinter GUI that clones/updates repo and installs via pip
- **install.sh**: Bash script for command-line installation with git operations
- **gui_wrapper**: Shell script that launches GUI installer with Python detection

## Usage Patterns

### Library Import
```python
import ghostcipher

# Basic encoding/decoding
encoded = ghostcipher.encode("hello world")
decoded = ghostcipher.decode(encoded)

# Steganography
hidden_text = ghostcipher.hide_in_text("This is visible", "secret message") 
secret = ghostcipher.reveal_from_text(hidden_text, len("secret message"))
```

### Command Line Testing
```bash
# Test encoding
python3 -c "import ghostcipher; print(ghostcipher.encode('test'))"

# Verify invisibility (should look empty but have length)
python3 -c "import ghostcipher; s=ghostcipher.encode('hi'); print(f'Length: {len(s)}, Visible: [{s}]')"
```

### Development Workflow
1. Make changes to `ghostcipher/__init__.py`
2. Test with quick one-liners or create test scripts  
3. Use `pip install -e .` for editable installation during development
4. The GUI installer can be used to update from upstream repository

## Technical Limitations

- **Security**: This is steganography, not cryptography - no encryption is applied
- **Detection**: Advanced Unicode analysis could detect the invisible characters
- **Length Dependency**: Revealing secrets requires knowing the exact character length
- **Unicode Support**: Only works with Unicode-aware text systems and fonts

## Upstream Repository

Original source: `https://github.com/LesterDaPow/ghostcipher_mit.git`

The installation scripts automatically handle cloning/updating from this repository.
