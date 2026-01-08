import re
with open('tools/input.json', 'r', encoding='utf-8') as f:
    content = f.read()
    # Match backslash followed by any character in the Cyrillic block
    matches = re.finditer(r'\\([\u0400-\u04FF])', content)
    for m in matches:
        print(fr"Invalid escape \\{m.group(1)} at {m.start()}: context: {content[m.start()-10:m.start()+10]}")
