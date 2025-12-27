import streamlit as st
import os
import re
import random
import subprocess
import tempfile

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
        
        # Екстракција на тагови (подобрено)
        tags = []
        # Бараме tags: проследено со листа со цртички
        tags_match = re.search(r'tags:\s*\n((?:\s*-\s*.*\n?)+)', yaml_text)
        if tags_match:
            tags_block = tags_match.group(1)
            tags = [t.strip().replace('- ', '').strip() for t in tags_block.split('\n') if t.strip()]
        meta['tags'] = tags

        # Екстракција на related_skills
        related_skills = []
        skills_match = re.search(r'related_skills:\s*\n((?:\s*-\s*.*\n?)+)', content) # Бараме во целиот content за секој случај
        if skills_match:
            skills_block = skills_match.group(1)
            related_skills = [s.strip().replace('- ', '').strip() for s in skills_block.split('\n') if s.strip()]
        meta['related_skills'] = related_skills
    
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
    
    # 5. Конверзија на LaTeX delimiters за Streamlit
    # \[ ... \] -> $$ ... $$
    body = re.sub(r'\\\[(.*?)\\\]', r'$$\1$$', body, flags=re.DOTALL)
    # \( ... \) -> $ ... $
    body = re.sub(r'\\\((.*?)\\\)', r'$\1$', body, flags=re.DOTALL)
    
    # Проверка за Manim placeholder
    has_manim_placeholder = "<!-- Ова место е резервирано за автоматската слика од Manim -->" in content
    meta['has_manim_placeholder'] = has_manim_placeholder

    return meta, body, file_path
    
    # Поправање на патеки за слики за да работат во Streamlit
    # (Ова е малку трики бидејќи Streamlit работи од tools папката, но ќе пробаме)
    # Засега само ги оставаме релативни, можеби нема да се прикажат сликите перфектно без дополнителен setup
    
    return meta, body, file_path

def generate_pdf(problems_list):
    """Генерира PDF од листа на задачи."""
    if not problems_list:
        return None
        
    # Креирање на привремен Markdown фајл
    md_content = ""
    for p in problems_list:
        md_content += f"# {p['filename'].replace('.md', '').replace('_', ' ').title()}\n\n"
        md_content += p['body'] + "\n\n---\n\n"
    
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".md", mode='w', encoding='utf-8') as tmp:
            tmp.write(md_content)
            tmp_path = tmp.name
            
        pdf_path = tmp_path.replace(".md", ".pdf")
        
        # Команда за Pandoc (иста како во export_to_pdf.py)
        command = [
            "pandoc", tmp_path, "-o", pdf_path,
            "--pdf-engine=xelatex", 
            "--from=markdown+tex_math_dollars",
            "-V", "geometry:margin=1in",
            "-V", "mainfont=Times New Roman", 
            "-V", "lang=mk",
            "-V", "fontsize=12pt"
        ]
        
        subprocess.run(command, check=True, capture_output=True)
        return pdf_path
    except Exception as e:
        print(f"PDF Generation Error: {e}")
        return None

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

# --- СТАТИСТИЧКИ ДАШБОРД ---
with st.expander("📊 Статистика на Архивата", expanded=True):
    col1, col2, col3 = st.columns(3)
    col1.metric("Вкупно Задачи", len(all_problems))
    
    # Пресметка за графикони
    grade_counts = {}
    cat_counts = {}
    
    for p in all_problems:
        g = p['grade']
        c = p['category']
        grade_counts[g] = grade_counts.get(g, 0) + 1
        cat_counts[c] = cat_counts.get(c, 0) + 1
        
    # Најпопуларна категорија
    if cat_counts:
        top_cat = max(cat_counts, key=cat_counts.get)
        col2.metric("Најчеста Област", f"{top_cat.capitalize()} ({cat_counts[top_cat]})")
    
    # Просечна тежина
    avg_diff = sum(p['difficulty'] for p in all_problems) / len(all_problems) if all_problems else 0
    col3.metric("Просечна Тежина", f"{avg_diff:.1f} / 5")

    st.markdown("---")
    
    # Графикони
    c1, c2 = st.columns(2)
    with c1:
        st.caption("Задачи по Одделение")
        st.bar_chart(grade_counts)
    with c2:
        st.caption("Задачи по Област")
        st.bar_chart(cat_counts)

