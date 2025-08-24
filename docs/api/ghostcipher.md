# GhostCipher API Reference

Complete reference for all public functions in the GhostCipher library.

## Module: `ghostcipher`

The main GhostCipher module provides four core functions for encoding, decoding, and steganography operations.

### Functions

---

## `encode(text: str) -> str`

Converts a string into invisible Unicode characters using base-16 encoding.

**Parameters:**
- `text` (str): The input text to encode. Can be any valid Unicode string.

**Returns:**
- `str`: A string of invisible Unicode characters representing the encoded input.

**Description:**
Each character in the input text is converted to its Unicode ordinal value, then split into high and low nibbles (4-bit values). Each nibble is mapped to one of 16 predefined invisible Unicode characters, resulting in exactly 2 invisible characters per input character.

**Example:**
```python
import ghostcipher

# Basic encoding
encoded = ghostcipher.encode("Hello")
print(f"Length: {len(encoded)}")  # 10 (5 chars × 2 invisible chars each)
print(f"Encoded: [{encoded}]")    # Appears empty but contains invisible chars

# Unicode support
encoded_unicode = ghostcipher.encode("Hello 🌟")
print(f"Unicode length: {len(encoded_unicode)}")  # 14 (7 chars × 2)
```

**Technical Details:**
- Each input character produces exactly 2 invisible output characters
- Output length is always `len(input) × 2`
- Supports full Unicode character set
- Uses 16 invisible Unicode characters as encoding digits

---

## `decode(invisible: str) -> str`

Converts invisible Unicode characters back into readable text.

**Parameters:**
- `invisible` (str): A string of invisible Unicode characters created by `encode()`.

**Returns:**
- `str`: The original text that was encoded.

**Raises:**
- `ValueError`: If the input length is odd (invalid encoding) or contains unrecognized characters.

**Description:**
Reverses the encoding process by parsing pairs of invisible characters, converting them back to nibbles, combining the nibbles into ordinal values, and converting to characters.

**Example:**
```python
import ghostcipher

# Basic decoding
encoded = ghostcipher.encode("Secret")
decoded = ghostcipher.decode(encoded)
print(decoded)  # "Secret"

# Round-trip verification
original = "Test message 123"
assert ghostcipher.decode(ghostcipher.encode(original)) == original

# Error handling
try:
    ghostcipher.decode("invalid")  # Wrong characters
except ValueError as e:
    print(f"Error: {e}")

try:
    encoded = ghostcipher.encode("test")
    ghostcipher.decode(encoded[:-1])  # Odd length
except ValueError as e:
    print(f"Error: {e}")  # "Invalid input length; should be even."
```

**Technical Details:**
- Input length must be even (pairs of invisible characters)
- Each pair of invisible characters produces one output character
- Validates that all characters are valid encoding digits
- Output length is always `len(input) ÷ 2`

---

## `hide_in_text(text: str, secret: str) -> str`

Hides a secret message inside visible text by appending invisible encoded characters.

**Parameters:**
- `text` (str): The visible text that will contain the hidden message.
- `secret` (str): The secret message to hide within the visible text.

**Returns:**
- `str`: Combined text containing both visible content and hidden invisible characters.

**Description:**
This function implements steganography by appending the encoded secret to the visible text. The result appears identical to the original visible text but contains hidden information that can be extracted if you know the secret length.

**Example:**
```python
import ghostcipher

# Basic steganography
visible = "This is a normal message."
secret = "hidden"
combined = ghostcipher.hide_in_text(visible, secret)

print(combined)  # Looks like: "This is a normal message."
print(len(combined))  # 24 + 12 = 36 (original + hidden chars)
print(combined == visible)  # False (contains extra invisible chars)

# Multiple secrets (not recommended)
text1 = ghostcipher.hide_in_text("Hello", "secret1")
text2 = ghostcipher.hide_in_text(text1, "secret2")  # Now has both secrets
```

**Use Cases:**
- Email signatures with hidden contact info
- Document watermarking
- Covert communication in plain text
- Metadata embedding in text files

**Important Notes:**
- The hidden content is not encrypted, only invisible
- You must know the secret length to extract it
- Multiple secrets will be concatenated (extract carefully)
- Copy-paste operations typically preserve invisible characters

---

## `reveal_from_text(text: str, secret_length: int) -> str`

Extracts a hidden secret from text containing invisible characters.

**Parameters:**
- `text` (str): Text containing hidden invisible characters (created by `hide_in_text()`).
- `secret_length` (int): The exact length of the hidden secret in characters.

**Returns:**
- `str`: The hidden secret message.

**Raises:**
- `ValueError`: If there aren't enough invisible characters for the specified length.

**Description:**
Extracts the last `secret_length × 2` invisible characters from the input text and decodes them to reveal the hidden message. The secret length must be known exactly.

