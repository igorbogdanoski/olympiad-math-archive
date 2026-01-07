with open('tools/input.json', 'rb') as f:
    f.seek(200)
    data = f.read(400)
    for i, b in enumerate(data):
        print(f"{i+200}: 0x{b:02x} ({chr(b) if b < 128 else '?'})")
