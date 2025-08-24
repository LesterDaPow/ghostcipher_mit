# Installation Guide

This guide covers all methods for installing GhostCipher on your system.

## Quick Installation

### Method 1: GUI Installer (Recommended for beginners)

The easiest way to install GhostCipher is using the graphical installer:

```bash
python3 GUI_Installer.py
```

This will:
1. Open a simple GUI window
2. Download/update the latest version from GitHub
3. Install GhostCipher in editable mode with user permissions
4. Show installation status and any errors

**Requirements:**
- Python 3.6 or later
- Tkinter (usually included with Python)
- Git (for repository cloning)
- Internet connection

### Method 2: Shell Script Installation

For command-line users:

```bash
chmod +x install.sh
./install.sh
```

Or use the shell wrapper:
```bash
./gui_wrapper
```

This will:
1. Clone or update the GhostCipher repository
2. Install in editable mode using pip
3. Provide command-line feedback

### Method 3: Manual pip Installation

For development or when you already have the source:

```bash
# Clone the repository
git clone https://github.com/LesterDaPow/ghostcipher_mit.git
cd ghostcipher_mit

# Install in editable mode
pip install -e .

# Or install for current user only
pip install --user -e .
```

## Detailed Installation Steps

### Prerequisites

Before installing GhostCipher, ensure you have:

1. **Python 3.6+**: Check your version with:
   ```bash
   python3 --version
   ```

2. **pip**: Usually comes with Python, verify with:
   ```bash
   pip --version
   ```

3. **Git**: Required for cloning the repository:
   ```bash
   git --version
   ```

4. **Internet connection**: For downloading the repository and dependencies

### Step-by-Step Manual Installation

#### 1. Download the Source Code

```bash
# Option A: Clone with Git (recommended)
git clone https://github.com/LesterDaPow/ghostcipher_mit.git
cd ghostcipher_mit

# Option B: Download ZIP file
# Visit https://github.com/LesterDaPow/ghostcipher_mit
# Click "Code" → "Download ZIP"
# Extract and navigate to the folder
```

#### 2. Verify the Installation

```bash
# Check that the files are present
ls -la
# Should see: ghostcipher/, setup.py, README.md, etc.

# Check the main module
python3 -c "import ghostcipher; print('GhostCipher found!')"
```

#### 3. Install with pip

```bash
# Development installation (recommended)
pip install -e .

# Or system-wide installation
pip install .

# Or user-only installation
pip install --user -e .
```

#### 4. Test the Installation

```bash
# Quick functionality test
python3 -c "import ghostcipher; print(repr(ghostcipher.encode('test')))"

# Full round-trip test
python3 -c "
import ghostcipher
text = 'Hello, World!'
encoded = ghostcipher.encode(text)
decoded = ghostcipher.decode(encoded)
print(f'Success: {decoded == text}')
print(f'Original: {text}')
print(f'Decoded:  {decoded}')
"
```

## Installation Options Explained

### Editable Installation (`-e` flag)

The editable installation option (`pip install -e .`) creates a link to the source code rather than copying files. This means:

**Advantages:**
- Changes to source code take effect immediately
- Perfect for development and testing
- Easy to update with `git pull`
- No need to reinstall after code changes

**When to use:**
- Development work
- Testing new features
- Frequent updates from the repository

### User Installation (`--user` flag)

The user installation option installs packages to your user directory instead of system-wide.

**Advantages:**
- No administrator privileges required
- Doesn't affect system Python packages
- Isolated from other users
- Safe for shared systems

**When to use:**
- On shared computers
- When you don't have admin rights
- To avoid conflicts with system packages

## Platform-Specific Instructions

### macOS

```bash
# Install Python 3 if needed (using Homebrew)
brew install python3

# Clone and install GhostCipher
git clone https://github.com/LesterDaPow/ghostcipher_mit.git
cd ghostcipher_mit
pip3 install --user -e .

# Test installation
python3 -c "import ghostcipher; print('Installation successful!')"
```

### Linux (Ubuntu/Debian)

```bash
# Install Python 3 and pip if needed
sudo apt update
sudo apt install python3 python3-pip git

# Clone and install GhostCipher
git clone https://github.com/LesterDaPow/ghostcipher_mit.git
cd ghostcipher_mit
pip3 install --user -e .

# Test installation
python3 -c "import ghostcipher; print('Installation successful!')"
```

### Windows

Using Command Prompt:
```cmd
# Install Git and Python 3 from their official websites first

# Clone the repository
git clone https://github.com/LesterDaPow/ghostcipher_mit.git
cd ghostcipher_mit

# Install GhostCipher
pip install --user -e .

# Test installation
python -c "import ghostcipher; print('Installation successful!')"
```

