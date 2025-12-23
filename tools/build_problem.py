import json
import os
import re
import sys
import subprocess
import datetime

# --- КОНФИГУРАЦИЈА ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "../"))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
INPUT_FILE = os.path.join(SCRIPT_DIR, "input.json")
IMAGES_DIR = os.path.join(BASE_DIR, "assets", "images")
PROMPTS_LOG_FILE = os.path.join(BASE_DIR, "assets", "visual_prompts_log.md")

# Проверка дали Manim е достапен (за да не крашира скри# filepath: c:\Users\pc4all\Documents\matholimpiad\olympiad-math-archive\tools\build_problem.py
# ...existing code...
# Проверка дали Manim е достапен (за да не крашира скриптата)
try:
    import manim  # type: ignore
    MANIM_AVAILABLE = True
except ImportError:
    MANIM_AVAILABLE = False

# Креирај папка за слики ако не постои
if not os.path.exists(IMAGES_DIR):
    os.makedirs(IMAGES_DIR)

def slugify(text):
    if not text: return "unknown"
    text = str(text).lower()
    text = re.sub(r'[^a-z0-9]+', '_', text)
    return text.strip('_')

def load_template(is_geometry):
    filename = "geometry_problem_template.md" if is_geometry else "problem_template.md"
    path = os.path.join(TEMPLATES_DIR, filename)
    if not os.path.exists(path):
        print(f"❌ ГРЕШКА: Не го наоѓам темплејтот: {path}")
        return None
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def log_visual_prompt(prob_id, title, prompt):
    """Го запишува промптот во централен лог фајл за лесно копирање."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    
    entry = f"""
