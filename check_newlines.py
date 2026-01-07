with open('tools/input.json', 'rb') as f:
    content = f.read()
    # Look for literal 0x0A or 0x0D bytes between double quotes
    in_string = False
    escaped = False
    for i, byte in enumerate(content):
        if byte == ord('"') and not escaped:
            in_string = not in_string
        if byte == ord('\\') and not escaped:
            escaped = True
        else:
            escaped = False
        
        if in_string and byte in [0x0A, 0x0D]:
            print(f"Literal newline found at byte {i}")
