import os
import random
import re
import argparse
import datetime
import sys
import json
import io
from collections import defaultdict
from typing import List, Dict, Any, Optional

# Fix encoding for Windows console
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# --- КОНФИГУРАЦИЈА ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVE_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "../"))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "output_documents")
TEMPLATES_DIR = os.path.join(SCRIPT_DIR, "templates")

for folder in [OUTPUT_DIR, TEMPLATES_DIR]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# --- MODERN HTML/CSS FRAMEWORK ---
MODERN_CSS = """
<style>
/* Modern Typography & Layout */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

:root {
    --primary: #2563eb;
    --secondary: #64748b;
    --success: #059669;
    --warning: #d97706;
    --danger: #dc2626;
    --light: #f8fafc;
    --dark: #1e293b;
    --border: #e2e8f0;
    --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    line-height: 1.6;
    color: var(--dark);
    background: var(--light);
    max-width: 210mm;
    margin: 0 auto;
    padding: 20mm;
    font-size: 11pt;
}

@media print {
    body { margin: 0; padding: 15mm; font-size: 10pt; }
    .no-print { display: none !important; }
    .page-break { page-break-before: always; }
}

/* Header Styles */
.header-section {
    background: linear-gradient(135deg, var(--primary), #1d4ed8);
    color: white;
    padding: 25px;
    border-radius: 12px;
    margin-bottom: 30px;
    text-align: center;
    box-shadow: var(--shadow);
}

.header-section h1 {
    font-size: 28pt;
    font-weight: 700;
    margin-bottom: 10px;
    letter-spacing: -0.5px;
}

.header-meta {
    font-size: 12pt;
    opacity: 0.9;
    margin-bottom: 20px;
}

.student-info {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin-top: 20px;
    font-size: 11pt;
}

.info-field {
    background: rgba(255, 255, 255, 0.1);
    padding: 12px 15px;
    border-radius: 8px;
    border: 1px solid rgba(255, 255, 255, 0.2);
}

.info-field label {
    display: block;
    font-weight: 600;
    margin-bottom: 5px;
    font-size: 9pt;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.info-field .line {
    border-bottom: 2px solid rgba(255, 255, 255, 0.3);
    min-height: 20px;
    display: block;
    width: 100%;
}

/* Problem Styles */
.problem-card {
    background: white;
    border: 2px solid var(--border);
    border-radius: 12px;
    margin-bottom: 25px;
    overflow: hidden;
    box-shadow: var(--shadow);
    transition: all 0.3s ease;
}

.problem-card:hover {
    box-shadow: 0 8px 25px -5px rgba(0, 0, 0, 0.15);
    transform: translateY(-2px);
}

.problem-header {
    background: linear-gradient(90deg, var(--primary), var(--secondary));
    color: white;
    padding: 15px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 3px solid var(--primary);
}

.problem-number {
    font-size: 16pt;
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 10px;
}

.problem-number::before {
    content: "📐";
    font-size: 18pt;
}

.problem-meta {
    font-size: 9pt;
    opacity: 0.9;
    text-align: right;
}

.problem-content {
    padding: 25px;
    font-size: 11pt;
}

.problem-content h1,
.problem-content h2,
.problem-content h3 {
    color: var(--primary);
    margin-bottom: 15px;
    font-weight: 600;
}

.problem-content p {
    margin-bottom: 12px;
    text-align: justify;
}

.problem-content .math {
    background: #f8fafc;
    padding: 15px;
    border-radius: 8px;
    border-left: 4px solid var(--primary);
    margin: 15px 0;
}

/* Teacher Version */
.teacher-solution {
    background: linear-gradient(135deg, #fef2f2, #fee2e2);
    border: 2px solid #fecaca;
    border-radius: 0 0 12px 12px;
    padding: 20px;
    margin-top: -10px;
    position: relative;
}

.teacher-solution::before {
    content: "🎯 РЕШЕНИЕ";
    position: absolute;
    top: -12px;
    left: 20px;
    background: var(--danger);
    color: white;
    padding: 6px 15px;
    border-radius: 8px 8px 0 0;
    font-size: 9pt;
    font-weight: 700;
    letter-spacing: 0.5px;
}

/* Student Version */
.student-workspace {
    min-height: 120px;
    border: 2px dashed #cbd5e1;
    border-radius: 8px;
    margin-top: 20px;
    background: linear-gradient(45deg, #f8fafc 25%, transparent 25%),
                linear-gradient(-45deg, #f8fafc 25%, transparent 25%),
                linear-gradient(45deg, transparent 75%, #f8fafc 75%),
                linear-gradient(-45deg, transparent 75%, #f8fafc 75%);
    background-size: 20px 20px;
    background-position: 0 0, 0 10px, 10px -10px, -10px 0px;
    position: relative;
}

.student-workspace::before {
    content: "✏️ ПРОСТОР ЗА РЕШЕНИЕ";
    position: absolute;
    top: -10px;
    left: 15px;
    background: white;
    color: var(--secondary);
    padding: 4px 10px;
    font-size: 8pt;
    font-weight: 600;
    border-radius: 4px;
    border: 1px solid #cbd5e1;
}

/* Footer */
.test-footer {
    margin-top: 40px;
    padding: 20px;
    background: var(--secondary);
    color: white;
    border-radius: 8px;
    text-align: center;
    font-size: 9pt;
}

.test-footer .stats {
    display: flex;
    justify-content: center;
    gap: 30px;
    margin-bottom: 15px;
}

.stat-item {
    text-align: center;
}

.stat-number {
    font-size: 14pt;
    font-weight: 700;
    display: block;
}

.stat-label {
    font-size: 8pt;
    opacity: 0.8;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

/* Print Optimizations */
@media print {
    .problem-card { break-inside: avoid; }
    .page-break { page-break-before: always; }
    .student-workspace { min-height: 80px; }
}
</style>
"""