Using PowerShell:
```powershell
# Same commands as Command Prompt
git clone https://github.com/LesterDaPow/ghostcipher_mit.git
cd ghostcipher_mit
pip install --user -e .
python -c "import ghostcipher; print('Installation successful!')"
```

## Troubleshooting

### Common Issues and Solutions

#### "python3: command not found"
**Problem**: Python 3 is not installed or not in PATH.
**Solution**: 
- Install Python 3 from [python.org](https://python.org)
- On some systems, use `python` instead of `python3`
- Add Python to your system PATH

#### "pip: command not found"  
**Problem**: pip is not installed.
**Solution**:
```bash
# Linux/macOS
python3 -m ensurepip --upgrade

# Or install pip manually
curl https://bootstrap.pypa.io/get-pip.py | python3

# Windows
python -m ensurepip --upgrade
```

#### "git: command not found"
**Problem**: Git is not installed.
**Solution**: Install Git from [git-scm.com](https://git-scm.com)

#### "Permission denied" errors
**Problem**: Insufficient permissions for installation.
**Solution**: Use `--user` flag or virtual environment:
```bash
# User installation
pip install --user -e .

# Or create virtual environment
python3 -m venv ghostcipher_env
source ghostcipher_env/bin/activate  # Linux/macOS
# ghostcipher_env\Scripts\activate  # Windows
pip install -e .
```

#### "ModuleNotFoundError: No module named 'ghostcipher'"
**Problem**: Installation didn't complete or Python can't find the module.
**Solutions**:
1. Check if installation succeeded:
   ```bash
   pip list | grep ghostcipher
   ```

2. Try reinstalling:
   ```bash
   pip uninstall ghostcipher
   pip install -e .
   ```

3. Check Python path:
   ```python
   import sys
   print('\n'.join(sys.path))
   ```

#### GUI Installer Won't Start
**Problem**: Tkinter not available or GUI issues.
**Solutions**:
1. Install Tkinter:
   ```bash
   # Ubuntu/Debian
   sudo apt install python3-tk
   
   # macOS (usually included)
   # Windows (usually included)
   ```

2. Use shell installer instead:
   ```bash
   ./install.sh
   ```

### Verification Commands

After installation, run these commands to verify everything works:

```bash
# 1. Import test
python3 -c "import ghostcipher; print('✓ Import successful')"

# 2. Basic functionality
python3 -c "
import ghostcipher
encoded = ghostcipher.encode('test')
decoded = ghostcipher.decode(encoded)
print(f'✓ Encode/decode: {decoded == \"test\"}')
"

# 3. Steganography test
python3 -c "
import ghostcipher
hidden = ghostcipher.hide_in_text('visible', 'secret')
revealed = ghostcipher.reveal_from_text(hidden, 6)
print(f'✓ Steganography: {revealed == \"secret\"}')
"

# 4. Unicode test
python3 -c "
import ghostcipher
text = 'Unicode: 🌟 café'
encoded = ghostcipher.encode(text)
decoded = ghostcipher.decode(encoded)
print(f'✓ Unicode support: {decoded == text}')
"
```

## Updating GhostCipher

### Using the Installers

The GUI and shell installers will automatically update to the latest version:

```bash
# GUI update
python3 GUI_Installer.py

# Shell update
./install.sh
```

### Manual Update

```bash
# Navigate to the repository
cd ghostcipher_mit

# Pull latest changes
git pull origin master

# No need to reinstall if using editable installation (-e)
# Otherwise, reinstall:
pip install -e .
```

## Uninstalling GhostCipher

```bash
# Uninstall the package
pip uninstall ghostcipher

# Remove the source directory if desired
rm -rf ghostcipher_mit/  # Linux/macOS
# rmdir /s ghostcipher_mit  # Windows
```

## Next Steps

After successful installation:

1. **Read the [Quick Start Guide](quickstart.md)** for your first steps
2. **Try the [Basic Examples](../examples/basic_usage.md)** to learn the API
3. **Explore [Steganography Examples](../examples/steganography.md)** for advanced usage
4. **Check the [API Reference](../api/ghostcipher.md)** for complete function documentation

## Support

If you encounter issues not covered in this guide:

1. Check the [API documentation](../api/ghostcipher.md)
2. Review the [examples](../examples/)
3. Consult the [troubleshooting section](#troubleshooting) above
4. Visit the [GitHub repository](https://github.com/LesterDaPow/ghostcipher_mit) for issues and discussions
