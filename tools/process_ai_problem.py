import os
import re
import subprocess
import frontmatter
from pathlib import Path
import sys

class ProblemProcessor:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)
        self.problems_dir = self.base_dir / "problems"
        self.assets_dir = self.base_dir / "assets" / "animations"
        self.manim_temp = self.base_dir / "tools" / "temp_manim.py"
        self.tools_dir = self.base_dir / "tools"
        
        # Креирај ги папките ако не постојат
        self.assets_dir.mkdir(parents=True, exist_ok=True)
    
    def validate_synthetic_geometry(self, content):
        """Проверува дали решението користи забранети методи."""
        forbidden_patterns = [
            r'координат', r'complex', r'trigonometr', r'\bz\s*=', r'x\s*=.*y\s*='
        ]
        warnings = []
        for pattern in forbidden_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                warnings.append(f"⚠️ Можен проблем: Најдено '{pattern}' - проверете дали е синтетичко решение")
        return warnings
    
    def extract_manim_code(self, markdown_content):
        """Извлекува го Manim кодот од Markdown."""
        pattern = r'# Manim Code\s*```python\s*(.*?)```'
        match = re.search(pattern, markdown_content, re.DOTALL)
        return match.group(1).strip() if match else None
    
    def run_manim(self, manim_code, problem_id):
        """Извршува Manim код и генерира слика."""
        with open(self.manim_temp, 'w', encoding='utf-8') as f:
            f.write(manim_code)
        
        class_match = re.search(r'class\s+(\w+)\(Scene\)', manim_code)
        if not class_match:
            print("❌ Не можам да го најдам класот на сцената")
            return None
        
        scene_class = class_match.group(1)
        output_path = self.assets_dir / problem_id
        output_path.mkdir(exist_ok=True)
        
        cmd = [
            'manim', '-qm', '-o', f'{problem_id}.png', '--format', 'png',
            '--save_last_frame', str(self.manim_temp), scene_class
        ]
        
        print(f"🎬 Генерирам Manim анимација за {problem_id}...")
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=str(output_path))
            if result.returncode == 0:
                generated_files = list(output_path.glob('*.png'))
                if generated_files:
                    print(f"✅ Manim слика генерирана: {generated_files[0].name}")
                    return f"assets/animations/{problem_id}/{generated_files[0].name}"
            else:
                print(f"❌ Manim грешка:\n{result.stderr}")
                return None
        except FileNotFoundError:
            print("❌ Manim не е инсталиран (pip install manim).")
            return None
    
    def insert_image_in_markdown(self, content, image_path):
        """Вметнува слика во Markdown после 'Текст на задачата'."""
        pattern = r'(# Текст на задачата\n.*?\n)'
        replacement = rf'\1\n![Diagram](/{image_path})\n'
        return re.sub(pattern, replacement, content, flags=re.DOTALL, count=1)
    
    def categorize_problem(self, metadata):
        """Одредува во која папка да ја стави задачата."""
        problem_type = metadata.get('type', 'general')
        grade = metadata.get('grade', 0)
        
        category_map = {
            'geometry': 'geometry', 'algebra': 'algebra',
            'number_theory': 'number_theory', 'combinatorics': 'combinatorics',
            'logic': 'logic', 'logic_puzzle': 'logic'
        }
        
        main_category = category_map.get(problem_type, 'general')
        grade_folder = 'elementary' if grade <= 5 else 'junior' if grade <= 9 else 'senior'
        
        target_dir = self.problems_dir / main_category / grade_folder
        target_dir.mkdir(parents=True, exist_ok=True)
        return target_dir
    
    def process(self, input_file_path):
        """Главна функција за обработка."""
        print("="*60)
        print("🚀 OLYMPIAD PROBLEM PROCESSOR (FILE MODE)")
        print("="*60)
        
        # 1. Читање на фајлот
        input_path = Path(input_file_path)
        if not input_path.exists():
            # Ако не постои, креирај го празен и извести го корисникот
            input_path.touch()
            print(f"❌ Фајлот {input_path.name} е празен/нов.")
            print("👉 Ве молам залепете ја задачата од AI во овој фајл и зачувајте, па повикајте ја скриптата повторно.")
            return False

        with open(input_path, 'r', encoding='utf-8') as f:
            markdown_input = f.read()

        if not markdown_input.strip():
            print(f"❌ Фајлот {input_path.name} е празен.")
            print("👉 Залепете го кодот од AI Studio во него и зачувајте.")
            return False

        # 2. Парсирање
        try:
            post = frontmatter.loads(markdown_input)
            metadata = post.metadata
            content = post.content
            if not metadata: raise ValueError("Нема YAML хедeр")
        except Exception as e:
            print(f"❌ Грешка при парсирање (проверете го YAML форматот): {e}")
            return False
        
        problem_id = metadata.get('problem_id', 'unknown')
        print(f"\n📋 Обработувам: {metadata.get('title', 'Без наслов')}")
        print(f"   ID: {problem_id}")
        print(f"   Тип: {metadata.get('type', 'N/A')}")
        
        # 3. Валидација за синтетичка геометрија
        if metadata.get('type') == 'geometry':
            warnings = self.validate_synthetic_geometry(content)
            if warnings:
                print("\n⚠️  ПРЕДУПРЕДУВАЊА:")
                for w in warnings: print(f"   {w}")
                if input("\nПродолжи? (y/n): ").lower() != 'y': return False
        
        # 4. Manim Обработка
        manim_code = self.extract_manim_code(markdown_input)
        image_path = None
        
        if manim_code:
            image_path = self.run_manim(manim_code, problem_id)
            if image_path:
                full_content = frontmatter.dumps(post)
                full_content = self.insert_image_in_markdown(full_content, image_path)
                post = frontmatter.loads(full_content)
        else:
            print("ℹ️  Нема Manim код.")
        
        # 5. Зачувување
        target_dir = self.categorize_problem(metadata)
        output_file = target_dir / f"{problem_id}.md"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(frontmatter.dumps(post))
        
        print(f"\n✅ ЗАВРШЕНО! Задачата е преместена во:")
        print(f"   📂 {output_file}")
        
        # 6. Чистење на влезниот фајл (опционално, за да е спремен за нова)
        with open(input_path, 'w', encoding='utf-8') as f:
            f.write("") # Испразни го фајлот
        print(f"🧹 Влезниот фајл {input_path.name} е исчистен и спремен за нова задача.")
        print("="*60)
        return True

def main():
    base_dir = Path(__file__).parent.parent
    
    # Ова е фајлот во кој ќе ги лепите задачите
    input_filename = "new_problem_input.md"
    input_file_path = base_dir / "tools" / input_filename
    
    processor = ProblemProcessor(base_dir)
    processor.process(input_file_path)

if __name__ == "__main__":
    main()