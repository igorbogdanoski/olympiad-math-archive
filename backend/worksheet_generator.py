import os
import re
import json
import random
import pymongo
import frontmatter
import markdown
from typing import List, Dict, Any, Optional

# --- CONFIGURATION ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = os.path.join(BASE_DIR, "problems")
THEOREMS_DIR = os.path.join(BASE_DIR, "docs/theorems")
MANIM_MAPPING_PATH = os.path.join(BASE_DIR, "web/src/data/manim_mapping.json")

# MongoDB Connection
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = pymongo.MongoClient(MONGO_URI)
db = client["olympiad_db"]
collection = db["curriculum"]

def find_standard_by_code(code: str):
    """
    Search for a specific standard across all grades and themes in MongoDB.
    """
    doc = collection.find_one({"themes.standards_with_codes.code": code})
    if not doc:
        return None
    
    for theme in doc.get("themes", []):
        for standard in theme.get("standards_with_codes", []):
            if standard["code"] == code:
                return {
                    "grade": doc["grade"],
                    "theme": theme["title"],
                    "standard": standard["description"],
                    "activities": theme.get("activities", []),
                    "objectives": theme.get("objectives", [])
                }
    return None

def find_matching_problems(grade: str, keywords: List[str], limit=3):
    search_dir = os.path.join(BASE_DIR, "problems")
    if not os.path.exists(search_dir):
        return []
    
    all_problems = []
    for root, _, files in os.walk(search_dir):
        for file in files:
            if file.endswith(".md") and file != "README.md":
                all_problems.append(os.path.join(root, file))
    
    scored_problems = []
    seen_ids = set()
    for prob_path in all_problems:
        score = 0
        try:
            post = frontmatter.load(prob_path)
            # Use problem_id or title as unique identifier
            prob_id = post.get('problem_id') or post.get('title') or os.path.basename(prob_path)
            if prob_id in seen_ids: continue
            
            content = post.content.lower()
            # Higher score for title matches
            title = post.get('title', '').lower()
            for kw in keywords:
                if len(kw) < 3: continue
                if kw.lower() in title:
                    score += 5
                if kw.lower() in content:
                    score += 1
            if score > 0:
                scored_problems.append((score, prob_path, prob_id))
                seen_ids.add(prob_id)
        except:
            continue
    
    scored_problems.sort(key=lambda x: x[0], reverse=True)
    
    final_problems = []
    for score, path, pid in scored_problems[:limit]:
        final_problems.append(path)
        
    return final_problems

def find_matching_animation(grade: str, keywords: List[str]):
    if not os.path.exists(MANIM_MAPPING_PATH):
        return None
    
    try:
        with open(MANIM_MAPPING_PATH, 'r', encoding='utf-8') as f:
            manim_data = json.load(f)
    except:
        return None

    grade_anims = manim_data.get(grade, [])
    # Flatten if it's nested or handle different structures
    if isinstance(manim_data, dict) and grade not in manim_data:
        # Try to find anywhere
        for g_list in manim_data.values():
            if isinstance(g_list, list):
                grade_anims.extend(g_list)

    for anim in grade_anims:
        for kw in keywords:
            if len(kw) > 3 and kw.lower() in anim.get('title', '').lower():
                return anim
    return None

def find_related_theorem(keywords: List[str]):
    if not os.path.exists(THEOREMS_DIR):
        return None
    
    best_theorem = None
    max_score = 0

    for file in os.listdir(THEOREMS_DIR):
        if file.endswith(".md") and file != "_template.md":
            try:
                post = frontmatter.load(os.path.join(THEOREMS_DIR, file))
                content = post.content
                score = 0
                content_lower = content.lower()
                
                for kw in keywords:
                    if len(kw) < 3: continue
                    if kw.lower() in post.get('title', '').lower():
                        score += 5
                    if kw.lower() in content_lower:
                        score += 1
                
                if score > max_score:
                    max_score = score
                    title = post.get('title') or file.replace('.md', '').title()
                    best_theorem = {"title": title, "content": content[:1000]}
            except:
                continue
    return best_theorem

