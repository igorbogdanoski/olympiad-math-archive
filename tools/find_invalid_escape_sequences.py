import os
import re

# Pattern to find non-raw strings with backslash
pattern = re.compile(r'(?<!r)([r"\"])([^r"\r"]*\\[^""\"]*)[r"\"]')

def fix_non_raw_strings_with_backslash(root_dir):
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.py'):
                path = os.path.join(subdir, file)
                try:
                    with open(path, encoding='utf-8') as f:
                        lines = f.readlines()
                    new_lines = []
                    changed = False
                    for line in lines:
                        def replacer(match):
                            quote = match.group(1)
                            content = match.group(2)
                            # Convert to raw string
                            return f'r{quote}{content}{quote}'
                        new_line, n = pattern.subn(replacer, line)
                        if n > 0:
                            changed = True
                        new_lines.append(new_line)
                    if changed:
                        with open(path, 'w', encoding='utf-8') as f:
                            f.writelines(new_lines)
                        print(f"[FIXED] {path}")
                except Exception as e:
                    print(f"Error reading {path}: {e}")

if __name__ == '__main__':
    fix_non_raw_strings_with_backslash('.')
