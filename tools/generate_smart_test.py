import json
import os
import random

# --- КОНФИГУРАЦИЈА ---
INPUT_FILE = "input.json"
OUTPUT_FILE = "Smart_Test_Broevi.html"
TARGET_TOPIC = "number_theory" # Може да биде: number_theory, geometry, algebra, combinatorics
TOTAL_PROBLEMS = 5

# --- HTML TEMPLATE (Истиот професионален дизајн) ---
HTML_HEAD = """
<!DOCTYPE html>
<html lang="mk">
<head>
    <meta charset="UTF-8">
    <title>Генериран Тест</title>
    <script>
    window.MathJax = {
      tex: { inlineMath: [['$', '$'], ['\\\\(', '\\\\)']], displayMath: [['$$', '$$']] },
      chtml: { scale: 1 }
    };
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
    <style>
        body { font-family: 'Segoe UI', sans-serif; max-width: 210mm; margin: 0 auto; padding: 20px; }
        .header-box { border: 2px solid #333; padding: 15px; margin-bottom: 30px; background-color: #f9f9f9; border-radius: 8px; }
        .header-row { display: flex; justify-content: space-between; margin-bottom: 10px; }
        .header-line { border-bottom: 1px solid #999; width: 200px; display: inline-block; }
        h1 { text-align: center; color: #2c3e50; margin: 5px 0; }
        .problem-container { margin-bottom: 25px; page-break-inside: avoid; }
        .problem-header { background-color: #eee; padding: 5px 10px; border-left: 5px solid #2980b9; font-weight: bold; display: flex; justify-content: space-between; }
        .problem-text { padding: 10px; border: 1px solid #eee; font-size: 16px; }
        .workspace { height: 120px; border: 1px dashed #ccc; margin-top: 10px; position: relative; }
        .workspace::after { content: "Простор за работа"; position: absolute; bottom: 5px; right: 10px; color: #ccc; font-size: 12px; }
        @media print { .no-print { display: none; } }
    </style>
</head>
<body>
    <div class="no-print" style="background:#d1ecf1; padding:10px; text-align:center; margin-bottom:20px;">
        <strong>🎯 ГЕНЕРИРАН ТЕСТ: БРОЕВИ</strong><br>
        Притисни Ctrl+P за да го зачуваш како PDF.
    </div>
    
    <div class="header-box">
        <h1>КОНТРОЛЕН ТЕСТ: БРОЕВИ</h1>
        <div style="text-align:center; color:#666; margin-bottom:15px;">Генерирано од Архивата</div>
        <div class="header-row">
            <div>Име и Презиме: <span class="header-line"></span></div>
            <div>Дата: <span class="header-line"></span></div>
        </div>
    </div>
"""

def load_data():
    if not os.path.exists(INPUT_FILE):
        print("❌ Не го наоѓам input.json")
        return []
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def select_balanced_problems(data, topic, count):
    """
    Бира задачи од дадена тема со различни тежини.
    Цел: 2 Лесни (1-2), 2 Средни (3-4), 1 Тешка (5+)
    """
    # 1. Филтрирај само задачи од таа тема
    candidates = [p for p in data if p.get('field') == topic]
    
    if not candidates:
        print(f"⚠️ Нема задачи од тема '{topic}'. Провери го полето 'field' во JSON.")
        return []

    # 2. Групирај по тежина
    easy = [p for p in candidates if p.get('difficulty', 1) <= 2]
    medium = [p for p in candidates if 3 <= p.get('difficulty', 1) <= 4]
    hard = [p for p in candidates if p.get('difficulty', 1) >= 5]

    selected = []

    # 3. Алгоритам за селекција (Цел: 5 задачи)
    # Пробај да земеш: 2 лесни, 2 средни, 1 тешка
    
    # Земаме лесни (до 2)
    selected.extend(random.sample(easy, min(len(easy), 2)))
    
    # Земаме средни (до 2)
    selected.extend(random.sample(medium, min(len(medium), 2)))
    
    # Земаме тешки (до 1)
    selected.extend(random.sample(hard, min(len(hard), 1)))

    # 4. Ако фалат задачи (на пр. немаме доволно тешки), дополни од останатите
    while len(selected) < count:
        remaining = [p for p in candidates if p not in selected]
        if not remaining: break # Нема повеќе задачи
        selected.append(random.choice(remaining))

    # 5. Сортирај ги по тежина за тестот (од најлесна до најтешка)
    selected.sort(key=lambda x: x.get('difficulty', 1))
    
    return selected[:count]

def generate_html(problems):
    html = HTML_HEAD
    
    for i, p in enumerate(problems, 1):
        html += f"""
        <div class="problem-container">
            <div class="problem-header">
                <span>Задача {i}</span>
                <span style="font-weight:normal; font-size:0.9em;">Тежина: {p.get('difficulty')}/10</span>
            </div>
            <div class="problem-text">
                {p.get('problem_text_mk', '')}
            </div>
            <div class="workspace"></div>
        </div>
        """
    
    html += "</body></html>"
    return html

if __name__ == "__main__":
    data = load_data()
    if data:
        print(f"🔍 Барам задачи од тема: {TARGET_TOPIC}...")
        
        selected_problems = select_balanced_problems(data, TARGET_TOPIC, TOTAL_PROBLEMS)
        
        if selected_problems:
            print(f"✅ Избрав {len(selected_problems)} задачи со различни тежини.")
            for p in selected_problems:
                print(f"   - [Тежина {p.get('difficulty')}] {p.get('problem_title')}")
            
            with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
                f.write(generate_html(selected_problems))
            
            print(f"\n🚀 Генериран е тестот: {OUTPUT_FILE}")
            print("👉 Отвори го во прелистувач и печати!")
        else:
            print("❌ Не успеав да најдам доволно задачи за генерирање тест.")