### 🆔 Задача: {prob_id} - {title}
**📅 Додадено:** {timestamp}
**📋 Промпт за Geo-Mentor / AI:**
```text
{prompt}
"""
    try:
        with open(PROMPTS_LOG_FILE, "a", encoding="utf-8") as f:
            f.write(entry)
        print(f"📝 Промптот е додаден во: assets/visual_prompts_log.md")
    except Exception as e:
        print(f"⚠️ Не успеав да запишам во логот: {e}")

def generate_manim_image(prob_id, code_body):
    """Го извршува Manim кодот САМО АКО е инсталиран."""
    if not MANIM_AVAILABLE:
        return False
    if not code_body: return False

    print(f"🎨 Генерирам слика за {prob_id}...")

    manim_script = f"""
from manim import *
class ProblemScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        {code_body}
"""
    temp_script_path = os.path.join(SCRIPT_DIR, "temp_manim.py")
    with open(temp_script_path, "w", encoding="utf-8") as f:
        f.write(manim_script)
    cmd = ["manim", "-s", "-pql", "--disable_caching", "-v", "WARNING", temp_script_path, "ProblemScene"]

    try:
        subprocess.run(cmd, check=True, cwd=SCRIPT_DIR)
        media_dir = os.path.join(SCRIPT_DIR, "media", "images", "temp_manim")
        if os.path.exists(media_dir):
            files = [f for f in os.listdir(media_dir) if f.endswith(".png")]
            if files:
                src = os.path.join(media_dir, files[0])
                dst = os.path.join(IMAGES_DIR, f"{prob_id}.png")
                if os.path.exists(dst): os.remove(dst)
                os.rename(src, dst)
                print(f"🖼️  Сликата е зачувана: assets/images/{prob_id}.png")
                return True
    except Exception as e:
        print(f"⚠️ Грешка при генерирање слика: {e}")

    return False

def create_problem_file(data):
    if not data or 'grade' not in data: return

    try:
        grade = int(data.get('grade', 0))
    except ValueError: grade = 0
    
    field_dir = data.get('field', 'other')
    source_slug = slugify(data.get('source', 'unknown'))
    prob_id = str(data.get('problem_id', '000'))
    filename = f"{source_slug}_{prob_id}.md"
    
    if grade <= 5:
        output_dir = os.path.join(BASE_DIR, "pre_olympiad", f"grade_{grade}", field_dir)
        img_rel_path_prefix = "../../../assets/images"
    else:
        output_dir = os.path.join(BASE_DIR, f"grade_{grade}", field_dir)
        img_rel_path_prefix = "../../assets/images"
    
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, filename)

    is_geo = data.get('is_geometry', False)
    content = load_template(is_geo)
    if not content: return

    # --- MANIM GENERATION (Safe Mode) ---
    if is_geo and data.get('manim_code') and MANIM_AVAILABLE:
        generate_manim_image(prob_id, data['manim_code'])

    # --- MAPPING ---
    content = content.replace("<6-12>", str(grade))
    content = content.replace("<algebra | geometry | number_theory | combinatorics>", field_dir)
    content = content.replace("<1-10>", str(data.get('difficulty', 1)))
    content = content.replace("<списание / натпревар / година>", data.get('source', ''))
    content = content.replace("<број_или_шифра>", prob_id)
    content = content.replace("<mk | en | sr | hr | ru | ...>", data.get('language_original', 'mk'))
    content = content.replace("<main_cognitive_tool>", data.get('primary_skill', 'logic'))

    related = data.get('related_skills', [])
    related_str = "\n".join([f"  - {s}" for s in related]) if related else "  - logic"
    content = content.replace("  - <skill_1>\n  - <skill_2>", related_str)

    tags = data.get('tags', [])
    tags_str = "\n".join([f"  - {t}" for t in tags]) if tags else "  - math"
    content = content.replace("  - <topic_1>\n  - <topic_2>", tags_str)

    if is_geo:
        geo_style = data.get('geometry_style', 'synthetic') or 'synthetic'
        content = content.replace("geometry_style: synthetic", f"geometry_style: {geo_style}")

    # --- VISUALS LOGIC ---
    image_filename = f"{prob_id}.png"
    image_abs_path = os.path.join(IMAGES_DIR, image_filename)
    
    visual_block = ""
    
    if os.path.exists(image_abs_path):
        visual_block = f"\n![Скица]({img_rel_path_prefix}/{image_filename})\n"
    elif data.get('visual_prompt'):
        visual_block = f"\n<!-- VISUAL PROMPT: {data['visual_prompt']} -->\n"
        log_visual_prompt(prob_id, data.get('problem_title', ''), data['visual_prompt'])

    content = content.replace("## 🧠 Анализа", f"{visual_block}\n## 🧠 Анализа")

    # --- TEXT ---
    content = content.replace("<Наслов на задачата>", data.get('problem_title', 'Наслов'))
    text_mk = data.get('problem_text_mk', '')
    content = content.replace("<Оригинален текст на задачата. Ако е превод, внимавај на терминологијата.>", text_mk)
    content = content.replace("<Текст.>", text_mk)
    
    hint = data.get('analysis_hint', 'Нема анализа.')
    content = content.replace("<Ова е најважниот дел за олимпијци. Не го пишувај решението тука, туку *интуицијата*. Како да се сетам да го користам тој skill?>", hint)
    content = content.replace("<Зошто повлековме баш таква помошна линија? Каде е \"клучот\" на задачата?>", hint)

    sol = data.get('solution_content', 'Решението е во изработка.')
    content = content.replace("<Детално решение, чекор по чекор.>", sol)
    content = content.replace("<Чекор по чекор. Секој чекор мора да има геометриско оправдување (на пр. \"агли над ист лак\").>", sol)

    notes = data.get('pedagogical_notes', '')
    content = content.replace("<Педагошки забелешки: каде грешат учениците, кои предуслови им требаат.>", notes)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ УСПЕХ! Креиран фајл: {output_path}")

if __name__ == "__main__":
    if os.path.exists(INPUT_FILE):
        print(f"📂 Чitam од фајлот: {INPUT_FILE}")
        try:
            with open(INPUT_FILE, 'r', encoding='utf-8') as f:
                json_data = json.load(f)
            
            if isinstance(json_data, list):
                print(f"📦 Детектирав листа од {len(json_data)} задачи. Започнувам...")
                for i, problem in enumerate(json_data, 1):
                    create_problem_file(problem)
            else:
                create_problem_file(json_data)
                
        except json.JSONDecodeError as e:
            print(f"❌ ГРЕШКА во input.json: {e}")
    else:
        print("📥 Внеси JSON рачно (Ctrl+Z па Enter):")
        try:
            input_data = sys.stdin.read()
            if input_data.strip():
                json_data = json.loads(input_data)
                if isinstance(json_data, list):
                    for problem in json_data: create_problem_file(problem)
                else:
                    create_problem_file(json_data)
        except Exception as e:
            print(f"❌ ГРЕШКА: {e}")