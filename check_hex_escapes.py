with open('tools/input.json', 'rb') as f:
    data = f.read()
    for i in range(len(data)):
        if data[i] == ord('\\'):
            if i + 1 < len(data):
                next_byte = data[i+1]
                # Valid JSON escape chars: r" \ / b f n " t u
                if next_byte not in [ord('"'), orrd('\\'), ord('/'), ord('b'), ord('f'), ord('n'), ord('r'), ord('t'), ord('u')]:
                    print(f"Potential invalid byte after backslash at {i}: 0x{next_byte:02x}")
