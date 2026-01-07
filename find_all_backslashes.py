import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('tools/input.json', 'r', encoding='utf-8') as f:
    content = f.read()
    for i, c in enumerate(content):
        if c == '\\':
            print(f"Backslash at {i}: '{content[i:i+5]}'")
