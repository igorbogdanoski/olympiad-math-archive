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

# --- КОНФИГУРАЦИЈА ---
BASE_DIR = Path(__file__).parent.parent.absolute()
DOCS_DIR = BASE_DIR / "docs" # <--- НОВО

# Сега бараме во docs/assets
LOG_FILE = DOCS_DIR / "assets" / "manim_code_log.md"
IMAGES_DIR = DOCS_DIR / "assets" / "images"
HASH_FILE = BASE_DIR / "tools" / ".manim_hashes" # Ова останува во tools

def get_code_blocks(content):
    """Ги вади ID-то и кодот од LOG фајлот."""
    # Ова е regex што бара: ### 🆔 Задача: ID ... ```python CODE ```
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
    """Оваа функција се повикува паралелно."""
    prob_id, code, existing_hash = args
    prob_id = prob_id.strip()
    
    # 1. Пресметај Hash на новиот код
    current_hash = hashlib.md5(code.encode('utf-8')).hexdigest()
    
    target_image = IMAGES_DIR / f"{prob_id}.png"
    
    # 2. ПРОВЕРКА: Дали треба да рендираме?
    # Рендираме САМО АКО: Сликата ја нема ИЛИ Кодот е сменет
    if target_image.exists() and existing_hash == current_hash:
        return f"⏭️  {prob_id}: Веќе постои и е ажурирана. Прескокнувам."
    
    print(f"🎨 {prob_id}: Започнувам рендирање...")
    
    try:
        # Повик до render_manim (ова е тешкиот дел)
        success = render_scene(prob_id, code)
        
        if success:
            save_hash(prob_id, current_hash) # Запиши дека успеавме со овој код
            return f"✅ {prob_id}: Успешно генерирана!"
        else:
            return f"❌ {prob_id}: Грешка при рендирање (види логови)."
            
    except Exception as e:
        return f"❌ {prob_id}: Критична грешка: {str(e)}"

def main():
    if not LOG_FILE.exists():
        print("📭 Нема log фајл. Ништо за работа.")
        return

    print(f"📂 Читање на задачи од: {LOG_FILE}")
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    tasks = get_code_blocks(content)
    if not tasks:
        print("📭 Не најдов Manim код во логот.")
        return

    # --- ДЕДУПЛИКАЦИЈА (SMART FILTER) ---
    # Ова е делот што го додадовме сега.
    # Ако имаме повеќе верзии на иста задача, ја сакаме само последната.
    unique_tasks = {}
    for pid, code in tasks:
        # Бидејќи читаме од горе надолу, секој нов запис ќе го пребрише стариот во речникот.
        # Така на крајот ќе ја имаме само најновата верзија за секое ID.
        unique_tasks[pid.strip()] = code 
    
    # Конвертирај назад во листа за процесирање
    final_tasks = list(unique_tasks.items())
    
    print(f"📦 Вкупно записи во логот: {len(tasks)}")
    print(f"✨ Уникатни задачи за процесирање: {len(final_tasks)}")
    
    # Вчитување на историјата на хашови
    hashes = load_hashes()
    
    # Подготовка на аргументи
    work_items = []
    for pid, code in final_tasks:
        work_items.append((pid, code, hashes.get(pid.strip())))

    # --- ПАРАЛЕЛНО ИЗВРШУВАЊЕ ---
    # max_workers=4 е добар баланс. Ако имаш многу јак PC, стави 8.
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(process_single_task, work_items))

    # Печатење резултати
    print("\n--- ИЗВЕШТАЈ ---")
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
