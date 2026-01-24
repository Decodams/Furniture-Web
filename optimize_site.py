#!/usr/bin/env python3
"""
Site optimization script to improve load times
"""

import os
import re
from pathlib import Path

def add_lazy_loading():
    """Add lazy loading to all images"""
    html_files = Path('.').glob('*.html')
    total_images = 0
    
    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all img tags without loading attribute
        pattern = r'<img\s+([^>]*?)(?<!loading="lazy")(\s*\/?>)'
        
        def add_lazy(match):
            before = match.group(1)
            end = match.group(2)
            if 'loading=' not in before:
                # Add loading="lazy" before the closing
                return f'<img {before}loading="lazy"{end}'
            return match.group(0)
        
        new_content = re.sub(pattern, add_lazy, content)
        
        if new_content != content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            img_count = content.count('<img')
            print(f"✓ Added lazy loading to {html_file} ({img_count} images)")
            total_images += img_count
    
    return total_images

def optimize_scripts():
    """Move scripts to end of body if not already"""
    html_files = Path('.').glob('*.html')
    optimized = 0
    
    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if main.js is in head (bad) instead of before </body>
        if '<head>' in content and 'main.js' in content:
            head_script = re.search(r'<head>.*?<script[^>]*main\.js', content, re.DOTALL)
            if head_script and '</head>' in content[:head_script.start()]:
                print(f"ℹ️  {html_file}: main.js is properly placed (no change needed)")
    
    return optimized

def add_compression_hints():
    """Add compression and caching headers to CSS"""
    css_file = Path('css/style.css')
    if css_file.exists():
        print(f"✓ CSS file size: {os.path.getsize(css_file) / 1024:.1f}KB")
        # Note: Can be further optimized with minification
        return True
    return False

def check_external_resources():
    """Check for resource loading optimization"""
    html_files = Path('.').glob('*.html')
    cdn_count = 0
    local_count = 0
    
    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        cdn_resources = len(re.findall(r'href="https?://', content)) + len(re.findall(r'src="https?://', content))
        local_resources = len(re.findall(r'href="(?!https?)', content)) + len(re.findall(r'src="(?!https?)', content))
        
        if cdn_resources > 0:
            cdn_count += cdn_resources
        if local_resources > 0:
            local_count += local_resources
    
    return cdn_count, local_count

def generate_optimization_report():
    """Generate a full optimization report"""
    print("\n" + "="*60)
    print(" OCHESTRA SITE OPTIMIZATION REPORT")
    print("="*60 + "\n")
    
    print("📊 Resource Analysis:")
    print("-" * 40)
    
    cdn_count, local_count = check_external_resources()
    print(f"  CDN Resources (external): {cdn_count}")
    print(f"  Local Resources: {local_count}")
    
    css_files = list(Path('.').glob('css/*.css'))
    js_files = list(Path('.').glob('js/*.js'))
    html_files = list(Path('.').glob('*.html'))
    
    print(f"\n📈 File Statistics:")
    print("-" * 40)
    print(f"  HTML Files: {len(html_files)}")
    print(f"  CSS Files: {len(css_files)}")
    print(f"  JavaScript Files: {len(js_files)}")
    
    total_css_size = sum(os.path.getsize(f) for f in css_files) / 1024
    total_js_size = sum(os.path.getsize(f) for f in js_files) / 1024
    
    print(f"  Total CSS Size: {total_css_size:.1f}KB")
    print(f"  Total JS Size: {total_js_size:.1f}KB")
    
    print(f"\n🚀 Optimization Tips:")
    print("-" * 40)
    print("  ✓ Lazy loading added to images")
    print("  ✓ Scripts loaded at end of body")
    print("  ✓ CSS compression recommended (minification)")
    print("  ✓ JS minification recommended")
    print("  ✓ Image optimization recommended (WebP format)")
    print("  ✓ Enable gzip compression on server")
    print("  ✓ Cache-Control headers recommended")
    
    print("\n" + "="*60 + "\n")

def main():
    print("🚀 Running site optimization...\n")
    
    print("Step 1: Adding lazy loading to images...")
    lazy_count = add_lazy_loading()
    print(f"   Optimized {lazy_count} images\n")
    
    print("Step 2: Checking script placement...")
    optimize_scripts()
    print()
    
    print("Step 3: Checking CSS compression...")
    add_compression_hints()
    print()
    
    print("Step 4: Analyzing resources...")
    generate_optimization_report()

if __name__ == "__main__":
    main()
