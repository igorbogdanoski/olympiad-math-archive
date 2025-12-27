import os
import re
import subprocess
import shutil

# --- КОНФИГУРАЦИЈА ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVE_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "../"))
ASSETS_DIR = os.path.join(ARCHIVE_ROOT, "assets", "images")
TEMP_MANIM_FILE = os.path.join(SCRIPT_DIR, "temp_scene.py")

def extract_manim_code(content):
    """Бара Python код блок што личи на Manim сцена."""
    # Бараме ```python ... class ... (Scene): ... ```
    match = re.search(r'```python\s+(.*?)```', content, re.DOTALL)
    if match:
        code = match.group(1)
        if "from manim import" in code or "class" in code and "(Scene)" in code:
            return code
    return None

def run_manim(code, filename_base):
    """Го извршува Manim кодот и ја враќа патеката до сликата."""
    
    # 1. Запиши го кодот во привремен фајл
    with open(TEMP_MANIM_FILE, 'w', encoding='utf-8') as f:
        # Осигурај се дека има imports ако фалат
        if "from manim import *" not in code:
            f.write("from manim import *\n")
        f.write(code)
        # Додај config за да зачува само последен фрејм како слика
        f.write(f"\n\nconfig.media_width = '100%'\nconfig.verbosity = 'ERROR'\n")

    # 2. Најди го името на сцената (класата)
    scene_match = re.search(r'class\s+(\w+)\(Scene\):', code)
    if not scene_match:
        return None
    scene_name = scene_match.group(1)
    
    # 3. Изврши Manim команда: manim -qm -s temp_scene.py SceneName
    # -qm: quality medium, -s: save last frame only (image)
    cmd = ["manim", "-qm", "-s", "--disable_caching", TEMP_MANIM_FILE, scene_name]
    
    print(f"   🎬 Rendering {scene_name}...")
    try:
        subprocess.run(cmd, check=True, capture_output=True)
        
        # 4. Најди ја генерираната слика
        # Manim по дифолт ја става во media/images/temp_scene/SceneName.png
        expected_output = os.path.join("media", "images", "temp_scene", f"{scene_name}.png")
        
        if os.path.exists(expected_output):
            # 5. Премести ја во assets/images со правилно име
            target_name = f"{filename_base}.png"
            target_path = os.path.join(ASSETS_DIR, target_name)
            
            # Креирај папка ако не постои
            os.makedirs(ASSETS_DIR, exist_ok=True)
            
            shutil.move(expected_output, target_path)
            
            # Исчисти media папка
            if os.path.exists("media"):
                shutil.rmtree("media", ignore_errors=True)
                
            return target_name
            
    except subprocess.CalledProcessError as e:
        print(f"   ❌ Manim Error: {e}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
        
    return None

def update_markdown_with_image(file_path, image_name):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    placeholder = "<!-- Ова место е резервирано за автоматската слика од Manim -->"
    
    # Пресметај релативна патека
    # file_path: .../grade_10/geometry/file.md
    # image_path: .../assets/images/file.png
    # Треба да одиме нагоре до root, па во assets
    
    file_dir = os.path.dirname(file_path)
    rel_path = os.path.relpath(os.path.join(ASSETS_DIR, image_name), file_dir)
    # Замени backslash со forward slash за Markdown
    rel_path = rel_path.replace("\\", "/")
    
    new_image_tag = f"![Визуелизација]({rel_path})"
    
    if placeholder in content:
        new_content = content.replace(placeholder, new_image_tag)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"   ✅ Link updated in Markdown")
        return True
    return False

def main():
    print("🎨 Starting Batch Manim Renderer...")
    
    BATCH_SIZE = 5
    processed_count = 0
    
    for root, dirs, files in os.walk(ARCHIVE_ROOT):
        if "tools" in root or "assets" in root: continue
        
        for file in files:
            if processed_count >= BATCH_SIZE:
                print(f"\n🛑 Batch limit of {BATCH_SIZE} reached. Run the script again to process the next batch.")
                return

            if file.endswith(".md"):
                path = os.path.join(root, file)
                
                # Провери дали веќе има слика (за да не рендерираме пак)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                if "<!-- Ова место е резервирано за автоматската слика од Manim -->" not in content:
                    continue # Или нема placeholder или веќе е средено
                
                # Провери дали има код
                code = extract_manim_code(content)
                if code:
                    print(f"🔍 Found Manim code in: {file}")
                    filename_base = file.replace(".md", "")
                    
                    # Рендерирај
                    image_name = run_manim(code, filename_base)
                    
                    if image_name:
                        if update_markdown_with_image(path, image_name):
                            processed_count += 1
                            print(f"   📊 Progress: {processed_count}/{BATCH_SIZE}")

if __name__ == "__main__":
    main()
