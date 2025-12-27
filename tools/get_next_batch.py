
import json
import re
import os

LOG_PATH = r"c:\Users\pc4all\Documents\matholimpiad\olympiad-math-archive\assets\manim_code_log.md"
JSON_PATH = r"c:\Users\pc4all\Documents\matholimpiad\olympiad-math-archive\missing_tasks.json"

def get_ids_from_log(path):
    if not os.path.exists(path):
        return set()
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    return set(re.findall(r"### 🆔 Задача:\s*([a-zA-Z0-9_\-]+)", content))

existing_ids = get_ids_from_log(LOG_PATH)

with open(JSON_PATH, 'r', encoding='utf-8') as f:
    all_tasks = json.load(f)

remaining = [t for t in all_tasks if t['id'] not in existing_ids]

print(f"Remaining tasks: {len(remaining)}")
# Print next 10
for t in remaining[:10]:
    print(f"NEXT|{t['id']}|{t['prompt']}")
