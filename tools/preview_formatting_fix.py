import os
import re

def preview_changes(root_dir):
    print("🔍 Scanning for ' * ' pattern in markdown files...")
    
    for dirpath, _, filenames in os.walk(root_dir):
        if 'node_modules' in dirpath or '.git' in dirpath:
            continue
            
        for filename in filenames:
            if not filename.endswith('.md'):
                continue
                
            filepath = os.path.join(dirpath, filename)
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
            except Exception as e:
                print(f"⚠️ Could not read {filepath}: {e}")
                continue
                
            in_code_block = False
            file_has_matches = False
            
            for i, line in enumerate(lines):
                stripped = line.strip()
                if stripped.startswith('```'):
                    in_code_block = not in_code_block
                    continue
                
                if in_code_block:
                    continue
                
                # Regex for " * " preceded by non-whitespace (inline separator)
                # We look for non-whitespace, spaces, asterisk, spaces
                matches = re.finditer(r'(?<=\S)\s+\*\s+(?=\S)', line)
                
                found = False
                for match in matches:
                    found = True
                    break
                
                if found:
                    if not file_has_matches:
                        print(fr"\n📂 File: {filepath}")
                        file_has_matches = True
                    
                    print(f"  Line {i+1}: {line.strip()}")
                    # Show proposed change
                    # new_line = re.sub(rr'(?<!\*)\s\*\s(?!\*)', r'\n- ', line)
                    # print(f"  ➡️ Proposed: {new_line.strip()}")

if __name__ == "__main__":
    # Check grade directories
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for item in os.listdir(base_dir):
        if item.startswith('grade_'):
            preview_changes(os.path.join(base_dir, item))