# --- MODERN HTML TEMPLATE ---
HTML_HEAD = f"""
<!DOCTYPE html>
<html lang="mk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Olympiad Math Test</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    {MODERN_CSS}
    <!-- MathJax 3 for better rendering -->
    <script>
    window.MathJax = {{
      tex: {{
        inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
        displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
        processEscapes: true,
        processEnvironments: true,
        packages: {{ '[+]': ['color', 'ams'] }}
      }},
      chtml: {{
        scale: 1.0,
        minScale: 0.5,
        matchFontHeight: false
      }},
      startup: {{
        ready: function() {{
          console.log('MathJax is ready!');
          MathJax.startup.defaultReady();
        }}
      }}
    }};
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
</head>
<body>
    <div class="no-print" style="background: linear-gradient(135deg, #dbeafe, #bfdbfe); border: 2px solid #3b82f6; color: #1e40af; padding: 20px; margin-bottom: 25px; border-radius: 12px; text-align: center; box-shadow: 0 4px 12px rgba(59, 130, 246, 0.15);">
        <div style="font-size: 18pt; margin-bottom: 10px;">🖨️ ПРОФЕСИОНАЛЕН МАТЕМАТИЧКИ ТЕСТ</div>
        <div style="font-size: 11pt; margin-bottom: 15px;">
            <strong>Притисни <code>Ctrl + P</code></strong> за печатење<br>
            Избери <strong>"Save as PDF"</strong> во дијалогот за зачувување
        </div>
        <div style="font-size: 9pt; color: #374151;">
            Во опциите исклучи "Headers and footers" за чист PDF
        </div>
    </div>
"""

