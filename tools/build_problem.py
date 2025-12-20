import json
import os
import re
import sys

# --- КОНФИГУРАЦИЈА ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "../"))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

def slugify(text):
    """Го претвора текстот во безбедно име за фајл."""
    if not text:
        return "unknown"
    text = str(text).lower()
    text = re.sub(r'[^a-z0-9]+', '_', text)
    return text.strip('_')

def load_template(is_geometry):
    """Го вчитува соодветниот Markdown шаблон."""
    filename = "geometry_problem_template.md" if is_geometry else "problem_template.md"
    path = os.path.join(TEMPLATES_DIR, filename)
    
    if not os.path.exists(path):
        print(f"❌ Грешка: Шаблонот не е пронајден на патеката: {path}")
        sys.exit(1)
        
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def create_problem_file(data):
    # 1. ОДРЕДУВАЊЕ НА ПАТЕКАТА
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

    # 2. ВЧИТУВАЊЕ НА ШАБЛОН
    is_geo = data.get('is_geometry', False)
    content = load_template(is_geo)

    # 3. ПОПОЛНУВАЊЕ (MAPPING)
    content = content.replace("<6-12>", str(grade))
    content = content.replace("<algebra | geometry | number_theory | combinatorics>", field_dir)
    content = content.replace("<1-10>", str(data.get('difficulty', 1)))
    content = content.replace("<списание / натпревар / година>", data.get('source', ''))
    content = content.replace("<број_или_шифра>", prob_id)
    content = content.replace("<mk | en | sr | hr | ru | ...>", data.get('language_original', 'mk'))
    
    content = content.replace("<main_cognitive_tool>", data.get('primary_skill', 'TBD'))
    
    related = data.get('related_skills', [])
    if related:
        related_str = "\n".join([f"  - {s}" for s in related])
        content = content.replace("  - <skill_1>\n  - <skill_2>", related_str)
    else:
        content = content.replace("  - <skill_1>\n  - <skill_2>", "  - logic")

    tags = data.get('tags', [])
    if tags:
        tags_str = "\n".join([f"  - {t}" for t in tags])
        content = content.replace("  - <topic_1>\n  - <topic_2>", tags_str)
    else:
        content = content.replace("  - <topic_1>\n  - <topic_2>", "  - math")

    if is_geo:
        geo_style = data.get('geometry_style', 'synthetic')
        if geo_style is None: geo_style = 'synthetic'
        content = content.replace("geometry_style: synthetic", f"geometry_style: {geo_style}")

    content = content.replace("<Наслов на задачата>", data.get('problem_title', 'Наслов'))
    
    text_mk = data.get('problem_text_mk', '')
    if not text_mk: text_mk = data.get('problem_text_original', '')
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

    # 4. ЗАПИШУВАЊЕ
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ УСПЕХ! Креиран фајл: {output_path}")

# --- MAIN ENTRY POINT ---
if __name__ == "__main__":
    print("📥 Внеси го JSON кодот од AI (потоа притисни Ctrl+Z па Enter на Windows):")
    
    try:
        input_data = sys.stdin.read()
        
        # ОВА БЕШЕ ПРОБЛЕМОТ - СЕГА Е ПОПРАВЕНО:
        if not input_data.strip():
            print("⚠️ Нема внесено податоци.")
            sys.exit(0)
            
        json_data = json.loads(input_data)
        create_problem_file(json_data)
        
    except json.JSONDecodeError as e:
        print(f"❌ ГРЕШКА: Невалиден JSON формат.\nДетали: {e}")
    except Exception as e:
        print(f"❌ ГРЕШКА: {e}")