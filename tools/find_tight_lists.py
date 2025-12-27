import os

def find_tight_lists(root_dir):
    print("🔍 Scanning for lists without preceding blank lines...")
    
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
            
            for i, line in enumerate(lines):
                stripped = line.strip()
                if stripped.startswith('```'):
                    in_code_block = not in_code_block
                    continue
                
                if in_code_block:
                    continue
                
                # Check if line is a list item (starts with "* " or "- ")
                # We focus on "*" as per user request
                if stripped.startswith('* ') and not stripped.startswith('**'):
                    # Check previous line
                    if i > 0:
                        prev_line = lines[i-1].strip()
                        # If previous line is not empty and not a list item
                        if prev_line and not prev_line.startswith('* ') and not prev_line.startswith('- '):
                            print(f"\n📂 File: {filepath}")
                            print(f"  Line {i}: {prev_line}")
                            print(f"  Line {i+1}: {stripped}")
                            # We found a candidate!

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for item in os.listdir(base_dir):
        if item.startswith('grade_'):
            find_tight_lists(os.path.join(base_dir, item))
