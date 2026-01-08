import os
import re
import subprocess
import frontmatter
from pathlib import Path
import shutil

class ProblemProcessor:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)
        self.output_dir = self.base_dir / "docs" 
        self.assets_dir = self.base_dir / "assets" / "images" 
        self.manim_temp = self.base_dir / "tools" / "temp_manim.py"
        self.assets_dir.mkdir(parents=True, exist_ok=True)
    
    def sanitize_manim_code(self, code):
        """
        Прави брзи поправки на кодот за да избегне LaTeX грешки ако нема инсталација.
        Заменува MathTex со Text.
        """
        # Ако претходно не успеало, пробај да замениш MathTex со Text
        # Ова е "нечиста" поправка, но врши работа за генерирање слика
        # code = code.replace("MathTex", "Text")
        # code = code.replace(r"\text{", "").replace("}", "") # Тргање на LaTeX команди
        return code

    def extract_manim_code(self, markdown_content):
        # Бараме блок што почнува со # Manim Code
        # и содржи ```python ... ```
        pattern = r'(?i)#\s*Manim Code\s*\n\s*```(?:python)?\s*(.*?)```'
        match = re.search(pattern, markdown_content, re.DOTALL)
        if match:
            return match.group(1).strip()
        return None
    
    def run_manim(self, manim_code, problem_id):
        # 1. Зачувај го привремениот фајл
        with open(self.manim_temp, 'w', encoding='utf-8') as f:
            f.write(manim_code)
        
        # 2. Најди го името на класата
        class_match = re.search(r'class\s+(\w+)\(Scene\)', manim_code)
        if not class_match:
            print("❌ Не можам да најдам 'class SceneName(Scene)' во кодот.")
            return None
        scene_name = class_match.group(1)
        
        # 3. Дефинирај патека за излез
        output_folder = self.assets_dir / problem_id
        output_folder.mkdir(exist_ok=True, parents=True)
        
        # 4. Изврши Manim команда (-s за слика, -ql за брзина)
        # --media_dir ги насочува привремените фајлови
        # -o го дефинира името на излезната слика
        cmd = [
            "manim", "-ql", "-s", 
            str(self.manim_temp), scene_name,
            "--media_dir", str(self.base_dir / "media_temp"), # Temp folder we can delete later
            "-o", f"{problem_id}.png"
        ]
        
        print(f"🎨 Генерирам илустрација за {problem_id}...")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode != 0:
            print("⚠️ Грешка при Manim. Обид 2: Без LaTeX...")
            # Fallback: Пробај со "Text" наместо "MathTex" ако пукнало за LaTeX
            safe_code = manim_code.replace("MathTex", "Text")
            with open(self.manim_temp, 'w', encoding='utf-8') as f:
                f.write(safe_code)
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode != 0:
                print(f"❌ Неуспешно генерирање. Грешка:\n{result.stderr[-300:]}") # Покажи ги последните 300 карактери
                return None

        # 5. Пронајди ја сликата и премести ја каде што треба
        # Manim ја става во media_temp/images/temp_manim/problem_id.png
        # Но со -o, понекогаш е потешко да се најде точно каде завршила.
        # Најсигурно е да пребараме низ media_temp
        
        found_images = list((self.base_dir / "media_temp").rglob(f"{problem_id}.png"))
        
        if found_images:
            source_img = found_images[0]
            dest_img = output_folder / f"{problem_id}.png"
            shutil.move(str(source_img), str(dest_img))
            
            # Враќаме релативна патека за Markdown (Linux style forward slashes)
            return f"assets/images/{problem_id}/{problem_id}.png"
        else:
            print("❌ Manim заврши, но не ја наоѓам сликата.")
            return None

    def remove_manim_block(self, content):
        pattern = r'(?i)#\s*Manim Code\s*\n\s*```(?:python)?.*?```'
        # Заменуваме со празен стринг
        return re.sub(pattern, '', content, flags=re.DOTALL).strip()

    def insert_image_link(self, content, image_rel_path):
        # Вметни ја сликата веднаш по текстот на задачата
        # Бараме "# Решение" и вметнуваме пред него
        if "![Илустрација]" in content: 
            return content # Веќе има слика
            
        insertion_point = "# Решение"
        image_markdown = f"\n![Илустрација]({image_rel_path})\n\n"
        
        if insertion_point in content:
            return content.replace(insertion_point, image_markdown + insertion_point)
        else:
            # Ако нема # Решение, додај на крај на "Текст на задачата"
            return content + image_markdown

    def categorize_and_save(self, post, problem_id):
        meta = post.metadata
        p_type = meta.get('type', 'general')
        grade = meta.get('grade', 'other')
        
        output_path = self.output_dir / f"grade_{grade}" / p_type
        output_path.mkdir(parents=True, exist_ok=True)
        
        final_file = output_path / f"{problem_id}.md"
        
        with open(final_file, 'w', encoding='utf-8') as f:
            f.write(frontmatter.dumps(post))
        
        print(f"✅ Задачата е зачувана во: {final_file}")

    def process_file(self, input_file):
        input_path = Path(input_file)
        if not input_path.exists():
            print("Фајлот не постои.")
            return

        with open(input_path, 'r', encoding='utf-8') as f:
            content_raw = f.read()

        try:
            post = frontmatter.loads(content_raw)
        except:
            print("❌ Грешка при читање на YAML метаподатоците.")
            return

        problem_id = post.metadata.get('problem_id', 'unknown')
        print(f"--- Обработка на: {problem_id} ---")

        # 1. Извади код
        manim_code = self.extract_manim_code(content_raw)
        
        if manim_code:
            # 2. Генерирај слика
            image_path = self.run_manim(manim_code, problem_id)
            
            if image_path:
                # 3. Ако успешно, модифицирај ја содржината
                new_content = self.remove_manim_block(post.content)
                new_content = self.insert_image_link(new_content, f"/{image_path}") # Додаваме / за апсолутна патека од root
                post.content = new_content
        
        # 4. Зачувај го финалниот фајл
        self.categorize_and_save(post, problem_id)
        
        # 5. Исчисти го влезниот фајл (за да знаеме дека е готово)
        with open(input_path, 'w', encoding='utf-8') as f:
            f.write("")

if __name__ == "__main__":
    # Патеки
    BASE = Path(__file__).parent.parent
    INPUT_FILE = BASE / "tools" / "new_problem_input.md"
    
    proc = ProblemProcessor(BASE)
    proc.process_file(INPUT_FILE)