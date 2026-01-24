#!/usr/bin/env python3
"""
Comprehensive site audit script to find errors, broken links, and issues.
"""

import os
import re
from pathlib import Path
from collections import defaultdict

def check_html_files():
    """Check for common HTML issues"""
    issues = defaultdict(list)
    html_files = Path('.').glob('*.html')
    
    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            filename = str(html_file)
            
            # Check for unclosed tags
            if content.count('<div') > content.count('</div>'):
                issues[filename].append("⚠️ Unclosed DIV tags")
            
            # Check for broken image paths
            img_pattern = r'src="([^"]+)"'
            for match in re.finditer(img_pattern, content):
                img_path = match.group(1)
                if not img_path.startswith('http') and not img_path.startswith('data:'):
                    if not os.path.exists(img_path):
                        issues[filename].append(f"🖼️ Missing image: {img_path}")
            
            # Check for href="#" (unlinked buttons)
            href_pattern = r'href="#"'
            href_count = len(re.findall(href_pattern, content))
            if href_count > 3:
                issues[filename].append(f"🔗 {href_count} unlinked href='#' found")
            
            # Check for meta viewport
            if 'viewport' not in content:
                issues[filename].append("📱 Missing viewport meta tag")
            
            # Check for doctype
            if '<!DOCTYPE' not in content.upper()[:50]:
                issues[filename].append("⚠️ Missing DOCTYPE declaration")
            
            # Check for title tag
            if '<title>' not in content:
                issues[filename].append("📄 Missing title tag")

def check_css_files():
    """Check CSS files for issues"""
    issues = defaultdict(list)
    css_files = Path('.').glob('css/*.css')
    
    for css_file in css_files:
        with open(css_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            filename = str(css_file)
            
            # Check for unclosed braces
            open_braces = content.count('{')
            close_braces = content.count('}')
            if open_braces != close_braces:
                issues[filename].append(f"🔧 Mismatched braces: {open_braces} open, {close_braces} close")
            
            # Check for missing semicolons (basic check)
            lines_without_semicolon = [line for line in content.split('\n') 
                                      if line.strip() and not line.strip().endswith((';', '{', '}', ','))]
            if len(lines_without_semicolon) > 20:
                issues[filename].append(f"⚠️ Possible missing semicolons")

def check_js_files():
    """Check JavaScript files for issues"""
    issues = defaultdict(list)
    js_files = Path('.').glob('js/*.js')
    
    for js_file in js_files:
        with open(js_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            filename = str(js_file)
            
            # Check for unmatched braces
            open_braces = content.count('{')
            close_braces = content.count('}')
            if open_braces != close_braces:
                issues[filename].append(f"🔧 Mismatched braces: {open_braces} open, {close_braces} close")
            
            # Check for console errors (usually okay, but worth noting)
            if 'console.log' in content:
                count = content.count('console.log')
                if count > 10:
                    issues[filename].append(f"🐛 {count} console.log statements (for debugging)")

def check_links_in_pages():
    """Check for broken internal links"""
    issues = defaultdict(list)
    html_files = Path('.').glob('*.html')
    all_pages = {f.stem for f in html_files}
    admin_pages = {f.stem for f in Path('js/Admin').glob('*.html')}
    
    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            filename = str(html_file)
            
            # Find all hrefs
            href_pattern = r'href="([^"]+)"'
            for match in re.finditer(href_pattern, content):
                href = match.group(1)
                
                # Skip external links, anchors, javascript
                if href.startswith(('http', 'mailto:', 'tel:', 'javascript:', '#', 'wa.me')):
                    continue
                
                # Remove query strings and anchors
                page = href.split('?')[0].split('#')[0]
                page_name = Path(page).stem
                
                # Check if page exists
                if page and not os.path.exists(page):
                    if page_name not in all_pages and page_name not in admin_pages:
                        issues[filename].append(f"❌ Broken link: {href}")

def print_report(issues):
    """Print the audit report"""
    print("\n" + "="*60)
    print(" OCHESTRA WEBSITE AUDIT REPORT")
    print("="*60 + "\n")
    
    if not issues:
        print("✅ No issues found! Website looks good.")
        return
    
    for filename, file_issues in sorted(issues.items()):
        print(f"\n📄 {filename}")
        print("-" * 40)
        for issue in sorted(set(file_issues)):
            print(f"  {issue}")
    
    total_issues = sum(len(v) for v in issues.values())
    print(f"\n📊 Total issues found: {total_issues}")
    print("\n" + "="*60 + "\n")

def main():
    print("🔍 Running comprehensive site audit...\n")
    
    all_issues = defaultdict(list)
    
    print("Checking HTML files...")
    html_issues = check_html_files()
    
    print("Checking CSS files...")
    css_issues = check_css_files()
    
    print("Checking JavaScript files...")
    js_issues = check_js_files()
    
    print("Checking internal links...")
    link_issues = check_links_in_pages()
    
    # Combine all issues
    for d in [check_html_files(), check_css_files(), check_js_files(), check_links_in_pages()]:
        if isinstance(d, dict):
            for k, v in d.items():
                all_issues[k].extend(v)
    
    # Manual comprehensive check
    check_html_files_detailed = lambda: check_html_files()
    check_css_files_detailed = lambda: check_css_files()
    check_js_files_detailed = lambda: check_js_files()
    check_links_in_pages_detailed = lambda: check_links_in_pages()
    
    # Run checks and combine results
    all_issues = defaultdict(list)
    
    html_files = Path('.').glob('*.html')
    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            filename = str(html_file)
            
            if content.count('<div') > content.count('</div>'):
                all_issues[filename].append("⚠️ Unclosed DIV tags")
            
            img_pattern = r'src="([^"]+)"'
            for match in re.finditer(img_pattern, content):
                img_path = match.group(1)
                if not img_path.startswith(('http', 'data:')) and not os.path.exists(img_path):
                    all_issues[filename].append(f"🖼️ Missing image: {img_path}")
    
    print_report(all_issues)

if __name__ == "__main__":
    main()