st.sidebar.header("🔍 Филтри")

# 1. Филтер за Одделение
grades = sorted(list(set(p['grade'] for p in all_problems if p['grade'] != "N/A")), key=lambda x: int(x) if x.isdigit() else 99)
selected_grades = st.sidebar.multiselect("Одделение", grades, default=grades)

# 2. Филтер за Категорија
categories = sorted(list(set(p['category'] for p in all_problems if p['category'] != "N/A")))
selected_categories = st.sidebar.multiselect("Категорија", categories, default=categories)

# 3. Филтер за Тежина
min_diff, max_diff = st.sidebar.slider("Тежина", 1, 10, (1, 10))

# 4. Филтер за Тагови
all_tags = sorted(list(set(tag for p in all_problems for tag in p['meta'].get('tags', []))))
selected_tags = st.sidebar.multiselect("Тагови", all_tags)

# 5. Пребарување текст
search_query = st.sidebar.text_input("Пребарај текст (пр. триаголник)")

# 6. Филтер за Визуелизација
show_missing_images = st.sidebar.checkbox("⚠️ Само задачи без слика")

# --- КОПЧЕ ЗА СЛУЧАЈНА ЗАДАЧА ---
if st.sidebar.button("🎲 Случајна Задача"):
    candidates = [p for p in all_problems if p['grade'] in selected_grades and p['category'] in selected_categories]
    if candidates:
        st.session_state['random_prob'] = random.choice(candidates)
    else:
        st.sidebar.warning("Нема задачи за избор!")

# --- ПРИМЕНА НА ФИЛТРИ ---
filtered_problems = [
    p for p in all_problems
    if p['grade'] in selected_grades
    and p['category'] in selected_categories
    and min_diff <= p['difficulty'] <= max_diff
    and (not selected_tags or any(tag in p['meta'].get('tags', []) for tag in selected_tags))
    and (search_query.lower() in p['body'].lower() if search_query else True)
    and (p['meta'].get('has_manim_placeholder', False) if show_missing_images else True)
]

# Ако е кликнато "Случајна", прикажи ја само неа
if 'random_prob' in st.session_state:
    filtered_problems = [st.session_state['random_prob']]
    del st.session_state['random_prob']
    st.info("🎲 Избрана е случајна задача!")

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

# --- PDF ГЕНЕРАТОР ---
if st.button("📄 Генерирај PDF од овие задачи"):
    with st.spinner("Генерирам PDF..."):
        pdf_file = generate_pdf(current_batch)
        if pdf_file and os.path.exists(pdf_file):
            with open(pdf_file, "rb") as f:
                st.download_button(
                    label="⬇️ Преземи PDF Тест",
                    data=f,
                    file_name="math_test.pdf",
                    mime="application/pdf"
                )
        else:
            st.error("Грешка при генерирање. Проверете дали Pandoc и LaTeX се инсталирани.")

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
            
            # --- ПОВРЗАНИ ЗАДАЧИ ---
            current_skills = prob['meta'].get('related_skills', [])
            if current_skills:
                related_probs = []
                for p in all_problems:
                    if p['path'] == prob['path']: continue # Не ја вклучувај истата задача
                    
                    other_skills = p['meta'].get('related_skills', [])
                    # Проверка дали има пресек на skills
                    if set(current_skills) & set(other_skills):
                        related_probs.append(p)
                        if len(related_probs) >= 3: break # Доволно се 3 препораки
                
                if related_probs:
                    st.markdown("#### 🔗 Поврзани задачи:")
                    cols = st.columns(len(related_probs))
                    for i, rp in enumerate(related_probs):
                        with cols[i]:
                            st.info(f"**{rp['filename'].replace('.md', '').replace('_', ' ').title()}**\n\n(Skill: {', '.join(set(current_skills) & set(rp['meta'].get('related_skills', [])))})")

            st.caption(f"Извор: {prob['meta'].get('source', 'Непознат')} | Патека: {prob['path']}")
            st.markdown("---")

# --- ФУТЕР ---
st.sidebar.markdown("---")
st.sidebar.info("Ова е прототип изработен со Streamlit.")
