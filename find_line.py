with open('tools/input.json', 'r', encoding='utf-8') as f:
    content = f.read()
    # In VS Code, a literal \n in the file doesn't start a new line unless it's a real newline.
    # However, if the user sees line 33, it's likely because of ACTUAL newline characters in the file.
    lines = content.splitlines()
    if len(lines) >= 33:
        print(f"Line 33: {lines[32]}")
    else:
        print(f"File only has {len(lines)} lines.")
