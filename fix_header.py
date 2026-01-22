import sys
import os

file_path = 'c:/Users/Osmaxin/Documents/DecodamsWork/Blegow/Ochestra/css/style.css'
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    modified = False
    for i, line in enumerate(lines):
        if line.strip() == 'header {' and i > 0 and '/* Header */' in lines[i-1]:
            print(f'Found header at line {i+1}')
            # Check if position: relative is already there
            if 'position: relative;' not in lines[i+1]:
                lines.insert(i+1, '    position: relative;\n')
                modified = True
            break
    
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        print('Successfully modified css/style.css')
    else:
        print('No changes made')

except Exception as e:
    print(f'Error: {e}')
