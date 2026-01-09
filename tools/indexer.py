import os
import re
import json
from pathlib import Path

def parse_problem(file_path):
    """Чита фајл и враќа метаподатоци и содржина."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return {}, "", file_path

    meta = {}
    # Екстракција на YAML frontmatter
    match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not match:
        # Пад назад ако нема нови редови веднаш по цртичките
        match = re.search(r'^---(.*?)---', content, re.DOTALL)
    
    if match:
        yaml_text = match.group(1)
        for line in yaml_text.split('\n'):
            if ':' in line:
                parts = line.split(':', 1)
                if len(parts) == 2:
                    key, val = parts
                    meta[key.strip()] = val.strip().replace('"', '').replace("'", "")
        
        # Екстракција на тагови
        tags = []
        tags_match = re.search(r'tags:\s*\n((?:\s*-\s*.*\n?)+)', yaml_text)
        if tags_match:
            tags_block = tags_match.group(1)
            tags = [t.strip().replace('- ', '').strip() for t in tags_block.split('\n') if t.strip()]
        meta['tags'] = tags

    # Екстракција на related_skills од content (бидејќи може да е надвор од yaml во некои формати или yaml парсерот е едноставен)
    related_skills = []
    skills_match = re.search(r'related_skills:\s*\n((?:\s*-\s*.*\n?)+)', content)
    if skills_match:
        skills_block = skills_match.group(1)
        related_skills = [s.strip().replace('- ', '').strip() for s in skills_block.split('\n') if s.strip()]
    meta['related_skills'] = related_skills
    
    # Екстракција на телото на задачата
    # 1. Тргни го YAML frontmatter
    body = re.sub(r'^---\s*\n[\s\S]*?\n---\s*', '', content).strip()
    
    # 2. Агресивно чистење на навигација и метаподатоци
    body = re.sub(r'\[⬅️ Назад кон Индексот\].*?(\n|$)', '', body)
    body = re.sub(r'# --- SKILL MAPPING[\s\S]*?(?=\n# |\Z)', '', body)
    body = re.sub(r'# --- TOPICS[\s\S]*?(?=\n# |\Z)', '', body)
    
    # 3. Чистење на MKDocs специфични карактери (admonitions)
    # Ги претвораме "??? tip" во нешто попрегледно или ги чистиме
    body = body.replace('??? tip "', '### ').replace('??? tip', '### Совет')
    body = body.replace('"', '') # Ги тргаме наводниците од насловите на тие секции
    
    # 4. Чистење на заостанати tags и непотребни заклучоци
    body = re.sub(r'tags:\s*\n(\s*- .*\n)*', '', body)
    body = re.sub(r'##\s+🏁\s+Заклучок.*', '', body)
    
    # 5. Тргни повеќекратни празни редови
    body = re.sub(r'\n{3,}', r'\n\n', body).strip()
    
    # 5. Конверзија на LaTeX delimiters за Streamlit/Web
    body = re.sub(r'\\\[(.*?)\\\]', r'$$\1$$', body, flags=re.DOTALL)
    body = re.sub(r'\\\((.*?)\\\)', r'$\1$', body, flags=re.DOTALL)
    
    # Проверка за Manim placeholder
    has_manim_placeholder = "<!-- Ова место е резервирано за автоматската слика од Manim -->" in content
    meta['has_manim_placeholder'] = has_manim_placeholder

    return meta, body, file_path

def build_index(archive_root):
    """Ги наоѓа сите задачи и креира листа од објекти."""
    problems = []
    # Избегнуваме печатење на патеки со кирилица во терминал што не поддржува
    
    for root, dirs, files in os.walk(archive_root):
        # Агресивно игнорирање на системски фолдери и фајлови во коренот
        if any(x in root for x in ["tools", "ai", "assets", "public", ".git", "web", "skill_guides", "theorems", "generated_worksheets", "media"]):
            continue
        
        # Игнорирај го коренот на docs (каде се README, MAINTENANCE итн.)
        if Path(root).resolve() == Path(archive_root).resolve() or Path(root).name == "docs":
            if "grade_" not in root: # Дозволи ако е docs/grade_X
                continue
            
        for file in files:
            # Само .md фајлови кои не се системски
            if file.endswith(".md") and not file.startswith("_") and file not in ["README.md", "problem_template.md", "geometry_problem_template.md", "MAINTENANCE.md", "plan.md"]:
                path = os.path.join(root, file)
                try:
                    meta, body, full_path = parse_problem(path)
                    
                    # Игнорирај задачи кои се празни или се "Work in Progress"
                    if not body or "Work in Progress" in body or len(body) < 50:
                        continue
                    parts = os.path.normpath(path).split(os.sep)
                    grade = "N/A"
                    category = "N/A"
                    
                    for part in parts:
                        if part.startswith("grade_"):
                            grade = part.replace("grade_", "")
                        elif part in ["algebra", "geometry", "number_theory", "combinatorics", "logic", "arithmetic", "analysis", "stereometry", "trigonometry"]:
                            category = part
                    
                    # Безбедно парсирање на тежина
                    try:
                        diff_val = int(meta.get('difficulty', 0))
                    except (ValueError, TypeError):
                        diff_val = 0
                            
                    problems.append({
                        "meta": meta,
                        "body": body,
                        "path": full_path,
                        "filename": file,
                        "grade": meta.get('grade', grade),
                        "category": meta.get('type', meta.get('category', category)),
                        "difficulty": diff_val
                    })
                except Exception as e:
                    # Избегнуваме UnicodeEncodeError при принт
                    try:
                        print(f"Error parsing {file}: {e}")
                    except:
                        print(f"Error parsing a file (encoding error)")
    
    return problems

def save_index(problems, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(problems, f, ensure_ascii=False, indent=2)
    print(f"Index saved to {output_path}")

def load_index(input_path):
    if os.path.exists(input_path):
        with open(input_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None
