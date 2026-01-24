#!/usr/bin/env python3
"""
Script to convert all USD prices to Nigerian Naira throughout the website.
Conversion rate: 1 USD = 416 NGN (approximate)
"""

import re
import os
from pathlib import Path

# Conversion rate
USD_TO_NGN = 416

# Files to process
html_files = [
    'index.html',
    'product.html',
    'collections.html',
    'services.html',
    'productdetails.html',
    'cart.html',
    'aboutus.html',
    'contact.html',
    'project.html',
    'js/Admin/admindashboard.html'
]

def convert_price(usd_match):
    """Convert a single USD price to NGN"""
    # Extract the numeric value (handle $1,200 or $1200 format)
    price_str = usd_match.group(1).replace(',', '')
    try:
        usd_amount = float(price_str)
        ngn_amount = int(usd_amount * USD_TO_NGN)
        # Format with commas
        formatted_ngn = f"₦{ngn_amount:,}"
        return formatted_ngn
    except ValueError:
        return usd_match.group(0)  # Return original if conversion fails

def convert_file(filepath):
    """Convert all prices in a single file"""
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return False
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Pattern to match: $X,XXX or $XXXX or $X,XXX.XX
        pattern = r'\$([0-9,]+(?:\.[0-9]{2})?)'
        content = re.sub(pattern, convert_price, content)
        
        # Also handle "From $X,XXX" pattern
        pattern2 = r'From \$([0-9,]+(?:\.[0-9]{2})?)'
        content = re.sub(pattern2, lambda m: f'From {convert_price(m)}', content)
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Converted: {filepath}")
            return True
        else:
            print(f"- No changes: {filepath}")
            return False
    except Exception as e:
        print(f"✗ Error processing {filepath}: {e}")
        return False

def main():
    """Main conversion process"""
    print("Starting currency conversion: USD → Nigerian Naira")
    print(f"Conversion rate: 1 USD = {USD_TO_NGN} NGN\n")
    
    converted_count = 0
    for html_file in html_files:
        if convert_file(html_file):
            converted_count += 1
    
    print(f"\n✓ Conversion complete! {converted_count} files updated.")

if __name__ == "__main__":
    main()
