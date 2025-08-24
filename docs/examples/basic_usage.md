# Basic Usage Examples

This guide provides simple, practical examples to get you started with GhostCipher.

## Quick Start

### Your First Encoding

```python
import ghostcipher

# Encode a simple message
message = "Hello, World!"
encoded = ghostcipher.encode(message)

print(f"Original: {message}")
print(f"Encoded length: {len(encoded)}")  # 26 characters (13 × 2)
print(f"Encoded: [{encoded}]")           # Appears empty but has content

# Decode it back
decoded = ghostcipher.decode(encoded)
print(f"Decoded: {decoded}")             # "Hello, World!"
```

### Basic Steganography

```python
import ghostcipher

# Hide a secret in visible text
visible_text = "This is a public message that everyone can see."
secret = "classified information"

# Combine visible and hidden text
hidden_text = ghostcipher.hide_in_text(visible_text, secret)

print("What people see:")
print(hidden_text)  # Looks like: "This is a public message that everyone can see."

print(f"\nActual length: {len(hidden_text)}")  # 46 + 44 = 90 characters
print(f"Original length: {len(visible_text)}")  # 46 characters

# Extract the secret (you need to know its length)
revealed_secret = ghostcipher.reveal_from_text(hidden_text, len(secret))
print(f"\nHidden message: {revealed_secret}")  # "classified information"
```

## Step-by-Step Examples

### Example 1: Simple Text Encoding

```python
import ghostcipher

def demonstrate_encoding():
    """Show basic encoding and decoding."""
    
    # Test with different types of text
    test_messages = [
        "Hello",
        "Python is awesome!",
        "Numbers: 123456",
        "Symbols: @#$%^&*()",
        "Unicode: 🌟 café naïve résumé"
    ]
    
    print("=== Encoding/Decoding Demo ===")
    for message in test_messages:
        # Encode the message
        encoded = ghostcipher.encode(message)
        
        # Decode it back
        decoded = ghostcipher.decode(encoded)
        
        # Verify the round-trip worked
        success = decoded == message
        
        print(f"Original: {message}")
        print(f"Encoded length: {len(encoded)} chars")
        print(f"Round-trip success: {success}")
        print(f"Decoded: {decoded}")
        print("-" * 40)

# Run the demonstration
demonstrate_encoding()
```

### Example 2: Steganography Basics

```python
import ghostcipher

def hide_contact_info():
    """Hide contact information in an email signature."""
    
    # Public email signature
    signature = """Best regards,
John Smith
Marketing Manager
Acme Corp"""
    
    # Secret contact info
    secret_info = "Direct line: 555-0123"
    
    # Hide the secret info in the signature
    signature_with_secret = ghostcipher.hide_in_text(signature, secret_info)
    
    print("Email signature (looks normal):")
    print(signature_with_secret)
    print()
    
    print(f"Visible length: {len(signature)}")
    print(f"Total length: {len(signature_with_secret)}")
    print(f"Hidden chars: {len(signature_with_secret) - len(signature)}")
    print()
    
    # Later, extract the hidden info
    extracted_info = ghostcipher.reveal_from_text(
        signature_with_secret, 
        len(secret_info)
    )
    
    print(f"Hidden message: {extracted_info}")
    
    return signature_with_secret

# Run the example
hidden_signature = hide_contact_info()
```

### Example 3: Document Watermarking

```python
import ghostcipher

def watermark_document():
    """Add invisible watermark to a document."""
    
    document = """PROJECT PROPOSAL
    
Subject: New Marketing Initiative
Date: 2024-01-15
Status: CONFIDENTIAL

Executive Summary:
This document outlines our new marketing strategy for Q2 2024.
The proposed budget is $50,000 and we expect a 25% increase in leads.

Key Objectives:
1. Increase brand awareness
2. Generate qualified leads  
3. Improve customer engagement

Next Steps:
- Review with legal team
- Present to board of directors
- Begin implementation"""

    # Add invisible watermark
    watermark = "INTERNAL-DRAFT-v1.2-JS-2024"
    watermarked = ghostcipher.hide_in_text(document, watermark)
    
    print("Document with invisible watermark:")
    print(watermarked)
    print()
    print(f"Original size: {len(document)} characters")
    print(f"Watermarked size: {len(watermarked)} characters")
    print(f"Watermark size: {len(watermark)} characters")
    
    # Verify watermark
    extracted_watermark = ghostcipher.reveal_from_text(watermarked, len(watermark))
    print(f"Extracted watermark: {extracted_watermark}")
    
    return watermarked

# Run the example
watermarked_doc = watermark_document()
```

