with open('tools/input.json', 'r', encoding='utf-8') as f:
    content = f.read()
    i = 0
    while i < len(content):
        if content[i] == '\\':
            # Check what follows
            if i + 1 < len(content):
                follow = content[i+1]
                if follow not in 'r"\\/bfn"tu':
                    print(fr"Invalid escape \\{follow} at index {i}")
                    print(f"Context: {content[max(0, i-10):min(len(content), i+10)]}")
            else:
                print("Backslash at end of file")
        i += 1
