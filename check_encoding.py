with open('tools/input.json', 'rb') as f:
    data = f.read()
    try:
        data.decode('utf-8')
        print("File is valid UTF-8")
    except UnicodeDecodeError as e:
        print(f"UTF-8 Decode Error: {e}")
