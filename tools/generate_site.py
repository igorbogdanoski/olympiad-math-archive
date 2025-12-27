import os
import re
import json
import shutil
import markdown

# --- CONFIGURATION ---
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
OUTPUT_DIR = os.path.join(BASE_DIR, "public")
SKILLS_DIR = os.path.join(BASE_DIR, "tools", "skill_guides")
THEOREMS_DIR = os.path.join(BASE_DIR, "tools", "theorems")

# --- HTML TEMPLATES ---
HTML_HEAD = """<!DOCTYPE html>
<html lang="mk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Математичка Архива</title>
    <link rel="stylesheet" href="{root_path}style.css">
    <!-- MathJax -->
    <script>
    window.MathJax = {{
      tex: {{ inlineMath: [['$', '$'], ['\\\\(', '\\\\)']], displayMath: [['$$', '$$']] }},
      chtml: {{ scale: 1 }}
    }};
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <a href="{root_path}index.html" class="logo"><i class="fas fa-cube"></i> МатАрхива</a>
            <div class="nav-links">
                <a href="{root_path}index.html">Почетна</a>
                <a href="{root_path}skills/index.html">Вештини</a>
                <a href="{root_path}theorems/index.html">Теореми</a>
            </div>
        </div>
    </nav>
    <div class="container main-content">
"""

HTML_FOOTER = """
    </div>
    <footer class="footer">
        <div class="container">
            <p>&copy; 2025 Македонска Математичка Архива. Генерирано со Python.</p>
        </div>
    </footer>
</body>
</html>
"""

def parse_frontmatter(content):
    """Parses YAML-like frontmatter from Markdown content."""
    meta = {}
    match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if match:
        lines = match.group(1).split('\n')
        for line in lines:
            if ':' in line:
                key, val = line.split(':', 1)
                clean_val = val.strip().strip('"').strip("'")
                # Handle lists (simple comma separated or yaml list syntax)
                if clean_val.startswith('[') and clean_val.endswith(']'):
                    clean_val = [x.strip() for x in clean_val[1:-1].split(',')]
                meta[key.strip()] = clean_val
        body = content[match.end():].strip()
    else:
        body = content.strip()
    return meta, body

def md_to_html(md_content):
    """Converts Markdown to HTML."""
    return markdown.markdown(md_content, extensions=['tables', 'fenced_code'])

def get_relative_root(path):
    """Calculates relative path to root from a given path."""
    depth = len(path.strip(os.sep).split(os.sep))
    if depth == 0: return "./"
    return "../" * depth

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def generate_page(output_path, title, content, root_path="./"):
    """Writes a full HTML page."""
    ensure_dir(os.path.dirname(output_path))
    full_html = HTML_HEAD.format(title=title, root_path=root_path) + content + HTML_FOOTER
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f"Generated: {output_path}")

