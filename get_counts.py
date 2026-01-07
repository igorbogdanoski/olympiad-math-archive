with open('pretty.json', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(f"Total lines: {len(lines)}")
    for i, l in enumerate(lines):
        if len(l) > 100:
            print(f"Line {i+1} is long: {len(l)} chars")
