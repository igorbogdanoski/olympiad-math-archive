import os
import re
import subprocess
import shutil

# --- КОНФИГУРАЦИЈА ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVE_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "../"))
ASSETS_DIR = os.path.join(ARCHIVE_ROOT, "assets", "images")
LOG_FILE = os.path.join(ARCHIVE_ROOT, "assets", "manim_code_log.md")
TEMP_MANIM_FILE = os.path.join(SCRIPT_DIR, "temp_scene.py")

def load_manim_code_map():
    """Parses the log file and returns a dict of {problem_id: code}."""
    if not os.path.exists(LOG_FILE):
        print(f"⚠️ Log file not found: {LOG_FILE}")
        return {}

    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Regex to find problem entries
    # Matches: ### 🆔 Задача: <ID> ... ```python <code> ```
    pattern = re.compile(
        r"### 🆔 Задача:\s*([a-zA-Z0-9_\-]+).*?```python\s+(.*?)```",
        re.DOTALL
    )
    
    code_map = {}
    for match in pattern.finditer(content):
        problem_id = match.group(1).strip()
        code = match.group(2)
        code_map[problem_id] = code
    
    print(f"📚 Loaded {len(code_map)} code snippets from log.")
    return code_map

def extract_problem_id(content):
    """Extracts problem_id from YAML frontmatter."""
    match = re.search(r'^problem_id:\s*(.+)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip().replace('"', '').replace("'", "")
    return None

def extract_manim_code(content):
    """Бара Python код блок што личи на Manim сцена (fallback)."""
    match = re.search(r'```python\s+(.*?)```', content, re.DOTALL)
    if match:
        code = match.group(1)
        if "from manim import" in code or "class" in code and "(Scene)" in code:
            return code
    return None

def run_manim(code, filename_base):
    """Го извршува Manim кодот и ја враќа патеката до сликата."""
    
    target_name = f"{filename_base}.png"
    target_path = os.path.join(ASSETS_DIR, target_name)
    
    # 0. Провери дали сликата веќе постои
    if os.path.exists(target_path):
        print(f"   ⏭️  Image already exists: {target_name}")
        return target_name

    # 1. Запиши го кодот во привремен фајл
    with open(TEMP_MANIM_FILE, 'w', encoding='utf-8') as f:
        # Осигурај се дека има imports ако фалат
        if "from manim import" not in code:
            f.write("from manim import *\n")
        f.write(code)
        # Додај config за да зачува само последен фрејм како слика
        f.write(f"\n\nconfig.media_width = '100%'\nconfig.verbosity = 'ERROR'\n")

    # 2. Најди го името на сцената (класата)
    scene_match = re.search(r'class\s+(\w+)\(Scene\):', code)
    if not scene_match:
        # Ако нема класа, можеби е само функција construct?
        # Засега претпоставуваме дека има класа.
        return None
    scene_name = scene_match.group(1)
    
    # 3. Изврши Manim команда
    # Користиме -o за да го фиксираме името на излезот (без верзија)
    cmd = ["manim", "-qm", "-s", "--disable_caching", "-o", f"{scene_name}.png", TEMP_MANIM_FILE, scene_name]
    
    print(f"   🎬 Rendering {scene_name}...")
    try:
        subprocess.run(cmd, check=True, capture_output=True)
        
        # 4. Најди ја генерираната слика
        expected_output = os.path.join("media", "images", "temp_scene", f"{scene_name}.png")
        
        if os.path.exists(expected_output):
            # 5. Премести ја во assets/images
            os.makedirs(ASSETS_DIR, exist_ok=True)
            shutil.move(expected_output, target_path)
            
            if os.path.exists("media"):
                shutil.rmtree("media", ignore_errors=True)
                
            return target_name
        else:
            print(f"   ❌ Expected output not found: {expected_output}")
            # Debug: list dir
            debug_dir = os.path.dirname(expected_output)
            if os.path.exists(debug_dir):
                print(f"   📂 Dir content: {os.listdir(debug_dir)}")
            
    except subprocess.CalledProcessError as e:
        print(f"   ❌ Manim Error: {e}")
        print(f"   ❌ Stderr: {e.stderr.decode('utf-8') if e.stderr else 'None'}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
        
    return None

def update_markdown_with_image(file_path, image_name):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Ако веќе има слика, не прави ништо (освен ако не сакаме да ја замениме, но засега не)
    if f"assets/images/{image_name}" in content:
        print(f"   ⏭️  Link already exists in Markdown")
        return True

    file_dir = os.path.dirname(file_path)
    rel_path = os.path.relpath(os.path.join(ASSETS_DIR, image_name), file_dir)
    rel_path = rel_path.replace("\\", "/")
    
    new_image_tag = f"![Визуелизација]({rel_path})"
    
    # 1. Пробај со стандардниот placeholder
    placeholder = "<!-- Ова место е резервирано за автоматската слика од Manim -->"
    if placeholder in content:
        new_content = content.replace(placeholder, new_image_tag)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"   ✅ Link updated (replaced placeholder)")
        return True

    # 2. Пробај со VISUAL PROMPT placeholder
    visual_prompt_regex = r"<!-- VISUAL PROMPT:.*?-->"
    if re.search(visual_prompt_regex, content):
        new_content = re.sub(visual_prompt_regex, new_image_tag, content)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"   ✅ Link updated (replaced VISUAL PROMPT)")
        return True

    # 3. Пробај да вметнеш после "## 📐 Скица"
    if "## 📐 Скица" in content:
        new_content = content.replace("## 📐 Скица", f"## 📐 Скица\n{new_image_tag}")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"   ✅ Link updated (inserted after Header)")
        return True

    # 4. Пробај да вметнеш пред "Geo-Mentor Code"
    if "> **👨‍💻 Geo-Mentor Code:**" in content:
        new_content = content.replace("> **👨‍💻 Geo-Mentor Code:**", f"{new_image_tag}\n\n> **👨‍💻 Geo-Mentor Code:**")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"   ✅ Link updated (inserted before Geo-Mentor)")
        return True

    # 5. Fallback: Вметни пред "## 🧠 Анализа" или "## 📝 Решение"
    if "## 🧠 Анализа" in content:
        new_content = content.replace("## 🧠 Анализа", f"## 📐 Скица\n{new_image_tag}\n\n## 🧠 Анализа")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"   ✅ Link updated (inserted before Analysis)")
        return True
        
    if "## 📝 Решение" in content:
        new_content = content.replace("## 📝 Решение", f"## 📐 Скица\n{new_image_tag}\n\n## 📝 Решение")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"   ✅ Link updated (inserted before Solution)")
        return True

    print(f"   ⚠️ Could not find a place to insert image in {os.path.basename(file_path)}")
    return False

