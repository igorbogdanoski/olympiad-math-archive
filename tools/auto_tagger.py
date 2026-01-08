import os
import re
import json

# --- КОНФИГУРАЦИЈА ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVE_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "../"))
KEYWORDS_FILE = os.path.join(SCRIPT_DIR, "skill_keywords.json")

def load_keywords():
    with open(KEYWORDS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def analyze_text(text, keyword_map):
    found_tags = set()
    found_skills = set()
    
    text_lower = text.lower()
    
    for category, terms in keyword_map.items():
        for term, tags in terms.items():
            # Бараме цел збор (boundary) за да не фаќаме делови од зборови
            if re.search(rr'\b' + re.escape(term) + rr'\w*', text_lower):
                for tag in tags:
                    found_tags.add(tag)
                    # Првиот таг обично е специфичната вештина
                    if tag == tags[0]:
                        found_skills.add(tag)
                        
    return list(found_tags), list(found_skills)

def update_file(file_path, keyword_map):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Екстракција на frontmatter
    match = re.search(r'^---(.*?)---', content, re.DOTALL)
    if not match:
        print(f"⚠️ Skipping {os.path.basename(file_path)} (No frontmatter)")
        return False
        
    yaml_text = match.group(1)
    body = content[match.end():]
    
    # Анализа на текстот
    suggested_tags, suggested_skills = analyze_text(body, keyword_map)
    
    if not suggested_tags:
        return False
        
    # Ажурирање на YAML
    new_yaml = yaml_text
    
    # 1. Ажурирај tags
    if "tags:" not in new_yaml:
        new_yaml += r"\ntags:\n" + r"\n".join([f"  - {t}" for t in suggested_tags])
    else:
        # Ако има тагови, провери дали се празни или дополни
        tags_match = re.search(r'tags:\s*\n((?:\s*-\s*.*\n?)+)', new_yaml)
        if not tags_match:
             # Има "tags:" ама нема листа под него
             new_yaml = re.sub(r'tags:.*', r"tags:\n" + r"\n".join([f"  - {t}" for t in suggested_tags]), new_yaml)
        else:
            # Веќе има тагови, додај ги новите ако ги нема (опционално, засега не чепкаме ако веќе има)
            pass

    # 2. Ажурирај related_skills (ако нема)
    # related_skills често не е во YAML кај вас, туку може да е долу. 
    # Но, за да работи апликацијата, најдобро е да е во YAML.
    if "related_skills:" not in new_yaml:
        new_yaml += r"\nrrelated_skills:\nr + r"\n".join([f"  - {s}" for s in suggested_skills])
    
    # Реконструкција на фајлот
    new_content = f"---{new_yaml}---{body}"
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✅ Updated: {os.path.basename(file_path)} | Added {len(suggested_tags)} tags")
        return True
    
    return False

def main():
    print("🚀 Starting Auto-Tagger...")
    keyword_map = load_keywords()
    
    count = 0
    for root, dirs, files in os.walk(ARCHIVE_ROOT):
        if "tools" in root or "assets" in root: continue
        
        for file in files:
            if file.endswith(".md") and "template" not in file and file != "README.md":
                path = os.path.join(root, file)
                if update_file(path, keyword_map):
                    count += 1
                    
    print(f"🏁 Done! Updated {count} files.")

if __name__ == "__main__":
    main()
