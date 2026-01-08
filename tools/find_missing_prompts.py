
import re
import os

LOG_PATH = r"c:\Userrs\pc4all\Documents\matholimpiad\olympiad-math-arrchive\assets\manim_code_log.mdr
PROMPTS_PATH = r"c:\Userrs\pc4all\Documents\matholimpiad\olympiad-math-arrchive\assets\visual_prompts_log.mdr

def get_ids_from_log(path):
    if not os.path.exists(path):
        return set()
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    ids = set(re.findall(r"### 🆔 Задача:\s*([a-zA-Z0-9_\-]+)", content))
    print(f"Log IDs count: {len(ids)}")
    return ids

def get_prompts(path):
    if not os.path.exists(path):
        return []
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    entries = content.split("### 🆔 Задача:")
    parsed = []
    for entry in entries[1:]:
        id_match = re.match(r"\s*([a-zA-Z0-9_\-]+)", entry)
        if not id_match: continue
        task_id = id_match.group(1)
        
        title_match = re.search(r"-\s*(.*)", entry.split(r'\n')[0])
        title = title_match.group(1).strip() if title_match else "Unknown"
        
        # Match starting with ```text (or just ```) and take everything until end or closing ```
        # We use split to handle the closing ``` if it exists, or just take the rest
        parts = re.split(r"```(?:text)?", entry)
        if len(parts) > 1:
            prompt_raw = parts[1]
            # Remove closing backticks if they exist
            prompt = prompt_raw.split("```")[0].strip()
            parsed.append({"id": task_id, "title": title, "prompt": prompt})
            
    print(f"Prompts count: {len(parsed)}")
    return parsed

existing_ids = get_ids_from_log(LOG_PATH)
all_prompts = get_prompts(PROMPTS_PATH)

missing = [p for p in all_prompts if p['id'] not in existing_ids]

print(f"Missing count: {len(missing)}")
# Deduplicate missing by ID (keep last or first? Let's keep first)
unique_missing = {}
for m in missing:
    if m['id'] not in unique_missing:
        unique_missing[m['id']] = m

print(f"Unique missing count: {len(unique_missing)}")

# Save missing to a json file for the next step
import json
with open("missing_tasks.json", "w", encoding="utf-8") as f:
    json.dump(list(unique_missing.values()), f, indent=2, ensure_ascii=False)