def main():
    print("🎨 Starting Batch Manim Renderer...")
    
    # Вчитај ги кодовите од логот
    manim_code_map = load_manim_code_map()
    
    BATCH_SIZE = 100
    processed_count = 0
    scanned_files = 0
    candidates_found = 0
    
    for root, dirs, files in os.walk(ARCHIVE_ROOT):
        if "tools" in root or "assets" in root: continue
        
        for file in files:
            if processed_count >= BATCH_SIZE:
                print(f"\n🛑 Batch limit of {BATCH_SIZE} reached. Run the script again to process the next batch.")
                return

            if file.endswith(".md"):
                scanned_files += 1
                path = os.path.join(root, file)
                
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                except Exception as e:
                    print(f"❌ Error reading {file}: {e}")
                    continue
                
                # Провери дали веќе има слика (било каква)
                if "![Визуелизација]" in content:
                    continue

                # Ако нема слика, провери дали имаме код за неа
                problem_id = extract_problem_id(content)
                code = None
                
                if problem_id and problem_id in manim_code_map:
                    candidates_found += 1
                    print(f"🔍 Found code in LOG for ID: {problem_id} ({file})")
                    code = manim_code_map[problem_id]
                else:
                    # Fallback: embedded code
                    code = extract_manim_code(content)
                    if code:
                        candidates_found += 1
                        print(f"🔍 Found embedded code in: {file}")
                
                if code:
                    filename_base = problem_id if problem_id else file.replace(".md", "")
                    image_name = run_manim(code, filename_base)
                    
                    if image_name:
                        if update_markdown_with_image(path, image_name):
                            processed_count += 1
                            print(f"   📊 Progress: {processed_count}/{BATCH_SIZE}")
                        else:
                            print(f"   ❌ Failed to update markdown for {file}")
                # else:
                    # print(f"⚠️  No code found for: {file} (ID: {problem_id})")

    print(f"\n🏁 Finished scan.")
    print(f"   📂 Scanned files: {scanned_files}")
    print(f"   🎯 Candidates (with placeholder): {candidates_found}")
    print(f"   ✅ Processed in this batch: {processed_count}")


if __name__ == "__main__":
    main()
