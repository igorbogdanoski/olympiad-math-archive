import json
import os
import re

# --- CONFIGURATION ---
BASE_DIR = "../"  # Adjust based on where you run the script
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '_', text)
    return text.strip('_')

def load_template(is_geometry):
    filename = "geometry_problem_template.md" if is_geometry else "problem_template.md"
    with open(os.path.join(TEMPLATES_DIR, filename), 'r', encoding='utf-8') as f:
        return f.read()

def create_problem_file(data):
    # 1. Determine Path
    grade_dir = f"grade_{data['grade']}"
    field_dir = data['field']
    filename = f"{slugify(data['source'])}_{data['problem_id']}.md"
    
    output_dir = os.path.join(BASE_DIR, grade_dir, field_dir)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, filename)

    # 2. Load Template
    template = load_template(data.get('is_geometry', False))

    # 3. Fill Template
    content = template
    
    # Replace Header Fields
    content = content.replace("<6-12>", str(data['grade']))
    content = content.replace("<algebra | geometry | number_theory | combinatorics>", data['field'])
    content = content.replace("<1-10>", str(data['difficulty']))
    content = content.replace("<списание / натпревар / година>", data['source'])
    content = content.replace("<број_или_шифра>", str(data['problem_id']))
    content = content.replace("<mk | en | sr | hr | ru | ...>", data['language_original'])
    
    # Skills & Tags
    content = content.replace("<main_cognitive_tool>", data['primary_skill'])
    
    related_skills_str = "\n".join([f"  - {s}" for s in data['related_skills']])
    content = content.replace("  - <skill_1>\n  - <skill_2>", related_skills_str)

    tags_str = "\n".join([f"  - {t}" for t in data['tags']])
    content = content.replace("  - <topic_1>\n  - <topic_2>", tags_str)

    # Geometry Specifics
    if data.get('is_geometry'):
        content = content.replace("geometry_style: synthetic", f"geometry_style: {data.get('geometry_style', 'synthetic')}")

    # Content Body
    content = content.replace("<Наслов на задачата>", data['problem_title'])
    content = content.replace("<Оригинален текст на задачата. Ако е превод, внимавај на терминологијата.>", data['problem_text_mk'])
    content = content.replace("<Ова е најважниот дел за олимпијци. Не го пишувај решението тука, туку *интуицијата*. Како да се сетам да го користам тој skill?>", data['analysis_hint'])
    content = content.replace("<Детално решение, чекор по чекор.>", data['solution_content'])
    content = content.replace("<Педагошки забелешки: каде грешат учениците, кои предуслови им требаат.>", data.get('pedagogical_notes', ''))

    # 4. Write File
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Success! Created: {output_path}")

# --- MAIN ---
if __name__ == "__main__":
    print("Paste the JSON from AI (Ctrl+D or Ctrl+Z to finish):")
    import sys
    try:
        input_data = sys.stdin.read()
        json_data = json.loads(input_data)
        create_problem_file(json_data)
    except json.JSONDecodeError:
        print("❌ Error: Invalid JSON format.")
    except Exception as e:
        print(f"❌ Error: {e}")