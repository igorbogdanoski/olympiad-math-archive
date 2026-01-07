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
    print("ERR Greshka: Ne mozham da go najdam 'render_manim.py'.")
    sys.exit(1)

# --- КОНФИГУРАЦИЈА (АЖУРИРАНА ЗА DOCS) ---
BASE_DIR = Path(__file__).parent.parent.absolute()
DOCS_DIR = BASE_DIR / "docs" # <--- НОВО

LOG_FILE = DOCS_DIR / "assets" / "manim_code_log.md" # <--- НОВО
IMAGES_DIR = DOCS_DIR / "assets" / "images" # <--- НОВО
HASH_FILE = BASE_DIR / "tools" / ".manim_hashes"

def get_code_blocks(content):
    pattern = r"### ID Zadacha: (.*?)\s-.*?\n.*?```python\n(.*?)\n```"
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
    
    print(f"RENDER {prob_id}: Zapochnuvam rendiranje...")
    try:
        success = render_scene(prob_id, code)
        if success:
            save_hash(prob_id, current_hash)
            # --- НОВО: Автоматско ажурирање на Markdown ---
            try:
                update_markdown_reference(prob_id)
            except Exception as update_err:
                print(f"⚠️ Greshka pri azhuriranje na Markdown za {prob_id}: {update_err}")
            
            return f"✅ {prob_id}: Успешно генерирана и поврзана!"
        else:
            return f"❌ {prob_id}: Грешка при рендирање."
    except Exception as e:
        return f"❌ {prob_id}: Критична грешка: {str(e)}"

def update_markdown_reference(prob_id):
    """
    Search for markdown files containing the 'missing visual' placeholder for this problem
    and replace it with the image link.
    """
    safe_id = re.sub(r'[^a-zA-Z0-9_]', '_', prob_id)
    placeholder_fragment = f"Task_{safe_id}" 
    
    # We scan all .md files in DOCS_DIR
    for root, dirs, files in os.walk(DOCS_DIR):
        for file in files:
            if not file.endswith(".md"): continue
            
            file_path = Path(root) / file
            
            # Skip the log files themselves and the archive
            if file_path == LOG_FILE or "manim_code_archive" in str(file_path): 
                continue

            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                # Check if this file has the specific placeholder for this task
                if placeholder_fragment in content and "> **👨‍💻 Geo-Mentor Code:**" in content:
                    
                    # Calculate relative path to image
                    image_path_abs = IMAGES_DIR / f"{prob_id}.png"
                    
                    try:
                        rel_path = os.path.relpath(image_path_abs, start=file_path.parent)
                        rel_path = rel_path.replace(os.path.sep, '/')
                    except ValueError:
                        print(f"⚠️ Ne mozham da presmetam relativna pateka za {file_path}")
                        continue

                    # Construct the replacement using Regex to capture the whole block
                    pattern = re.compile(
                        r">\s*\*\*👨‍💻 Geo-Mentor Code:\*\*\n"
                        r">\s*Одете во `assets/manim_code_log.md`.*?" + re.escape(f"Task_{safe_id}") + r".*?\n",
                        re.DOTALL
                    )
                    
                    # Check if pattern matches
                    if pattern.search(content):
                        new_block = f"![Скица]({rel_path})\n"
                        new_content = pattern.sub(new_block, content)
                        
                        if new_content != content:
                            with open(file_path, "w", encoding="utf-8") as f:
                                f.write(new_content)
                            print(f"LINK Azhuriran fajl so slika: {file}")
                            return True # Found and updated

            except Exception as e:
                # Ignore read errors
                pass
    return False

def to_ascii(text):
    m = {
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Ѓ': 'Gj', 'Е': 'E', 'Ж': 'Zh', 'З': 'Z', 'Ѕ': 'Dz',
        'И': 'I', 'Ј': 'J', 'К': 'K', 'Л': 'L', 'Љ': 'Lj', 'М': 'M', 'Н': 'N', 'Њ': 'Nj', 'О': 'O', 'П': 'P',
        'Р': 'R', 'С': 'S', 'Т': 'T', 'Ќ': 'Kj', 'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'C', 'Ч': 'Ch', 'Џ': 'Dj', 'Ш': 'Sh',
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'ѓ': 'gj', 'е': 'e', 'ж': 'zh', 'з': 'z', 'ѕ': 'dz',
        'и': 'i', 'ј': 'j', 'к': 'k', 'л': 'l', 'љ': 'lj', 'м': 'm', 'н': 'n', 'њ': 'nj', 'о': 'o', 'п': 'p',
        'р': 'r', 'с': 's', 'т': 't', 'ќ': 'kj', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'џ': 'dj', 'ш': 'sh',
        "✅": "OK", "❌": "ERR", "⏭️": "SKIP", "🎨": "RENDER", "⚠️": "WARN", "📭": "EMPTY", "📂": "READ", "✨": "DONE", "📎": "LINK", "🆔": "ID", "👨‍💻": "DEV"
    }
    return "".join(m.get(c, c) for c in text)

def safe_print(obj):
    print(to_ascii(str(obj)))

def main():
    if not LOG_FILE.exists():
        print(f"EMPTY Nema log fajl na lokacija: {LOG_FILE}")
        return

    print(f"READ Chitanje na zadachi od: {LOG_FILE}")
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    tasks = get_code_blocks(content)
    if not tasks:
        print("EMPTY Ne najdov Manim kod vo logot.")
        return

    unique_tasks = {}
    for pid, code in tasks:
        unique_tasks[pid.strip()] = code 
    
    final_tasks = list(unique_tasks.items())
    print(f"DONE Unikatni zadachi za procesiranje: {len(final_tasks)}")
    
    hashes = load_hashes()
    work_items = []
    for pid, code in final_tasks:
        work_items.append((pid, code, hashes.get(pid.strip())))

    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(process_single_task, work_items))

    print("\n--- IZVEShTAJ ---")
    for res in results:
        safe_print(res)

if __name__ == "__main__":
    main()