## Interactive Examples

### Example 4: User Input Demo

```python
import ghostcipher

def interactive_demo():
    """Interactive demonstration allowing user input."""
    
    print("=== GhostCipher Interactive Demo ===")
    print("Choose an option:")
    print("1. Encode a message")
    print("2. Decode a message")
    print("3. Hide text in a message")
    print("4. Reveal hidden text")
    
    choice = input("Enter your choice (1-4): ").strip()
    
    if choice == "1":
        message = input("Enter text to encode: ")
        encoded = ghostcipher.encode(message)
        print(f"\nEncoded message (invisible): [{encoded}]")
        print(f"Length: {len(encoded)} characters")
        
    elif choice == "2":
        print("Note: You need invisible characters from a previous encoding.")
        print("For demo, I'll encode 'demo' and then decode it:")
        demo_encoded = ghostcipher.encode("demo")
        decoded = ghostcipher.decode(demo_encoded)
        print(f"Demo encoded: [{demo_encoded}]")
        print(f"Demo decoded: {decoded}")
        
    elif choice == "3":
        visible = input("Enter visible text: ")
        secret = input("Enter secret to hide: ")
        hidden = ghostcipher.hide_in_text(visible, secret)
        print(f"\nText with hidden message:")
        print(hidden)
        print(f"\n(Remember: secret length is {len(secret)})")
        
    elif choice == "4":
        print("For demo, hiding 'secret' in 'Hello World':")
        demo_hidden = ghostcipher.hide_in_text("Hello World", "secret")
        revealed = ghostcipher.reveal_from_text(demo_hidden, 6)  # "secret" is 6 chars
        print(f"Hidden text: [{demo_hidden}]")
        print(f"Revealed secret: {revealed}")
        
    else:
        print("Invalid choice!")

# Run interactive demo
# interactive_demo()  # Uncomment to run interactively
```

### Example 5: Validation and Error Handling

```python
import ghostcipher

def demonstrate_error_handling():
    """Show proper error handling techniques."""
    
    print("=== Error Handling Examples ===\n")
    
    # Example 1: Decoding invalid input
    print("1. Decoding invalid input:")
    try:
        # This will fail because "hello" contains regular characters
        result = ghostcipher.decode("hello")
    except ValueError as e:
        print(f"   Expected error: {e}")
    
    # Example 2: Decoding odd-length input
    print("\n2. Decoding odd-length input:")
    try:
        # Encode something, then remove one character
        encoded = ghostcipher.encode("test")
        invalid_encoded = encoded[:-1]  # Remove last character
        result = ghostcipher.decode(invalid_encoded)
    except ValueError as e:
        print(f"   Expected error: {e}")
    
    # Example 3: Revealing from text without enough hidden chars
    print("\n3. Revealing from insufficient hidden text:")
    try:
        short_text = "Hello"  # Only 5 visible chars, no hidden content
        result = ghostcipher.reveal_from_text(short_text, 10)  # Asking for 10 chars
    except ValueError as e:
        print(f"   Expected error: {e}")
    
    # Example 4: Safe encoding/decoding function
    print("\n4. Safe encoding/decoding wrapper:")
    
    def safe_round_trip(text):
        """Safely encode and decode text with error handling."""
        try:
            encoded = ghostcipher.encode(text)
            decoded = ghostcipher.decode(encoded)
            success = decoded == text
            return success, decoded
        except Exception as e:
            return False, f"Error: {e}"
    
    # Test the safe function
    test_cases = ["Hello", "🌟", "", "Normal text"]
    for test in test_cases:
        success, result = safe_round_trip(test)
        print(f"   '{test}' -> Success: {success}, Result: '{result}'")

# Run the demonstration
demonstrate_error_handling()
```

## Utility Functions

### Example 6: Helper Functions

