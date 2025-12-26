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
MANIM_LOG_FILE = os.path.join(BASE_DIR, "assets", "manim_code_log.md")

# Проверка за Manim (за секој случај, иако користиш Geo-Mentor)
try:
    import manim # type: ignore
    MANIM_AVAILABLE = True
except (ImportError, Exception):
    MANIM_AVAILABLE = False

if not os.path.exists(IMAGES_DIR): os.makedirs(IMAGES_DIR)

def slugify(text):
    if not text: return "unknown"
    text = str(text).lower()
    text = re.sub(r'[^a-z0-9]+', '_', text)
    return text.strip('_')

def load_template(is_geometry):
    filename = "geometry_problem_template.md" if is_geometry else "problem_template.md"
    path = os.path.join(TEMPLATES_DIR, filename)
    if not os.path.exists(path):
        # Fallback ако нема темплејт
        return "# <Наслов на задачата>\n\n## Текст\n<Текст.>\n\n## Решение\n<Детално решение, чекор по чекор.>"
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def ensure_skill_exists(skill_name, is_theorem=False):
    if not skill_name: return
    folder = os.path.join(BASE_DIR, "tools", "theorems" if is_theorem else "skill_guides")
    if not os.path.exists(folder): os.makedirs(folder)
    
    filename = f"{skill_name}.md"
    path = os.path.join(folder, filename)

    if not os.path.exists(path):
        print(f"🆕 Креирам нов фајл за вештина: {filename}")
        content = f"# {skill_name.replace('_', ' ').title()}\n\n*(Автоматски генерирано. Потребно пополнување.)*\n"
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

def log_manim_code(prob_id, title, code):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    safe_id = re.sub(r'[^a-zA-Z0-9_]', '_', prob_id)
    class_name = f"Task_{safe_id}"
    
    full_code = f"""from manim import *

class {class_name}(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
{code}
        # --- AI GENERATED CODE END ---
"""
    entry = f"\n### 🆔 Задача: {prob_id} - {title}\n**📅 Додадено:** {timestamp}\n**🐍 Python/Manim Код:**\n```python\n{full_code}\n```\n---\n"
    try:
        with open(MANIM_LOG_FILE, "a", encoding="utf-8") as f:
            f.write(entry)
    except Exception: pass

def generate_manim_image(prob_id, code_body):
    if not MANIM_AVAILABLE or not code_body: return False
    safe_id = re.sub(r'[^a-zA-Z0-9_]', '_', prob_id)
    class_name = f"Task_{safe_id}"
    print(f"🎨 Генерирам слика за {prob_id}...")
    
    manim_script = f"from manim import *\nclass {class_name}(Scene):\n    def construct(self):\n        self.camera.background_color = WHITE\n        Text.set_default(color=BLACK)\n        MathTex.set_default(color=BLACK)\n        Mobject.set_default(color=BLACK)\n        {code_body}\n"
    temp_script_path = os.path.join(SCRIPT_DIR, "temp_manim.py")
    
    try:
        with open(temp_script_path, "w", encoding="utf-8") as f:
            f.write(manim_script)
        
        cmd = ["manim", "-s", "-pql", "--disable_caching", "-v", "ERROR", temp_script_path, class_name]
        subprocess.run(cmd, check=True, cwd=SCRIPT_DIR, stdout=subprocess.DEVNULL)
        
        media_dir = os.path.join(SCRIPT_DIR, "media", "images", "temp_manim")
        if os.path.exists(media_dir):
            files = [f for f in os.listdir(media_dir) if f.endswith(".png")]
            if files:
                src = os.path.join(media_dir, files[0])
                dst = os.path.join(IMAGES_DIR, f"{prob_id}.png")
                if os.path.exists(dst): os.remove(dst)
                os.rename(src, dst)
                if os.path.exists(temp_script_path): os.remove(temp_script_path)
                return True
    except Exception:
        return False
    return False

