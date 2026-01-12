with open('tools/process_olympiad.py', 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')

for i, line in enumerate(lines):
    if 'math_blocks = re.findall(r\'\\\$\\\$[^$]+\\\$\\' in line:
        print(f"Found broken line at {i+1}: {repr(line)}")
        # This is the broken line
        lines[i] = '        math_blocks = re.findall(r\'$$[^$]+$$\', content)'
        # Add the rest
        lines.insert(i+1, '        for block in math_blocks:')
        lines.insert(i+2, '            if block.count(\'$$\') != 2:')
        lines.insert(i+3, '                print("❌ STOP: Malformed LaTeX block equation.")')
        lines.insert(i+4, '                return False')
        lines.insert(i+5, '')
        lines.insert(i+6, '        # Tags validation (should exist and be non-empty)')
        lines.insert(i+7, '        tags = metadata.get(\'tags\', [])')
        lines.insert(i+8, '        if not tags or len(tags) == 0:')
        lines.insert(i+9, '            print("⚠️ WARNING: No tags specified. Consider adding relevant tags.")')
        lines.insert(i+10, '            # Not blocking, just warning')
        lines.insert(i+11, '')
        lines.insert(i+12, '        print("✅ Quality validation passed.")')
        lines.insert(i+13, '        return True')
        break

content = '\n'.join(lines)

with open('tools/process_olympiad.py', 'w', encoding='utf-8') as f:
    f.write(content)