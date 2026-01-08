import os
import random
import re
import argparse
import datetime
import sys

# --- КОНФИГУРАЦИЈА ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVE_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "../"))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "output_documents")

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# --- HTML TEMPLATE ---
HTML_HEAD = """
<!DOCTYPE html>
<html lang="mk">
<head>
    <meta charset="UTF-8">
    <title>Тест по Математика</title>
    <link rel="stylesheet" href="../../public/style.css">
    <!-- MathJax -->
    <script>
    window.MathJax = {
      tex: { inlineMath: [['$', '$'], [rr'\\\\(', r'\\\\)']], displayMath: [['$$', '$$']] },
      chtml: { scale: 1 }
    };
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
</head>
<body>
    <div class="no-print" style="background:#d1ecf1; color:#0c5460; padding:15px; margin-bottom:20px; border-radius:5px; text-align:center;">
        <strong>🖨️ СПРЕМНО ЗА ПЕЧАТЕЊЕ!</strong><br>
        Притисни <code>Ctrl + P</code> и избери <strong>"Save as PDF"</strong>.<br>
        Во опциите (More settings), исклучи "Headers and footers".
    </div>
"""

def parse_problem(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    meta = {}
    match = re.search(r'^---(.*?)---', content, re.DOTALL)
    if match:
        yaml_text = match.group(1)
        for line in yaml_text.split(r'\n'):
            if ':' in line:
                key, val = line.split(':', 1)
                meta[key.strip()] = val.strip().replace('"', '').replace("'", "")
    
    body = re.sub(rr'^---[\s\S]*?---', '', content).strip()
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

def format_problem_html(problem, index, is_teacher=False):
    meta = problem['meta']
    body = problem['body']
    
    # Extract question (before solution)
    parts = body.split('## Решение')
    question_text = parts[0].strip()
    # Remove title if it exists in markdown (# Title)
    question_text = re.sub(r'^# .*?\n', '', question_text)
    
    # Fix image paths
    question_text = question_text.replace("../../assets", "../../assets") # Adjust if needed
    
    html = f"""
    <div class="problem-container">
        <div class="problem-header" style="{ 'border-left-color:#c0392b;' if is_teacher else '' }">
            <span>Задача {index}</span>
            <span style="font-weight:normal; font-size:0.9em;">
                {meta.get('source', 'N/A')} | Тежина: {meta.get('difficulty')}/10
            </span>
        </div>
        <div class="problem-text">
            {question_text}
        </div>
    """
    
    if is_teacher:
        solution_text = parts[1] if len(parts) > 1 else "Нема решение."
        html += f"""
        <div style="background:#fff5f5; padding:10px; border:1px solid #ffcccc; margin-top:10px;">
            <strong>📝 Решение:</strong><br>
            {solution_text}
        </div>
        """
    else:
        html += '<div class="workspace"></div>'
        
    html += "</div>"
    return html

def generate_test(grade, field, count, difficulty):
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
    
    # --- HEADER ---
    header_html = f"""
    <div class="header-box">
        <h1>ТЕСТ ПО МАТЕМАТИКА</h1>
        <div style="text-align:center; color:#666; margin-bottom:15px;">Одделение: {grade} | Област: {field_name}</div>
        <div class="header-row">
            <div>Име и Презиме: <span class="header-line"></span></div>
            <div>Дата: {date_str}</div>
        </div>
        <div class="header-row">
            <div>Бодови: <span class="header-line" style="width:50px"></span> / 100</div>
            <div>Оценка: <span class="header-line" style="width:50px"></span></div>
        </div>
    </div>
    """

    # --- STUDENT HTML ---
    student_html = HTML_HEAD + header_html
    for i, prob in enumerate(selected, 1):
        student_html += format_problem_html(prob, i, is_teacher=False)
        if i % 3 == 0 and i != len(selected):
            student_html += '<div class="page-break"></div>'
    student_html += "</body></html>"

    # --- TEACHER HTML ---
    teacher_html = HTML_HEAD + f"<h1 style='color:#c0392b; text-align:center;'>КЛУЧ СО РЕШЕНИЈА</h1><h3 style='text-align:center;'>{date_str}</h3><hr>"
    for i, prob in enumerate(selected, 1):
        teacher_html += format_problem_html(prob, i, is_teacher=True)
    teacher_html += "</body></html>"

    # --- SAVE ---
    base_name = f"Test_Grade{grade}_{field if field else 'All'}_{difficulty}_{date_str.replace('.','')}"
    
    path_student = os.path.join(OUTPUT_DIR, f"{base_name}_STUDENT.html")
    with open(path_student, 'w', encoding='utf-8') as f:
        f.write(student_html)
    
    path_teacher = os.path.join(OUTPUT_DIR, f"{base_name}_TEACHER.html")
    with open(path_teacher, 'w', encoding='utf-8') as f:
        f.write(teacher_html)
    
    print(f"✅ УСПЕХ! Генерирани се 2 фајла во {OUTPUT_DIR}:")
    print(f"   📄 {os.path.basename(path_student)}")
    print(f"   📄 {os.path.basename(path_teacher)}")
    print("👉 Отвори ги во прелистувач за печатење.")

# --- MAIN ---
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Генератор на Тестови (HTML)")
    parser.add_argument("-g", "--grade", type=int, help="Одделение")
    parser.add_argument("-f", "--field", type=str, help="Област")
    parser.add_argument("-c", "--count", type=int, default=5, help="Број на задачи")
    parser.add_argument("-d", "--difficulty", type=str, default="all", choices=['easy', 'medium', 'hard', 'all'])
    
    args = parser.parse_args()
    
    if not args.grade:
        try:
            g = int(input("Одделение (1-9): "))
            f = input("Област (algebra/geometry/all): ")
            if f == 'all' or f == '': f = None
            c = int(input("Број на задачи: "))
            d = input("Тежина (easy/medium/hard/all): ")
            generate_test(g, f, c, d)
        except ValueError:
            print("❌ Грешен внес.")
    else:
        generate_test(args.grade, args.field, args.count, args.difficulty)
