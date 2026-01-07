import os
import re
import subprocess
import frontmatter
from pathlib import Path
import sys

class ProblemProcessor:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)
        # ПРОМЕНА: Сега зачувуваме во 'docs' наместо во 'problems'
        self.output_dir = self.base_dir / "docs" 
        self.assets_dir = self.base_dir / "assets" / "animations"
        self.manim_temp = self.base_dir / "tools" / "temp_manim.py"
        
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
        pattern = r'# Manim Code\s*```python\s*(.*?)```'
        match = re.search(pattern, markdown_content, re.DOTALL)
        return match.group(1).strip() if match else None
    
    def run_manim(self, manim_code, problem_id):
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
        pattern = r'(# Текст на задачата\n.*?\n)'
        replacement = rf'\1\n![Diagram](/{image_path})\n'
        return re.sub(pattern, replacement, content, flags=re.DOTALL, count=1)
    
    def categorize_problem(self, metadata):
        """Одредува во која папка во 'docs' да ја стави задачата."""
        problem_type = metadata.get('type', 'general')
        grade = int(metadata.get('grade', 0)) # Осигурај се дека е int
        
        # Мапирање на типови (ако има разлика во имињата)
        category_map = {
            'geometry': 'geometry', 
            'algebra': 'algebra', 
            'number_theory': 'number_theory', 
            'combinatorics': 'combinatorics',
            'logic': 'logic', 
            'logic_puzzle': 'logic'
        }
        
        category_folder = category_map.get(problem_type, 'general')
        grade_folder = f"grade_{grade}"
        
        # ВРАЌАЊЕ НА СТАРАТА СТРУКТУРА: docs/grade_X/category
        target_dir = self.output_dir / grade_folder / category_folder
        target_dir.mkdir(parents=True, exist_ok=True)
        return target_dir
    
    def process(self, input_file_path):
        print("="*60)
        print("🚀 OLYMPIAD PROBLEM PROCESSOR (DOCS MODE)")
        print("="*60)
        
        input_path = Path(input_file_path)
        if not input_path.exists():
            input_path.touch()
            print(f"❌ Фајлот {input_path.name} е празен/нов.")
            return False

        with open(input_path, 'r', encoding='utf-8') as f:
            markdown_input = f.read()

        if not markdown_input.strip():
            print(f"❌ Фајлот {input_path.name} е празен.")
            return False

        try:
            post = frontmatter.loads(markdown_input)
            metadata = post.metadata
            content = post.content
        except Exception as e:
            print(f"❌ Грешка при парсирање YAML: {e}")
            return False
        
        problem_id = metadata.get('problem_id', 'unknown')
        print(f"\n📋 Обработувам: {metadata.get('title', 'Без наслов')}")
        print(f"   ID: {problem_id}")
        
        if metadata.get('type') == 'geometry':
            warnings = self.validate_synthetic_geometry(content)
            if warnings:
                print("\n⚠️  ПРЕДУПРЕДУВАЊА:")
                for w in warnings: print(f"   {w}")
                if input("\nПродолжи? (y/n): ").lower() != 'y': return False
        
        manim_code = self.extract_manim_code(markdown_input)
        image_path = None
        
        if manim_code:
            image_path = self.run_manim(manim_code, problem_id)
            if image_path:
                full_content = frontmatter.dumps(post)
                full_content = self.insert_image_in_markdown(full_content, image_path)
                post = frontmatter.loads(full_content)
        
        target_dir = self.categorize_problem(metadata)
        output_file = target_dir / f"{problem_id}.md"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(frontmatter.dumps(post))
        
        print(f"\n✅ ЗАВРШЕНО! Задачата е преместена во:")
        print(f"   📂 {output_file}")
        
        # Исчисти го влезниот фајл
        with open(input_path, 'w', encoding='utf-8') as f:
            f.write("")
        
        return True

def main():
    base_dir = Path(__file__).parent.parent
    input_filename = "new_problem_input.md"
    input_file_path = base_dir / "tools" / input_filename
    processor = ProblemProcessor(base_dir)
    processor.process(input_file_path)

if __name__ == "__main__":
    main()