import os
import random
import re
import argparse
import datetime
import sys

# Обид за увоз на export скриптата
try:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from export import export_file
except ImportError:
    print("⚠️ Предупредување: export.py не е пронајден. Ќе генерирам само Markdown.")
    export_file = None

# --- КОНФИГУРАЦИЈА ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVE_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "../"))

def parse_problem(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    meta = {}
    match = re.search(r'^---(.*?)---', content, re.DOTALL)
    if match:
        yaml_text = match.group(1)
        for line in yaml_text.split('\n'):
            if ':' in line:
                key, val = line.split(':', 1)
                meta[key.strip()] = val.strip().replace('"', '').replace("'", "")
    
    body = re.sub(r'^---[\s\S]*?---', '', content).strip()
    return meta, body

def find_problems(grade, field, difficulty_range):
    candidates = []
    min_diff, max_diff = difficulty_range
    
    if grade and grade <= 5:
        search_dir = os.path.join(ARCHIVE_ROOT, "pre_olympiad", f"grade_{grade}")
    elif grade:
        search_dir = os.path.join(ARCHIVE_ROOT, f"grade_{grade}")
    else:
        search_dir = ARCHIVE_ROOT

    if not os.path.exists(search_dir):
        print(f"❌ Папката не постои: {search_dir}")
        return []

    for root, _, files in os.walk(search_dir):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                meta, body = parse_problem(path)
                
                if field and meta.get('field') != field: continue
                
                diff = int(meta.get('difficulty', 0))
                if not (min_diff <= diff <= max_diff): continue
                
                candidates.append({'path': path, 'meta': meta, 'body': body})
    return candidates

def format_problem_for_test(problem, index):
    parts = problem['body'].split('## Решение')
    question_text = parts[0].strip()
    question_text = re.sub(r'^# .*?\n', '', question_text)
    
    # Корекција на патеки за слики
    question_text = question_text.replace("../../assets", "../assets")
    question_text = question_text.replace("../../../assets", "../assets")

    return f"**{index}.** {question_text}\n\n\\vspace{{4cm}}\n"

def format_solution_for_key(problem, index):
    meta = problem['meta']
    body = problem['body'].replace("../../assets", "../assets")
    body = body.replace("../../../assets", "../assets")

    text = f"### Задача {index} (Извор: {meta.get('source', 'N/A')})\n"
    text += f"**Тежина:** {meta.get('difficulty')}/10 | **Skill:** {meta.get('primary_skill')}\n\n"
    text += body + "\n\n***\n" # Користиме *** за сепаратор
    return text

def generate_test(grade, field, count, difficulty, output_format):
    print(f"🔍 Генерирам тест: Одд: {grade} | Област: {field} | Тежина: {difficulty}...")
    
    diff_map = {'easy': (1, 3), 'medium': (4, 6), 'hard': (7, 10), 'all': (1, 10)}
    diff_range = diff_map.get(difficulty, (1, 10))

    problems = find_problems(grade, field, diff_range)
    
    if not problems:
        print("❌ Не најдов задачи со овие критериуми.")
        return

    if len(problems) < count:
        print(f"⚠️ Најдов само {len(problems)} задачи. Ги вклучувам сите.")
        selected = problems
    else:
        selected = random.sample(problems, count)

    date_str = datetime.datetime.now().strftime("%d.%m.%Y")
    field_name = field.capitalize() if field else "Општ тест"
    
    # --- YAML HEADER ---
    md_content = f"""---
title: "ТЕСТ ПО МАТЕМАТИКА"
subtitle: "Одделение: {grade} | Област: {field_name}"
date: "{date_str}"
geometry: margin=1in
mainfont: "Times New Roman"
---

**Име и Презиме:** _________________________________________________

**Бодови:** _______ / 100  |  **Оценка:** _______

***

"""
    # --- ЗАДАЧИ ---
    for i, prob in enumerate(selected, 1):
        md_content += format_problem_for_test(prob, i)
        # ВАЖНО: Користиме *** наместо --- за да не го збуниме Pandoc
        md_content += "\n***\n" 

    # --- ПРЕЛОМ ---
    md_content += "\n\\newpage\n"
    
    # --- КЛУЧ ---
    md_content += "# КЛУЧ СО РЕШЕНИЈА\n\n"
    for i, prob in enumerate(selected, 1):
        md_content += format_solution_for_key(prob, i)

    # --- ЗАЧУВУВАЊЕ ---
    filename = f"Test_Grade{grade}_{field if field else 'All'}_{difficulty}_{date_str.replace('.','')}.md"
    output_path = os.path.join(SCRIPT_DIR, filename)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    print(f"📄 Markdown фајлот е креиран: {filename}")

    if export_file:
        print("⚙️ Стартувам конверзија...")
        export_file(output_path, output_format)
    else:
        print("⚠️ export.py не е достапен.")

# --- MAIN ---
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Генератор на Тестови")
    parser.add_argument("-g", "--grade", type=int, help="Одделение")
    parser.add_argument("-f", "--field", type=str, help="Област")
    parser.add_argument("-c", "--count", type=int, default=5, help="Број на задачи")
    parser.add_argument("-d", "--difficulty", type=str, default="all", choices=['easy', 'medium', 'hard', 'all'])
    parser.add_argument("--pdf", action="store_true", help="PDF формат")
    
    args = parser.parse_args()
    fmt = 'pdf' if args.pdf else 'docx'
    
    if not args.grade:
        try:
            g = int(input("Одделение (1-9): "))
            f = input("Област (algebra/geometry/all): ")
            if f == 'all' or f == '': f = None
            c = int(input("Број на задачи: "))
            d = input("Тежина (easy/medium/hard/all): ")
            generate_test(g, f, c, d, fmt)
        except ValueError:
            print("❌ Грешен внес.")
    else:
        generate_test(args.grade, args.field, args.count, args.difficulty, fmt)