def process_collection(input_dir, output_subdir, title_prefix):
    """Processes a collection of markdown files (Skills or Theorems)."""
    items = []
    output_base = os.path.join(OUTPUT_DIR, output_subdir)
    ensure_dir(output_base)

    if not os.path.exists(input_dir):
        print(f"Warning: Directory not found {input_dir}")
        return []

    for filename in os.listdir(input_dir):
        if filename.endswith(".md") and not filename.startswith("_"):
            filepath = os.path.join(input_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                raw_content = f.read()
            
            meta, body = parse_frontmatter(raw_content)
            html_body = md_to_html(body)
            
            item_title = meta.get('title', filename.replace('.md', '').replace('_', ' ').title())
            item_slug = filename.replace('.md', '')
            
            # Generate individual page
            page_content = f"""
            <div class="card">
                <span class="badge badge-category">{meta.get('category', 'General')}</span>
                <span class="badge badge-difficulty">{meta.get('difficulty', 'All Levels')}</span>
                {html_body}
            </div>
            """
            generate_page(
                os.path.join(output_base, f"{item_slug}.html"), 
                item_title, 
                page_content, 
                root_path="../"
            )
            
            items.append({
                'title': item_title,
                'slug': item_slug,
                'category': meta.get('category', 'General'),
                'difficulty': meta.get('difficulty', '-')
            })
    
    # Generate Index Page for Collection
    index_content = f"<h1>{title_prefix}</h1><div class='grid'>"
    for item in sorted(items, key=lambda x: x['title']):
        index_content += f"""
        <div class="card">
            <h3><a href="{item['slug']}.html">{item['title']}</a></h3>
            <div class="card-meta">
                <span class="badge badge-category">{item['category']}</span>
                <span class="badge badge-difficulty">{item['difficulty']}</span>
            </div>
        </div>
        """
    index_content += "</div>"
    
    generate_page(
        os.path.join(output_base, "index.html"), 
        title_prefix, 
        index_content, 
        root_path="../"
    )
    return items

def process_grades():
    """Processes grade folders and problems."""
    grades = []
    for item in os.listdir(BASE_DIR):
        if item.startswith("grade_") and os.path.isdir(os.path.join(BASE_DIR, item)):
            grade_num = item.split('_')[1]
            grades.append(item)
            
            # Process problems within grade
            grade_path = os.path.join(BASE_DIR, item)
            output_grade_path = os.path.join(OUTPUT_DIR, item)
            
            problems = []
            
            # Walk through subfolders (algebra, geometry, etc.)
            for root, dirs, files in os.walk(grade_path):
                for file in files:
                    if file.endswith(".md") and file != "README.md":
                        filepath = os.path.join(root, file)
                        rel_dir = os.path.relpath(root, grade_path) # e.g. "algebra"
                        
                        with open(filepath, 'r', encoding='utf-8') as f:
                            raw_content = f.read()
                        
                        meta, body = parse_frontmatter(raw_content)
                        html_body = md_to_html(body)
                        
                        prob_title = meta.get('title', file)
                        prob_slug = file.replace('.md', '')
                        
                        # Output path: public/grade_10/algebra/prob1.html
                        out_file_dir = os.path.join(output_grade_path, rel_dir)
                        generate_page(
                            os.path.join(out_file_dir, f"{prob_slug}.html"),
                            prob_title,
                            f"<div class='card'>{html_body}</div>",
                            root_path="../../../" if rel_dir != "." else "../../"
                        )
                        
                        problems.append({
                            'title': prob_title,
                            'path': f"{rel_dir}/{prob_slug}.html" if rel_dir != "." else f"{prob_slug}.html",
                            'category': rel_dir.title()
                        })

            # Generate Grade Index
            grade_index_content = f"<h1>Grade {grade_num} Problems</h1>"
            
            # Group by category
            cats = {}
            for p in problems:
                c = p['category']
                if c not in cats: cats[c] = []
                cats[c].append(p)
            
            for cat, probs in cats.items():
                grade_index_content += f"<h2>{cat}</h2><ul>"
                for p in probs:
                    grade_index_content += f"<li><a href='{p['path']}'>{p['title']}</a></li>"
                grade_index_content += "</ul>"
                
            generate_page(
                os.path.join(output_grade_path, "index.html"),
                f"Grade {grade_num}",
                grade_index_content,
                root_path="../"
            )

    return grades

def generate_main_index(skills, theorems, grades):
    """Generates the main dashboard."""
    content = """
    <div class="hero" style="text-align: center; margin-bottom: 40px;">
        <h1>Македонска Математичка Архива</h1>
        <p>Централизирана база на знаење за олимписка математика.</p>
    </div>
    
    <div class="grid">
        <div class="card">
            <h2>📚 Вештини</h2>
            <p>Водичи за специфични техники и концепти.</p>
            <a href="skills/index.html" class="badge badge-category">Прегледај {skill_count} вештини</a>
        </div>
        <div class="card">
            <h2>📜 Теореми</h2>
            <p>Дефиниции, докази и примери за клучни теореми.</p>
            <a href="theorems/index.html" class="badge badge-category">Прегледај {theorem_count} теореми</a>
        </div>
    </div>
    
    <h2>📂 Задачи по Одделенија</h2>
    <div class="grid">
    """.format(skill_count=len(skills), theorem_count=len(theorems))
    
    for grade in sorted(grades):
        grade_num = grade.split('_')[1]
        content += f"""
        <div class="card">
            <h3><a href="{grade}/index.html">Grade {grade_num}</a></h3>
            <p>Задачи за {grade_num} година.</p>
        </div>
        """
    
    content += "</div>"
    
    generate_page(os.path.join(OUTPUT_DIR, "index.html"), "Почетна", content)

def main():
    print("🚀 Starting Site Generation...")
    
    # 1. Process Skills
    skills = process_collection(SKILLS_DIR, "skills", "Skill Guides")
    
    # 2. Process Theorems
    theorems = process_collection(THEOREMS_DIR, "theorems", "Theorems")
    
    # 3. Process Grades
    grades = process_grades()
    
    # 4. Main Index
    generate_main_index(skills, theorems, grades)
    
    print("✅ Site Generation Complete! Open public/index.html")

if __name__ == "__main__":
    main()
