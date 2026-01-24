#!/usr/bin/env python3
"""
Fix image paths and other issues in HTML files
"""

import re
import os
from pathlib import Path

def fix_image_paths():
    """Fix leading slashes in image paths"""
    html_files = Path('.').glob('*.html')
    fixed_count = 0
    
    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace /Image/ with Image/
        new_content = content.replace('src="/Image/', 'src="Image/')
        new_content = new_content.replace('src=\'/Image/', 'src=\'Image/')
        new_content = new_content.replace('background-image: url(\'/Image/', 'background-image: url(\'Image/')
        new_content = new_content.replace('background-image: url("/Image/', 'background-image: url("Image/')
        
        if new_content != content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✓ Fixed image paths in: {html_file}")
            fixed_count += 1
    
    return fixed_count

def fix_project_html():
    """Fix unclosed divs in project.html"""
    project_file = Path('project.html')
    if not project_file.exists():
        print("project.html not found")
        return False
    
    with open(project_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Count divs
    open_count = content.count('<div')
    close_count = content.count('</div>')
    
    if open_count > close_count:
        diff = open_count - close_count
        # Add missing closing divs at the end of main/body
        if '</main>' in content:
            for _ in range(diff):
                content = content.replace('</main>', '</div>\n</main>', 1)
        
        with open(project_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Fixed unclosed DIVs in project.html (added {diff} closing tags)")
        return True
    
    return False

def main():
    print("🔧 Fixing HTML issues...\n")
    
    fixed = fix_image_paths()
    print(f"   Fixed image paths in {fixed} files\n")
    
    if fix_project_html():
        print("\n✓ All issues fixed!")
    else:
        print("   project.html: No DIV fixes needed")
    
    print("\n✓ HTML file audit complete!")

if __name__ == "__main__":
    main()
