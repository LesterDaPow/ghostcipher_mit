# ghostcipher/__init__.py
"""
GhostCipher: Encode/decode text using invisible Unicode characters.
Each character is encoded as exactly 2 invisible characters.
"""

# Base-16 invisible Unicode digits
digits = [
    "\u200B","\u200C","\u200D","\u2060",
    "\u2061","\u2062","\u2063","\u2064",
    "\u206A","\u206B","\u206C","\u206D",
    "\u206E","\u206F","\uFEFF","\uFFF9"
]

def encode(text: str) -> str:
    """Encode a string into invisible characters."""
    result = ""
    for char in text:
        n = ord(char)
        high = n // 16
        low = n % 16
        result += digits[high] + digits[low]
    return result

def decode(invisible: str) -> str:
    """Decode a string of invisible characters back into normal text."""
    if len(invisible) % 2 != 0:
        raise ValueError("Invalid input length; should be even.")
    
    result = ""
    for i in range(0, len(invisible), 2):
        high = digits.index(invisible[i])
        low = digits.index(invisible[i+1])
        result += chr(high * 16 + low)
    return result

def hide_in_text(text: str, secret: str) -> str:
    """Hide a secret inside visible text using invisible characters."""
    return text + encode(secret)

def reveal_from_text(text: str, secret_length: int) -> str:
    """Reveal an invisible secret from text, given its length in characters."""
    invisible_part = text[-secret_length*2:]
    return decode(invisible_part)
