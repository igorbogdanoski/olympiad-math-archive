import json
import os
import shutil

# --- КОНФИГУРАЦИЈА ---
INPUT_FILE = "input.json"
OUTPUT_DIR = "public"
PROBLEMS_DIR = os.path.join(OUTPUT_DIR, "problems")

# --- HTML TEMPLATES ---

# 1. ГЛАВЕН ХЕДЕР (Се појавува на секоја страна)
HTML_HEAD = """
<!DOCTYPE html>
<html lang="mk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Математичка Архива</title>
    <link rel="stylesheet" href="../style.css">
    <!-- MathJax -->
    <script>
    window.MathJax = {
      tex: { inlineMath: [['$', '$'], ['\\\\(', '\\\\)']], displayMath: [['$$', '$$']] },
      chtml: { scale: 1 }
    };
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
    <!-- Font Awesome за икони -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <a href="../index.html" class="logo"><i class="fas fa-cube"></i> МатАрхива</a>
            <div class="nav-links">
                <a href="../index.html">Почетна</a>
                <a href="#">За Нас</a>
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

# 2. CSS СТИЛОВИ (Модерен дизајн)
CSS_CONTENT = """
:root { --primary: #2c3e50; --accent: #3498db; --bg: #f4f7f6; --card-bg: #ffffff; --text: #333; }
body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: var(--bg); color: var(--text); margin: 0; padding: 0; line-height: 1.6; }
a { text-decoration: none; color: inherit; }