def create_problem_file(data):
    if not data: return

    # --- 1. ОДРЕДУВАЊЕ НА ПАПКА (THE FIX) ---
    try:
        grade = int(data.get('grade', 9))
    except ValueError: grade = 9
    
    # Бараме 'field' ИЛИ 'category', ако нема ништо -> 'other'
    raw_field = data.get('field') or data.get('category') or 'other'
    
    # Нормализација: "Analytic Geometry" -> "analytic_geometry"
    field_dir = raw_field.lower().strip().replace(" ", "_")
    
    source_slug = slugify(data.get('source', 'unknown'))
    prob_id = str(data.get('problem_id', '000'))
    filename = f"{source_slug}_{prob_id}.md"
    
    # Патеки
    if grade <= 5:
        output_dir = os.path.join(BASE_DIR, "pre_olympiad", f"grade_{grade}", field_dir)
        img_rel_path_prefix = "../../../assets/images"
    else:
        output_dir = os.path.join(BASE_DIR, f"grade_{grade}", field_dir)
        img_rel_path_prefix = "../../assets/images"
    
    # Креирај ја папката ако ја нема!
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, filename)

    # --- 2. ВЧИТУВАЊЕ ТЕМПЛЕЈТ ---
    is_geo = data.get('is_geometry', False)
    content = load_template(is_geo)
    
    # --- 3. SKILLS ---
    p_skill = data.get('primary_skill')
    if p_skill: ensure_skill_exists(p_skill, 'theorem' in p_skill or 'lemma' in p_skill)
    for r_skill in data.get('related_skills', []):
        ensure_skill_exists(r_skill, 'theorem' in r_skill or 'lemma' in r_skill)

    # --- 4. VISUALS (Geo-Mentor Support) ---
    image_filename = f"{prob_id}.png"
    image_abs_path = os.path.join(IMAGES_DIR, image_filename)
    
    manim_code = data.get('manim_code')
    
    # ПОДОБРУВАЊЕ: Ако има код, секогаш запишувај го во логот (за Geo-Mentor)
    if manim_code and len(manim_code.strip()) > 0:
        log_manim_code(prob_id, data.get('problem_title', ''), manim_code)
        
        # Пробај да генерираш слика само ако Manim е инсталиран локално
        if MANIM_AVAILABLE and not os.path.exists(image_abs_path):
            generate_manim_image(prob_id, manim_code)

    # Одлучи дали да прикажеш placeholder во Markdown
    visual_block = ""
    if os.path.exists(image_abs_path):
        # Сликата веќе постои (си ја направил со Geo-Mentor и си ја ставил во assets)
        visual_block = f"\n![Скица]({img_rel_path_prefix}/{image_filename})\n"
    elif manim_code:
        # Сликата ја нема, но има код -> Дај инструкција за Geo-Mentor
        safe_id = re.sub(r'[^a-zA-Z0-9_]', '_', prob_id)
        visual_block = f"\n> **👨‍💻 Geo-Mentor Code:**\n> Одете во `assets/manim_code_log.md`, копирајте го кодот за `Task_{safe_id}` и генерирајте ја сликата.\n"
    
    content = content.replace("<visual_placeholder>", visual_block)
    content = content.replace("## 🧠 Анализа", f"{visual_block}\n## 🧠 Анализа") # Fallback за стари темплејти

    # --- 5. ЗАМЕНА НА СОДРЖИНА ---
    # Metadata
    content = content.replace("<6-12>", str(grade))
    content = content.replace("<algebra | geometry | number_theory | combinatorics>", field_dir)
    content = content.replace("<1-10>", str(data.get('difficulty', 1)))
    content = content.replace("<problem_type>", data.get('problem_type', 'calculation'))
    content = content.replace("<списание / натпревар / година>", data.get('source', ''))
    content = content.replace("<број_или_шифра>", prob_id)
    content = content.replace("<mk | en | sr | hr | ru | ...>", data.get('language_original', 'mk'))
    content = content.replace("<main_cognitive_tool>", p_skill if p_skill else 'logic')

    # Lists
    related = data.get('related_skills', [])
    related_str = "\n".join([f"  - {s}" for s in related]) if related else "  - logic"
    content = content.replace("  - <skill_1>\n  - <skill_2>", related_str)

    prereqs = data.get('prerequisites', [])
    prereq_str = "\n".join([f"  - {p}" for p in prereqs]) if prereqs else "  - basic_math"
    content = content.replace("  - <prerequisite_1>", prereq_str)

    tags = data.get('tags', [])
    tags_str = "\n".join([f"  - {t}" for t in tags]) if tags else "  - math"
    content = content.replace("  - <topic_1>\n  - <topic_2>", tags_str)

    if is_geo:
        geo_style = data.get('geometry_style', 'synthetic') or 'synthetic'
        content = content.replace("<geometry_style>", geo_style)
        v_prompt = data.get('visual_prompt', 'No visual prompt provided.')
        content = content.replace("<visual_prompt>", v_prompt if v_prompt else "None")

    # Text & Solution
    content = content.replace("<Наслов на задачата>", data.get('problem_title', 'Наслов'))
    text_mk = data.get('problem_text_mk', '')
    content = content.replace("<Текст.>", text_mk)
    content = content.replace("<Оригинален текст на задачата. Ако е превод, внимавај на терминологијата.>", text_mk)
    
    hint = data.get('analysis_hint', 'Нема анализа.')
    content = content.replace("<Ова е најважниот дел за олимпијци. Не го пишувај решението тука, туку *интуицијата*. Како да се сетам да го користам тој skill?>", hint)
    content = content.replace("<Зошто повлековме баш таква помошна линија? Каде е \"клучот\" на задачата?>", hint)

    # Collapsible Solution
    sol = data.get('solution_content', 'Решението е во изработка.')
    collapsible_sol = f"\n<details>\n<summary>👀 Прикажи го решението</summary>\n\n{sol}\n\n</details>\n"
    content = content.replace("<Детално решение, чекор по чекор.>", collapsible_sol)
    content = content.replace("<Чекор по чекор. Секој чекор мора да има геометриско оправдување (на пр. \"агли над ист лак\").>", collapsible_sol)

    notes = data.get('pedagogical_notes', '')
    content = content.replace("<Педагошки забелешки: каде грешат учениците, кои предуслови им требаат.>", notes)
    content = content.replace("<Педагошки забелешки.>", notes)

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