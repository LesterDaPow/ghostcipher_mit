# Steganography Examples

Advanced examples showing how to hide information in various types of text content.

## Email Communication

### Example 1: Secret Messages in Professional Email

```python
import ghostcipher

def create_business_email_with_secret():
    """Hide confidential information in a business email."""
    
    email_body = """Subject: Q4 Budget Review Meeting
    
Dear Team,

I hope this email finds you well. I wanted to schedule our Q4 budget review meeting for next Wednesday at 2:00 PM in the main conference room.

Please bring your departmental reports and be prepared to discuss:
- Current spending vs. budget allocations
- Proposed adjustments for Q1 2024
- Resource requirements for upcoming projects

Looking forward to a productive discussion.

Best regards,
Sarah Johnson
Finance Director"""

    # Hide sensitive information that only certain recipients should see
    confidential_note = "Board meeting moved to Friday - merger talks confidential"
    
    email_with_secret = ghostcipher.hide_in_text(email_body, confidential_note)
    
    print("=== Business Email (appears normal) ===")
    print(email_with_secret)
    print()
    
    # Recipients with the secret key can extract the hidden message
    print("=== Hidden Message Extraction ===")
    extracted = ghostcipher.reveal_from_text(email_with_secret, len(confidential_note))
    print(f"Confidential message: {extracted}")
    
    return email_with_secret

# Run the example
business_email = create_business_email_with_secret()
```

### Example 2: Layered Secrets

```python
import ghostcipher

def create_layered_secrets():
    """Hide multiple pieces of information at different levels."""
    
    public_message = "The meeting is scheduled for tomorrow at 3 PM in Room B."
    
    # First secret layer
    level1_secret = "Bring the Johnson file"
    text_with_level1 = ghostcipher.hide_in_text(public_message, level1_secret)
    
    # Second secret layer (contains the first)
    level2_secret = "Password: ALPHA7799"
    text_with_both = ghostcipher.hide_in_text(text_with_level1, level2_secret)
    
    print("=== Layered Secrets Demo ===")
    print(f"Public message: {public_message}")
    print(f"Text appears as: {text_with_both}")
    print()
    
    # Extract secrets in reverse order (most recent first)
    print("Extracting secrets:")
    
    # Extract level 2 secret
    secret_2 = ghostcipher.reveal_from_text(text_with_both, len(level2_secret))
    print(f"Level 2 secret: {secret_2}")
    
    # Remove level 2 to get text with only level 1
    text_without_level2 = text_with_both[:-len(level2_secret)*2]
    secret_1 = ghostcipher.reveal_from_text(text_without_level2, len(level1_secret))
    print(f"Level 1 secret: {secret_1}")
    
    return text_with_both

# Run the example
layered_message = create_layered_secrets()
```

## Document Security

### Example 3: Document Version Control

```python
import ghostcipher
from datetime import datetime

def add_version_tracking():
    """Add invisible version tracking to documents."""
    
    document = """CONFIDENTIAL REPORT
    
Market Analysis: Consumer Electronics Q3 2024

Executive Summary:
Our analysis shows a 15% growth in the consumer electronics sector, 
primarily driven by smartphone and wearable device sales. Key findings 
include increased demand for sustainable products and premium features.

Recommendations:
1. Increase investment in sustainable product lines
2. Expand premium feature offerings  
3. Develop strategic partnerships with eco-friendly suppliers

Market Outlook:
The trend toward sustainable electronics is expected to continue 
through 2025, with projected growth rates of 12-18% annually."""

    # Create version metadata
    version_info = {
        "version": "2.1",
        "author": "M.Rodriguez",
        "date": "2024-01-15",
        "classification": "CONFIDENTIAL",
        "review_by": "2024-02-01"
    }
    
    # Encode version info as a single string
    version_string = f"v{version_info['version']}|{version_info['author']}|{version_info['date']}|{version_info['classification']}|{version_info['review_by']}"
    
    # Hide version info in document
    versioned_document = ghostcipher.hide_in_text(document, version_string)
    
    print("=== Document with Hidden Version Control ===")
    print(versioned_document)
    print()
    
    # Extract and parse version info
    extracted_version = ghostcipher.reveal_from_text(versioned_document, len(version_string))
    version_parts = extracted_version.split('|')
    
    print("=== Hidden Version Information ===")
    print(f"Version: {version_parts[0]}")
    print(f"Author: {version_parts[1]}")
    print(f"Date: {version_parts[2]}")
    print(f"Classification: {version_parts[3]}")
    print(f"Review By: {version_parts[4]}")
    
    return versioned_document

# Run the example
versioned_doc = add_version_tracking()
```