/* Navbar */
.navbar { background-color: var(--primary); color: white; padding: 1rem 0; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
.navbar .container { display: flex; justify-content: space-between; align-items: center; }
.logo { font-size: 1.5rem; font-weight: bold; color: white; }
.nav-links a { margin-left: 20px; color: #ecf0f1; transition: 0.3s; }
.nav-links a:hover { color: var(--accent); }

/* Layout */
.container { max-width: 1100px; margin: 0 auto; padding: 0 20px; }
.main-content { min-height: 80vh; padding-top: 40px; padding-bottom: 40px; }

/* Cards Grid (Index Page) */
.filters { margin-bottom: 30px; text-align: center; }
.filter-btn { padding: 8px 15px; border: none; background: #ddd; cursor: pointer; border-radius: 20px; margin: 5px; transition: 0.3s; }
.filter-btn.active, .filter-btn:hover { background: var(--accent); color: white; }

.problems-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; }
.problem-card { background: var(--card-bg); border-radius: 10px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); transition: transform 0.2s; border-top: 4px solid var(--accent); }
.problem-card:hover { transform: translateY(-5px); box-shadow: 0 8px 15px rgba(0,0,0,0.1); }
.card-meta { font-size: 0.85rem; color: #7f8c8d; margin-bottom: 10px; display: flex; justify-content: space-between; }
.card-title { font-size: 1.2rem; margin: 0 0 10px 0; color: var(--primary); }
.card-tags span { background: #eef2f3; padding: 2px 8px; border-radius: 4px; font-size: 0.75rem; color: #555; margin-right: 5px; }

/* Single Problem Page */
.problem-detail { background: white; padding: 40px; border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); }
.problem-header { border-bottom: 2px solid #eee; padding-bottom: 20px; margin-bottom: 20px; }
.problem-text { font-size: 1.1rem; margin-bottom: 30px; }
.solution-section { margin-top: 40px; border-top: 1px dashed #ccc; padding-top: 20px; }
.toggle-btn { background: var(--accent); color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; font-size: 1rem; }
.hidden-content { display: none; margin-top: 20px; background: #f8f9fa; padding: 20px; border-radius: 8px; border-left: 4px solid #27ae60; }

/* Footer */
.footer { background: #2c3e50; color: #bdc3c7; text-align: center; padding: 20px 0; margin-top: auto; }
"""

def load_data():
    if not os.path.exists(INPUT_FILE): return []
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def create_problem_page(problem):
    """Генерира HTML фајл за една задача."""
    filename = f"problem_{problem['problem_id']}.html"
    filepath = os.path.join(PROBLEMS_DIR, filename)
    
    # Tags HTML
    tags_html = "".join([f"<span>#{t}</span>" for t in problem.get('tags', [])])
    
    content = HTML_HEAD.replace("{title}", problem['problem_title'])
    content = content.replace("../style.css", "../style.css") # Fix path
    
    content += f"""
    <div class="problem-detail">
        <div class="problem-header">
            <span style="color: #7f8c8d;">ID: {problem['problem_id']} | Одделение: {problem['grade']} | Тежина: {problem['difficulty']}/10</span>
            <h1>{problem['problem_title']}</h1>
            <div class="card-tags">{tags_html}</div>
        </div>
        
        <div class="problem-text">
            {problem['problem_text_mk']}
        </div>
        
        <div class="solution-section">
            <button class="toggle-btn" onclick="document.getElementById('sol-{problem['problem_id']}').style.display = 'block'; this.style.display='none'">
                <i class="fas fa-eye"></i> Покажи Решение
            </button>
            
            <div id="sol-{problem['problem_id']}" class="hidden-content">
                <h3>💡 Анализа</h3>
                <p>{problem.get('analysis_hint', '')}</p>
                <hr>
                <h3>📝 Решение</h3>
                <div>{problem.get('solution_content', '')}</div>
                <br>
                <div style="font-size: 0.9rem; color: #c0392b;">
                    <strong>👩‍🏫 За наставникот:</strong> {problem.get('pedagogical_notes', '')}
                </div>
            </div>
        </div>
        
        <div style="margin-top: 30px;">
            <a href="../index.html" style="color: var(--accent);">&larr; Назад кон сите задачи</a>
        </div>
    </div>
    """
    
    content += HTML_FOOTER
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

def create_index_page(data):
    """Генерира почетна страна (Каталог)."""
    filepath = os.path.join(OUTPUT_DIR, "index.html")
    
    # Fix CSS path for index (it's in root)
    head = HTML_HEAD.replace("../style.css", "style.css").replace("../index.html", "index.html").replace("{title}", "Почетна")
    
    content = head + """
    <div style="text-align: center; margin-bottom: 40px;">
        <h1>🗂️ Архива на Задачи</h1>
        <p>Пребарувај, решавај и учи.</p>
    </div>
    
    <!-- Филтри (Едноставни линкови за сега) -->
    <div class="filters">
        <button class="filter-btn active">Сите</button>
        <button class="filter-btn">4 Одд</button>
        <button class="filter-btn">5 Одд</button>
        <button class="filter-btn">6 Одд</button>
        <button class="filter-btn">Геометрија</button>
        <button class="filter-btn">Броеви</button>
    </div>

    <div class="problems-grid">
    """
    
    for p in data:
        tags_html = "".join([f"<span>{t}</span>" for t in p.get('tags', [])[:3]]) # Max 3 tags
        link = f"problems/problem_{p['problem_id']}.html"
        
        content += f"""
        <a href="{link}" class="problem-card">
            <div class="card-meta">
                <span>{p.get('source')}</span>
                <span>Тежина: {p.get('difficulty')}</span>
            </div>
            <h3 class="card-title">{p.get('problem_title')}</h3>
            <div class="card-tags">
                <span style="background:#dfe6e9; color:#2d3436;">{p.get('grade')} Одд</span>
                {tags_html}
            </div>
        </a>
        """
        
    content += "</div>" + HTML_FOOTER
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    # 1. Подготовка на папки
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR) # Исчисти старо
    os.makedirs(PROBLEMS_DIR)
    
    # 2. Вчитување податоци
    data = load_data()
    print(f"📦 Вчитани {len(data)} задачи.")
    
    # 3. Креирање CSS
    with open(os.path.join(OUTPUT_DIR, "style.css"), "w", encoding="utf-8") as f:
        f.write(CSS_CONTENT)
        
    # 4. Креирање страни за секоја задача
    for p in data:
        create_problem_page(p)
        
    # 5. Креирање Индекс
    create_index_page(data)
    
    print(f"✅ Веб-сајтот е генериран во папката: {OUTPUT_DIR}/")
    print("👉 Отвори го 'public/index.html' за да го видиш!")

if __name__ == "__main__":
    main()