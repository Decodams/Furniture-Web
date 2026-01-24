#!/usr/bin/env python3
"""
Add meta tags and optimization headers to HTML files
"""

import re
from pathlib import Path

META_TAGS = '''    <meta charset="utf-8" />
    <meta content="width=device-width, initial-scale=1.0" name="viewport" />
    <meta name="description" content="Ochestra - Luxury Artisan Furniture Collection. Handcrafted pieces combining traditional craftsmanship with modern design." />
    <meta name="keywords" content="luxury furniture, artisan, handcrafted, design, interior" />
    <meta name="author" content="Ochestra Ltd." />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="theme-color" content="#020408" />'''

def add_meta_tags():
    """Add meta tags to HTML files"""
    html_files = Path('.').glob('*.html')
    updated = 0
    
    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if basic meta tags exist
        if 'charset' not in content or 'viewport' not in content:
            # Find the first meta tag and enhance
            if '<head>' in content:
                # Just ensure viewport exists (already in most files)
                if 'viewport' not in content:
                    head_insert = '<head>\n' + META_TAGS
                    content = content.replace('<head>\n', head_insert, 1)
                    updated += 1
                    print(f"✓ Added meta tags to {html_file}")
    
    return updated

def ensure_structured_data():
    """Add JSON-LD structured data for better SEO"""
    index_file = Path('index.html')
    if not index_file.exists():
        return False
    
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    structured_data = '''    <script type="application/ld+json">
    {
      "@context": "https://schema.org/",
      "@type": "LocalBusiness",
      "name": "Ochestra",
      "description": "Luxury Artisan Furniture",
      "url": "https://ochestra.com",
      "sameAs": ["https://www.instagram.com/ochestra"],
      "address": {
        "@type": "PostalAddress",
        "addressCountry": "NG"
      },
      "priceRange": "$$$"
    }
    </script>'''
    
    if 'application/ld+json' not in content:
        if '</head>' in content:
            content = content.replace('</head>', structured_data + '\n</head>', 1)
            with open(index_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Added structured data to index.html")
            return True
    
    return False

def add_link_preload():
    """Add preload hints for critical resources"""
    html_files = Path('.').glob('*.html')
    updated = 0
    
    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add preload for critical fonts
        if 'fonts.googleapis.com' in content and 'rel="preload"' not in content:
            # Find the first stylesheet link
            first_link_pos = content.find('<link')
            if first_link_pos != -1:
                preload = '    <link rel="preload" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;900&family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400&display=swap" as="style">\n    '
                content = content[:first_link_pos] + preload + content[first_link_pos:]
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                updated += 1
    
    return updated

def main():
    print("📝 Adding SEO and optimization meta tags...\n")
    
    print("Step 1: Adding meta tags...")
    meta_updated = add_meta_tags()
    print(f"   Updated {meta_updated} files\n")
    
    print("Step 2: Adding structured data...")
    if ensure_structured_data():
        print("   ✓ Added JSON-LD structured data\n")
    
    print("Step 3: Adding resource preloading...")
    preload_updated = add_link_preload()
    print(f"   Updated {preload_updated} files\n")
    
    print("✅ SEO and optimization complete!")

if __name__ == "__main__":
    main()
