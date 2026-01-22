import sys
import os

file_path = 'c:/Users/Osmaxin/Documents/DecodamsWork/Blegow/Ochestra/css/style.css'
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    modified = False
    
    # Check if we already have .hidden-lg globally
    # We'll just define it after .hidden if not present
    has_hidden_lg = False
    for line in lines[:400]: # Check first 400 lines (before media queries usually)
        if '.hidden-lg' in line:
            has_hidden_lg = True
            break
    
    if not has_hidden_lg:
        for i, line in enumerate(lines):
            if line.strip() == '.hidden {' and 'display: none;' in lines[i+1]:
                print(f"Found .hidden at line {i+1}")
                lines.insert(i+3, '\n.hidden-lg {\n    display: none;\n}\n')
                modified = True
                break

    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
             f.writelines(lines)
        print('Successfully added .hidden-lg to css/style.css')
    else:
        print('No changes made (.hidden-lg might already exist or .hidden not found)')

except Exception as e:
    print(f'Error: {e}')
