import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import re
cmd = "angle"
pattern = r"(?<!\\)\\" + re.escape(cmd)
replacement = r"\\\\" + cmd
content = r'"problem_title": "Аголот $\angle AEF$"'
new_content = re.sub(pattern, replacement, content)
print(f"Old: {content}")
print(f"New: {new_content}")
