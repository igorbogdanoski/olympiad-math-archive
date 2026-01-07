with open('tools/input.json', 'r', encoding='utf-8') as f:
    content = f.read()
    i = 0
    count = 0
    while i < len(content):
        if content[i] == '\\':
            count += 1
            if i + 1 >= len(content):
                print(f"ERROR: Backslash at end of file at {i}")
                break
            follow = content[i+1]
            if follow == '\\':
                i += 2
                continue
            if follow in '"/bfnrtu':
                i += 2
                continue
            if follow == 'u' and i + 5 < len(content):
                if all(c in '0123456789abcdefABCDEF' for c in content[i+2:i+6]):
                    i += 6
                    continue
            
            print(f"CRITICAL ERROR: Invalid escape \\{follow} (char code {ord(follow)}) at index {i}")
            print(f"Context: {content[max(0, i-20):min(len(content), i+20)]}")
            i += 1
        else:
            i += 1
print(f"Scan complete. Checked {count} backslashes.")