### Example 4: Legal Document Authentication

```python
import ghostcipher
import hashlib

def authenticate_legal_document():
    """Add invisible authentication to legal documents."""
    
    legal_text = """MUTUAL NON-DISCLOSURE AGREEMENT

This Mutual Non-Disclosure Agreement ("Agreement") is entered into on January 15, 2024, between TechCorp Inc., a Delaware corporation ("Company"), and InnovateLab LLC, a California limited liability company ("Recipient").

1. CONFIDENTIAL INFORMATION
For purposes of this Agreement, "Confidential Information" shall mean any and all technical data, trade secrets, know-how, research, product plans, products, services, customers, customer lists, markets, software, developments, inventions, processes, formulas, technology, designs, drawings, engineering, hardware configuration information, marketing, finances, or other business information.

2. NON-DISCLOSURE OBLIGATIONS
Recipient agrees to hold and maintain the Confidential Information in strict confidence and not to disclose such information to any third parties without the prior written consent of Company.

IN WITNESS WHEREOF, the parties have executed this Agreement as of the date first written above.

TechCorp Inc.                    InnovateLab LLC
_________________              _________________
John Smith, CEO                 Sarah Wilson, CTO"""

    # Create document hash for integrity verification
    document_hash = hashlib.md5(legal_text.encode()).hexdigest()[:16]
    
    # Create authentication metadata
    auth_data = f"HASH:{document_hash}|NOTARY:JM2024|TIME:20240115-1430"
    
    # Hide authentication data
    authenticated_doc = ghostcipher.hide_in_text(legal_text, auth_data)
    
    print("=== Legal Document (with hidden authentication) ===")
    print(authenticated_doc)
    print()
    
    # Verify authenticity
    extracted_auth = ghostcipher.reveal_from_text(authenticated_doc, len(auth_data))
    auth_parts = extracted_auth.split('|')
    
    print("=== Authentication Verification ===")
    for part in auth_parts:
        key, value = part.split(':')
        print(f"{key}: {value}")
    
    # Verify document integrity
    stored_hash = auth_parts[0].split(':')[1]
    current_hash = hashlib.md5(legal_text.encode()).hexdigest()[:16]
    
    if stored_hash == current_hash:
        print("✓ Document integrity verified")
    else:
        print("✗ Document may have been tampered with")
    
    return authenticated_doc

# Run the example
auth_document = authenticate_legal_document()
```

## Social Media & Web Content

### Example 5: Social Media Metadata