def process_latex(text: str):
    """
    Converts $...$ to \( ... \) and $$...$$ to \[ ... \] for MathJax.
    """
    # Replace block math first
    text = re.sub(r'\$\$(.*?)\$\$', r'\\\[ \1 \\\]', text, flags=re.DOTALL)
    # Replace inline math
    text = re.sub(r'\$([^\$]+)\$', r'\\\( \1 \\\)', text)
    return text

def render_content(text: str):
    """
    Processes LaTeX and then converts Markdown to HTML.
    """
    if not text: return ""
    processed_text = process_latex(text)
    # Use extra extensions for better math support if needed, 
    # but basic markdown usually suffices for the rest.
    return markdown.markdown(processed_text, extensions=['extra', 'nl2br', 'sane_lists'])

def extract_section(content: str, section_name: str):
    """
    Extracts a section from markdown based on headers.
    """
    # Look for # Section or ## Section
    pattern = rf'(?:^|\n)#+\s*{section_name}.*?\n(.*?)(?=\n#+|$)'
    match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return None

CSS_STYLE = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    body { font-family: 'Inter', sans-serif; line-height: 1.6; color: #333; max-width: 900px; margin: 0 auto; padding: 40px; background-color: #f3f4f6; }
    .sheet-container { background: white; padding: 60px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); border-radius: 16px; position: relative; }
    .watermark { position: absolute; top: 20px; right: 20px; font-size: 12px; color: #cbd5e1; font-weight: 800; text-transform: uppercase; letter-spacing: 2px; }
    header { text-align: center; border-bottom: 4px solid #3b82f6; padding-bottom: 30px; margin-bottom: 40px; }
    h1 { color: #1e293b; margin: 0; font-size: 28px; letter-spacing: -0.5px; }
    .meta-info { color: #64748b; margin-top: 10px; font-size: 14px; font-weight: 500; }
    .section-title { background: #eff6ff; color: #1d4ed8; padding: 12px 20px; border-radius: 8px; font-weight: 800; margin-top: 40px; border-left: 6px solid #3b82f6; text-transform: uppercase; font-size: 14px; letter-spacing: 1px; }
    .box { margin-bottom: 25px; padding: 25px; border: 1px solid #e2e8f0; border-radius: 12px; background: #fff; }
    .problem-box { border-color: #3b82f6; background: #f8faff; position: relative; }
    .problem-number { position: absolute; top: -12px; left: 20px; background: #3b82f6; color: white; padding: 2px 12px; border-radius: 20px; font-size: 12px; font-weight: 700; }
    .activity-box { border-color: #10b981; background: #f0fdf4; }
    .theorem-box { border-color: #f59e0b; background: #fffbeb; }
    .solution-box { border: 2px dashed #94a3b8; background: #f1f5f9; margin-top: 15px; display: none; }
    .teacher-mode .solution-box { display: block; }
    .content-body p { margin-top: 0; margin-bottom: 12px; }
    .content-body p:last-child { margin-bottom: 0; }
    .content-body ul, .content-body ol { margin-bottom: 12px; }
    .animation-link { display: inline-block; margin-top: 15px; padding: 10px 20px; background: #3b82f6; color: white; text-decoration: none; border-radius: 8px; font-weight: 700; transition: all 0.2s; }
    .animation-link:hover { background: #2563eb; transform: translateY(-1px); }
    footer { margin-top: 60px; text-align: center; font-size: 12px; color: #94a3b8; border-top: 1px solid #e2e8f0; padding-top: 20px; }
    @media print {
        body { background: white; padding: 0; }
        .sheet-container { box-shadow: none; border: none; padding: 0; }
        .animation-link { display: none; }
        .section-title { -webkit-print-color-adjust: exact; }
    }
</style>
"""

def generate_worksheet_html(standard_code: str, teacher_mode: bool = False):
    std_info = find_standard_by_code(standard_code)
    if not std_info:
        return None
    
    # Extract keywords for matching (filter out small words)
    raw_keywords = re.findall(r'\w+', f"{std_info['standard']} {std_info['theme']}")
    keywords = [kw for kw in raw_keywords if len(kw) > 3]
    
    problems = find_matching_problems(std_info['grade'], keywords)
    animation = find_matching_animation(std_info['grade'], keywords)
    theorem = find_related_theorem(keywords)
    
    mode_class = "teacher-mode" if teacher_mode else ""
    
    html = f"""
    <!DOCTYPE html>
    <html lang="mk">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Работен лист: {standard_code}</title>
        <script>
            window.MathJax = {{
                tex: {{
                    inlineMath: [['\\\\(', '\\\\)']],
                    displayMath: [['\\\\[', '\\\\]']],
                    processEscapes: true
                }}
            }};
        </script>
        <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
        {CSS_STYLE}
    </head>
    <body class="{mode_class}">
        <div class="sheet-container">
            <div class="watermark">МатАрхива AI</div>
            <header>
                <h1>{std_info['theme']}</h1>
                <div class="meta-info">
                    {std_info['grade'].replace('_', ' ').title()} • {standard_code}<br>
                    <span style="font-size: 16px; color: #1e293b; display: block; margin-top: 8px;">{std_info['standard']}</span>
                </div>
            </header>

            <div class="section-title">📘 Основни поими и цели</div>
            <div class="box">
                <p><b>Цели на часот:</b></p>
                <ul style="margin-bottom: 0;">
                    {"".join(f"<li>{obj}</li>" for obj in std_info['objectives'][:4])}
                </ul>
            </div>
    """
    
    if theorem:
        html += f"""
            <div class="section-title">📜 Клучен концепт</div>
            <div class="box theorem-box">
                <h3 style="margin-top: 0; color: #b45309;">{theorem['title']}</h3>
                <div class="content-body">{render_content(theorem['content'])}</div>
            </div>
        """
        
    if animation:
         html += f"""
            <div class="section-title">🎥 Визуелизација</div>
            <div class="box">
                <p>Скенирајте го QR кодот или кликнете на линкот за да ја погледнете анимацијата:</p>
                <a href="/animations/{animation['filename'].replace('.py', '.mp4')}" class="animation-link">▶ Пушти Анимација: {animation['title']}</a>
            </div>
        """

    html += '<div class="section-title">🛠️ Активности и вежби</div>'
    html += '<div class="box activity-box"><ul style="margin-bottom: 0;">'
    for act in std_info['activities']:
        html += f"<li>{act}</li>"
    html += '</ul></div>'

    if problems:
        html += '<div class="section-title">🏆 Олимписки предизвик</div>'
        for i, prob_path in enumerate(problems):
            try:
                post = frontmatter.load(prob_path)
                p_content = post.content
                
                title = post.get('title') or "Задача"
                p_text = extract_section(p_content, "Текст на задачата") or extract_section(p_content, "Текст")
                p_solution = extract_section(p_content, "Решение")
                
                if not p_text:
                    p_text = p_content[:500] + "..."
                
                html += f"""
                <div class="box problem-box">
                    <div class="problem-number">Задача {i+1}</div>
                    <strong style="color: #1d4ed8;">{title}</strong>
                    <div class="content-body" style="margin-top: 15px; font-size: 15px;">{render_content(p_text)}</div>
                    
                    {f'<div class="solution-box"><strong>Решение:</strong><br><div class="content-body">{render_content(p_solution)}</div></div>' if p_solution else ''}
                </div>
                """
            except:
                continue

    html += f"""
            <footer>
                <p>© {random.randint(2024, 2025)} МатАрхива - Сите права се задржани. Генерирано за {standard_code}</p>
            </footer>
        </div>
    </body>
    </html>
    """
    return html

