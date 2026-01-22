import sys
import os

file_path = 'c:/Users/Osmaxin/Documents/DecodamsWork/Blegow/Ochestra/css/style.css'
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Find the start of corruption
    clean_lines = []
    corruption_found = False
    
    for line in lines:
        # Check for the specific corrupted comment start or just the first spaced out line
        # The spaced out line looks like " . f o r m "
        if ' . f o r m ' in line or ' / *   C o n t a c t ' in line:
            corruption_found = True
            break
        clean_lines.append(line)
    
    if corruption_found:
        print("Found corrupted lines. Truncating and appending clean CSS.")
        
        # Define the clean CSS to append
        clean_css = """
/* Contact Page Styles */
.form-group {
    position: relative;
    margin-bottom: 2rem;
}

.form-input,
.form-select,
.form-textarea {
    width: 100%;
    padding: 0.75rem 0;
    background: transparent;
    border: none;
    border-bottom: 1px solid rgba(10, 12, 18, 0.2);
    font-family: var(--font-display);
    font-size: 1rem;
    color: #0a0c12;
    transition: all 0.3s ease;
    border-radius: 0;
    box-shadow: none;
}

.form-input:focus,
.form-select:focus,
.form-textarea:focus {
    outline: none;
    border-bottom-color: var(--color-gold);
}

.form-label {
    position: absolute;
    top: 0.75rem;
    left: 0;
    font-size: 0.875rem;
    color: rgba(10, 12, 18, 0.5);
    pointer-events: none;
    transition: all 0.3s ease;
    transform-origin: left top;
}

.form-input:focus ~ .form-label,
.form-input:not(:placeholder-shown) ~ .form-label,
.form-textarea:focus ~ .form-label,
.form-textarea:not(:placeholder-shown) ~ .form-label {
    transform: translateY(-1.5rem) scale(0.85);
    color: var(--color-gold);
    font-weight: 700;
}

/* Walnut Grain Pattern */
.walnut-grain {
    background-color: var(--color-walnut);
    background-image: repeating-linear-gradient(45deg, rgba(0,0,0,0.1) 0px, rgba(0,0,0,0.1) 2px, transparent 2px, transparent 4px);
}

/* Contact Button */
.btn-contact-submit {
    align-self: flex-start;
    background-color: transparent;
    border: 2px solid #0a0c12;
    padding: 1rem 3rem;
    font-family: inherit;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: #0a0c12;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    gap: 1rem;
    cursor: pointer;
}

.btn-contact-submit:hover {
    background-color: #0a0c12;
    color: var(--color-gold);
}
"""
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(clean_lines)
            f.write(clean_css)
        print('Successfully fixed css/style.css')
    else:
        print('No corrupted lines found (check pattern)')

except Exception as e:
    print(f'Error: {e}')