```python
import ghostcipher
import json

def social_media_with_metadata():
    """Hide metadata in social media posts."""
    
    # Public social media post
    post_content = """Just finished an amazing hiking trip in the mountains! 🏔️ 
The views were absolutely breathtaking and the weather was perfect. 
Can't wait to share more photos from this adventure. 
#hiking #mountains #adventure #nature #photography"""

    # Hidden metadata for analytics/tracking
    metadata = {
        "campaign": "outdoor-gear-Q1",
        "target_audience": "hiking-enthusiasts", 
        "post_id": "POST_7834",
        "scheduled_time": "2024-01-15T14:30:00Z",
        "hashtag_performance_tracking": "enabled"
    }
    
    # Convert metadata to string
    metadata_string = json.dumps(metadata, separators=(',', ':'))
    
    # Hide metadata in post
    post_with_metadata = ghostcipher.hide_in_text(post_content, metadata_string)
    
    print("=== Social Media Post (public view) ===")
    print(post_with_metadata)
    print()
    
    # Extract hidden metadata for analytics
    extracted_metadata_string = ghostcipher.reveal_from_text(
        post_with_metadata, 
        len(metadata_string)
    )
    extracted_metadata = json.loads(extracted_metadata_string)
    
    print("=== Hidden Analytics Metadata ===")
    for key, value in extracted_metadata.items():
        print(f"{key}: {value}")
    
    return post_with_metadata

# Run the example
social_post = social_media_with_metadata()
```

### Example 6: Website Content Management

```python
import ghostcipher

def cms_content_tracking():
    """Hide content management data in web pages."""
    
    webpage_content = """<h1>Welcome to Our Technology Blog</h1>

<p>Stay up to date with the latest trends in artificial intelligence, 
machine learning, and software development. Our expert team brings you 
insights from industry leaders and cutting-edge research.</p>

<h2>Featured Articles</h2>
<ul>
    <li>The Future of AI in Healthcare</li>
    <li>Sustainable Software Development Practices</li>
    <li>Emerging Trends in Cloud Computing</li>
</ul>

<p>Subscribe to our newsletter to never miss an update!</p>"""

    # CMS tracking information
    cms_data = "PAGE_ID:7823|AUTHOR:j.doe|MODIFIED:2024-01-15T10:30:00|STATUS:published|SEO_SCORE:87"
    
    # Hide CMS data in content
    tracked_content = ghostcipher.hide_in_text(webpage_content, cms_data)
    
    print("=== Web Page Content ===")
    print(tracked_content)
    print()
    
    # Extract CMS data for management system
    extracted_cms = ghostcipher.reveal_from_text(tracked_content, len(cms_data))
    cms_fields = extracted_cms.split('|')
    
    print("=== Hidden CMS Data ===")
    for field in cms_fields:
        key, value = field.split(':', 1)
        print(f"{key.replace('_', ' ').title()}: {value}")
    
    return tracked_content

# Run the example
cms_content = cms_content_tracking()
```

## Messaging & Communication

### Example 7: Secure Group Communication

```python
import ghostcipher

def secure_group_messaging():
    """Create a secure group messaging system with hidden instructions."""
    
    # Public group message
    group_message = """Team Update - January 15, 2024

Hi everyone,

Great work on last week's project deliverables! The client feedback 
has been very positive and we're on track for the final presentation 
next month.

This week's priorities:
- Complete testing phase by Wednesday
- Prepare demo materials
- Schedule client review meeting

Have a great week!
- Project Team Lead"""

    # Hidden instructions for specific team members
    hidden_instructions = {
        "security_team": "Run penetration test on staging server - Priority HIGH",
        "qa_team": "Check edge cases in payment module - Due Friday",
        "dev_team": "Database migration scheduled for Saturday 2 AM"
    }
    
    # Create different versions for different recipients
    messages_by_role = {}
    
    for role, instruction in hidden_instructions.items():
        role_message = ghostcipher.hide_in_text(group_message, instruction)
        messages_by_role[role] = role_message
        
        print(f"=== Message for {role.replace('_', ' ').title()} ===")
        print("Public content appears the same, but contains hidden instructions")
        print(f"Hidden instruction length: {len(instruction)} characters")
        print()
    
    # Demonstrate extraction for one role
    print("=== Extracting Hidden Instructions (Security Team) ===")
    security_message = messages_by_role["security_team"]
    hidden_instruction = ghostcipher.reveal_from_text(
        security_message, 
        len(hidden_instructions["security_team"])
    )
    print(f"Security team instruction: {hidden_instruction}")
    
    return messages_by_role

# Run the example
group_messages = secure_group_messaging()
```

