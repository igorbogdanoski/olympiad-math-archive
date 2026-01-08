import os
import re
import subprocess
import shutil
import sys
import datetime
import ast
from pathlib import Path

# Обид за импорт на frontmatter
try:
    import frontmatter
except ImportError:
    print("❌ ГРЕШКА: Библиотеката 'python-frontmatter' не е инсталирана.")
    print("👉 Инсталирај ја со: pip install python-frontmatter")
    sys.exit(1)

class PlatinumProcessor:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)
        self.output_dir = self.base_dir / "docs"
        self.assets_dir = self.base_dir / "assets" / "images"
        self.tools_dir = self.base_dir / "tools"
        self.archive_dir = self.tools_dir / "archive"
        
        # Привремени патеки
        self.manim_temp_script = self.tools_dir / "temp_manim_render.py"
        self.manim_media_temp = self.tools_dir / "media_temp"

        # Креирање на потребните папки
        for folder in [self.output_dir, self.assets_dir, self.archive_dir, self.manim_media_temp]:
            folder.mkdir(parents=True, exist_ok=True)

    def check_system(self):
        """Проверува дали Manim е инсталиран во системот."""
        if not shutil.which("manim"):
            print("❌ КРИТИЧНА ГРЕШКА: Manim не е пронајден во системот!")
            print("👉 Инсталирај го или додај го во PATH.")
            return False
        return True

    def extract_manim_code(self, content):
        """
        ПОПРАВЕНА ВЕРЗИЈА: Не запира на линии што почнуваат со '#' 
        бидејќи тоа се често Python коментари.
        """
        # 1. Најди каде ПОЧНУВА кодот
        start_pattern = r'(?i)#\s*Manim Code\s*\n\s*```(?:python)?'
        match_start = re.search(start_pattern, content)
        
        if not match_start:
            return None

        # Ги земаме сите линии ПО почетокот
        raw_rest = content[match_start.end():]
        lines = raw_rest.splitlines()
        
        captured_lines = []
        code_closed_properly = False

        for line in lines:
            stripped = line.strip()
            
            # 1. Ако најдеме затворање на кодот (```)
            if stripped == "```":
                code_closed_properly = True
                break
            
            # 2. УСЛОВИ ЗА КРАЈ (STOP CONDITIONS)
            # ВНИМАНИЕ: Тргната е проверката за 'startswith("# ")' бидејќи тоа се Python коментари!
            # Запираме само на ## (Heading 2), ### (Heading 3) или --- (Horizontal Rule)
            if line.startswith("## ") or line.startswith("### ") or line.startswith("---"):
                print("⚠️  Детектирав нова секција. Го прекинувам читањето на кодот тука.")
                break
            
            # Ако линијата е празна, ја чуваме (за да не се расипе formatting-от)
            captured_lines.append(line)

        full_code = "\n".join(captured_lines).strip()
        
        if not code_closed_properly:
            print(f"🔧 АВТО-КОРЕКЦИЈА: Додадов '```' што недостасуваше на крајот.")
            
        return full_code

    def sanitize_code_safe_mode(self, code):
        """Напреден Safe Mode: Ги отстранува LaTeX зависностите."""
        print("🔧 Активирам SAFE MODE: Конверзија на LaTeX во обичен текст...")
        
        code = code.replace("MathTex", "Text")
        replacements = {
            r"\\": " ", r"\cdot": "*", r"\frac": "", 
            r"{": "", r"}": "", r"\boxed": ""
        }
        for old, new in replacements.items():
            code = code.replace(old, new)
        return code

    def find_scene_class(self, code):
        """Наоѓа било каква Scene класа."""
        match = re.search(r'class\s+(\w+)\(.*Scene\)', code)
        if match:
            return match.group(1)
        return None

    def run_manim(self, manim_code, problem_id):
        scene_name = self.find_scene_class(manim_code)
        if not scene_name:
            print("❌ ГРЕШКА: Не е пронајдена класа што наследува од Scene.")
            return None

        with open(self.manim_temp_script, 'w', encoding='utf-8') as f:
            f.write(manim_code)

        problem_assets_dir = self.assets_dir / problem_id
        problem_assets_dir.mkdir(parents=True, exist_ok=True)

        cmd = [
            "manim", "-ql", "-s", "-v", "WARNING",
            str(self.manim_temp_script), scene_name,
            "--media_dir", str(self.manim_media_temp),
            "-o", f"{problem_id}.png"
        ]

        print(f"🎬 Рендерирање на илустрација за: {problem_id}...")
        
        # --- ОБИД 1 ---
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        # --- ОБИД 2 (Safe Mode) ---
        if result.returncode != 0:
            print("⚠️  Грешка при рендерирање (најверојатно LaTeX).")
            safe_code = self.sanitize_code_safe_mode(manim_code)
            with open(self.manim_temp_script, 'w', encoding='utf-8') as f:
                f.write(safe_code)
            
            print("🔄 Втор обид (Safe Mode)...")
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode != 0:
                print("❌ FATAL: И вториот обид не успеа.")
                print("\n🔍 --- ДЕТАЛИ ЗА ГРЕШКАТА (LOG) ---")
                print(result.stderr[-1000:])
                print("-----------------------------------\n")
                return None

        # Преместување на сликата
        generated_image = list(self.manim_media_temp.rglob(f"{problem_id}.png"))
        
        if generated_image:
            final_path = problem_assets_dir / f"{problem_id}.png"
            shutil.move(str(generated_image[0]), str(final_path))
            print(f"✅ Сликата е креирана: {final_path.name}")
            return f"/assets/images/{problem_id}/{problem_id}.png"
        else:
            print("❌ Сликата не беше пронајдена по рендерирањето.")
            return None

    def update_markdown_content(self, post, image_rel_path):
        """Го брише Manim кодот и додава линк до сликата."""
        content = post.content
        # Бришење на кодот
        content = re.sub(r'(?i)#\s*Manim Code.*$', '', content, flags=re.DOTALL).strip()
        
        # Вметнување на слика
        if image_rel_path and "![Илустрација]" not in content:
            image_md = f"\n\n---\n### 🎨 Визуелизација\n![Илустрација]({image_rel_path})\n"
            if "## 👨‍🏫 Менторски Белешки" in content:
                content = content.replace("## 👨‍🏫 Менторски Белешки", image_md + "\n## 👨‍🏫 Менторски Белешки")
            else:
                content += image_md
        
        post.content = content
        return post

    def archive_input_file(self, input_path):
        """Го преместува фајлот во Archive и креира нов празен."""
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = input_path.stem
        archive_name = f"{timestamp}_{filename}.md"
        target_path = self.archive_dir / archive_name
        
        shutil.move(str(input_path), str(target_path))
        print(f"📦 Оригиналниот фајл е безбедно архивиран во: tools/archive/{archive_name}")
        
        with open(input_path, 'w', encoding='utf-8') as f:
            f.write("") # Reset
        print(f"🔄 Креиран е нов, чист фајл: {input_path.name} за следната задача.")

    def cleanup(self):
        """Чистење на ѓубрето."""
        if self.manim_temp_script.exists():
            self.manim_temp_script.unlink()
        if self.manim_media_temp.exists():
            shutil.rmtree(self.manim_media_temp, ignore_errors=True)

    def validate_input(self, post):
        """Валидација на задолжителните полиња."""
        pid = post.metadata.get('problem_id')
        if not pid or pid == 'unknown':
            print("⛔ СТОП! Недостасува 'problem_id' во задачата.")
            print("👉 Ве молиме пополнете го полето problem_id пред процесирање.")
            return False
        return True

    def check_python_syntax(self, code):
        """
        Проверува дали дадениот Python код е синтаксно валиден.
        Враќа None ако е валиден, или порака за грешка ако не е.
        """
        try:
            ast.parse(code)
            return None
        except SyntaxError as e:
            return f"Синтаксна грешка во Manim кодот: {e}"

    def fix_manim_code(self, code):
        """
        Автоматски ги заменува:
        - Line(..., stroke_dash_pattern=...) -> DashedLine(...)
        - Аргументи quadrant=1 -> quadrant=[1, -1] (или tuple)
        """
        import re

        # 1. Замени stroke_dash_pattern со DashedLine
        pattern = r'Line\(([^)]*),\s*stroke_dash_pattern\s*=\s*([^\),]+)([^)]*)\)'
        def replacer(match):
            before = match.group(1)
            after = match.group(3)
            return f'DashedLine({before}{after})'
        code = re.sub(pattern, replacer, code)

        # 2. Поправи quadrant=1 -> quadrant=[1, -1]
        code = re.sub(r'quadrant\s*=\s*([0-9]+)', r'quadrant=[1, -1]', code)

        return code

    def process_file(self, input_file):
        if not self.check_system():
            return

        input_path = Path(input_file)
        if not input_path.exists():
            print(f"❌ Влезниот фајл не постои: {input_path}")
            return

        print(f"\n📂 Отворам фајл: {input_path.name}")
        
        with open(input_path, 'r', encoding='utf-8') as f:
            content_raw = f.read().strip()
            
        if not content_raw:
            print("⚠️  Фајлот е празен. Чекам нова задача...")
            return

        try:
            post = frontmatter.loads(content_raw)
        except Exception as e:
            print(f"❌ Грешка во YAML форматот: {e}")
            return

        # ВАЛИДАЦИЈА
        if not self.validate_input(post):
            return

        problem_id = post.metadata.get('problem_id')
        grade = post.metadata.get('grade', 'other')
        p_type = post.metadata.get('type', 'general')

        print(f"⚙️  ID: {problem_id} | Клас: {grade} | Тип: {p_type}")

        # --- MANIM ---
        manim_code = self.extract_manim_code(post.content)
        if manim_code:
            # 1. Автоматска корекција на познати Manim багови
            manim_code = self.fix_manim_code(manim_code)
            # 2. Синтаксна проверка
            syntax_error = self.check_python_syntax(manim_code)
            if syntax_error:
                print(f"❌ {syntax_error}")
                print("⛔ Manim нема да се изврши поради синтаксна грешка.")
                image_path = None
            else:
                image_path = self.run_manim(manim_code, problem_id)
        else:
            print("ℹ️  Нема Manim код во оваа задача.")
            image_path = None

        # --- UPDATE & SAVE ---
        updated_post = self.update_markdown_content(post, image_path)
        
        save_dir = self.output_dir / f"grade_{grade}" / p_type
        save_dir.mkdir(parents=True, exist_ok=True)
        save_path = save_dir / f"{problem_id}.md"

        with open(save_path, 'w', encoding='utf-8') as f:
            f.write(frontmatter.dumps(updated_post))
        
        print(f"💾 Задачата е зачувана: {save_path}")

        # --- ARCHIVE ---
        self.archive_input_file(input_path)
        self.cleanup()
        print("✨ Процесот заврши успешно!\n")

if __name__ == "__main__":
    BASE_DIR = Path(__file__).parent.parent
    INPUT_FILE = BASE_DIR / "tools" / "new_problem_input.md"
    
    print("="*60)
    print("💎 PLATINUM OLYMPIAD PROCESSOR - IGOR'S EDITION (FINAL) 💎")
    print("="*60)
    
    processor = PlatinumProcessor(BASE_DIR)
    processor.process_file(INPUT_FILE)