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
        # ...existing code...

    def check_for_videos(self, problem_id):
        """Stub: Returns None. Implement video lookup if needed."""
        return None
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
        Екстрахира Manim код од Markdown содржина и го враќа целиот блок за бришење.
        """
        # 1. Наоѓање на хедерот '# Manim Code' и почетокот на кодот
        manim_header_pattern = r'(?i)#\s*Manim Code.*?\n\s*```(?:python)?\s*\n'
        header_match = re.search(manim_header_pattern, content, re.DOTALL)

        if not header_match:
            return None, None

        # Почетокот на самиот Python код (веднаш по ```)
        code_start = header_match.end()
        remaining_content = content[code_start:]

        # 2. Наоѓање на затворачките ```
        # ПОПРАВКА: Regex сега фаќа ``` дури и ако се на самиот крај на фајлот ($)
        closing_match = re.search(r'\n\s*```\s*(\n|$)', remaining_content)

        if not closing_match:
            print("⚠️ Најдов почеток на Manim код, но не и крај (```).")
            # Fallback: земи сè до крајот
            code_content = remaining_content.strip()
            full_block = content[header_match.start():]
            return code_content, full_block

        # 3. Пресметување на точните индекси
        code_end = code_start + closing_match.start()
        
        # block_end е крајот на затворачките наводници
        # Ова осигурува дека `full_block` ги содржи и последните ```
        block_end = code_start + closing_match.end()

        # Екстракција
        code_content = content[code_start:code_end].strip()
        full_block = content[header_match.start():block_end]

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
        """
        Fixes common Manim AI errors via manim_utils and додава auto-comments/warnings за напредни техники.
        """
        print("🔧 Applying automated fixes to Manim code...")
        fixed_code = fix_manim_common_errors(code)

        # Auto-comment/warning logic for expert Manim techniques

        expert_patterns = [
            # Напредни Manim техники и best practices
            (r'apply_complex_function',
             '# Совет: За мазно нелинеарно виткање користи prepare_for_nonlinear_transform пред apply_complex_function.'),
            (r'apply_matrix',
             '# Совет: За линеарни трансформации користи grid.prepare_for_nonlinear_transform() ако има нелинеарни деформации.'),
            (r'always_redraw',
             '# Совет: always_redraw е одличен за динамички објекти, но внимавај на перформанси ако има многу објекти.'),
            (r'f_always',
             '# Совет: f_always е најдобар за динамички вредности (на пр. DecimalNumber).'),
            (r'get_grid',
             '# Совет: get_grid е најбрз начин за создавање мрежа од објекти.'),
            (r'i2gp|input_to_graph_point',
             '# Совет: i2gp овозможува точка да се движи по графикон со ValueTracker.'),
            (r'TransformMatchingTex.*path_arc',
             '# Совет: path_arc овозможува поприродна ротација при трансформации на равенки.'),
            (r'ValueTracker',
             '# Совет: ValueTracker е основа за интерактивни анимации.'),
            (r'DecimalNumber',
             '# Совет: DecimalNumber е најдобар за динамички приказ на вредности.'),
            (r'next_slide\\s*\\\(.*loop\\s*=\\s*True',
             '# Совет: loop=True во next_slide овозможува бескрајни анимациски јамки во презентации.'),
            (r'on_mouse_motion',
             '# Совет: on_mouse_motion овозможува вистинска интерактивност со глушецот.'),
            (r'WindowEventLogger',
             '# Совет: WindowEventLogger помага за дебагирање на интерактивни сцени.'),
            # Нови напредни елементи од експертските совети
            (r'Brace',
             '# Совет: always_redraw(Brace, ...) овозможува заградите да се прилагодуваат динамички на објектот.'),
            (r'ComplexPlane',
             '# Совет: За комплексни мапирања користи ComplexPlane и prepare_for_nonlinear_transform.'),
            (r'Sphere|TexturedSurface',
             '# Совет: За 3D текстури користи TexturedSurface врз Sphere или Torus.'),
            (r'async def construct',
             '# Совет: Во Manim-Web (Pyodide) користи async/await за анимации.'),
            (r'VBox|Tab|ipywidgets|interact|interact_manual',
             '# Совет: За интерактивни Jupyter сцени користи ipywidgets и Tab за организација.'),
            (r'self\.embed\\(\\)',
             '# Совет: self.embed() овозможува директорски режим и live интеракција во ManimGL.'),
            (r'touch\\(\\)',
             '# Совет: touch() овозможува рачна навигација и зумирање во интерактивен терминал.'),
        ]

        for pattern, comment in expert_patterns:
            if re.search(pattern, fixed_code):
                # Додај коментар на почетокот ако не постои
                if comment not in fixed_code:
                    fixed_code = comment + '\n' + fixed_code

        return fixed_code

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

    def format_pedagogical_notes(self, notes_section):
        """Форматира Pedagogical Notes со емоджи и подобра структура."""
        # Раздели ги белешките по линии
        lines = notes_section.strip().split('\n')

        formatted_lines = []
        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Замени ги стандардните заглавија со емоджи и подобра структура
            if '**Основна идеја:**' in line or 'Основна идеја:' in line or line.startswith('1.'):
                if '**Основна идеја:**' in line:
                    content = line.replace('**Основна идеја:**', '').strip()
                    formatted_lines.append('### 🎯 **Основна идеја**')
                    if content:
                        formatted_lines.append(content)
                else:
                    # Handle numbered list format
                    content = re.sub(r'^\d+\.\s*', '', line).strip()
                    formatted_lines.append('### 🎯 **Основна идеја**')
                    if content.startswith('**') and content.endswith('**'):
                        content = content[2:-2]  # Remove ** ** if present
                    formatted_lines.append(content)

            elif '**Совет' in line or 'Совет' in line or line.startswith('2.'):
                if 'Совет' in line:
                    content = re.sub(r'.*?\*\*Совет.*?\*\*:\s*', '', line).strip()
                    formatted_lines.append('### 💡 **Совет од Олимпиец**')
                    if content:
                        formatted_lines.append(content)
                else:
                    # Handle numbered list format
                    content = re.sub(r'^\d+\.\s*', '', line).strip()
                    formatted_lines.append('### 💡 **Совет од Олимпиец**')
                    formatted_lines.append(content)

            elif '**Чести грешки' in line or 'Чести грешки' in line or line.startswith('3.'):
                if 'Чести грешки' in line:
                    content = re.sub(r'.*?\*\*Чести грешки.*?\*\*:\s*', '', line).strip()
                    formatted_lines.append('### ⚠️ **Чести грешки**')
                    if content:
                        formatted_lines.append(content)
                else:
                    # Handle numbered list format
                    content = re.sub(r'^\d+\.\s*', '', line).strip()
                    formatted_lines.append('### ⚠️ **Чести грешки**')
                    formatted_lines.append(content)

            elif '**Модуларна аритметика' in line or 'Модуларна аритметика' in line:
                content = line.replace('**Модуларна аритметика:**', '').replace('**Модуларна аритметика**', '').strip()
                formatted_lines.append('### 🔢 **Модуларна аритметика**')
                if content:
                    formatted_lines.append(content)

            else:
                # Други линии (содржина) - додај ги директно
                formatted_lines.append(line)

        return '\n\n'.join(formatted_lines)

    def convert_pedagogical_notes_to_accordion(self, content):
        """Претвора Pedagogical Notes секцијата во collapsible details/summary со подобро македонско форматирање."""
        # Наоѓање на "# Pedagogical Notes" секцијата - земи сè до крајот на фајлот
        notes_pattern = r'# Pedagogical Notes\n\n(.*)'
        match = re.search(notes_pattern, content, re.DOTALL)

        if not match:
            return content

        notes_section = match.group(1).strip()

        # Ако веќе има details/summary формат, не го менувај
        if '<details>' in notes_section or '<summary>' in notes_section:
            return content

        # Форматирај ги белешките со подобар стил
        formatted_notes = self.format_pedagogical_notes(notes_section)

        # Градење на нова accordion секција со македонско заглавие и емоджи
        accordion_content = f'# 👨‍🏫 Педагошки Белешки\n\n<details>\n<summary>Педагошки забелешки</summary>\n\n{formatted_notes}\n\n</details>'

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

    def generate_problem_id(self, source):
        """Generate meaningful problem ID from source information."""
        if not source:
            # Fallback to timestamp-based ID
            return f"prob_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"

        # Parse common source formats
        source = source.lower().strip()

        # Sigma magazine format: "Sigma 138, Zadaca 1900" or "Zbirka_Geom_1882"
        sigma_match = re.search(r'sigma\s+(\d+).*?(?:zadaca|p|problem)?\s*(\d+)', source, re.IGNORECASE)
        if sigma_match:
            magazine_num = sigma_match.group(1)
            problem_num = sigma_match.group(2)
            return f"sigma{magazine_num}_p{problem_num}"

        # Geometry collection format
        geom_match = re.search(r'zbirka_geom[_]?(\d+)', source)
        if geom_match:
            problem_num = geom_match.group(1)
            return f"geom_p{problem_num}"

        # General collection format
        collection_match = re.search(r'(\w+)[_\s](\d+)', source)
        if collection_match:
            collection = collection_match.group(1)
            number = collection_match.group(2)
            return f"{collection}_p{number}"

        # If no pattern matches, create a hash-based ID
        import hashlib
        hash_obj = hashlib.md5(source.encode())
        short_hash = hash_obj.hexdigest()[:8]
        return f"src_{short_hash}"

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
        """Validate problem meets SmartTestGenerator quality standards."""
        metadata = post.metadata

        # Required fields validation
        required_fields = ['problem_id', 'title', 'grade', 'difficulty', 'type']
        for field in required_fields:
            if not metadata.get(field):
                print(f"❌ STOP: Missing required field '{field}'.")
                return False

        # Problem ID validation
        pid = metadata.get('problem_id')
        if not pid or pid == 'unknown':
            print("❌ STOP: Invalid 'problem_id'.")
            return False

        # Difficulty validation (1-10 scale per SmartTestGenerator)
        difficulty = metadata.get('difficulty')
        try:
            diff_val = int(difficulty)
            if not (1 <= diff_val <= 10):
                print(f"❌ STOP: Difficulty {difficulty} not in valid range (1-10).")
                return False
        except (ValueError, TypeError):
            print(f"❌ STOP: Invalid difficulty value '{difficulty}'. Must be integer 1-10.")
            return False

        # Grade validation
        grade = metadata.get('grade')
        try:
            grade_val = int(grade)
            if not (1 <= grade_val <= 12):
                print(f"⚠️ WARNING: Unusual grade {grade}. Expected 1-12.")
        except (ValueError, TypeError):
            print(f"❌ STOP: Invalid grade value '{grade}'. Must be integer 1-12.")
            return False

        # Content quality checks
        content = post.content or ""
        if len(content.strip()) < 50:
            print("❌ STOP: Content too short (minimum 50 characters).")
            return False

        # Solution presence check
        if '## Решение' not in content and 'Решение' not in content:
            print("❌ STOP: Missing solution section ('## Решение').")
            return False



        # LaTeX validation (basic check for proper formatting)
        math_blocks = re.findall(r'\$\$[^$]+\$\$', content)

        # Tags validation (should exist and be non-empty)
        tags = metadata.get('tags', [])
        if not tags or len(tags) == 0:
            print("⚠️ WARNING: No tags specified. Consider adding relevant tags.")
            # Not blocking, just warning

        print("✅ Quality validation passed.")
        return True

    def _check_latex_balance(self, latex_content):
        """
        Проверува дали заградите {} се балансирани, игнорирајќи ги ескејпираните \{ \}.
        """
        balance = 0
        i = 0
        length = len(latex_content)

        while i < length:
            char = latex_content[i]

            # 1. Игнорирај ескејпирани карактери (пр. \{ или \\)
            if char == '\\':
                i += 2 # Скокни го backslash-от и наредниот знак
                continue
            
            # 2. Проверка на баланс
            if char == '{':
                balance += 1
            elif char == '}':
                balance -= 1
                # Ако балансот отиде во минус, имаме '}' без претходна '{'
                if balance < 0:
                    return False
            
            i += 1

        # Ако на крајот балансот не е 0, имаме отворена '{' што не е затворена
        return balance == 0

    def check_python_syntax(self, code, metadata):
        """
        Smart validation: Checks valid Python syntax via AST.
        Allows skipping checks if 'trusted: true' is in metadata or '# skip_check' in code.
        """
        # 1. Проверка за "Trusted Code" (Бајпас механизам)
        if metadata.get('trusted', False) or "# skip_check" in code:
            print("🛡️ INFO: Skipping syntax validation (Trusted Code detected).")
            return None

        try:
            # 2. Парсирање на синтаксата (ова фаќа грешки како missing :, ), indent)
            tree = ast.parse(code)
            
            # 3. Анализа на структурата (AST Analysis) наместо String Matching
            has_scene_class = False
            has_construct = False

            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    # Проверуваме дали има било каква класа (претпоставуваме дека е Scene)
                    has_scene_class = True
                    
                    # Проверуваме дали во класата има метод 'construct'
                    for item in node.body:
                        if isinstance(item, ast.FunctionDef) and item.name == 'construct':
                            has_construct = True

            # 4. Логички проверки (само ако не е најдена структурата)
            if not has_scene_class:
                return "⚠️ Warning: No class definition found. Make sure to define a Scene class."
            
            if not has_construct:
                 # Ова е само Warning, бидејќи некои напредни корисници може да користат __init__
                print("⚠️ Warning: 'construct' method not found in class (Unusual for Manim).")

            return None # Сè е во ред

        except SyntaxError as e:
            return f"❌ Python Syntax Error: {e.msg} on line {e.lineno}"
        except Exception as e:
            return f"❌ Validation Error: {e}"

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
            # Try to generate meaningful ID from source
            source = post.metadata.get('source', '')
            new_id = self.generate_problem_id(source)
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
            
            # ТУКА Е ПРОМЕНАТА: Додаваме post.metadata во повикот
            syntax_error = self.check_python_syntax(manim_code, post.metadata)
            
            if syntax_error and "Warning" not in syntax_error:
                # Ако е вистинска грешка, застани
                print(f"ERROR: {syntax_error}")
            else:
                # Ако е None или само Warning, продолжи со рендерирање
                if syntax_error: print(syntax_error) # Испечати го предупредувањето
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
            # Try to generate meaningful ID from source
            source = post.metadata.get('source', '')
            new_id = self.generate_problem_id(source)
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
            
            # ТУКА Е ПРОМЕНАТА: Додаваме post.metadata во повикот
            syntax_error = self.check_python_syntax(manim_code, post.metadata)
            
            if syntax_error and "Warning" not in syntax_error:
                # Ако е вистинска грешка, застани
                print(f"ERROR: {syntax_error}")
            else:
                # Ако е None или само Warning, продолжи со рендерирање
                if syntax_error: print(syntax_error) # Испечати го предупредувањето
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

    def _check_latex_balance(self, latex_content):
        """
        Проверува дали заградите {} се балансирани, игнорирајќи ги ескејпираните \{ \}.
        """
        balance = 0
        i = 0
        length = len(latex_content)

        while i < length:
            char = latex_content[i]

            # 1. Игнорирај ескејпирани карактери (пр. \{ или \\)
            if char == '\\':
                i += 2 # Скокни го backslash-от и наредниот знак
                continue
            
            # 2. Проверка на баланс
            if char == '{':
                balance += 1
            elif char == '}':
                balance -= 1
                # Ако балансот отиде во минус, имаме '}' без претходна '{'
                if balance < 0:
                    return False
            
            i += 1

        # Ако на крајот балансот не е 0, имаме отворена '{' што не е затворена
        return balance == 0

    def check_python_syntax(self, code, metadata):
        """
        Smart validation: Checks valid Python syntax via AST.
        Allows skipping checks if 'trusted: true' is in metadata or '# skip_check' in code.
        """
        # 1. Проверка за "Trusted Code" (Бајпас механизам)
        if metadata.get('trusted', False) or "# skip_check" in code:
            print("🛡️ INFO: Skipping syntax validation (Trusted Code detected).")
            return None

        try:
            # 2. Парсирање на синтаксата (ова фаќа грешки како missing :, ), indent)
            tree = ast.parse(code)
            
            # 3. Анализа на структурата (AST Analysis) наместо String Matching
            has_scene_class = False
            has_construct = False

            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    # Проверуваме дали има било каква класа (претпоставуваме дека е Scene)
                    has_scene_class = True
                    
                    # Проверуваме дали во класата има метод 'construct'
                    for item in node.body:
                        if isinstance(item, ast.FunctionDef) and item.name == 'construct':
                            has_construct = True

            # 4. Логички проверки (само ако не е најдена структурата)
            if not has_scene_class:
                return "⚠️ Warning: No class definition found. Make sure to define a Scene class."
            
            if not has_construct:
                 # Ова е само Warning, бидејќи некои напредни корисници може да користат __init__
                print("⚠️ Warning: 'construct' method not found in class (Unusual for Manim).")

            return None # Сè е во ред

        except SyntaxError as e:
            return f"❌ Python Syntax Error: {e.msg} on line {e.lineno}"
        except Exception as e:
            return f"❌ Validation Error: {e}"

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
            # Try to generate meaningful ID from source
            source = post.metadata.get('source', '')
            new_id = self.generate_problem_id(source)
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
            
            # ТУКА Е ПРОМЕНАТА: Додаваме post.metadata во повикот
            syntax_error = self.check_python_syntax(manim_code, post.metadata)
            
            if syntax_error and "Warning" not in syntax_error:
                # Ако е вистинска грешка, застани
                print(f"ERROR: {syntax_error}")
            else:
                # Ако е None или само Warning, продолжи со рендерирање
                if syntax_error: print(syntax_error) # Испечати го предупредувањето
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
