#!/usr/bin/env python3
"""
Script to add WhatsApp social media icon and link to all HTML files.
Replaces the closing of LinkedIn link with WhatsApp link added after.
"""

import re
import os
from pathlib import Path

# Files to update
html_files = [
    'index.html',
    'product.html',
    'collections.html',
    'services.html',
    'productdetails.html',
    'cart.html',
]

# WhatsApp link - using business WhatsApp format
# Format: https://wa.me/[country code][phone number]
# You can customize the phone number here
WHATSAPP_PHONE = "2349000000000"  # Nigeria country code +234
WHATSAPP_LINK = f"https://wa.me/{WHATSAPP_PHONE}"

# WhatsApp SVG Icon (compatible with existing social-link style)
WHATSAPP_SVG = '''<a href="{whatsapp_link}" class="social-link" aria-label="WhatsApp" target="_blank" rel="noopener noreferrer">
                            <svg viewBox="0 0 24 24" fill="currentColor">
                                <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.67-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.076 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421-7.403h-.004c-1.579 0-3.051.487-4.283 1.398l-.308.19-3.19.501.51-3.065.199-.314C2.704 4.9 4.499 2.5 7.07 2.5c1.932 0 3.75.75 5.112 2.107.656.653 1.148 1.432 1.468 2.304-.018.001-.034.001-.051.001-1.734 0-3.374.522-4.74 1.496-.186-.043-.37-.082-.556-.082m10.906-3.88C19.412.499 15.917 0 12.319 0 5.932 0 .549 5.338.549 11.726c0 2.065.505 4.078 1.47 5.868L.687 23.834l6.336-1.959c1.682.921 3.58 1.407 5.512 1.407 6.387 0 11.77-5.338 11.77-11.726 0-3.136-.996-6.066-2.889-8.55z" />
                            </svg>
                        </a>'''

def add_whatsapp_to_social_links(content):
    """Add WhatsApp icon to social links sections"""
    # Pattern to find the last closing </a> in a social-links section
    # We'll search for LinkedIn link and add WhatsApp after it
    
    linkedin_pattern = r'(<a href="#" class="social-link" aria-label="LinkedIn">.*?</a>)(\s*</div>\s*</div>)'
    
    def replace_linkedin(match):
        linkedin_section = match.group(1)
        closing_tags = match.group(2)
        whatsapp_html = WHATSAPP_SVG.format(whatsapp_link=WHATSAPP_LINK)
        return linkedin_section + '\n                        ' + whatsapp_html + closing_tags
    
    new_content = re.sub(linkedin_pattern, replace_linkedin, content, flags=re.DOTALL)
    return new_content

def process_file(filepath):
    """Add WhatsApp link to a file"""
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return False
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        content = add_whatsapp_to_social_links(content)
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Added WhatsApp: {filepath}")
            return True
        else:
            print(f"- No changes: {filepath}")
            return False
    except Exception as e:
        print(f"✗ Error processing {filepath}: {e}")
        return False

def main():
    """Main process"""
    print("Adding WhatsApp social media link")
    print(f"WhatsApp Link: {WHATSAPP_LINK}\n")
    
    updated_count = 0
    for html_file in html_files:
        if process_file(html_file):
            updated_count += 1
    
    print(f"\n✓ Complete! {updated_count} files updated.")
    print(f"\nNote: Please update the WhatsApp phone number in the script:")
    print(f"Current: {WHATSAPP_PHONE}")

if __name__ == "__main__":
    main()
