import os
import re
import random
import datetime

# --- КОНФИГУРАЦИЈА ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "../"))
GRADE_DIR = os.path.join(BASE_DIR, "grade_8")
OUTPUT_DIR = os.path.join(BASE_DIR, "generated_worksheets")

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# --- CSS СТИЛОВИ (МОДЕРЕН ДИЗАЈН) ---
CSS_STYLE = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    body {
        font-family: 'Inter', sans-serif;
        line-height: 1.6;
        color: #333;
        max-width: 900px;
        margin: 0 auto;
        padding: 40px;
        background-color: #f9fafb;
    }
    .sheet-container {
        background: white;
        padding: 50px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border-radius: 12px;
    }
    header {
        text-align: center;
        border-bottom: 3px solid #2563eb;
        padding-bottom: 20px;
        margin-bottom: 40px;
    }
    h1 { color: #1e293b; margin: 0; font-size: 24px; text-transform: uppercase; letter-spacing: 1px; }
    .subtitle { color: #64748b; font-size: 14px; margin-top: 5px; }
    
    .section-title {
        background: #eff6ff;
        color: #1d4ed8;
        padding: 10px 20px;
        border-radius: 6px;
        font-weight: 700;
        margin-top: 40px;
        margin-bottom: 20px;
        border-left: 5px solid #2563eb;
    }
    
    .problem-box {
        margin-bottom: 30px;
        padding: 20px;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        background: #fff;
        transition: transform 0.2s;
    }
    .problem-header {
        display: flex;
        justify-content: space-between;
        margin-bottom: 10px;
        font-size: 0.9em;
        color: #94a3b8;
        font-weight: 600;
    }
    .problem-text { font-size: 1.1em; font-weight: 500; }
    
    .solution-box {
        margin-top: 15px;
        padding: 15px;
        background-color: #f0fdf4;
        border: 1px solid #bbf7d0;
        border-radius: 6px;
        color: #166534;
    }
    .solution-title { font-weight: bold; color: #15803d; margin-bottom: 5px; display: block; }
    
    .workspace {
        height: 150px;
        border: 2px dashed #e2e8f0;
        border-radius: 8px;
        margin-top: 15px;
        background: #f8fafc;
    }
    
    .footer {
        margin-top: 50px;
        text-align: center;
        font-size: 0.8em;
        color: #cbd5e1;
    }
    
    @media print {
        body { background: white; padding: 0; }
        .sheet-container { box-shadow: none; padding: 20px; }
        .problem-box { break-inside: avoid; }
        .workspace { border: 1px solid #ccc; }
    }
</style>
"""

MATHJAX_SCRIPT = """
<script>
MathJax = {
  tex: {
    inlineMath: [['$', '$'], ['\\\\(', '\\\\)']]
  }
};
</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
"""

def parse_markdown_problem(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract Title
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else "Задача"
    
    # Split content by level 2 headers
    # We use a lookahead to keep the delimiter or just split and reconstruct
    # Simpler: split by '\n##'
    sections = re.split(r'\n##\s+', content)
    
    problem_text = "Текстот не е пронајден."
    solution = "Решението не е достапно."
    
    for section in sections:
        # The first line of the section is the header title (e.g., "📝 Текст на задачата")
        lines = section.split('\n', 1)
        header = lines[0].lower()
        body = lines[1].strip() if len(lines) > 1 else ""
        
        if "текст" in header:
            problem_text = body
        elif "решение" in header:
            solution = body
            
    # Clean up <details> and <summary> tags
    solution = re.sub(r'<details>\s*<summary>.*?</summary>', '', solution, flags=re.DOTALL)
    solution = solution.replace('</details>', '')
    solution = solution.strip()
    
    # Extract Image (Global search is usually fine for these files)
    img_match = re.search(r'!\[.*?\]\((.*?)\)', content)
    image_url = None
    if img_match:
        raw_path = img_match.group(1)
        if "assets/images" in raw_path:
            filename = os.path.basename(raw_path)
            image_url = f"../assets/images/{filename}"

    # Convert Markdown bold/italic to HTML
    problem_text = problem_text.replace('**', '<b>').replace('**', '</b>')
    solution = solution.replace('**', '<b>').replace('**', '</b>')
    
    # Convert newlines to <br>
    solution = solution.replace('\n', '<br>')
    problem_text = problem_text.replace('\n', '<br>')
    
    return {
        "title": title,
        "text": problem_text,
        "solution": solution,
        "image_url": image_url,
        "id": os.path.basename(file_path).replace('.md', '')
    }

def get_grade_8_problems():
    problems = []
    if not os.path.exists(GRADE_DIR):
        print(f"⚠️ Папката {GRADE_DIR} не постои!")
        return []
        
    for root, dirs, files in os.walk(GRADE_DIR):
        for file in files:
            if file.endswith(".md") and file != "README.md":
                problems.append(os.path.join(root, file))
    return problems

def generate_html(problems_main, problems_extra, is_teacher_version):
    date_str = datetime.datetime.now().strftime("%d.%m.%Y")
    type_str = "РЕШЕНИЈА ЗА НАСТАВНИК" if is_teacher_version else "РАБОТЕН ЛИСТ ЗА УЧЕНИК"
    
    html = f"""
    <!DOCTYPE html>
    <html lang="mk">
    <head>
        <meta charset="UTF-8">
        <title>Општински Натпревар - 8 Одделение</title>
        {CSS_STYLE}
        {MATHJAX_SCRIPT}
    </head>
    <body>
        <div class="sheet-container">
            <header>
                <h1>Подготовка за Општински Натпревар</h1>
                <div class="subtitle">Математика - 8 Одделение | {date_str}</div>
                <div class="subtitle" style="color: #2563eb; font-weight: bold; margin-top: 10px;">{type_str}</div>
            </header>
    """
    
    # --- MAIN PROBLEMS ---
    html += '<div class="section-title">📝 ГЛАВНИ ЗАДАЧИ (40 мин)</div>'
    for i, prob in enumerate(problems_main, 1):
        html += f"""
        <div class="problem-box">
            <div class="problem-header">
                <span>Задача {i}</span>
                <span>{prob['title']}</span>
            </div>
            <div class="problem-text">
                {prob['text']}
            </div>
        """
        
        if prob.get('image_url'):
             html += f"""
             <div style="text-align: center; margin: 20px 0;">
                <img src="{prob['image_url']}" style="max-width: 100%; max-height: 300px; border-radius: 8px; border: 1px solid #e2e8f0;">
             </div>
             """
        
        if is_teacher_version:
            html += f"""
            <div class="solution-box">
                <span class="solution-title">💡 Решение:</span>
                {prob['solution']}
            </div>
            """
        else:
            html += '<div class="workspace"></div>'
            
        html += "</div>"

    # --- EXTRA PROBLEMS ---
    html += '<div class="section-title" style="border-color: #7c3aed; color: #7c3aed; background: #f5f3ff;">🚀 ДОПОЛНИТЕЛНИ ЗАДАЧИ (За вежбање)</div>'
    for i, prob in enumerate(problems_extra, 5):
        html += f"""
        <div class="problem-box">
            <div class="problem-header">
                <span>Задача {i}</span>
                <span>{prob['title']}</span>
            </div>
            <div class="problem-text">
                {prob['text']}
            </div>
        """
        
        if prob.get('image_url'):
             html += f"""
             <div style="text-align: center; margin: 20px 0;">
                <img src="{prob['image_url']}" style="max-width: 100%; max-height: 300px; border-radius: 8px; border: 1px solid #e2e8f0;">
             </div>
             """
        
        if is_teacher_version:
            html += f"""
            <div class="solution-box" style="border-color: #ddd6fe; background: #f5f3ff; color: #5b21b6;">
                <span class="solution-title">💡 Решение:</span>
                {prob['solution']}
            </div>
            """
        else:
            html += '<div class="workspace"></div>'
            
        html += "</div>"

    html += """
            <div class="footer">
                Генерирано од Olympiad Math Archive AI • © 2025
            </div>
        </div>
    </body>
    </html>
    """
    return html

def main():
    print("🔍 Барам задачи за 8-мо одделение...")
    files = get_grade_8_problems()
    
    if len(files) < 8:
        print(f"⚠️ Најдов само {len(files)} задачи. Ќе ги искористам сите, но се препорачуваат барем 8.")
        selected_files = files
    else:
        selected_files = random.sample(files, 8)
        
    parsed_problems = [parse_markdown_problem(f) for f in selected_files]
    
    main_probs = parsed_problems[:4]
    extra_probs = parsed_problems[4:]
    
    # Generate Student Version
    student_html = generate_html(main_probs, extra_probs, is_teacher_version=False)
    student_path = os.path.join(OUTPUT_DIR, "Grade8_Worksheet_Student.html")
    with open(student_path, "w", encoding="utf-8") as f:
        f.write(student_html)
    print(f"✅ Генериран ученички лист: {student_path}")
    
    # Generate Teacher Version
    teacher_html = generate_html(main_probs, extra_probs, is_teacher_version=True)
    teacher_path = os.path.join(OUTPUT_DIR, "Grade8_Worksheet_Teacher.html")
    with open(teacher_path, "w", encoding="utf-8") as f:
        f.write(teacher_html)
    print(f"✅ Генериран наставнички лист: {teacher_path}")
    
    print("\n💡 СОВЕТ: Отворете ги HTML фајловите во прелистувач (Chrome/Edge) и одберете 'Print -> Save as PDF'.")

if __name__ == "__main__":
    main()
