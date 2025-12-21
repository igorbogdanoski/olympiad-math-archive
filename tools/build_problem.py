import json
import os
import re
import sys

# --- КОНФИГУРАЦИЈА ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "../"))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
INPUT_FILE = os.path.join(SCRIPT_DIR, "input.json")

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

def create_problem_file(data):
    # Валидација на податоци
    if not data or 'grade' not in data:
        print(f"⚠️ Прескокнувам невалиден запис (фали grade или е празен).")
        return

    try:
        grade = int(data.get('grade', 0))
    except ValueError:
        grade = 0
    
    field_dir = data.get('field', 'other')
    source_slug = slugify(data.get('source', 'unknown'))
    prob_id = str(data.get('problem_id', '000'))
    filename = f"{source_slug}_{prob_id}.md"
    
    # Логика за папки
    if grade <= 5:
        output_dir = os.path.join(BASE_DIR, "pre_olympiad", f"grade_{grade}", field_dir)
    else:
        output_dir = os.path.join(BASE_DIR, f"grade_{grade}", field_dir)
    
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, filename)

    is_geo = data.get('is_geometry', False)
    template_content = load_template(is_geo)
    if not template_content: return

    content = template_content

    # MAPPING
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

    content = content.replace("<Наслов на задачата>", data.get('problem_title', 'Наслов'))
    text_mk = data.get('problem_text_mk', '') or data.get('problem_text_original', '')
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
            
            # --- НОВА ЛОГИКА ЗА ЛИСТИ ---
            if isinstance(json_data, list):
                print(f"📦 Детектирав листа од {len(json_data)} задачи. Започнувам...")
                for i, problem in enumerate(json_data, 1):
                    print(f"--- Обработка на задача {i} ---")
                    create_problem_file(problem)
            else:
                # Ако е само една задача (dictionary)
                create_problem_file(json_data)
                
        except json.JSONDecodeError as e:
            print(f"❌ ГРЕШКА во input.json: {e}")
    else:
        print("📥 Внеси JSON рачно (Ctrl+Z па Enter):")
        # Истата логика и за рачен внес
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