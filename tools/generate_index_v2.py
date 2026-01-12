import os
import re

# --- КОНФИГУРАЦИЈА ---
# Ова претпоставува дека скриптата е во /tools папката
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
IGNORE_DIRS = {'assets', 'tools', 'templates', 'media', '.git', '.vscode', '__pycache__'}

def parse_frontmatter(content):
    """Робустен парсер за метаподатоци."""
    meta = {}
    match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if match:
        lines = match.group(1).split('\n')
        for line in lines:
            if ':' in line:
                key, val = line.split(':', 1)
                clean_val = val.strip().strip('"').strip("'")
                meta[key.strip()] = clean_val
    return meta

def get_problem_details(file_path):
    """Враќа речник со податоци за една задача."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            meta = parse_frontmatter(content)
            
            title_match = re.search(r'\n# (.*?)\n', content)
            title = title_match.group(1).strip() if title_match else os.path.basename(file_path)
            
            return {
                'id': meta.get('problem_id', '???'),
                'title': title,
                'difficulty': meta.get('difficulty', '-'),
                'skill': meta.get('primary_skill', 'Logic'),
                'type': meta.get('problem_type', 'General'),
                'filename': os.path.basename(file_path)
            }
    except Exception as e:
        print(f"⚠️ Грешка при читање {file_path}: {e}")
        return None

def generate_category_index(folder_path, category_name):
    """Креира табела со задачи за крајна папка (на пр. Algebra)."""
    files = [f for f in os.listdir(folder_path) if f.endswith('.md') and f != 'README.md']
    files.sort()
    
    if not files:
        return 0 

    content = f"# 📂 {category_name.replace('_', ' ').title()}\n\n"
    content += "[⬅️ Назад кон прегледот](../README.md)\n\n"
    content += f"**Вкупно задачи:** {len(files)}\n\n"
    content += "| ID | Наслов | Тежина | Тип | Клучна Вештина |\n"
    content += "|:---|:---|:---:|:---|:---|\n"
    
    for file in files:
        details = get_problem_details(os.path.join(folder_path, file))
        if details:
            link = f"[{details['id']}]({details['filename']})"
            diff = details['difficulty']
            row = f"| {link} | {details['title']} | {diff}/10 | {details['type']} | {details['skill']} |\n"
            content += row

    with open(os.path.join(folder_path, "README.md"), 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"   ✅ Генериран индекс за: {category_name} ({len(files)} задачи)")
    return len(files)

def generate_grade_index(grade_path, grade_name):
    """Креира листа на категории за главна папка (на пр. Grade 9)."""
    subdirs = [d for d in os.listdir(grade_path) if os.path.isdir(os.path.join(grade_path, d)) and d not in IGNORE_DIRS]
    subdirs.sort()
    
    total_problems_in_grade = 0
    category_rows = ""
    
    for sub in subdirs:
        sub_path = os.path.join(grade_path, sub)
        count = generate_category_index(sub_path, sub)
        
        if count > 0:
            total_problems_in_grade += count
            category_rows += f"| [📁 {sub.capitalize()}]({sub}/README.md) | {count} |\n"

    if total_problems_in_grade == 0:
        return

    content = f"# 🎓 {grade_name.replace('_', ' ').title()}\n\n"
    content += "[🏠 Назад кон почеток](../../README.md)\n\n"
    content += f"Оваа папка содржи **{total_problems_in_grade}** олимписки задачи поделени по области.\n\n"
    content += "| Област | Број на задачи |\n"
    content += "|:---|:---:|\n"
    content += category_rows

    with open(os.path.join(grade_path, "README.md"), 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"🏛️  Генериран ГЛАВЕН индекс за: {grade_name}")

def main():
    print("🚀 Започнувам индексирање на архивата...")
    
    for item in os.listdir(BASE_DIR):
        full_path = os.path.join(BASE_DIR, item)
        
        if os.path.isdir(full_path):
            if item.startswith("grade_") or item == "pre_olympiad":
                generate_grade_index(full_path, item)

    print("🏁 Индексирањето заврши успешно!")

if __name__ == "__main__":
    main()