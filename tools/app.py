import streamlit as st
import os
import re

# --- КОНФИГУРАЦИЈА ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVE_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "../"))

st.set_page_config(page_title="МатАрхива Експлорер", page_icon="🧮", layout="wide")

# --- ФУНКЦИИ ЗА ЧИТАЊЕ ---
def parse_problem(file_path):
    """Чита фајл и враќа метаподатоци и содржина."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    meta = {}
    # Екстракција на YAML frontmatter
    match = re.search(r'^---(.*?)---', content, re.DOTALL)
    if match:
        yaml_text = match.group(1)
        for line in yaml_text.split('\n'):
            if ':' in line:
                key, val = line.split(':', 1)
                meta[key.strip()] = val.strip().replace('"', '').replace("'", "")
    
    # Екстракција на телото на задачата
    # 1. Тргни го YAML frontmatter (првиот блок помеѓу ---)
    body = re.sub(r'^---\s*\n[\s\S]*?\n---\s*', '', content).strip()
    
    # 2. Агресивно чистење на SKILL MAPPING и TOPICS блоковите
    # Ги бараме линиите што почнуваат со "# --- SKILL" или "# --- TOPICS" и бришеме сè до следниот наслов (# )
    body = re.sub(r'# --- SKILL MAPPING[\s\S]*?(?=\n# |\Z)', '', body)
    body = re.sub(r'# --- TOPICS[\s\S]*?(?=\n# |\Z)', '', body)
    
    # 3. Чистење на заостанати tags ако не се фатени погоре
    body = re.sub(r'tags:\s*\n(\s*- .*\n)*', '', body)
    
    # 4. Тргни повеќекратни празни редови
    body = re.sub(r'\n{3,}', '\n\n', body).strip()
    
    return meta, body, file_path
    
    # Поправање на патеки за слики за да работат во Streamlit
    # (Ова е малку трики бидејќи Streamlit работи од tools папката, но ќе пробаме)
    # Засега само ги оставаме релативни, можеби нема да се прикажат сликите перфектно без дополнителен setup
    
    return meta, body, file_path

@st.cache_data
def load_all_problems():
    """Ги наоѓа сите задачи во архивата."""
    problems = []
    
    # Шетаме низ сите папки
    for root, dirs, files in os.walk(ARCHIVE_ROOT):
        # Игнорирај ги tools, ai, assets, public папките
        if "tools" in root or "ai" in root or "assets" in root or "public" in root or ".git" in root:
            continue
            
        for file in files:
            if file.endswith(".md") and file not in ["README.md", "problem_template.md", "geometry_problem_template.md"]:
                path = os.path.join(root, file)
                try:
                    meta, body, full_path = parse_problem(path)
                    
                    # Додај дополнителни полиња за полесно филтрирање
                    # Претпоставуваме патека од тип: .../grade_9/algebra/...
                    parts = os.path.normpath(path).split(os.sep)
                    
                    grade = "N/A"
                    category = "N/A"
                    
                    for part in parts:
                        if part.startswith("grade_"):
                            grade = part.replace("grade_", "")
                        elif part in ["algebra", "geometry", "number_theory", "combinatorics", "logic", "arithmetic"]:
                            category = part
                            
                    problems.append({
                        "meta": meta,
                        "body": body,
                        "path": full_path,
                        "filename": file,
                        "grade": grade,
                        "category": category,
                        "difficulty": int(meta.get('difficulty', 0))
                    })
                except Exception as e:
                    print(f"Error parsing {file}: {e}")
                    
    return problems

# --- ГЛАВЕН ИНТЕРФЕЈС ---

st.title("🧮 Математичка Архива - Експлорер")
st.markdown("Пребарувајте, филтрирајте и прегледувајте задачи од архивата.")

# Вчитување на податоци
with st.spinner('Ја вчитувам архивата...'):
    all_problems = load_all_problems()

st.sidebar.header("🔍 Филтри")

# 1. Филтер за Одделение
grades = sorted(list(set(p['grade'] for p in all_problems if p['grade'] != "N/A")), key=lambda x: int(x) if x.isdigit() else 99)
selected_grades = st.sidebar.multiselect("Одделение", grades, default=grades)

# 2. Филтер за Категорија
categories = sorted(list(set(p['category'] for p in all_problems if p['category'] != "N/A")))
selected_categories = st.sidebar.multiselect("Категорија", categories, default=categories)

# 3. Филтер за Тежина
min_diff, max_diff = st.sidebar.slider("Тежина", 1, 10, (1, 10))

# 4. Пребарување текст
search_query = st.sidebar.text_input("Пребарај текст (пр. триаголник)")

# --- ПРИМЕНА НА ФИЛТРИ ---
filtered_problems = [
    p for p in all_problems
    if p['grade'] in selected_grades
    and p['category'] in selected_categories
    and min_diff <= p['difficulty'] <= max_diff
    and (search_query.lower() in p['body'].lower() if search_query else True)
]

st.metric("Пронајдени задачи", len(filtered_problems))

# --- ПАГИНАЦИЈА ---
items_per_page = 5
total_pages = max(1, (len(filtered_problems) + items_per_page - 1) // items_per_page)

col1, col2 = st.columns([3, 1])
with col2:
    page = st.number_input("Страна", min_value=1, max_value=total_pages, value=1)

start_idx = (page - 1) * items_per_page
end_idx = start_idx + items_per_page
current_batch = filtered_problems[start_idx:end_idx]

st.caption(f"Прикажувам {start_idx + 1}-{min(end_idx, len(filtered_problems))} од {len(filtered_problems)} задачи")

# --- ПРИКАЗ НА ЗАДАЧИ ---
if not current_batch:
    st.warning("Нема задачи што одговараат на филтрите.")
else:
    for prob in current_batch:
        # Креирање на "Картичка" со HTML/CSS
        with st.container():
            st.markdown(f"""
            <div style="border: 1px solid #ddd; border-radius: 10px; padding: 20px; margin-bottom: 20px; background-color: #f9f9f9; box-shadow: 0 2px 5px rgba(0,0,0,0.05);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 10px;">
                    <h3 style="margin: 0; color: #2c3e50; font-size: 1.2rem;">{prob['filename'].replace('.md', '').replace('_', ' ').title()}</h3>
                    <div style="display:flex; gap:5px;">
                        <span style="background-color: #3498db; color: white; padding: 2px 8px; border-radius: 10px; font-size: 0.7em;">Одд: {prob['grade']}</span>
                        <span style="background-color: #2ecc71; color: white; padding: 2px 8px; border-radius: 10px; font-size: 0.7em;">{prob['category'].capitalize()}</span>
                        <span style="background-color: #e67e22; color: white; padding: 2px 8px; border-radius: 10px; font-size: 0.7em;">Тежина: {prob['difficulty']}</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Поделба на Текст и Решение (подобрено со Regex за да фаќа и "💡 Решение")
            parts = re.split(r'##\s+.*Решение', prob['body'], maxsplit=1)
            question = parts[0]
            
            if len(parts) > 1:
                solution = parts[1].strip()
                # Чистење на HTML таговите <details> и <summary> бидејќи користиме st.expander
                solution = solution.replace('<details>', '').replace('</details>', '')
                solution = re.sub(r'<summary>.*?</summary>', '', solution, flags=re.DOTALL)
            else:
                solution = "Нема решение."
            
            # Приказ на текстот на задачата
            st.markdown(question)
            
            # Експандер за решение
            with st.expander("👀 Прикажи решение"):
                st.markdown("### 💡 Решение")
                st.markdown(solution)
                
            st.caption(f"Извор: {prob['meta'].get('source', 'Непознат')} | Патека: {prob['path']}")
            st.markdown("---")

# --- ФУТЕР ---
st.sidebar.markdown("---")
st.sidebar.info("Ова е прототип изработен со Streamlit.")
