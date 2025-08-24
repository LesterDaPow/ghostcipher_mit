# GhostCipher

Encode and decode text using invisible Unicode characters. GhostCipher allows you to hide messages in plain sight by converting text into a sequence of invisible Unicode characters, which can be embedded in any text or document.

## Features
- Encode any string into invisible Unicode characters
- Decode invisible Unicode back to readable text
- Hide secrets inside visible text
- Reveal hidden secrets from text
- Simple Python API
- GUI installer for easy setup

## Installation

### Quick Install (Recommended)

#### Using the GUI Installer
Run the GUI installer script:

```sh
python3 GUI_Installer.py
```

#### Using the Shell Script
Alternatively, run the shell installer:

```sh
chmod +x install.sh
./install.sh
```

This will clone/update the repository and install GhostCipher in editable mode.

## Usage

### Python API

```python
import ghostcipher

# Encode a message
secret = ghostcipher.encode("hello")
print(secret)  # Invisible characters

# Decode
print(ghostcipher.decode(secret))  # 'hello'

# Hide a secret in visible text
hidden = ghostcipher.hide_in_text("Visible text", "secret")

# Reveal the secret (if you know its length)
revealed = ghostcipher.reveal_from_text(hidden, secret_length=6)
print(revealed)  # 'secret'
```

### Command Line
Test the encoding from the command line:

```sh
python3 -c 'import ghostcipher; print(ghostcipher.encode("meow"))'
```

## Project Structure

- `ghostcipher/` — Core Python package
- `GUI_Installer.py` — GUI installer (Tkinter)
- `install.sh` — Shell installer
- `gui_wrapper` — Shell wrapper for GUI installer
- `setup.py` — Python package setup

## License

This project is licensed under the MIT License. See `LICENSE` for details.
