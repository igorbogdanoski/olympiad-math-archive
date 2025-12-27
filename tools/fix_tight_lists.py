import os

def fix_tight_lists(root_dir):
    print("🔧 Fixing tight lists (inserting blank lines)...")
    
    count = 0
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
                
            new_lines = []
            in_code_block = False
            modified = False
            
            for i, line in enumerate(lines):
                stripped = line.strip()
                
                # Toggle code block
                if stripped.startswith('```'):
                    in_code_block = not in_code_block
                    new_lines.append(line)
                    continue
                
                if in_code_block:
                    new_lines.append(line)
                    continue
                
                # Check if it's a list item starting with "* "
                # We exclude "**" (bold) starting lines if they don't have space after first *
                # But startswith('* ') ensures space.
                if stripped.startswith('* '):
                    # Check previous line in new_lines
                    if new_lines:
                        prev_line = new_lines[-1].strip()
                        # If previous line is not empty and not a list item
                        if prev_line and not prev_line.startswith('* ') and not prev_line.startswith('- ') and not prev_line.startswith('>'):
                            # Insert blank line
                            new_lines.append('\n')
                            modified = True
                
                new_lines.append(line)
            
            if modified:
                try:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.writelines(new_lines)
                    print(f"✅ Fixed: {filepath}")
                    count += 1
                except Exception as e:
                    print(f"❌ Could not write {filepath}: {e}")

    print(f"🎉 Finished! Fixed {count} files.")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for item in os.listdir(base_dir):
        if item.startswith('grade_'):
            fix_tight_lists(os.path.join(base_dir, item))