### Example 8: Customer Support Ticketing

```python
import ghostcipher

def customer_support_system():
    """Hide internal tracking data in customer communications."""
    
    # Public customer response
    customer_email = """Dear Mr. Johnson,

Thank you for contacting our customer support team regarding your recent 
order #12345. We understand your concern about the delivery delay and 
sincerely apologize for any inconvenience this may have caused.

Our shipping department has confirmed that your order was processed and 
shipped yesterday. You should receive a tracking number within 2-4 hours 
via email. The estimated delivery time is 2-3 business days.

As a gesture of goodwill, we're including expedited shipping at no 
additional cost. We value your business and want to ensure you have 
a positive experience with our company.

If you have any other questions or concerns, please don't hesitate 
to reach out to us.

Best regards,
Customer Support Team
TechGear Solutions"""

    # Internal tracking data
    internal_data = "TICKET:T-7834|AGENT:sarah.m|PRIORITY:high|ESCALATED:yes|REFUND_AUTH:manager_req|FOLLOW_UP:2days"
    
    # Hide internal data in customer email
    tracked_email = ghostcipher.hide_in_text(customer_email, internal_data)
    
    print("=== Customer Email (public view) ===")
    print(tracked_email)
    print()
    
    # Extract internal tracking for support system
    extracted_internal = ghostcipher.reveal_from_text(tracked_email, len(internal_data))
    tracking_fields = extracted_internal.split('|')
    
    print("=== Internal Support Tracking Data ===")
    for field in tracking_fields:
        key, value = field.split(':', 1)
        print(f"{key.replace('_', ' ').title()}: {value}")
    
    return tracked_email

# Run the example
support_email = customer_support_system()
```

## Advanced Techniques

### Example 9: Multi-Format Steganography

```python
import ghostcipher
import base64

def multi_format_steganography():
    """Combine different encoding methods with steganography."""
    
    # Base document
    document = """TECHNICAL SPECIFICATION
    
System Requirements:
- Python 3.8 or higher
- 4GB RAM minimum
- 10GB available storage
- Network connectivity required

Installation Instructions:
1. Download the installation package
2. Run the installer with administrator privileges
3. Follow the setup wizard prompts
4. Restart the system when prompted

For additional support, contact our technical team."""

    # Secret data in multiple formats
    secret_config = {
        "api_key": "sk_live_abc123def456",
        "database_url": "postgresql://user:pass@localhost:5432/db",
        "debug_mode": True,
        "max_connections": 100
    }
    
    # Encode secret as JSON, then base64, then hide with GhostCipher
    import json
    config_json = json.dumps(secret_config)
    config_b64 = base64.b64encode(config_json.encode()).decode()
    
    # Hide the base64-encoded config
    document_with_secret = ghostcipher.hide_in_text(document, config_b64)
    
    print("=== Document (appears normal) ===")
    print(document_with_secret)
    print()
    
    # Extract and decode the secret
    print("=== Multi-Stage Secret Extraction ===")
    
    # Step 1: Extract hidden base64 string
    extracted_b64 = ghostcipher.reveal_from_text(document_with_secret, len(config_b64))
    print(f"Step 1 - Extracted base64: {extracted_b64[:50]}...")
    
    # Step 2: Decode base64
    decoded_json = base64.b64decode(extracted_b64).decode()
    print(f"Step 2 - Decoded JSON: {decoded_json}")
    
    # Step 3: Parse JSON
    final_config = json.loads(decoded_json)
    print("Step 3 - Final configuration:")
    for key, value in final_config.items():
        # Mask sensitive values
        if 'key' in key.lower() or 'password' in key.lower() or 'url' in key.lower():
            masked_value = str(value)[:8] + "***" if len(str(value)) > 8 else "***"
            print(f"  {key}: {masked_value}")
        else:
            print(f"  {key}: {value}")
    
    return document_with_secret

# Run the example
multi_format_doc = multi_format_steganography()
```

