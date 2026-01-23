import os

css_path = r'c:\Users\Osmaxin\Documents\DecodamsWork\Blegow\Ochestra\css\style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the start of the corrupted block
corrupted_start = -1
for i, line in enumerate(lines):
    if '.btn-contact-submit:hover {' in line:
        corrupted_start = i
        break

if corrupted_start != -1:
    new_lines = lines[:corrupted_start]
    new_lines.append('.btn-contact-submit:hover {\n')
    new_lines.append('    background-color: #0a0c12;\n')
    new_lines.append('    color: var(--color-gold);\n')
    new_lines.append('}\n\n')
    new_lines.append('/* Responsiveness */\n')
    new_lines.append('@media (max-width: 1024px) {\n')
    new_lines.append('    .nav-menu {\n')
    new_lines.append('        display: none;\n')
    new_lines.append('        position: absolute;\n')
    new_lines.append('        top: 100%;\n')
    new_lines.append('        left: 0;\n')
    new_lines.append('        width: 100%;\n')
    new_lines.append('        flex-direction: column;\n')
    new_lines.append('        background-color: var(--color-midnight);\n')
    new_lines.append('        padding: 2rem;\n')
    new_lines.append('        gap: 1.5rem;\n')
    new_lines.append('        border-bottom: 1px solid rgba(255, 255, 255, 0.05);\n')
    new_lines.append('    }\n')
    new_lines.append('\n')
    new_lines.append('    .nav-menu.active {\n')
    new_lines.append('        display: flex;\n')
    new_lines.append('    }\n')
    new_lines.append('\n')
    new_lines.append('    .mobile-toggle {\n')
    new_lines.append('        display: block;\n')
    new_lines.append('    }\n')
    new_lines.append('\n')
    new_lines.append('    .logo-text {\n')
    new_lines.append('        font-size: 1.125rem;\n')
    new_lines.append('    }\n')
    new_lines.append('}\n')
    new_lines.append('\n')
    new_lines.append('@media (max-width: 768px) {\n')
    new_lines.append('    .container {\n')
    new_lines.append('        padding: 0 1rem;\n')
    new_lines.append('    }\n')
    new_lines.append('\n')
    new_lines.append('    body {\n')
    new_lines.append('        font-size: 14px;\n')
    new_lines.append('    }\n')
    new_lines.append('}\n')
    
    with open(css_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("Success")
else:
    print("Could not find start block")
