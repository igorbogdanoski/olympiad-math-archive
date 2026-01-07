import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('tools/input.json', 'r', encoding='utf-8') as f:
    content = f.read()
    start = max(0, 31 - 10)
    end = min(len(content), 31 + 20)
    for i in range(start, end):
        c = content[i]
        print(f"{i}: {repr(c)} ({ord(c)})")