class SmartTestGenerator:
    def __init__(self):
        self.validation_rules = {
            'content_length': lambda meta, body: len(body.strip()) > 10,  # More lenient
            'has_solution': lambda meta, body: '## Решение' in body or 'Решение' in body,
            'valid_difficulty': lambda meta, body: 1 <= int(meta.get('difficulty', 5)) <= 10,
            'has_title': lambda meta, body: len(meta.get('title', '').strip()) > 0,
        }

    def parse_problem(self, file_path: str) -> tuple:
        """Parse problem file with enhanced validation"""
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

    def validate_problem(self, meta: dict, body: str) -> tuple[bool, list]:
        """Validate problem meets quality standards"""
        errors = []
        for rule_name, rule_func in self.validation_rules.items():
            if not rule_func(meta, body):
                errors.append(rule_name)
        return len(errors) == 0, errors

    def find_problems(self, grade: int, field: str, difficulty_range: tuple) -> List[Dict]:
        """Find and validate problems with enhanced filtering"""
        candidates = []
        min_diff, max_diff = difficulty_range

        # Search in problems directory
        search_dir = os.path.join(ARCHIVE_ROOT, "problems")

        if not os.path.exists(search_dir):
            print(f"[ERROR] Папката не постои: {search_dir}")
            return []

        for root, _, files in os.walk(search_dir):
            for file in files:
                if file.endswith(".md"):
                    path = os.path.join(root, file)
                    meta, body = self.parse_problem(path)

                    # Validate problem
                    is_valid, errors = self.validate_problem(meta, body)
                    if not is_valid:
                        continue  # Skip invalid problems

                    # Apply filters
                    if grade and int(meta.get('grade', 0)) != grade:
                        continue
                    # Temporarily disable field filtering for testing
                    # if field and meta.get('tags') and field not in meta.get('tags', []):
                    #     continue

                    diff = int(meta.get('difficulty', 0))
                    if not (min_diff <= diff <= max_diff):
                        continue

                    candidates.append({
                        'path': path,
                        'meta': meta,
                        'body': body,
                        'quality_score': self._calculate_quality_score(meta, body)
                    })

        # Sort by quality score for better selection
        candidates.sort(key=lambda x: x['quality_score'], reverse=True)
        return candidates

    def _calculate_quality_score(self, meta: dict, body: str) -> float:
        """Calculate problem quality score"""
        score = 0
        score += min(len(body) / 500, 1) * 20  # Content length
        score += int(meta.get('difficulty', 5)) * 2  # Difficulty contribution
        score += 10 if '## Решение' in body else 0  # Has solution
        score += 5 if len(meta.get('title', '')) > 5 else 0  # Has good title
        return score

    def format_problem_html(self, problem: Dict, index: int, is_teacher: bool = False) -> str:
        """Format problem as modern HTML"""
        meta = problem['meta']
        body = problem['body']

        # Extract question (before solution)
        parts = body.split('## Решение')
        question_text = parts[0].strip()
        # Remove title if it exists in markdown (# Title)
        question_text = re.sub(r'^# .*?\n', '', question_text)

        # Convert markdown to HTML
        question_html = self._markdown_to_html(question_text)

        html = f"""
        <div class="problem-card">
            <div class="problem-header">
                <div class="problem-number">Задача {index}</div>
                <div class="problem-meta">
                    {meta.get('source', 'N/A')} | Тежина: {meta.get('difficulty', 'N/A')}/10
                </div>
            </div>
            <div class="problem-content">
                {question_html}
            </div>"""

        if is_teacher:
            solution_text = parts[1] if len(parts) > 1 else "Нема решение."
            solution_html = self._markdown_to_html(solution_text)
            html += f"""
            <div class="teacher-solution">
                {solution_html}
            </div>"""
        else:
            html += """
            <div class="student-workspace"></div>"""

        html += "</div>"
        return html

    def _markdown_to_html(self, text: str) -> str:
        """Convert basic markdown to HTML"""
        # Basic conversions
        text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)  # Bold
        text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)  # Italic
        text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)  # Code

        # Math blocks
        text = re.sub(r'\$\$([^$]+)\$\$', r'<div class="math">$$\1$$</div>', text)

        # Paragraphs
        lines = text.split('\n')
        html_lines = []
        for line in lines:
            line = line.strip()
            if line.startswith('# '):
                line = f'<h1>{line[2:].strip()}</h1>'
            elif line.startswith('## '):
                line = f'<h2>{line[3:].strip()}</h2>'
            elif line.startswith('### '):
                line = f'<h3>{line[4:].strip()}</h3>'
            elif line:
                line = f'<p>{line}</p>'
            if line:
                html_lines.append(line)

        return '\n'.join(html_lines)

    def generate_header_html(self, grade: int, field_name: str) -> str:
        """Generate modern header HTML"""
        date_str = datetime.datetime.now().strftime("%d.%m.%Y")

        return f"""
        <div class="header-section">
            <h1>МАТЕМАТИЧКИ ТЕСТ</h1>
            <div class="header-meta">
                Одделение {grade} | {field_name} | {date_str}
            </div>
            <div class="student-info">
                <div class="info-field">
                    <label>Име и презиме</label>
                    <span class="line"></span>
                </div>
                <div class="info-field">
                    <label>Одделение</label>
                    <span class="line"></span>
                </div>
            </div>
        </div>"""

    def generate_test(self, grade: int, field: str, count: int, difficulty: str) -> None:
        """Generate complete test with validation"""
        print(f"[INFO] Генерирам паметен тест: Одд: {grade} | Област: {field} | Тежина: {difficulty}...")

        diff_map = {'easy': (1, 3), 'medium': (4, 6), 'hard': (7, 10), 'all': (1, 10)}
        diff_range = diff_map.get(difficulty, (1, 10))

        problems = self.find_problems(grade, field, diff_range)

        if not problems:
            print("[ERROR] Не најдов валидни задачи со овие критериуми.")
            return

        if len(problems) < count:
            print(f"[WARNING] Најдов само {len(problems)} валидни задачи. Ги вклучувам сите.")
            selected = problems
        else:
            selected = random.sample(problems, count)

        field_name = field.capitalize() if field else "Општ тест"

        # Generate HTML
        header_html = self.generate_header_html(grade, field_name)

        # Student version
        student_html = HTML_HEAD + header_html
        for i, prob in enumerate(selected, 1):
            student_html += self.format_problem_html(prob, i, is_teacher=False)
            if i % 3 == 0 and i != len(selected):
                student_html += '<div class="page-break"></div>'

        # Add footer with stats
        total_difficulty = sum(int(p['meta'].get('difficulty', 5)) for p in selected)
        avg_difficulty = total_difficulty / len(selected)

        student_html += f"""
        <div class="test-footer">
            <div class="stats">
                <div class="stat-item">
                    <span class="stat-number">{len(selected)}</span>
                    <span class="stat-label">ЗАДАЧИ</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">{avg_difficulty:.1f}</span>
                    <span class="stat-label">ПРОСЕЧНА ТЕЖИНА</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">{total_difficulty}</span>
                    <span class="stat-label">ВКУПНИ ПОЕНИ</span>
                </div>
            </div>
            <p>Успех!</p>
        </div>
        </body></html>"""

        # Teacher version
        teacher_html = HTML_HEAD.replace('ПРОФЕСИОНАЛЕН МАТЕМАТИЧКИ ТЕСТ', 'КЛУЧ СО РЕШЕНИЈА')
        teacher_html += f"""
        <div class="header-section" style="background: linear-gradient(135deg, #dc2626, #b91c1c);">
            <h1>КЛУЧ СО РЕШЕНИЈА</h1>
            <div class="header-meta">
                Одделение {grade} | {field_name} | {datetime.datetime.now().strftime("%d.%m.%Y")}
            </div>
        </div>"""

        for i, prob in enumerate(selected, 1):
            teacher_html += self.format_problem_html(prob, i, is_teacher=True)

        teacher_html += "</body></html>"

        # Save files
        date_str = datetime.datetime.now().strftime("%d%m%Y")
        base_name = f"Smart_Test_Grade{grade}_{field or 'All'}_{difficulty}_{date_str}"

        path_student = os.path.join(OUTPUT_DIR, f"{base_name}_STUDENT.html")
        with open(path_student, 'w', encoding='utf-8') as f:
            f.write(student_html)

        path_teacher = os.path.join(OUTPUT_DIR, f"{base_name}_TEACHER.html")
        with open(path_teacher, 'w', encoding='utf-8') as f:
            f.write(teacher_html)

        print("[SUCCESS] УСПЕХ! Генерирани се паметни тестови:")
        print(f"   [FILE] {os.path.basename(path_student)} ({len(selected)} задачи)")
        print(f"   [FILE] {os.path.basename(path_teacher)} (со решенија)")
        print(f"   [INFO] Просечна тежина: {avg_difficulty:.1f}/10")
        print("[INFO] Отвори ги во прелистувач за печатење.")

def main():
    parser = argparse.ArgumentParser(description="Паметен Генератор на Математички Тестови")
    parser.add_argument("-g", "--grade", type=int, help="Одделение (1-9)")
    parser.add_argument("-f", "--field", type=str, help="Област (algebra/geometry/numbers)")
    parser.add_argument("-c", "--count", type=int, default=8, help="Број на задачи")
    parser.add_argument("-d", "--difficulty", type=str, default="all", choices=['easy', 'medium', 'hard', 'all'])

    args = parser.parse_args()

    generator = SmartTestGenerator()

    if not args.grade:
        try:
            g = int(input("Одделение (1-9): "))
            f = input("Област (algebra/geometry/numbers/all): ").strip()
            if f in ['all', '']: f = None
            c = int(input("Број на задачи (3-15): ") or "8")
            d = input("Тежина (easy/medium/hard/all): ").strip() or "all"
            generator.generate_test(g, f, c, d)
        except ValueError as e:
            print(f"[ERROR] Грешен внес: {e}")
    else:
        generator.generate_test(args.grade, args.field, args.count, args.difficulty)

if __name__ == "__main__":
    main()
