
import re
import os

LOG_PATH = r"c:\Users\pc4all\Documents\matholimpiad\olympiad-math-archive\assets\manim_code_log.md"
PROMPTS_PATH = r"c:\Users\pc4all\Documents\matholimpiad\olympiad-math-archive\assets\visual_prompts_log.md"

def get_ids_from_log(path):
    if not os.path.exists(path):
        return set()
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Matches: ### 🆔 Задача: <ID>
    return set(re.findall(r"### 🆔 Задача:\s*([a-zA-Z0-9_\-]+)", content))

def get_prompts(path):
    if not os.path.exists(path):
        return []
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by "### 🆔 Задача:"
    entries = content.split("### 🆔 Задача:")
    parsed = []
    for entry in entries[1:]: # Skip first empty split
        # Extract ID
        id_match = re.match(r"\s*([a-zA-Z0-9_\-]+)", entry)
        if not id_match: continue
        task_id = id_match.group(1)
        
        # Extract Title (optional, just for context)
        title_match = re.search(r"-\s*(.*)", entry.split('\n')[0])
        title = title_match.group(1).strip() if title_match else "Unknown"
        
        # Extract Prompt
        prompt_match = re.search(r"```text\s+(.*?)```", entry, re.DOTALL)
        if prompt_match:
            prompt = prompt_match.group(1).strip()
            parsed.append({"id": task_id, "title": title, "prompt": prompt})
            
    return parsed

existing_ids = get_ids_from_log(LOG_PATH)
all_prompts = get_prompts(PROMPTS_PATH)

missing = [p for p in all_prompts if p['id'] not in existing_ids]

print(f"Found {len(missing)} missing tasks.")
for m in missing:
    print(f"MISSING|{m['id']}|{m['title']}|{m['prompt'].replace(chr(10), ' ')}")
