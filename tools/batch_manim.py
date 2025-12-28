import os
import re
import sys
import hashlib
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor

# Обид за импорт на рендерот
try:
    from render_manim import render_scene
except ImportError:
    print("❌ Грешка: Не можам да го најдам 'render_manim.py'.")
    sys.exit(1)

# --- КОНФИГУРАЦИЈА (АЖУРИРАНА ЗА DOCS) ---
BASE_DIR = Path(__file__).parent.parent.absolute()
DOCS_DIR = BASE_DIR / "docs" # <--- НОВО

LOG_FILE = DOCS_DIR / "assets" / "manim_code_log.md" # <--- НОВО
IMAGES_DIR = DOCS_DIR / "assets" / "images" # <--- НОВО
HASH_FILE = BASE_DIR / "tools" / ".manim_hashes"

def get_code_blocks(content):
    pattern = r"### 🆔 Задача: (.*?)\s-.*?\n.*?```python\n(.*?)\n```"
    return re.findall(pattern, content, re.DOTALL)

def load_hashes():
    if not HASH_FILE.exists(): return {}
    with open(HASH_FILE, 'r', encoding='utf-8') as f:
        return dict(line.strip().split('::') for line in f if '::' in line)

def save_hash(prob_id, code_hash):
    hashes = load_hashes()
    hashes[prob_id] = code_hash
    with open(HASH_FILE, 'w', encoding='utf-8') as f:
        for k, v in hashes.items():
            f.write(f"{k}::{v}\n")

def process_single_task(args):
    prob_id, code, existing_hash = args
    prob_id = prob_id.strip()
    current_hash = hashlib.md5(code.encode('utf-8')).hexdigest()
    target_image = IMAGES_DIR / f"{prob_id}.png"
    
    if target_image.exists() and existing_hash == current_hash:
        return f"⏭️  {prob_id}: Веќе постои и е ажурирана. Прескокнувам."
    
    print(f"🎨 {prob_id}: Започнувам рендирање...")
    try:
        success = render_scene(prob_id, code)
        if success:
            save_hash(prob_id, current_hash)
            return f"✅ {prob_id}: Успешно генерирана!"
        else:
            return f"❌ {prob_id}: Грешка при рендирање."
    except Exception as e:
        return f"❌ {prob_id}: Критична грешка: {str(e)}"

def main():
    if not LOG_FILE.exists():
        print(f"📭 Нема log фајл на локација: {LOG_FILE}")
        return

    print(f"📂 Читање на задачи од: {LOG_FILE}")
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    tasks = get_code_blocks(content)
    if not tasks:
        print("📭 Не најдов Manim код во логот.")
        return

    unique_tasks = {}
    for pid, code in tasks:
        unique_tasks[pid.strip()] = code 
    
    final_tasks = list(unique_tasks.items())
    print(f"✨ Уникатни задачи за процесирање: {len(final_tasks)}")
    
    hashes = load_hashes()
    work_items = []
    for pid, code in final_tasks:
        work_items.append((pid, code, hashes.get(pid.strip())))

    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(process_single_task, work_items))

    print("\n--- ИЗВЕШТАЈ ---")
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
