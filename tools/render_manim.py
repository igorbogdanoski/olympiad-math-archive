import re
import os
import sys
import subprocess
import shutil
import tempfile
from pathlib import Path

# Обид за импорт на Manim. Ако го нема, враќаме грешка.
try:
    from manim import *
except ImportError:
    print("❌ Manim library not found. Install it via 'pip install manim'.")
    sys.exit(1)

# --- КОНФИГУРАЦИЈА ---
BASE_DIR = Path(__file__).parent.parent.absolute()
IMAGES_DIR = BASE_DIR / "assets" / "images"
LOG_FILE = PROJECT_ROOT / "assets" / "manim_code_log.md"

# Осигурај се дека папката постои
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

def parse_log_file():
    """Parses the log file and returns a list of (problem_id, code) tuples."""
    if not LOG_FILE.exists():
        print(f"Log file not found: {LOG_FILE}")
        return []

    content = LOG_FILE.read_text(encoding="utf-8")
    
    # Regex to find problem entries
    # Matches: ### 🆔 Задача: <ID> ... ```python <code> ```
    pattern = re.compile(
        r"### 🆔 Задача:\s*([a-zA-Z0-9_\-]+).*?```python\s+(.*?)```",
        re.DOTALL
    )
    
    entries = []
    for match in pattern.finditer(content):
        problem_id = match.group(1).strip()
        code = match.group(2)
        entries.append((problem_id, code))
    
    return entries

def wrap_code_in_class(code_body, class_name="SolutionScene"):
    """
    Го пакува 'суровиот' код (само командите) во целосна Manim класа.
    """
    return f"""
from manim import *

class {class_name}(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        # Глобални стилови за да изгледа како скица на хартија
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        Dot.set_default(color=BLACK)
        Line.set_default(color=BLACK)
        
        # --- USER CODE START ---
{code_body}
        # --- USER CODE END ---
"""

def clean_code(code):
    """
    Cleans up the extracted code to ensure it's a valid Manim script.
    """
    if "# --- AI GENERATED CODE START ---" in code:
        parts = code.split("# --- AI GENERATED CODE START ---")
        preamble = parts[0]
        generated = parts[1]
        
        # Check if generated code contains a full class definition
        if re.search(r"class\s+\w+\(Scene\):", generated):
            # Use the generated code as the source of truth
            # But ensure imports are there
            new_code = ""
            if "from manim import" not in generated:
                new_code += "from manim import *\n\n"
            new_code += generated
            code = new_code
        else:
            # Assume it's a method body or method definition
            # We need to wrap it in the class from preamble or a default one
            
            # 1. Get imports
            imports = "from manim import *\n"
            
            # 2. Get the body
            # Remove 'def construct(self):' line if present to avoid duplication when we wrap
            generated_lines = generated.split('\n')
            body_lines = []
            for line in generated_lines:
                if "def construct(self):" in line:
                    continue
                body_lines.append(line)
                
            # 3. Construct new file content
            final_code = imports
            final_code += f"\nclass ProblemScene(Scene):\n"
            final_code += "    def construct(self):\n"
            final_code += "        self.camera.background_color = WHITE\n"
            final_code += "        Text.set_default(color=BLACK)\n"
            final_code += "        MathTex.set_default(color=BLACK)\n"
            final_code += "        Mobject.set_default(color=BLACK)\n"
            
            for line in body_lines:
                # Fix indentation: Add 8 spaces
                if line.strip():
                    final_code += "        " + line.strip() + "\n"
            
            code = final_code

    # Common fixes for AI hallucinations
    # Remove background_line_style from Axes/NumberPlane as it causes TypeError in recent Manim versions
    code = re.sub(r"background_line_style\s*=\s*\{[^}]*\},?", "", code)
    
    return code