```python
import ghostcipher

def create_utility_functions():
    """Create useful utility functions for common tasks."""
    
    def is_text_hidden(text, min_hidden_length=1):
        """Check if text likely contains hidden content."""
        # Count potential invisible characters at the end
        invisible_chars = 0
        for char in reversed(text):
            if char in ''.join(ghostcipher.digits):  # Check against invisible chars
                invisible_chars += 1
            else:
                break
        
        return invisible_chars >= min_hidden_length * 2
    
    def get_hidden_length(text):
        """Estimate the length of hidden content in text."""
        invisible_count = 0
        for char in reversed(text):
            if char in ''.join(ghostcipher.digits):
                invisible_count += 1
            else:
                break
        return invisible_count // 2  # Each character needs 2 invisible chars
    
    def safe_hide_and_verify(visible, secret):
        """Safely hide text and verify it can be extracted."""
        try:
            hidden = ghostcipher.hide_in_text(visible, secret)
            # Verify by extracting
            extracted = ghostcipher.reveal_from_text(hidden, len(secret))
            if extracted == secret:
                return hidden
            else:
                raise ValueError("Verification failed")
        except Exception as e:
            print(f"Error in safe_hide_and_verify: {e}")
            return None
    
    def analyze_text(text):
        """Analyze text for hidden content."""
        print(f"Text: '{text[:50]}{'...' if len(text) > 50 else ''}'")
        print(f"Total length: {len(text)}")
        
        if is_text_hidden(text):
            estimated_hidden = get_hidden_length(text)
            print(f"Likely contains hidden text: {estimated_hidden} characters")
        else:
            print("No hidden content detected")
        print()
    
    # Test the utility functions
    print("=== Utility Functions Demo ===\n")
    
    # Test with normal text
    analyze_text("This is normal text with no hidden content.")
    
    # Test with hidden content
    hidden_text = ghostcipher.hide_in_text("Visible message", "hidden")
    analyze_text(hidden_text)
    
    # Test safe hiding
    result = safe_hide_and_verify("Public info", "private")
    if result:
        print("Safe hiding successful!")
        analyze_text(result)

# Run the utility demo
create_utility_functions()
```

## Command Line Usage

### Example 7: Command Line Interface Simulation

```python
import ghostcipher
import sys

def cli_simulator():
    """Simulate command-line usage patterns."""
    
    # Simulate command line arguments
    commands = [
        ["encode", "Hello World"],
        ["decode", ghostcipher.encode("Hello World")],
        ["hide", "Public message", "secret"],
        ["reveal", ghostcipher.hide_in_text("Public message", "secret"), "6"]
    ]
    
    print("=== Command Line Usage Simulation ===\n")
    
    for i, cmd in enumerate(commands, 1):
        print(f"Command {i}: {' '.join(cmd[:2])}")
        
        if cmd[0] == "encode":
            text = cmd[1]
            result = ghostcipher.encode(text)
            print(f"Input: {text}")
            print(f"Output: [{result}] (length: {len(result)})")
            
        elif cmd[0] == "decode":
            encoded = cmd[1]
            result = ghostcipher.decode(encoded)
            print(f"Input: (invisible text)")
            print(f"Output: {result}")
            
        elif cmd[0] == "hide":
            visible, secret = cmd[1], cmd[2]
            result = ghostcipher.hide_in_text(visible, secret)
            print(f"Visible: {visible}")
            print(f"Secret: {secret}")
            print(f"Output: {result}")
            
        elif cmd[0] == "reveal":
            hidden, length = cmd[1], int(cmd[2])
            result = ghostcipher.reveal_from_text(hidden, length)
            print(f"Input: (text with hidden content)")
            print(f"Length: {length}")
            print(f"Output: {result}")
        
        print("-" * 50)

# Run the CLI simulation
cli_simulator()
```

## Next Steps

After trying these basic examples:

1. **Explore [Steganography Examples](steganography.md)** for advanced hiding techniques
2. **Read the [User Guide](../guides/user_guide.md)** for comprehensive usage information
3. **Check [Advanced Examples](advanced.md)** for complex use cases
4. **Review [Best Practices](../guides/best_practices.md)** for optimal usage

## Tips for Beginners

1. **Always verify**: Test encoding/decoding immediately to catch errors
2. **Remember lengths**: You must know the exact secret length to extract it
3. **Test with different text**: Try Unicode characters, symbols, and various lengths
4. **Handle errors**: Always use try/except blocks for robust applications
5. **Start simple**: Begin with basic encoding before attempting steganography
