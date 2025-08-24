# GhostCipher User Guide

Complete guide to using GhostCipher for Unicode steganography and invisible text encoding.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Basic Concepts](#basic-concepts)
3. [Core Functions](#core-functions)
4. [Steganography Techniques](#steganography-techniques)
5. [Best Practices](#best-practices)
6. [Common Use Cases](#common-use-cases)
7. [Troubleshooting](#troubleshooting)
8. [Advanced Topics](#advanced-topics)

## Getting Started

### What is GhostCipher?

GhostCipher is a Unicode steganography library that converts text into invisible Unicode characters. This allows you to:

- **Hide messages in plain sight**: Embed secrets in normal-looking text
- **Create invisible text**: Convert any text into completely invisible characters
- **Watermark documents**: Add invisible tracking or metadata
- **Secure communications**: Share hidden information through normal channels

### Key Concepts

Before diving into usage, understand these fundamental concepts:

- **Encoding**: Converting visible text into invisible Unicode characters
- **Decoding**: Converting invisible characters back to readable text
- **Steganography**: Hiding secret messages inside visible text
- **Base-16 Mapping**: Each character becomes exactly 2 invisible characters

## Basic Concepts

### How It Works

GhostCipher uses a mathematically sound approach:

1. **Character Analysis**: Each character is converted to its Unicode number
2. **Nibble Splitting**: The number is split into two 4-bit values (nibbles)
3. **Invisible Mapping**: Each nibble maps to one of 16 invisible Unicode characters
4. **Combination**: The invisible characters are combined to form the encoded result

### Example Walkthrough

Let's trace through encoding the letter "A":

```python
import ghostcipher

# Step by step encoding of "A"
char = "A"
ordinal = ord(char)        # 65
high_nibble = 65 // 16     # 4
low_nibble = 65 % 16       # 1

# Maps to digits[4] + digits[1]
# Result: invisible character + invisible character
encoded = ghostcipher.encode(char)
print(f"'{char}' -> [{encoded}] (length: {len(encoded)})")
```

### The Invisible Character Set

GhostCipher uses 16 carefully selected Unicode characters:

- **Zero-width spaces** (U+200B, U+2060, U+FEFF)
- **Text joiners** (U+200C, U+200D)  
- **Mathematical invisibles** (U+2061-U+2064)
- **Format controls** (U+206A-U+206F, U+FFF9)

These characters are invisible in most applications but preserved in text processing.

## Core Functions

### Encoding Text: `encode()`

Converts visible text into invisible Unicode characters.

```python
import ghostcipher

# Basic encoding
message = "Hello, World!"
invisible = ghostcipher.encode(message)

print(f"Original: {message}")
print(f"Encoded: [{invisible}]")           # Appears empty but contains data
print(f"Length: {len(invisible)}")         # 26 characters (13 × 2)
```

**Key Points:**
- Output is always 2× the input length
- Works with any Unicode text
- Result appears empty but contains invisible characters

### Decoding Text: `decode()`

Converts invisible characters back to readable text.

```python
import ghostcipher

# Decode invisible text back to original
encoded_text = ghostcipher.encode("Secret message")
decoded_text = ghostcipher.decode(encoded_text)

print(f"Round trip successful: {decoded_text == 'Secret message'}")
```

**Key Points:**
- Input must be valid invisible characters from `encode()`
- Input length must be even (pairs of invisible characters)
- Perfect round-trip fidelity

### Hiding Secrets: `hide_in_text()`

Embeds invisible text within visible text.

```python
import ghostcipher

# Hide a secret in normal text
public_text = "Meet me at the coffee shop at 3 PM."
secret = "Bring the documents"

combined = ghostcipher.hide_in_text(public_text, secret)

print("What everyone sees:")
print(combined)  # Looks exactly like: "Meet me at the coffee shop at 3 PM."

print(f"Actual length: {len(combined)}")    # 37 + 34 = 71 characters
print(f"Hidden content: {len(secret)} characters")
```

**Key Points:**
- Result looks identical to original visible text
- Contains invisible characters appended at the end
- Length increases by 2× the secret length

### Revealing Secrets: `reveal_from_text()`

Extracts hidden messages from text containing invisible characters.

```python
import ghostcipher

# Extract the hidden message (you must know its length)
text_with_secret = ghostcipher.hide_in_text("Public info", "private")
extracted = ghostcipher.reveal_from_text(text_with_secret, len("private"))

print(f"Extracted secret: {extracted}")    # "private"
```

**Critical Requirement:**
You must know the exact length of the hidden secret to extract it.

## Steganography Techniques

### Basic Message Hiding

The simplest steganography approach:

```python
import ghostcipher

def basic_hiding_example():
    # Create a normal-looking email
    email = """Subject: Project Update
    
Hi team,

The Q4 project is on track. Please review the attached 
documents and provide feedback by Friday.

Thanks,
Sarah"""

    # Hide confidential information
    confidential = "Budget approved - $250K additional"
    
    # Combine visible and invisible
    email_with_secret = ghostcipher.hide_in_text(email, confidential)
    
    return email_with_secret, len(confidential)

hidden_email, secret_length = basic_hiding_example()

# Later, extract the secret
secret = ghostcipher.reveal_from_text(hidden_email, secret_length)
print(f"Hidden message: {secret}")
```

### Multi-Layer Secrets

Hide multiple pieces of information:

```python
import ghostcipher

def layered_secrets():
    base_text = "The meeting is at 2 PM in Conference Room A."
    
    # Layer 1: Basic info
    layer1 = "Bring your laptop"
    text_l1 = ghostcipher.hide_in_text(base_text, layer1)
    
    # Layer 2: Sensitive info (includes layer 1)
    layer2 = "Password: SECURE123"
    text_l2 = ghostcipher.hide_in_text(text_l1, layer2)
    
    # Layer 3: Most sensitive (includes layers 1 & 2)
    layer3 = "Merger announcement Friday"
    final_text = ghostcipher.hide_in_text(text_l2, layer3)
    
    return final_text, [len(layer3), len(layer2), len(layer1)]

layered_text, lengths = layered_secrets()

# Extract in reverse order (most recent first)
secret3 = ghostcipher.reveal_from_text(layered_text, lengths[0])
print(f"Layer 3: {secret3}")

# Remove layer 3 and extract layer 2
without_l3 = layered_text[:-lengths[0]*2]
secret2 = ghostcipher.reveal_from_text(without_l3, lengths[1])
print(f"Layer 2: {secret2}")

# Remove layer 2 and extract layer 1  
without_l2 = without_l3[:-lengths[1]*2]
secret1 = ghostcipher.reveal_from_text(without_l2, lengths[2])
print(f"Layer 1: {secret1}")
```

### Document Watermarking

Add invisible metadata to documents:

```python
import ghostcipher
from datetime import datetime

def watermark_document(content, metadata):
    """Add invisible watermark to any document."""
    
    # Create watermark string
    watermark = f"CREATED:{datetime.now().isoformat()}|AUTHOR:{metadata.get('author', 'unknown')}|VERSION:{metadata.get('version', '1.0')}"
    
    # Add to document
    watermarked = ghostcipher.hide_in_text(content, watermark)
    
    return watermarked, len(watermark)

# Usage example
document = """CONFIDENTIAL REPORT
Market analysis shows strong growth potential...
[rest of document]"""

metadata = {"author": "J.Smith", "version": "2.1"}
watermarked_doc, watermark_len = watermark_document(document, metadata)

# Verify watermark
watermark = ghostcipher.reveal_from_text(watermarked_doc, watermark_len)
print(f"Document watermark: {watermark}")
```

## Best Practices

### Security Guidelines

1. **Understand Limitations**
   - GhostCipher provides steganography (hiding), not cryptography (encryption)
   - Hidden text is not encrypted and can be decoded by anyone who finds it
   - For sensitive information, encrypt before hiding

```python
# Good: Combine with encryption for sensitive data
import ghostcipher
from cryptography.fernet import Fernet

def secure_hiding(visible_text, secret, encryption_key):
    # Encrypt first, then hide
    encrypted = Fernet(encryption_key).encrypt(secret.encode())
    encrypted_string = encrypted.decode('latin1')  # Convert to string
    
    return ghostcipher.hide_in_text(visible_text, encrypted_string)
```

2. **Length Management**
   - Always track secret lengths for reliable extraction
   - Consider storing lengths separately or using fixed-length formats

```python
# Good: Fixed-length approach
def fixed_length_secret(secret, max_length=100):
    if len(secret) > max_length:
        raise ValueError(f"Secret too long (max {max_length})")
    
    # Pad to fixed length
    padded = secret.ljust(max_length, '\0')
    return padded

# Usage
secret = "My secret message"
padded_secret = fixed_length_secret(secret)
hidden = ghostcipher.hide_in_text("Public text", padded_secret)

# Extract (always use fixed length)
extracted = ghostcipher.reveal_from_text(hidden, 100)
# Remove padding
original = extracted.rstrip('\0')
```

3. **Content Guidelines**
   - Keep hidden content short to avoid detection
   - Use natural-looking visible text
   - Test copy/paste behavior in target environments

### Technical Best Practices

1. **Error Handling**

```python
import ghostcipher

def safe_steganography(visible, secret):
    """Safely hide and verify secrets."""
    try:
        # Hide the secret
        hidden = ghostcipher.hide_in_text(visible, secret)
        
        # Immediately verify by extracting
        verification = ghostcipher.reveal_from_text(hidden, len(secret))
        
        if verification != secret:
            raise ValueError("Secret verification failed")
            
        return hidden
        
    except Exception as e:
        print(f"Steganography failed: {e}")
        return None
```

2. **Unicode Handling**

```python
# Good: Handle Unicode properly
text_with_emoji = "Hello 🌟 World!"
encoded = ghostcipher.encode(text_with_emoji)
decoded = ghostcipher.decode(encoded)
assert decoded == text_with_emoji  # Should always pass
```

3. **Platform Testing**

```python
def test_environment():
    """Test if the environment preserves invisible characters."""
    test_cases = [
        ("Simple", "test"),
        ("Unicode", "café 🌟"),
        ("Special", "line\nbreak\ttab"),
        ("Long", "A" * 100)
    ]
    
    for name, text in test_cases:
        try:
            encoded = ghostcipher.encode(text)
            decoded = ghostcipher.decode(encoded)
            
            if decoded == text:
                print(f"✓ {name}: OK")
            else:
                print(f"✗ {name}: Failed")
                
        except Exception as e:
            print(f"✗ {name}: Error - {e}")
```

## Common Use Cases

### 1. Email Communications

```python
import ghostcipher

def secure_email_communication():
    """Hide sensitive information in business emails."""
    
    # Normal business email
    email = """Subject: Quarterly Review Meeting
    
Dear Team,

Please join us for the quarterly review on Friday at 2 PM 
in the main conference room. We'll be discussing our 
progress and planning for the next quarter.

Best regards,
Management"""

    # Hidden instruction for specific recipients
    hidden_instruction = "Bring Q3 financial reports - CONFIDENTIAL"
    
    # Create email with hidden content
    secure_email = ghostcipher.hide_in_text(email, hidden_instruction)
    
    return secure_email, len(hidden_instruction)

# Usage
email_with_secret, instruction_length = secure_email_communication()

# Recipients who know the secret can extract it
instruction = ghostcipher.reveal_from_text(email_with_secret, instruction_length)
print(f"Hidden instruction: {instruction}")
```

### 2. Document Version Control

```python
import ghostcipher
import json
from datetime import datetime

def version_controlled_document():
    """Add invisible version control to documents."""
    
    document = """PROJECT SPECIFICATION
    
System Requirements:
- Python 3.8+
- PostgreSQL database
- Redis cache
- Docker containers

The system should handle 1000+ concurrent users..."""

    # Version metadata
    version_data = {
        "version": "3.2.1",
        "author": "engineering.team",
        "timestamp": datetime.now().isoformat(),
        "branch": "main",
        "commit": "a7b9c3d"
    }
    
    # Encode as JSON and hide
    metadata_json = json.dumps(version_data, separators=(',', ':'))
    versioned_doc = ghostcipher.hide_in_text(document, metadata_json)
    
    return versioned_doc, len(metadata_json)

# Usage
doc, metadata_len = version_controlled_document()

# Extract version information
metadata_str = ghostcipher.reveal_from_text(doc, metadata_len)
metadata = json.loads(metadata_str)

print("Document metadata:")
for key, value in metadata.items():
    print(f"  {key}: {value}")
```

### 3. Social Media Analytics

```python
import ghostcipher
import json

def social_media_with_tracking():
    """Hide analytics metadata in social media posts."""
    
    # Public social media content
    post = """Amazing sunset from today's hike! 🌅 
Nature never fails to inspire and recharge the soul. 
Perfect end to a beautiful weekend.

#hiking #sunset #nature #weekend #inspiration"""

    # Hidden analytics data
    analytics = {
        "campaign_id": "nature_content_q1",
        "target_demographic": "outdoor_enthusiasts_25_45", 
        "posting_time": "optimal_engagement_window",
        "expected_reach": 5000,
        "performance_tracking": True
    }
    
    # Hide analytics in post
    analytics_json = json.dumps(analytics, separators=(',', ':'))
    tracked_post = ghostcipher.hide_in_text(post, analytics_json)
    
    return tracked_post, len(analytics_json)

# Usage
post_with_analytics, analytics_len = social_media_with_tracking()

# Platform can extract analytics data
analytics_str = ghostcipher.reveal_from_text(post_with_analytics, analytics_len)
analytics_data = json.loads(analytics_str)

print("Hidden analytics:")
for key, value in analytics_data.items():
    print(f"  {key}: {value}")
```

### 4. Customer Support Systems

```python
import ghostcipher

def customer_support_email():
    """Hide internal tracking data in customer communications."""
    
    # Public customer response
    response = """Dear Customer,

Thank you for contacting us about your recent order. 
We understand your concern and are happy to help resolve 
this issue promptly.

Your order has been processed and will ship within 1-2 
business days. You will receive a tracking number via 
email once the package is dispatched.

We appreciate your patience and business.

Best regards,
Customer Service Team"""

    # Internal tracking information
    internal_data = "TICKET_7834|AGENT_sarah_m|PRIORITY_high|ESCALATED_yes|REFUND_PREAUTH_manager"
    
    # Hide tracking data
    tracked_response = ghostcipher.hide_in_text(response, internal_data)
    
    return tracked_response, len(internal_data)

# Usage
email_with_tracking, tracking_len = customer_support_email()

# Support system extracts tracking data
tracking_data = ghostcipher.reveal_from_text(email_with_tracking, tracking_len)
tracking_fields = tracking_data.split('|')

print("Internal tracking:")
for field in tracking_fields:
    key, value = field.split('_', 1)
    print(f"  {key}: {value}")
```

## Troubleshooting

### Common Issues

#### 1. "Invalid input length; should be even"

```python
# Problem: Trying to decode corrupted or partial invisible text
try:
    ghostcipher.decode("some random text")
except ValueError as e:
    print(f"Error: {e}")

# Solution: Only decode text created by encode()
original = "Hello"
encoded = ghostcipher.encode(original)
decoded = ghostcipher.decode(encoded)  # This works
```

#### 2. "ModuleNotFoundError: No module named 'ghostcipher'"

```bash
# Problem: GhostCipher not installed
# Solution: Install using one of these methods

# Method 1: GUI installer
python3 GUI_Installer.py

# Method 2: Shell installer  
./install.sh

# Method 3: Manual installation
pip install -e .
```

#### 3. Secret extraction fails

```python
# Problem: Wrong secret length or no hidden content
text = "Normal text with no hidden content"
try:
    secret = ghostcipher.reveal_from_text(text, 10)
except ValueError as e:
    print(f"Extraction failed: {e}")

# Solution: Ensure text contains hidden content and use correct length
hidden_text = ghostcipher.hide_in_text("Visible", "secret")
secret = ghostcipher.reveal_from_text(hidden_text, 6)  # "secret" = 6 chars
```

#### 4. Copy/paste doesn't preserve hidden content

```python
# Problem: Some applications strip invisible characters
# Solution: Test your environment and use appropriate formats

def test_copy_paste_preservation():
    """Test if copy/paste preserves hidden content."""
    
    original = "Test message with hidden content"
    secret = "hidden"
    hidden_text = ghostcipher.hide_in_text(original, secret)
    
    print("Original hidden text:")
    print(repr(hidden_text))  # Shows invisible characters as escapes
    
    # Instructions for manual testing
    print("\n1. Copy the text above")
    print("2. Paste it into your target application")  
    print("3. Copy it back and paste below")
    print("4. Check if the length matches:")
    print(f"   Expected length: {len(hidden_text)}")
    
    # Test extraction
    try:
        extracted = ghostcipher.reveal_from_text(hidden_text, len(secret))
        print(f"✓ Extraction successful: {extracted}")
    except Exception as e:
        print(f"✗ Extraction failed: {e}")

test_copy_paste_preservation()
```

### Debugging Tips

1. **Check String Lengths**
```python
# Always verify lengths when debugging
text = "Some text"
encoded = ghostcipher.encode(text)
print(f"Original: {len(text)} chars")
print(f"Encoded: {len(encoded)} chars (should be {len(text) * 2})")
```

2. **Use repr() for Invisible Text**
```python
# Make invisible characters visible for debugging
encoded = ghostcipher.encode("Hello")
print(f"Encoded (repr): {repr(encoded)}")
# Shows: '\u200b\u2061\u200b\u2063...'
```

3. **Test Round-Trip Operations**
```python
# Always test encode/decode cycles
def test_round_trip(text):
    encoded = ghostcipher.encode(text)
    decoded = ghostcipher.decode(encoded)
    success = decoded == text
    print(f"Round trip for '{text}': {success}")
    return success

# Test various inputs
test_cases = ["Hello", "🌟", "café", ""]
for case in test_cases:
    test_round_trip(case)
```

## Advanced Topics

### Custom Encoding Schemes

While GhostCipher uses a fixed set of invisible characters, you can create custom encoding schemes:

```python
import ghostcipher

# Access the internal character mapping
def show_character_mapping():
    """Display the internal character mapping."""
    print("GhostCipher Character Mapping:")
    for i, char in enumerate(ghostcipher.digits):
        print(f"  {i:2d}: U+{ord(char):04X} ({repr(char)})")

show_character_mapping()
```

### Performance Optimization

For high-volume operations:

```python
import ghostcipher
import time

def performance_test():
    """Test encoding/decoding performance."""
    
    # Test data of various sizes
    test_sizes = [100, 1000, 10000, 100000]
    
    for size in test_sizes:
        test_text = "A" * size
        
        # Time encoding
        start = time.time()
        encoded = ghostcipher.encode(test_text)
        encode_time = time.time() - start
        
        # Time decoding
        start = time.time()
        decoded = ghostcipher.decode(encoded)
        decode_time = time.time() - start
        
        print(f"Size: {size:6d} | Encode: {encode_time:.4f}s | Decode: {decode_time:.4f}s")

performance_test()
```

### Integration Patterns

Common integration patterns for applications:

```python
import ghostcipher

class SecureDocumentManager:
    """Document manager with invisible metadata."""
    
    def __init__(self):
        self.metadata_separator = "|META:"
    
    def save_document(self, content, metadata):
        """Save document with invisible metadata."""
        metadata_str = f"AUTHOR:{metadata.get('author')}|VERSION:{metadata.get('version')}|TIMESTAMP:{metadata.get('timestamp')}"
        
        return ghostcipher.hide_in_text(content, metadata_str), len(metadata_str)
    
    def load_document(self, document_with_metadata, metadata_length):
        """Load document and extract metadata."""
        # Extract metadata
        metadata_str = ghostcipher.reveal_from_text(document_with_metadata, metadata_length)
        
        # Parse metadata
        metadata = {}
        for item in metadata_str.split('|'):
            if ':' in item:
                key, value = item.split(':', 1)
                metadata[key.lower()] = value
        
        # Get clean content
        content = document_with_metadata[:-metadata_length*2]
        
        return content, metadata

# Usage
manager = SecureDocumentManager()

# Save document
doc_content = "This is my document content..."
doc_metadata = {"author": "john.doe", "version": "1.0", "timestamp": "2024-01-15"}

saved_doc, meta_len = manager.save_document(doc_content, doc_metadata)

# Load document  
loaded_content, loaded_metadata = manager.load_document(saved_doc, meta_len)

print("Loaded metadata:", loaded_metadata)
```

## Next Steps

Now that you understand GhostCipher thoroughly:

1. **Practice with Examples**: Try the [Basic Usage Examples](../examples/basic_usage.md)
2. **Explore Advanced Techniques**: Check out [Steganography Examples](../examples/steganography.md)
3. **Review Technical Details**: Read the [Architecture Documentation](../technical/architecture.md)
4. **Check API Reference**: See [Complete API Documentation](../api/ghostcipher.md)
5. **Learn Best Practices**: Review [Security Best Practices](best_practices.md)

Remember: GhostCipher is a powerful tool for steganography, but always consider security implications and test thoroughly in your target environment.
