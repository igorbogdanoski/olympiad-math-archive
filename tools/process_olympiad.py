import os
import re
import subprocess
import shutil
import sys
import datetime
import ast
import json
from pathlib import Path

# Обид за импорт на локални модули
try:
    import indexer
    from manim_utils import fix_manim_common_errors, sanitize_for_latex_free
except ImportError:
    # Ако не може да го најде директно, додај ја tools папката во path
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    import indexer
    from manim_utils import fix_manim_common_errors, sanitize_for_latex_free

# Обид за импорт на frontmatter
try:
    import frontmatter
except ImportError:
    print("❌ ГРЕШКА: Библиотеката 'python-frontmatter' не е инсталирана.")
    print("👉 Инсталирај ја со: pip install python-frontmatter")
    sys.exit(1)

class PlatinumProcessor:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir).resolve()
        self.output_dir = self.base_dir / "docs"
        # Adjusted assets path to match process_ai_problem.py if that's the preferred structure
        # In process_ai_problem.py it was: self.assets_dir = self.base_dir / "assets" / "images"
        # In process_olympiad.py it was: self.assets_dir = self.base_dir / "web" / "public" / "assets" / "images"
        # Let's check which one is used in the Astro app.
        self.assets_dir = self.base_dir / "web" / "public" / "assets" / "images"
        self.tools_dir = self.base_dir / "tools"
        self.archive_dir = self.tools_dir / "archive"
        self.index_file = self.base_dir / "web" / "src" / "data" / "problems.json"
        self.public_index_file = self.base_dir / "web" / "public" / "data" / "problems.json"
        self.videos_dir = self.base_dir / "media" / "videos"
        
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
            return False
        return True

    def extract_manim_code(self, content):
        """
        Екстрахира Manim код од Markdown содржина.
        """
        # Find '# Manim Code' followed by a code block
        manim_header_pattern = r'(?i)#\s*Manim Code.*?\n\s*```(?:python)?\s*\n'
        header_match = re.search(manim_header_pattern, content, re.DOTALL)

        if not header_match:
            return None, None

        # Start of code after the header
        code_start = header_match.end()

        # Find the closing ```
        remaining_content = content[code_start:]
        closing_match = re.search(r'\n\s*```\s*\n', remaining_content)

        if not closing_match:
            print("⚠️ Најдов почеток на Manim код, но не и крај (```).")
            # Fallback: take everything until end of file or next section
            code_content = remaining_content.split('\n#')[0].strip()
            full_block = content[header_match.start():]
            return code_content, full_block

        code_end = code_start + closing_match.start()

        # Extract code and full block
        code_content = content[code_start:code_end].strip()
        full_block = content[header_match.start():code_start + closing_match.end()]

        return code_content, full_block

    def sanitize_code_safe_mode(self, code):
        """Safe Mode: Ги отстранува LaTeX зависностите преку manim_utils."""
        print("🔧 SAFE MODE: Converting LaTeX to plain text...")
        return sanitize_for_latex_free(code)

    def find_scene_class(self, code):
        """Наоѓа било каква Scene класа."""
        match = re.search(r'class\s+(\w+)\(.*Scene\)', code)
        if match:
            return match.group(1)
        return None

    def run_manim(self, manim_code, problem_id):
        scene_name = self.find_scene_class(manim_code)
        if not scene_name:
            print("ERROR: Ne e pronajdena klasa sto nasleduva od Scene.")
            return None

        with open(self.manim_temp_script, 'w', encoding='utf-8') as f:
            f.write(manim_code)

        # Папка за специфичниот проблем
        problem_assets_dir = self.assets_dir / problem_id
        problem_assets_dir.mkdir(parents=True, exist_ok=True)
        
        # Конечна патека каде ја очекуваме сликата
        final_image_path = problem_assets_dir / f"{problem_id}.png"

        # Команда за Manim
        # -qh = Quality High (1080p)
        cmd = [
            "manim", "-qh", "-s", "--disable_caching",
            str(self.manim_temp_script), scene_name,
            "--media_dir", str(self.manim_media_temp),
            "-o", f"{problem_id}.png" # Го форсираме името на фајлот
        ]

        print(f"Rendering illustration for: {problem_id}...")
        
        # --- ОБИД 1 ---
        # Fixed: capture_output and text=True can cause encoding issues on Windows with some Manim outputs
        # Using encoding='utf-8' and errors='replace' for robustness
        result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
        
        success = False
        
        # Проверка дали фајлот е генериран (Manim понекогаш го закопува длабоко)
        generated_files = list(self.manim_media_temp.rglob(f"{problem_id}.png"))
        
        if result.returncode == 0 and generated_files:
            success = True
        else:
            # --- ОБИД 2 (Safe Mode) ---
            print("WARNING: Prviot obid ne uspea. Probuvam Safe Mode...")
            if result.returncode != 0:
                print(f"Error: {result.stderr[-300:]}") 

            safe_code = self.sanitize_code_safe_mode(manim_code)
            with open(self.manim_temp_script, 'w', encoding='utf-8') as f:
                f.write(safe_code)
            
            result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
            generated_files = list(self.manim_media_temp.rglob(f"{problem_id}.png"))
            
            if result.returncode == 0 and generated_files:
                success = True
            else:
                print("FATAL: Manim ne uspea da generira slika.")
                print(r"--- LOG START ---")
                print(result.stderr[-1000:])
                print(r"--- LOG END ---")
                return None

        # Преместување на сликата
        if success and generated_files:
            source_img = generated_files[0]
            shutil.move(str(source_img), str(final_image_path))
            print(f"OK: Slika e kreirana: {final_image_path.name}")
            # Correct relative path for the web (assuming /assets/images is public)
            return f"/assets/images/{problem_id}/{problem_id}.png"
        
        return None

    def fix_manim_code_logic(self, code):
        """Fixes common Manim AI errors via manim_utils"""
        print("🔧 Applying automated fixes to Manim code...")
        return fix_manim_common_errors(code)

    def convert_steps_to_accordion(self, content):
        """Претвора чекор по чекор форматот во collapsible details/summary."""
        # Наоѓање на "## Чекор по чекор" секцијата
        step_pattern = r'(## Чекор по чекор\n\n)(.*?)(\n\n##|$)'
        match = re.search(step_pattern, content, re.DOTALL)

        if not match:
            return content

        steps_section = match.group(2)

        # Претворање на секој чекор во details/summary
        # Наоѓање на сите чекори (bold headers со "**Чекор X:**")
        step_regex = r'\*\*Чекор (\d+): ([^*]+)\*\*\n(.*?)(?=\n\*\*Чекор \d+:|\n\n##|$)'
        steps = re.findall(step_regex, steps_section, re.DOTALL)

        if not steps:
            return content

        # Градење на нова accordion секција
        accordion_content = "## 📐 Детално Решение\n\n"

        for step_num, step_title, step_content in steps:
            # Чистење на содржината (отстранување на вишок празни редови)
            step_content = step_content.strip()
            accordion_content += f'<details>\n<summary>Чекор {step_num}: {step_title.strip()}</summary>\n\n{step_content}\n\n</details>\n\n'

        # Замена на оригиналната секција
        new_content = content.replace(match.group(0), accordion_content + match.group(3))

        return new_content

    def convert_pedagogical_notes_to_accordion(self, content):
        """Претвора Pedagogical Notes секцијата во collapsible details/summary."""
        # Наоѓање на "# Pedagogical Notes" секцијата - може да биде на крајот од фајлот
        notes_pattern = r'# Pedagogical Notes\n\n(.*)'
        match = re.search(notes_pattern, content, re.DOTALL)

        if not match:
            return content

        notes_section = match.group(1).strip()

        # Ако веќе има details/summary формат, не го менувај
        if '<details>' in notes_section or '<summary>' in notes_section:
            return content

        # Градење на нова accordion секција
        accordion_content = f'# Pedagogical Notes\n\n<details>\n<summary>Педагошки забелешки</summary>\n\n{notes_section}\n\n</details>'

        # Замена на оригиналната секција
        new_content = content.replace(match.group(0), accordion_content)

        return new_content

    def update_markdown_content(self, post, image_rel_path, raw_manim_block):
        """Го брише Manim кодот и додава линк до сликата."""
        content = post.content

        # 1. Претворање на чекори во accordion формат
        content = self.convert_steps_to_accordion(content)

        # 2. Претворање на Pedagogical Notes во accordion формат
        content = self.convert_pedagogical_notes_to_accordion(content)

        # 3. Бришење на кодот (Користиме replace со точниот блок што го најдовме претходно)
        if raw_manim_block:
            content = content.replace(raw_manim_block, "")

        # Чистење на заостанати празни редови и Manim секции ако останале
        content = re.sub(r'(?i)#\s*Manim Code\s*', '', content).strip()

        # 4. Вметнување на слика
        # Сликата ја ставаме пред "Менторски Белешки" или на крај ако нема белешки
        if image_rel_path:
            image_md = f"\n\n---\n### 🎨 Визуелизација\n![Илустрација]({image_rel_path})\n"

            if "## 👨‍🏫 Менторски Белешки" in content:
                content = content.replace("## 👨‍🏫 Менторски Белешки", image_md + "\n## 👨‍🏫 Менторски Белешки")
            elif "## Pedagogical Notes" in content:
                content = content.replace("## Pedagogical Notes", image_md + "\n## Pedagogical Notes")
            elif "## Решение" in content:
                 # Ако нема менторски, пробај после решение
                 content += image_md
            else:
                 content += image_md
        else:
            print("WARNING: Image was not generated and not added to file.")

        post.content = content
        return post

    def archive_input_file(self, input_path):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = input_path.stem
        archive_name = f"{timestamp}_{filename}.md"
        target_path = self.archive_dir / archive_name
        
        shutil.move(str(input_path), str(target_path))
        with open(input_path, 'w', encoding='utf-8') as f:
            f.write("") 
        print(f"Archived in: {archive_name}")

    def cleanup(self):
        if self.manim_temp_script.exists():
            self.manim_temp_script.unlink()
        if self.manim_media_temp.exists():
            shutil.rmtree(self.manim_media_temp, ignore_errors=True)

    def check_for_videos(self, problem_id):
        """Проверува дали постојат видеа за овој проблем."""
        video_extensions = [".mp4", ".mov", ".webm"]
        # Бараме во media/videos и подпапки
        for ext in video_extensions:
            video_files = list(self.videos_dir.rglob(f"{problem_id}{ext}"))
            if video_files:
                # Враќаме релативна патека за вебот
                rel_path = video_files[0].relative_to(self.base_dir).as_posix()
                return f"/{rel_path}"
        return None

    def update_web_index(self):
        """Го ажурира централниот JSON индекс за вебот."""
        print("Updating web index...")
        try:
            problems = indexer.build_index(str(self.base_dir))
            indexer.save_index(problems, str(self.index_file))
            # Ажурирај го и јавниот индекс за Teachers алатката
            self.public_index_file.parent.mkdir(parents=True, exist_ok=True)
            indexer.save_index(problems, str(self.public_index_file))
            print(f"SUCCESS: Index updated with {len(problems)} tasks.")
        except Exception as e:
            print(f"WARNING: Error updating index: {e}")

    def validate_input(self, post):
        pid = post.metadata.get('problem_id')
        if not pid or pid == 'unknown':
            print("STOP: Missing 'problem_id'.")
            return False
        return True

    def check_python_syntax(self, code):
        """Enhanced validation for Manim code with more detailed error checking."""
        try:
            # First check basic Python syntax
            ast.parse(code)
            # Additional checks for common Manim issues
            if "from manim import" not in code:
                return "Missing Manim import statement"
            if "class " not in code:
                return "No Scene class defined"
            if "Scene" not in code:
                return "Scene class not inherited"
            if "def construct(self):" not in code:
                return "construct method not found"
            return None
        except SyntaxError as e:
            return f"Syntax Error: {e}"
        except Exception as e:
            return f"Code validation error: {e}"

    def process_file(self, input_file):
        """Process a single input file."""
        if not self.check_system(): return

        input_path = Path(input_file).resolve()
        if not input_path.exists():
            print(f"❌ Фајлот не постои: {input_path}")
            return

        with open(input_path, 'r', encoding='utf-8') as f:
            content_raw = f.read().strip()

        if not content_raw:
            print("WARNING: File is empty.")
            return

        try:
            post = frontmatter.loads(content_raw)
        except Exception as e:
            print(f"ERROR: YAML error: {e}")
            return

        # --- AUTO-GENERATE ID IF MISSING ---
        if not post.metadata.get('problem_id') or post.metadata.get('problem_id') == 'unknown':
            new_id = f"prob_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
            post.metadata['problem_id'] = new_id
            print(f"ID: Generated new ID: {new_id}")

        if not self.validate_input(post): return

        problem_id = post.metadata.get('problem_id')
        grade = post.metadata.get('grade', 'other')
        p_type = post.metadata.get('type', 'general')

        # Проверка за видео пред процесирање
        video_url = self.check_for_videos(problem_id)
        if video_url:
            post.metadata['video_url'] = video_url
            print(f"VIDEO: Found video: {video_url}")

        print(f"PROCESSING: ID: {problem_id} | Grade: {grade}")

        # --- EXTRACT CODE ---
        # Сега extract_manim_code враќа ДВЕ работи: самиот код и целиот блок текст за бришење
        manim_code, full_raw_block = self.extract_manim_code(post.content)

        image_path = None
        if manim_code:
            manim_code = self.fix_manim_code_logic(manim_code)
            syntax_error = self.check_python_syntax(manim_code)
            if syntax_error:
                print(f"ERROR: {syntax_error}")
            else:
                image_path = self.run_manim(manim_code, problem_id)
        else:
            print("INFO: No Manim code.")

        # --- UPDATE CONTENT ---
        # Го подаваме full_raw_block за да знае што точно да избрише
        updated_post = self.update_markdown_content(post, image_path, full_raw_block)

        save_dir = self.output_dir / f"grade_{grade}" / p_type
        save_dir.mkdir(parents=True, exist_ok=True)
        save_path = save_dir / f"{problem_id}.md"

        with open(save_path, 'w', encoding='utf-8') as f:
            f.write(frontmatter.dumps(updated_post))

        print(f"SAVED: {save_path.name}")
        self.archive_input_file(input_path)
        self.cleanup()

        # --- АЖУРИРАЊЕ НА ВЕБ ИНДЕКСОТ ---
        self.update_web_index()

        print("DONE!")

    def process_batch(self, input_files):
        """Process multiple input files with optimized batch handling."""
        if not self.check_system(): return

        successful = 0
        failed = 0

        print(f"🔄 Starting batch processing of {len(input_files)} files...")

        for i, input_file in enumerate(input_files, 1):
            print(f"\n{'='*50}")
            print(f"BATCH: Processing file {i}/{len(input_files)}")
            print(f"{'='*50}")

            try:
                self.process_file(input_file)
                successful += 1
            except Exception as e:
                print(f"❌ Failed to process {input_file}: {e}")
                failed += 1

        print(f"\n{'='*60}")
        print("BATCH PROCESSING COMPLETE")
        print(f"✅ Successful: {successful}")
        print(f"❌ Failed: {failed}")
        print(f"📊 Total: {len(input_files)}")
        print(f"{'='*60}")

        # Final index update after batch
        if successful > 0:
            print("\n🔄 Performing final web index update...")
            self.update_web_index()

if __name__ == "__main__":
    import io
    # Handle Windows encoding
    if sys.stdout.encoding != 'utf-8':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    BASE_DIR = Path(__file__).parent.parent

    print("="*60)
    print("PLATINUM PROCESSOR - IMPROVED")
    print("="*60)

    processor = PlatinumProcessor(BASE_DIR)

    # Check command line arguments for batch processing
    if len(sys.argv) > 1:
        # Batch mode: process multiple files
        input_files = []
        for arg in sys.argv[1:]:
            input_path = Path(arg).resolve()
            if input_path.exists() and input_path.suffix.lower() == '.md':
                input_files.append(str(input_path))
            else:
                print(f"⚠️ Skipping invalid file: {arg}")

        if input_files:
            processor.process_batch(input_files)
        else:
            print("❌ No valid input files provided for batch processing.")
    else:
        # Single file mode (default behavior)
        INPUT_FILE = BASE_DIR / "tools" / "new_problem_input.md"
        processor.process_file(INPUT_FILE)