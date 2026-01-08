import os
import re
import subprocess
import frontmatter
from pathlib import Path
import shutil
import sys

class ProblemProcessor:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)
        self.output_dir = self.base_dir / "docs"
        self.assets_dir = self.base_dir / "assets" / "images"
        self.manim_temp = self.base_dir / "tools" / "temp_manim.py"
        self.manim_media_temp = self.base_dir / "media_temp"
        
        # Креирај ги потребните фолдери
        self.assets_dir.mkdir(parents=True, exist_ok=True)

    def extract_manim_code(self, markdown_content):
        """
        Наоѓа Manim код дури и ако фалат наводници на крајот.
        """
        # 1. Обид: Стандарден блок затворен со наводници
        pattern_closed = r'(?i)#\s*Manim Code\s*\n\s*```(?:python)?\s*(.*?)```'
        match = re.search(pattern_closed, markdown_content, re.DOTALL)
        if match:
            return match.group(1).strip()
        
        # 2. Обид: Отворен блок до крајот на фајлот (Backup)
        pattern_open = r'(?i)#\s*Manim Code\s*\n\s*```(?:python)?\s*(.*)$'
        match = re.search(pattern_open, markdown_content, re.DOTALL)
        if match:
            print("⚠️  ПРЕДУПРЕДУВАЊЕ: Кодот не беше затворен со ```. Го преземам до крајот на фајлот.")
            return match.group(1).strip()
            
        return None
    
    def sanitize_code_for_no_latex(self, code):
        """
        Го менува кодот за да работи без LaTeX инсталација.
        """
        print("🔧 Правам 'Safe Mode' корекции на кодот (MathTex -> Text)...")
        # Замени MathTex со Text
        code = code.replace("MathTex", "Text")
        # Тргни LaTeX специфични работи ако прават проблем
        code = code.replace(r"\text", "")
        return code

    def run_manim(self, manim_code, problem_id):
        # 1. Зачувај го привремениот фајл
        with open(self.manim_temp, 'w', encoding='utf-8') as f:
            f.write(manim_code)
        
        # 2. Најди го името на класата
        class_match = re.search(r'class\s+(\w+)\(Scene\)', manim_code)
        if not class_match:
            print("❌ ГРЕШКА: Не можам да најдам 'class ImeNaScena(Scene)' во кодот.")
            return None
        scene_name = class_match.group(1)
        
        # 3. Дефинирај патека за излез
        output_folder = self.assets_dir / problem_id
        output_folder.mkdir(exist_ok=True, parents=True)
        
        # 4. Изврши Manim команда
        # -ql = Quality Low (побрзо render)
        # -s = Save Last Frame as Image (не прави видео)
        cmd = [
            "manim", "-ql", "-s", 
            str(self.manim_temp), scene_name,
            "--media_dir", str(self.manim_media_temp),
            "-o", f"{problem_id}.png"
        ]
        
        print(f"🎬 Генерирам илустрација за: {problem_id}...")
        
        # Прв обид: Нормален Manim
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        # Ако не успее (најчесто поради LaTeX), пробај втор пат со "Safe Mode"
        if result.returncode != 0:
            print(f"⚠️  Manim јави грешка (најверојатно недостасува LaTeX).")
            
            safe_code = self.sanitize_code_for_no_latex(manim_code)
            with open(self.manim_temp, 'w', encoding='utf-8') as f:
                f.write(safe_code)
                
            print("🔄 Втор обид со поедноставен код...")
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode != 0:
                print("❌ ГРЕШКА: И вториот обид не успеа.")
                print("------------- MANIM LOG -------------")
                print(result.stderr[-500:]) 
                print("-------------------------------------")
                return None

        # 5. Пронајди ја и премести ја сликата
        # Бараме рекурзивно во temp фолдерот
        found_images = list(self.manim_media_temp.rglob(f"{problem_id}.png"))
        
        if found_images:
            source_img = found_images[0]
            dest_img = output_folder / f"{problem_id}.png"
            shutil.move(str(source_img), str(dest_img))
            
            # Враќаме патека со forward slash (за компатибилност со Markdown)
            return f"assets/images/{problem_id}/{problem_id}.png"
        else:
            print("❌ ГРЕШКА: Manim заврши, но сликата не е пронајдена.")
            return None

    def remove_manim_block(self, content):
        """Брише сè од '# Manim Code' до крајот."""
        # 1. Затвори со наводници ако има
        pattern_closed = r'(?i)#\s*Manim Code\s*\n\s*```(?:python)?.*?```'
        content = re.sub(pattern_closed, '', content, flags=re.DOTALL)
        
        # 2. Ако нема наводници, бриши до крај на фајлот
        pattern_open = r'(?i)#\s*Manim Code\s*\n\s*```(?:python)?.*$'
        content = re.sub(pattern_open, '', content, flags=re.DOTALL)
        
        return content.strip()

    def insert_image_link(self, content, image_rel_path):
        if "![Илустрација]" in content: 
            return content
            
        insertion_point = "# Решение"
        image_markdown = f"\n![Илустрација]({image_rel_path})\n\n"
        
        if insertion_point in content:
            return content.replace(insertion_point, image_markdown + insertion_point)
        else:
            return content + image_markdown

    def cleanup(self):
        """Бришење на привремените фајлови"""
        if self.manim_temp.exists():
            self.manim_temp.unlink()
        if self.manim_media_temp.exists():
            shutil.rmtree(self.manim_media_temp, ignore_errors=True)
            print("🧹 Привремените фајлови се исчистени.")

    def categorize_and_save(self, post, problem_id):
        meta = post.metadata
        p_type = meta.get('type', 'general')
        grade = meta.get('grade', 'other')
        
        output_path = self.output_dir / f"grade_{grade}" / p_type
        output_path.mkdir(parents=True, exist_ok=True)
        final_file = output_path / f"{problem_id}.md"
        
        with open(final_file, 'w', encoding='utf-8') as f:
            f.write(frontmatter.dumps(post))
        
        print(f"✅ УСПЕХ! Задачата е зачувана во:")
        print(f"   📂 {final_file}")

    def process_file(self, input_file):
        input_path = Path(input_file)
        if not input_path.exists():
            print(f"❌ Фајлот {input_path} не постои.")
            return

        with open(input_path, 'r', encoding='utf-8') as f:
            content_raw = f.read()

        try:
            post = frontmatter.loads(content_raw)
        except Exception as e:
            print(f"❌ Грешка при читање на YAML метаподатоците: {e}")
            return

        problem_id = post.metadata.get('problem_id', 'unknown')
        print(f"⚙️  Обработка на ID: {problem_id}")

        # 1. Manim Processing
        manim_code = self.extract_manim_code(content_raw)
        
        if manim_code:
            image_path = self.run_manim(manim_code, problem_id)
            if image_path:
                new_content = self.remove_manim_block(post.content)
                new_content = self.insert_image_link(new_content, f"/{image_path}")
                post.content = new_content
            else:
                print("⚠️  Сликата не се генерираше, го задржувам оригиналниот текст.")
        else:
            print("ℹ️  Не е пронајден Manim код. Само го преместувам текстот.")
        
        # 2. Save
        self.categorize_and_save(post, problem_id)
        
        # 3. Reset Input File
        with open(input_path, 'w', encoding='utf-8') as f:
            f.write("")
        
        # 4. Clean Temp Files
        self.cleanup()

if __name__ == "__main__":
    BASE = Path(__file__).parent.parent
    INPUT_FILE = BASE / "tools" / "new_problem_input.md"
    
    print("="*50)
    print("🤖 OLYMPIAD PROBLEM PROCESSOR v2.0")
    print("="*50)
    
    proc = ProblemProcessor(BASE)
    proc.process_file(INPUT_FILE)
    print("="*50)