def render_scene(prob_id, code_body):
    """
    Ја рендира сликата и ја зачувува во assets/images/{prob_id}.png.
    Враќа True ако е успешно.
    """
    # 1. Креирај привремен фајл за оваа конкретна задача
    # Користиме tempfile за да нема конфликти при паралелно процесирање
    fd, temp_path = tempfile.mkstemp(suffix=".py", prefix=f"manim_{prob_id}_")
    
    try:
        # 2. Запиши го кодот во привремениот фајл
        full_code = wrap_code_in_class(code_body)
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            f.write(full_code)
            
        # 3. Конфигурирај го Manim
        # Користиме посебна media_dir за секој процес за да нема мешање
        temp_media_dir = Path(tempfile.gettempdir()) / f"manim_media_{prob_id}"
        
        config.media_dir = str(temp_media_dir)
        config.images_dir = str(temp_media_dir)
        config.verbosity = "ERROR"  # Само критични грешки, без спам
        config.pixel_height = 1080
        config.pixel_width = 1080
        config.frame_rate = 15      # Не е битно за слика, но забрзува иницијализација
        config.dry_run = False
        
        # 4. Рендирање
        # Ова е еквивалент на: manim -s -r 1080,1080 temp_file.py SolutionScene
        scene = Scene() # Dummy init to access config context if needed, but usually render() handles it
        
        # Најсигурен начин е преку command line interface wrapper на Manim
        # но за брзина ќе користиме директен Python повик ако е можно.
        # За жал, Manim config е глобален и тежок за ресетирање во thread-ови.
        # Затоа, најробусно за BATCH е subprocess.
        
        # --- SUBPROCESS APPROACH (Најстабилно за Batch) ---
        cmd = [
            sys.executable, "-m", "manim", 
            temp_path, "SolutionScene",
            "--format=png", "-s", # -s значи "save last frame only"
            "--media_dir", str(temp_media_dir),
            "--disable_caching" # За да сме сигурни дека го прави новото
        ]
        
        # Стартувај го Manim во тишина
        result = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True, 
            encoding='utf-8'
        )
        
        if result.returncode != 0:
            print(f"❌ Manim Error for {prob_id}:\n{result.stderr}")
            return False

        # 5. Најди ја сликата и премести ја
        # Manim ја става во: media_dir/videos/temp_path/1080p15/SolutionScene.png
        # Или за слики: media_dir/images/SolutionScene.png (зависи од верзијата)
        
        # Пребаруваме рекурзивно бидејќи Manim ги менува патеките често
        found_image = None
        for root, dirs, files in os.walk(temp_media_dir):
            for file in files:
                if file.endswith(".png") and "SolutionScene" in file:
                    found_image = Path(root) / file
                    break
            if found_image: break
            
        if found_image and found_image.exists():
            target_path = IMAGES_DIR / f"{prob_id}.png"
            shutil.move(str(found_image), str(target_path))
            return True
        else:
            print(f"❌ Сликата не беше пронајдена во output папката за {prob_id}")
            return False

    except Exception as e:
        print(f"❌ Exception во render_manim: {e}")
        return False
        
    finally:
        # 6. Чистење (Cleanup)
        # Избриши го Python фајлот
        if os.path.exists(temp_path):
            os.remove(temp_path)
        # Избриши ја привремена папка со видеа
        if os.path.exists(temp_media_dir):
            shutil.rmtree(temp_media_dir, ignore_errors=True)

def main():
    entries = parse_log_file()
    print(f"Found {len(entries)} entries.")
    
    for problem_id, code in entries:
        # Clean ID (remove extra text if any)
        problem_id = problem_id.split()[0] 
        render_scene(problem_id, code)
        
    # Cleanup
    if TEMP_SCENE_FILE.exists():
        os.remove(TEMP_SCENE_FILE)

# Тест блок (ако ја пуштиш само оваа скрипта)
if __name__ == "__main__":
    test_code = "self.add(Circle())"
    print("Тестирам рендирање...")
    if render_scene("test_001", test_code):
        print("✅ Тестот помина!")
    else:
        print("❌ Тестот не успеа.")
    main()
