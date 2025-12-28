import re
import os
import sys
import shutil
import tempfile
import subprocess
from pathlib import Path

# Обид за импорт на Manим
try:
    from manim import *
except ImportError:
    # Ова е само за проверка, вистинското рендирање оди преку subprocess
    pass

# --- КОНФИГУРАЦИЈА (АЖУРИРАНА ЗА DOCS) ---
BASE_DIR = Path(__file__).parent.parent.absolute()
DOCS_DIR = BASE_DIR / "docs"  # <--- НОВО
IMAGES_DIR = DOCS_DIR / "assets" / "images" # <--- НОВО

# Креирање на папката ако не постои
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

def wrap_code_in_class(code_body, class_name="SolutionScene"):
    """
    Го пакува 'суровиот' код во целосна Manim класа.
    """
    return f"""
from manim import *

class {class_name}(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        # Глобални стилови
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        Dot.set_default(color=BLACK)
        Line.set_default(color=BLACK)
        
        # --- USER CODE START ---
{code_body}
        # --- USER CODE END ---
"""

def render_scene(prob_id, code_body):
    """
    Ја рендира сликата и ја зачувува во assets/images/{prob_id}.png.
    """
    # 1. Креирај привремен фајл
    fd, temp_path = tempfile.mkstemp(suffix=".py", prefix=f"manim_{prob_id}_")
    
    try:
        # 2. Запиши го кодот
        full_code = wrap_code_in_class(code_body)
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            f.write(full_code)
            
        # 3. Конфигурирај привремена папка за media
        temp_media_dir = Path(tempfile.gettempdir()) / f"manim_media_{prob_id}"
        
        # 4. Стартувај го Manim преку subprocess (најбезбедно)
        cmd = [
            sys.executable, "-m", "manim", 
            temp_path, "SolutionScene",
            "--format=png", "-s", 
            "--media_dir", str(temp_media_dir),
            "--disable_caching"
        ]
        
        # Изврши тивко (capture_output=True)
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
            print(f"❌ Сликата не беше пронајдена за {prob_id}")
            return False

    except Exception as e:
        print(f"❌ Exception во render_manim: {e}")
        return False
        
    finally:
        # 6. Чистење
        if os.path.exists(temp_path):
            os.remove(temp_path)
        if os.path.exists(temp_media_dir):
            shutil.rmtree(temp_media_dir, ignore_errors=True)

if __name__ == "__main__":
    print("Оваа скрипта се користи како модул.")
