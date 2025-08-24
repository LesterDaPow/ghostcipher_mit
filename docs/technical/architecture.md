# GhostCipher Architecture

Technical documentation of GhostCipher's Unicode steganography implementation.

## Overview

GhostCipher implements Unicode steganography using a base-16 encoding scheme that maps text characters to invisible Unicode control characters. This approach allows text to be hidden in plain sight within any Unicode-compatible document or communication.

## Core Algorithm

### Base-16 Encoding Process

The fundamental encoding process follows these steps:

1. **Character to Ordinal**: Convert each character to its Unicode ordinal value
2. **Nibble Split**: Split the ordinal into high and low 4-bit nibbles
3. **Nibble to Invisible**: Map each nibble to an invisible Unicode character
4. **Concatenation**: Combine invisible characters into the final encoded string

```python
def encode(text: str) -> str:
    result = ""
    for char in text:
        ordinal = ord(char)           # Step 1: Get Unicode ordinal
        high = ordinal // 16          # Step 2a: High nibble
        low = ordinal % 16            # Step 2b: Low nibble
        result += digits[high] + digits[low]  # Steps 3 & 4
    return result
```

### Mathematical Foundation

The encoding is mathematically equivalent to base-16 conversion with a custom alphabet:

- **Input domain**: Any Unicode character (0 to 1,114,111)
- **Nibble range**: 0-15 for both high and low nibbles
- **Output alphabet**: 16 invisible Unicode characters
- **Expansion ratio**: 2:1 (each character becomes 2 invisible characters)

**Ordinal Recovery Formula:**
```
original_ordinal = (high_nibble × 16) + low_nibble
original_character = chr(original_ordinal)
```

## Unicode Character Selection

### Invisible Character Criteria

The 16 invisible Unicode characters were selected based on these criteria:

1. **True Invisibility**: Characters that render with zero width
2. **Cross-Platform Support**: Wide compatibility across systems and fonts
3. **Preservation**: Survive copy/paste and text processing operations
4. **Format Safety**: Don't interfere with text layout or formatting
5. **Standard Compliance**: Follow Unicode specifications for their intended use

### Character Mapping Table

| Index | Code Point | Unicode Name | Category | Purpose |
|-------|------------|--------------|----------|---------|
| 0 | U+200B | ZERO WIDTH SPACE | Format | Text breaking |
| 1 | U+200C | ZERO WIDTH NON-JOINER | Format | Script shaping |
| 2 | U+200D | ZERO WIDTH JOINER | Format | Script joining |
| 3 | U+2060 | WORD JOINER | Format | Line breaking |
| 4 | U+2061 | FUNCTION APPLICATION | Symbol | Math formatting |
| 5 | U+2062 | INVISIBLE TIMES | Symbol | Math operators |
| 6 | U+2063 | INVISIBLE SEPARATOR | Symbol | Math punctuation |
| 7 | U+2064 | INVISIBLE PLUS | Symbol | Math operators |
| 8 | U+206A | INHIBIT SYMMETRIC SWAPPING | Format | BiDi control |
| 9 | U+206B | ACTIVATE SYMMETRIC SWAPPING | Format | BiDi control |
| 10 | U+206C | INHIBIT ARABIC FORM SHAPING | Format | Arabic text |
| 11 | U+206D | ACTIVATE ARABIC FORM SHAPING | Format | Arabic text |
| 12 | U+206E | NATIONAL DIGIT SHAPES | Format | Number display |
| 13 | U+206F | NOMINAL DIGIT SHAPES | Format | Number display |
| 14 | U+FEFF | ZERO WIDTH NO-BREAK SPACE | Format | BOM/joining |
| 15 | U+FFF9 | INTERLINEAR ANNOTATION ANCHOR | Format | Annotations |

### Character Categories

The selected characters fall into two main Unicode categories:

1. **Format Characters (Cf)**: Control formatting and text flow
   - Zero-width spaces and joiners
   - BiDi (bidirectional text) controls
   - Number formatting controls

2. **Math Symbols (Sm)**: Invisible mathematical operators
   - Function application symbols
   - Invisible arithmetic operators
   - Mathematical separators

## Steganography Implementation

### Hiding Mechanism

Steganography is implemented by appending encoded invisible characters to visible text:

```
visible_text + invisible_encoded_secret = steganographic_text
```

The result appears identical to the original visible text but contains additional invisible characters at the end.

### Extraction Algorithm

Secret extraction works by taking a suffix of known length:

```python
def reveal_from_text(text: str, secret_length: int) -> str:
    invisible_chars_needed = secret_length * 2
    invisible_suffix = text[-invisible_chars_needed:]
    return decode(invisible_suffix)
```

**Critical Requirements:**
- Exact secret length must be known
- Invisible characters must be preserved at the end of the text
- No additional invisible characters should be added after hiding

## Performance Characteristics

### Time Complexity

| Operation | Time Complexity | Notes |
|-----------|----------------|-------|
| `encode(text)` | O(n) | Linear in input length |
| `decode(invisible)` | O(n) | Linear in input length |
| `hide_in_text(text, secret)` | O(n + m) | n = text length, m = secret length |
| `reveal_from_text(text, length)` | O(m) | m = secret length |

