import json

try:
    with open('input.json', 'r', encoding='utf-8') as f:
        content = f.read()
        data = json.loads(content)
    print("JSON is valid.")
except json.JSONDecodeError as e:
    print(f"JSON Error: {e}")
    print(f"Line {e.lineno}, Column {e.colno}")
    # Print the context
    lines = content.splitlines()
    if e.lineno <= len(lines):
        print(f"Content at line {e.lineno}:")
        print(lines[e.lineno - 1])