### Example 10: Steganography with Error Correction

```python
import ghostcipher

def error_corrected_steganography():
    """Add redundancy to hidden messages for error correction."""
    
    # Original message
    message = """BOARD MEETING AGENDA
    
Date: January 20, 2024
Time: 10:00 AM - 12:00 PM
Location: Executive Conference Room

1. Review of Q4 Financial Results
2. Strategic Planning for 2024
3. New Product Line Discussion
4. Budget Allocation for Next Quarter
5. Other Business

Please confirm your attendance by January 18th."""

    # Critical secret that needs error correction
    critical_secret = "MERGER_TALKS_FRIDAY_CONFIDENTIAL"
    
    # Create redundant copies with checksums
    import hashlib
    secret_hash = hashlib.md5(critical_secret.encode()).hexdigest()[:8]
    
    # Triple redundancy with hash verification
    redundant_secret = f"{critical_secret}|{secret_hash}|{critical_secret}|{secret_hash}|{critical_secret}|{secret_hash}"
    
    # Hide the redundant secret
    protected_message = ghostcipher.hide_in_text(message, redundant_secret)
    
    print("=== Message with Error-Corrected Hidden Content ===")
    print(protected_message)
    print()
    
    # Extract and verify with error correction
    print("=== Error Correction Verification ===")
    
    extracted_redundant = ghostcipher.reveal_from_text(protected_message, len(redundant_secret))
    parts = extracted_redundant.split('|')
    
    # Extract the three copies and their hashes
    copy1, hash1 = parts[0], parts[1]
    copy2, hash2 = parts[2], parts[3]
    copy3, hash3 = parts[4], parts[5]
    
    # Verify each copy
    copies = [copy1, copy2, copy3]
    hashes = [hash1, hash2, hash3]
    valid_copies = []
    
    for i, (copy, stored_hash) in enumerate(zip(copies, hashes)):
        computed_hash = hashlib.md5(copy.encode()).hexdigest()[:8]
        if computed_hash == stored_hash:
            valid_copies.append(copy)
            print(f"Copy {i+1}: ✓ Valid")
        else:
            print(f"Copy {i+1}: ✗ Corrupted")
    
    # Use majority voting for final result
    if len(valid_copies) >= 2:
        # Check if valid copies match
        if all(copy == valid_copies[0] for copy in valid_copies):
            final_secret = valid_copies[0]
            print(f"✓ Secret successfully recovered: {final_secret}")
        else:
            print("✗ Valid copies don't match - possible corruption")
    else:
        print("✗ Too many copies corrupted - cannot recover secret")
    
    return protected_message

# Run the example
error_corrected_doc = error_corrected_steganography()
```

## Practical Applications

### Tips for Real-World Steganography

1. **Keep secrets short**: Longer hidden messages are more detectable
2. **Use natural text**: Hidden content should blend with normal communication
3. **Consider the audience**: Only hide what recipients need to know
4. **Plan extraction**: Always know how you'll retrieve the hidden information
5. **Test thoroughly**: Verify hidden content survives copy/paste operations
6. **Layer security**: Combine with encryption for sensitive information
7. **Document lengths**: Keep track of secret lengths for reliable extraction

### Common Use Cases

- **Corporate communications**: Hide internal tracking information
- **Document management**: Invisible version control and metadata
- **Content marketing**: Track campaign performance and audience targeting  
- **Legal documents**: Add authentication and integrity verification
- **Customer support**: Internal ticketing data alongside public responses
- **Social media**: Analytics metadata and audience insights
- **Web development**: CMS tracking and content management data

## Next Steps

1. **Review [Best Practices](../guides/best_practices.md)** for secure usage
2. **Check [Advanced Examples](advanced.md)** for complex scenarios
3. **Read [Technical Documentation](../technical/architecture.md)** for implementation details
4. **Explore [API Reference](../api/ghostcipher.md)** for complete function documentation
