with open('tools/input.json', 'rb') as f:
    data = f.read(100)
    for i, b in enumerate(data):
        print(f"{i}: 0x{b:02x} ({chr(b) if b < 128 else '?'})")
