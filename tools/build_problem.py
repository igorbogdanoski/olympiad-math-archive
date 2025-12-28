import json
import os
import re
import sys
import subprocess
import datetime

# Import the new renderer
try:
    from render_manim import render_scene
    RENDERER_AVAILABLE = True
except ImportError:
    RENDERER_AVAILABLE = False

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
    if not RENDERER_AVAILABLE or not code_body: 
        print("⚠️ Renderer not available or no code provided.")
        return False
    
    print(f"🎨 Генерирам слика за {prob_id} користејќи render_manim...")
    try:
        # render_scene handles cleaning, temp files, and moving the image to assets/images
        render_scene(prob_id, code_body)
        
        # Check if successful
        expected_path = os.path.join(IMAGES_DIR, f"{prob_id}.png")
        if os.path.exists(expected_path):
            return True
    except Exception as e:
        print(f"❌ Error rendering manim: {e}")
        return False
    
    return False

def create_problem_file(data):
    if not data: return

    # --- 1. ОДРЕДУВАЊЕ НА ПАПКА ---
    try:
        grade = int(data.get('grade', 9))
    except ValueError: grade = 9
    
    raw_field = data.get('field') or data.get('category') or 'other'
    field_dir = raw_field.lower().strip().replace(" ", "_")
    
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

    # --- 2. ВЧИТУВАЊЕ ТЕМПЛЕЈТ ---
    is_geo = data.get('is_geometry', False)
    content = load_template(is_geo)
    
    # --- 3. SKILLS ---
    p_skill = data.get('primary_skill')
    if p_skill: ensure_skill_exists(p_skill, 'theorem' in p_skill or 'lemma' in p_skill)
    for r_skill in data.get('related_skills', []):
        ensure_skill_exists(r_skill, 'theorem' in r_skill or 'lemma' in r_skill)

    # --- 4. VISUALS ---
    image_filename = f"{prob_id}.png"
    image_abs_path = os.path.join(IMAGES_DIR, image_filename)
    manim_code = data.get('manim_code')
    
    if manim_code and len(manim_code.strip()) > 0:
        log_manim_code(prob_id, data.get('problem_title', ''), manim_code)

    visual_block = ""
    if os.path.exists(image_abs_path):
        visual_block = f"\n![Скица]({img_rel_path_prefix}/{image_filename})\n"
    elif manim_code:
        safe_id = re.sub(r'[^a-zA-Z0-9_]', '_', prob_id)
        visual_block = f"\n> **👨‍💻 Geo-Mentor Code:**\n> Одете во `assets/manim_code_log.md`, копирајте го кодот за `Task_{safe_id}` и генерирајте ја сликата.\n"
    
    # Вметнување на визуелизацијата
    if "<visual_placeholder>" in content:
        content = content.replace("<visual_placeholder>", visual_block)
    else:
        # Ако нема placeholder, стави го пред Анализата
        content = content.replace("## 🧠 Анализа", f"{visual_block}\n## 🧠 Анализа")

    # --- 5. ЗАМЕНА НА МЕТАПОДАТОЦИ ---
    content = content.replace("<6-12>", str(grade))
    content = content.replace("<algebra | geometry | number_theory | combinatorics>", field_dir)
    content = content.replace("<1-10>", str(data.get('difficulty', 1)))
    content = content.replace("<problem_type>", data.get('problem_type', 'calculation'))
    content = content.replace("<списание / натпревар / година>", data.get('source', ''))
    content = content.replace("<број_или_шифра>", prob_id)
    
    lang = data.get('language_original', 'mk')
    content = re.sub(r'<mk\s*\|\s*en[^>]*>', lang, content) 
    content = content.replace("<main_cognitive_tool>", p_skill if p_skill else 'logic')

    # Листи
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

    # Текст
    content = content.replace("<Наслов на задачата>", data.get('problem_title', 'Наслов'))
    text_mk = data.get('problem_text_mk', '')
    content = content.replace("<Текст.>", text_mk)
    content = content.replace("<Оригинален текст на задачата. Ако е превод, внимавај на терминологијата.>", text_mk)
    
    # --- 6. ПЕДАГОШКИ ДЕЛ (КЛУЧНИ ИЗМЕНИ) ---
    
    # А. Анализа (Hint) - Скриена
    hint_text = data.get('analysis_hint', 'Нема анализа.')
    strategy_text = data.get('solution_strategy', '') 
    
    full_hint = hint_text
    if strategy_text:
        full_hint += f"\n\n**Стратегија:**\n{strategy_text}"

    interactive_hint = f"""
<details>
<summary>💡 Прикажи помош (Анализа)</summary>

{full_hint}
</details>
"""
    # FIX: Користиме lambda x: interactive_hint за да избегнеме 'bad escape' грешки
    # Ова му кажува на Python: "Не го гледај текстот како regex, само залепи го".
    content = re.sub(r'<Ова е најважниот дел.*?skill\?>', lambda x: interactive_hint, content, flags=re.DOTALL)
    content = re.sub(r'<Зошто повлековме.*?задачата\?>', lambda x: interactive_hint, content, flags=re.DOTALL)
    
    # Fallback ако темплејтот е веќе чист
    if "## 🧠 Анализа" in content and interactive_hint not in content:
         pass 

    # Б. Решение - Скриено
    sol = data.get('solution_content', 'Решението е во изработка.')
    collapsible_sol = f"\n<details>\n<summary>📝 Прикажи го целото решение</summary>\n\n{sol}\n\n</details>\n"
    
    # FIX: Истата поправка и тука (lambda x: ...)
    content = re.sub(r'<Детално решение.*?чекор\.>', lambda x: collapsible_sol, content, flags=re.DOTALL)
    content = re.sub(r'<Чекор по чекор.*?лак"\)\.>', lambda x: collapsible_sol, content, flags=re.DOTALL)

    # В. Краен резултат
    final_ans = data.get('final_answer', '')
    if final_ans:
        content = content.replace("<Краен резултат.>", f"**{final_ans}**")
    else:
        content = content.replace("<Краен резултат.>", "")

    # Г. Педагошки белешки
    notes = data.get('pedagogical_notes', '')
    content = re.sub(r'<Педагошки забелешки.*?>', notes, content, flags=re.DOTALL)

    # --- 7. ЗАПИШУВАЊЕ ---
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

    # --- AUTOMATED VISUALIZATION GENERATION ---
    print("\n🎨 Стартувам автоматско генерирање на слики (batch_manim)...")
    batch_script = os.path.join(SCRIPT_DIR, "batch_manim.py")
    if os.path.exists(batch_script):
        try:
            subprocess.run([sys.executable, batch_script], check=False)
        except Exception as e:
            print(f"⚠️ Не успеав да го стартувам batch_manim: {e}")
    else:
        print(f"⚠️ Скриптата {batch_script} не постои.")