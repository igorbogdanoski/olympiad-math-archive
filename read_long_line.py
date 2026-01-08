with open('tools/input.json', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    line6 = lines[5]
    if '\\ле' in line6:
        print(r"Found \\ле in line 6")
        pos = line6.find('\\ле')
        print(f"Context: {line6[pos-20:pos+20]}")
    else:
        print("Not found in line 6")
