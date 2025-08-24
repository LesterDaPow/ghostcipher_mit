# GhostCipher Documentation

Welcome to the GhostCipher documentation! GhostCipher is a Unicode steganography library that allows you to encode text into invisible Unicode characters and hide secrets in plain sight.

## Table of Contents

### Quick Start
- [Installation Guide](guides/installation.md) - Get GhostCipher up and running
- [Quick Start Tutorial](guides/quickstart.md) - Your first steps with GhostCipher
- [Basic Examples](examples/basic_usage.md) - Simple code examples to get started

### User Guides
- [User Guide](guides/user_guide.md) - Comprehensive guide to using GhostCipher
- [Steganography Guide](guides/steganography.md) - Advanced steganography techniques
- [Best Practices](guides/best_practices.md) - Tips and recommendations

### API Reference
- [API Documentation](api/ghostcipher.md) - Complete function reference
- [Core Functions](api/core.md) - encode(), decode(), hide_in_text(), reveal_from_text()

### Technical Documentation
- [Architecture Overview](technical/architecture.md) - How GhostCipher works internally
- [Unicode Encoding](technical/encoding.md) - Details of the base-16 Unicode encoding
- [Character Mapping](technical/characters.md) - Unicode character reference table

### Examples
- [Basic Usage](examples/basic_usage.md) - Simple encoding/decoding examples
- [Steganography Examples](examples/steganography.md) - Hiding text in documents
- [Advanced Examples](examples/advanced.md) - Complex use cases and patterns
- [Command Line Usage](examples/cli.md) - Using GhostCipher from the command line

### Development
- [Contributing](../WARP.md) - Development setup and guidelines
- [Building from Source](guides/development.md) - Development environment setup

## Getting Started

The fastest way to get started is to install GhostCipher and try the basic examples:

```python
import ghostcipher

# Encode a message into invisible characters
secret = ghostcipher.encode("Hello, World!")
print(f"Encoded length: {len(secret)}")  # Shows character count
print(f"Visible content: [{secret}]")     # Appears empty but has content

# Decode back to original text
decoded = ghostcipher.decode(secret)
print(f"Decoded: {decoded}")  # "Hello, World!"
```

## Key Features

- **Invisible Encoding**: Convert any text into invisible Unicode characters
- **Steganography**: Hide secret messages inside visible text
- **Simple API**: Easy-to-use Python functions
- **Unicode Safe**: Works with any Unicode-aware system
- **Cross-Platform**: Pure Python, works everywhere

## Use Cases

- **Hidden Messages**: Embed secrets in documents, emails, or web pages
- **Watermarking**: Add invisible signatures to text content  
- **Covert Communication**: Exchange messages that appear as normal text
- **Data Embedding**: Store metadata invisibly within documents

## Important Notes

⚠️ **Security Notice**: GhostCipher provides steganography (hiding data), not cryptography (encrypting data). The hidden text is not encrypted and can be decoded by anyone who knows it's there.

📝 **Length Dependency**: To reveal hidden text, you must know the exact length of the secret message.

🔍 **Detection**: Advanced Unicode analysis tools may be able to detect the presence of hidden content.

## Support

- Check the [API Documentation](api/ghostcipher.md) for detailed function reference
- See [Examples](examples/) for practical usage patterns
- Review [Technical Documentation](technical/) for implementation details
- Consult [Best Practices](guides/best_practices.md) for optimal usage

---

**GhostCipher** - Making secrets invisible since 2025 ✨
