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
    body = re.sub(r'^---[\s\S]*?---', '', content).strip()
    
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

# --- ПРИКАЗ НА ЗАДАЧИ ---
if not filtered_problems:
    st.warning("Нема задачи што одговараат на филтрите.")
else:
    for prob in filtered_problems:
        with st.expander(f"[{prob['grade']} одд] {prob['category'].capitalize()} - Тежина: {prob['difficulty']} - {prob['filename']}"):
            # Поделба на Текст и Решение
            parts = prob['body'].split('## Решение')
            question = parts[0]
            solution = parts[1] if len(parts) > 1 else "Нема решение."
            
            st.markdown("### 📝 Текст на задачата")
            st.markdown(question)
            
            if st.checkbox("👀 Прикажи решение", key=prob['path']):
                st.markdown("### 💡 Решение")
                st.info(solution)
            
            st.caption(f"Извор: {prob['meta'].get('source', 'Непознат')} | Патека: {prob['path']}")

# --- ФУТЕР ---
st.sidebar.markdown("---")
st.sidebar.info("Ова е прототип изработен со Streamlit.")
