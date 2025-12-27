import json
import os
import datetime

# --- КОНФИГУРАЦИЈА ---
# Патеките се релативни во однос на скриптата
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(SCRIPT_DIR, "input.json")
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "output_documents")

# Креирај папка за излез ако не постои
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# --- HTML & CSS TEMPLATE (ПРОФЕСИОНАЛЕН ДИЗАЈН) ---
HTML_HEAD = """
<!DOCTYPE html>
<html lang="mk">
<head>
    <meta charset="UTF-8">
    <title>Математички Материјали</title>
    <link rel="stylesheet" href="../../public/style.css">
    <!-- MathJax Конфигурација за перфектни формули -->
    <script>
    window.MathJax = {
      tex: {
        inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
        displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
        processEscapes: true
      },
      chtml: { scale: 1 }
    };
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
</head>
<body>
    <div class="no-print" style="background:#d1ecf1; color:#0c5460; padding:15px; margin-bottom:20px; border-radius:5px; text-align:center;">
        <strong>🖨️ СПРЕМНО ЗА ПЕЧАТЕЊЕ!</strong><br>
        Притисни <code>Ctrl + P</code> и избери <strong>"Save as PDF"</strong>.<br>
        Во опциите (More settings), исклучи "Headers and footers" за почист изглед.
    </div>
"""

def load_data():
    if not os.path.exists(INPUT_FILE):
        print(f"❌ ГРЕШКА: Фајлот {INPUT_FILE} не постои!")
        return []
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_header(title, subtitle=""):
    return f"""
    <div class="header-box">
        <h1>{title}</h1>
        <div style="text-align:center; color:#666; margin-bottom:15px;">{subtitle}</div>
        <div class="header-row">
            <div>Име и Презиме: <span class="header-line"></span></div>
            <div>Дата: <span class="header-line"></span></div>
        </div>
        <div class="header-row">
            <div>Одделение: <span class="header-line"></span></div>
            <div>Оценка: <span class="header-line"></span></div>
        </div>
    </div>
    """

def generate_worksheet(data):
    html = HTML_HEAD + get_header("РАБОТЕН ЛИСТ", "Математички натпревари и вежби")
    
    for i, p in enumerate(data, 1):
        html += f"""
        <div class="problem-container">
            <div class="problem-header">
                <span>Задача {i}</span>
                <span style="font-weight:normal; font-size:0.9em;">{p.get('source', 'Numerus')} | Тежина: {p.get('difficulty')}/10</span>
            </div>
            <div class="problem-text">
                {p.get('problem_text_mk', '')}
            </div>
            <div class="workspace"></div>
        </div>
        """
        if i % 3 == 0 and i != len(data):
            html += '<div class="page-break"></div>'
            
    html += "</body></html>"
    return html

def generate_teacher_key(data):
    html = HTML_HEAD 
    html += "<h1 style='color:#c0392b;'>КЛУЧ СО РЕШЕНИЈА (ЗА НАСТАВНИЦИ)</h1><hr>"
    
    for i, p in enumerate(data, 1):
        html += f"""
        <div class="problem-container">
            <div class="problem-header" style="border-left-color: #c0392b;">
                <span>Задача {i} - РЕШЕНИЕ</span>
                <span>ID: {p.get('problem_id')}</span>
            </div>
            <div class="problem-text" style="background-color:#fff5f5;">
                <strong>Текст:</strong> {p.get('problem_text_mk', '')}
                <hr style="border:0; border-top:1px solid #ccc; margin:10px 0;">
                <strong>💡 Анализа:</strong> {p.get('analysis_hint', 'Нема хинт.')}<br><br>
                <strong>📝 Решение:</strong><br>
                {p.get('solution_content', '')}
                <br><br>
                <div style="color:#c0392b; font-size:0.9em;">
                    <strong>👩‍🏫 Педагошка забелешка:</strong> {p.get('pedagogical_notes', '')}
                </div>
            </div>
        </div>
        """
    html += "</body></html>"
    return html

def generate_flashcards(data):
    html = HTML_HEAD + "<h1>✂️ КАРТИЧКИ ЗА СЕЧЕЊЕ</h1><p style='text-align:center'>Страна 1: Задачи | Страна 2: Решенија (Двострано печатење)</p>"
    
    chunk_size = 4 # 4 картички по страна (2x2)
    for i in range(0, len(data), chunk_size):
        chunk = data[i:i+chunk_size]
        
        # Пополни празни места ако се помалку од 4 за да се задржи гридот
        while len(chunk) < 4:
            chunk.append(None) # Dummy
            
        # --- ПРЕДНА СТРАНА (ЗАДАЧИ) ---
        html += '<div class="cards-grid">'
        for p in chunk:
            if p:
                html += f"""
                <div class="flashcard">
                    <div style="color:#999; font-size:0.8em;">{p.get('source')}</div>
                    <h3>Задача {p.get('problem_id')}</h3>
                    <div style="overflow:hidden; max-height:180px;">{p.get('problem_text_mk')}</div>
                </div>
                """
            else:
                html += '<div class="flashcard" style="border:0;"></div>'
        html += '</div><div class="page-break"></div>'
        
        # --- ЗАДНА СТРАНА (РЕШЕНИЈА) ---
        # ВАЖНО: За двострано печатење (flip on long edge), редоследот е обично:
        # [1][2]  -> Back: [2][1]
        # [3][4]  -> Back: [4][3]
        # Но, за едноставно сечење, ќе ги оставиме исти, па наставникот може да лепи.
        
        html += '<div class="cards-grid">'
        for p in chunk:
            if p:
                html += f"""
                <div class="flashcard card-back">
                    <h3 style="color:#27ae60;">Решение {p.get('problem_id')}</h3>
                    <div style="font-size:0.85em; overflow-y:auto; max-height:300px; width:100%; text-align:left;">
                        {p.get('solution_content')}
                    </div>
                </div>
                """
            else:
                html += '<div class="flashcard" style="border:0;"></div>'
        html += '</div><div class="page-break"></div>'

    html += "</body></html>"
    return html

if __name__ == "__main__":
    data = load_data()
    if data:
        print(f"📦 Вчитани се {len(data)} задачи од input.json.")
        
        # 1. Работен лист
        path_ws = os.path.join(OUTPUT_DIR, "1_Raboten_List_Ucenici.html")
        with open(path_ws, "w", encoding="utf-8") as f:
            f.write(generate_worksheet(data))
            
        # 2. Клуч со решенија
        path_key = os.path.join(OUTPUT_DIR, "2_Kluc_Resenija_Nastavnici.html")
        with open(path_key, "w", encoding="utf-8") as f:
            f.write(generate_teacher_key(data))
            
        # 3. Картички
        path_cards = os.path.join(OUTPUT_DIR, "3_Karticki_Secenje.html")
        with open(path_cards, "w", encoding="utf-8") as f:
            f.write(generate_flashcards(data))
            
        print(f"\n✅ УСПЕХ! Генерирани се 3 документи во папката:")
        print(f"   📂 {OUTPUT_DIR}")
        print("\n👉 Упатство: Отвори ги HTML фајловите во прелистувач и избери 'Print to PDF'.")
    else:
        print("⚠️ Нема податоци во input.json. Внеси задачи прво.")