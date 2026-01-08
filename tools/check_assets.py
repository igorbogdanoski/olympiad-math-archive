import json
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
PROBLEMS_JSON = os.path.join(BASE_DIR, "web/src/data/problems.json")
IMAGES_DIR = os.path.join(BASE_DIR, "web/public/assets/images")

with open(PROBLEMS_JSON, 'r', encoding='utf-8') as f:
    problems = json.load(f)

missing = []
for p in problems:
    pid = p.get('meta', {}).get('problem_id') or p.get('filename', '').replace('.md', '')
    img_path = os.path.join(IMAGES_DIR, pid, f"{pid}.png")
    
    if not os.path.exists(img_path):
        missing.append({
            "id": pid,
            "title": p.get('filename'),
            "grade": p.get('grade'),
            "category": p.get('category')
        })

print(f"Total problems: {len(problems)}")
print(f"Missing illustrations: {len(missing)}")

with open(os.path.join(BASE_DIR, "missing_illustrations.json"), 'w', encoding='utf-8') as f:
    json.dump(missing, f, ensure_ascii=False, indent=2)

print("Report saved to missing_illustrations.json")