**Example:**
```python
import ghostcipher

# Basic secret extraction
visible = "Public message"
secret = "classified"
hidden_text = ghostcipher.hide_in_text(visible, secret)

# Extract the secret (must know length)
revealed = ghostcipher.reveal_from_text(hidden_text, len(secret))
print(revealed)  # "classified"

# Alternative: if you remember the original secret
original_secret = "my password"
hidden_document = ghostcipher.hide_in_text("Dear Sir,\n...", original_secret)
extracted = ghostcipher.reveal_from_text(hidden_document, len(original_secret))
assert extracted == original_secret

# Error: insufficient characters
try:
    ghostcipher.reveal_from_text("short", 10)  # Need 20 invisible chars
except ValueError:
    print("Not enough hidden characters")
```

**Technical Details:**
- Extracts exactly `secret_length × 2` characters from the end of the text
- These characters must be valid invisible Unicode encoding digits
- Works by taking the suffix and passing it to `decode()`
- Does not modify the input text

**Tips:**
- Store the secret length separately or use a fixed-length format
- Consider prefixing secrets with length information
- Test extraction immediately after hiding to verify the process

---

## Unicode Character Mapping

GhostCipher uses 16 invisible Unicode characters as encoding digits:

| Index | Unicode | Name | Description |
|-------|---------|------|-------------|
| 0 | `\u200B` | ZERO WIDTH SPACE | Most common invisible character |
| 1 | `\u200C` | ZERO WIDTH NON-JOINER | Text shaping control |
| 2 | `\u200D` | ZERO WIDTH JOINER | Text shaping control |
| 3 | `\u2060` | WORD JOINER | Non-breaking invisible space |
| 4 | `\u2061` | FUNCTION APPLICATION | Mathematical invisible operator |
| 5 | `\u2062` | INVISIBLE TIMES | Mathematical invisible operator |
| 6 | `\u2063` | INVISIBLE SEPARATOR | Mathematical invisible operator |
| 7 | `\u2064` | INVISIBLE PLUS | Mathematical invisible operator |
| 8 | `\u206A` | INHIBIT SYMMETRIC SWAPPING | BiDi format control |
| 9 | `\u206B` | ACTIVATE SYMMETRIC SWAPPING | BiDi format control |
| 10 | `\u206C` | INHIBIT ARABIC FORM SHAPING | Arabic text control |
| 11 | `\u206D` | ACTIVATE ARABIC FORM SHAPING | Arabic text control |
| 12 | `\u206E` | NATIONAL DIGIT SHAPES | Number formatting control |
| 13 | `\u206F` | NOMINAL DIGIT SHAPES | Number formatting control |
| 14 | `\uFEFF` | ZERO WIDTH NO-BREAK SPACE | Byte order mark character |
| 15 | `\uFFF9` | INTERLINEAR ANNOTATION ANCHOR | Text annotation control |

---

## Error Handling

All functions may raise the following exceptions:

### `ValueError`
- **`decode()`**: Invalid input length (not even) or unrecognized characters
- **`reveal_from_text()`**: Insufficient invisible characters for requested secret length
- **Encoding errors**: Invalid Unicode characters in input

### Best Practices for Error Handling

```python
import ghostcipher

def safe_encode_decode(text):
    """Safely encode and decode text with error handling."""
    try:
        encoded = ghostcipher.encode(text)
        decoded = ghostcipher.decode(encoded)
        return decoded == text
    except (ValueError, TypeError) as e:
        print(f"Encoding error: {e}")
        return False

def safe_steganography(visible_text, secret):
    """Safely hide and reveal secrets with validation."""
    try:
        # Hide the secret
        hidden_text = ghostcipher.hide_in_text(visible_text, secret)
        
        # Immediately verify by extracting
        revealed = ghostcipher.reveal_from_text(hidden_text, len(secret))
        
        if revealed == secret:
            return hidden_text
        else:
            print("Secret verification failed")
            return None
            
    except (ValueError, TypeError) as e:
        print(f"Steganography error: {e}")
        return None
```

---

## Performance Considerations

- **Encoding Speed**: Linear time complexity O(n) where n is input length
- **Memory Usage**: Output strings are exactly 2× input length for encoding
- **Unicode Handling**: All operations work with Python's native Unicode strings
- **Large Texts**: No special handling needed for large inputs; Python's string handling scales well

## Compatibility

- **Python Version**: Compatible with Python 3.6+
- **Unicode Support**: Full Unicode character set supported
- **Platform**: Cross-platform (Windows, macOS, Linux)
- **Text Editors**: Most Unicode-aware editors preserve invisible characters
- **Copy/Paste**: Generally preserved across applications that support Unicode