### Space Complexity

| Operation | Space Complexity | Output Size |
|-----------|------------------|-------------|
| `encode(text)` | O(n) | 2 × input length |
| `decode(invisible)` | O(n) | 0.5 × input length |
| `hide_in_text(text, secret)` | O(n + m) | text length + (2 × secret length) |

### Memory Usage

- **Encoding**: Creates new string 2× the input size
- **Decoding**: Creates new string 0.5× the input size  
- **Steganography**: Minimal additional memory (string concatenation)
- **No buffering**: All operations work with complete strings

## Implementation Details

### Error Handling

The implementation includes robust error handling:

```python
# Decode validation
if len(invisible) % 2 != 0:
    raise ValueError("Invalid input length; should be even.")

# Character validation
for char in invisible:
    if char not in digits:
        raise ValueError(f"Invalid character: {char}")

# Extraction validation  
if len(text) < secret_length * 2:
    raise ValueError("Insufficient characters for extraction")
```

### Edge Cases

1. **Empty Input**: Empty strings encode to empty strings
2. **Single Character**: Becomes exactly 2 invisible characters
3. **Unicode Edge Cases**: High Unicode values (> 65535) work correctly
4. **Null Character**: U+0000 encodes as two U+200B characters

### Character Encoding Behavior

**Examples of character encoding:**

| Character | Ordinal | High Nibble | Low Nibble | Encoded |
|-----------|---------|-------------|------------|---------|
| 'A' | 65 | 4 | 1 | digits[4] + digits[1] |
| '🌟' | 127775 | 7839 → 15,3 | 15 | digits[15] + digits[3] |
| '\n' | 10 | 0 | 10 | digits[0] + digits[10] |

## Security Considerations

### Steganography Limitations

⚠️ **Important Security Notes:**

1. **Not Cryptography**: Hidden content is not encrypted, only invisible
2. **Detectability**: Advanced Unicode analysis can detect patterns
3. **Length Dependency**: Extraction requires knowing exact secret length
4. **No Authentication**: No built-in verification of message integrity

### Detection Vectors

Potential methods for detecting hidden content:

1. **Statistical Analysis**: Unusual distribution of invisible characters
2. **Length Analysis**: Text longer than expected for visible content
3. **Character Frequency**: Repeated invisible character patterns
4. **Unicode Normalization**: Some processes may strip invisible characters

### Mitigation Strategies

To reduce detection risk:

1. **Limit Hidden Content**: Keep secrets short and infrequent
2. **Natural Distribution**: Spread hidden content across multiple documents
3. **Format Considerations**: Choose appropriate document types
4. **Layered Security**: Combine with encryption for sensitive content

## Platform Compatibility

### Unicode Support Requirements

- **Python Version**: 3.6+ (full Unicode support)
- **Encoding**: UTF-8 or UTF-16 recommended
- **Text Editors**: Must support Unicode format characters
- **Fonts**: Should handle invisible characters gracefully

### Known Compatibility Issues

1. **Plain Text Editors**: Some may strip format characters
2. **Email Systems**: May normalize or filter invisible characters
3. **Database Storage**: Ensure UTF-8 support for proper storage
4. **Copy/Paste**: Generally preserved but system-dependent

### Testing Platform Compatibility

```python
def test_platform_compatibility():
    """Test if the platform properly handles invisible characters."""
    test_text = "Hello"
    encoded = ghostcipher.encode(test_text)
    
    # Test round-trip
    decoded = ghostcipher.decode(encoded)
    if decoded != test_text:
        return False, "Round-trip failed"
    
    # Test steganography
    hidden = ghostcipher.hide_in_text("Visible", "Secret")
    revealed = ghostcipher.reveal_from_text(hidden, 6)
    if revealed != "Secret":
        return False, "Steganography failed"
    
    return True, "Platform compatible"
```

## Technical Specifications

### Character Limits

- **Maximum input character**: U+10FFFF (1,114,111)
- **Minimum input character**: U+0000 (0)
- **Output character range**: 16 specific invisible Unicode characters
- **Practical text limit**: Limited by Python string handling (~2^31 characters)

### Encoding Properties

- **Deterministic**: Same input always produces same output
- **Reversible**: Perfect round-trip encoding/decoding
- **Order-preserving**: Character order maintained in encoding
- **Length-predictable**: Output length always 2× input length

## Future Considerations

### Potential Improvements

1. **Error Correction**: Add redundancy for noisy environments
2. **Compression**: Compress before encoding for efficiency
3. **Alternative Mappings**: Support different invisible character sets
4. **Length Encoding**: Embed secret length in hidden content

### Research Directions

1. **Detection Resistance**: More sophisticated hiding techniques
2. **Format Integration**: Native support for specific document formats
3. **Multi-Layer Hiding**: Hierarchical steganography systems
4. **Adaptive Encoding**: Context-aware character selection

---

For implementation details and usage examples, see:
- [API Reference](../api/ghostcipher.md)
- [Basic Usage](../examples/basic_usage.md)
- [Steganography Examples](../examples/steganography.md)
