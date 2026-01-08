import os
import re
import datetime

# --- КОНФИГУРАЦИЈА ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "../"))
LOG_FILE = os.path.join(BASE_DIR, "docs", "assets", "manim_code_log.md")
ARCHIVE_FILE = os.path.join(BASE_DIR, "docs", "assets", "manim_code_archive.md")

entries_to_keep = 20

def to_ascii(text):
    m = {
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Ѓ': 'Gj', 'Е': 'E', 'Ж': 'Zh', 'З': 'Z', 'Ѕ': 'Dz',
        'И': 'I', 'Ј': 'J', 'К': 'K', 'Л': 'L', 'Љ': 'Lj', 'М': 'M', 'Н': 'N', 'Њ': 'Nj', 'О': 'O', 'П': 'P',
        'Р': 'R', 'С': 'S', 'Т': 'T', 'Ќ': 'Kj', 'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'C', 'Ч': 'Ch', 'Џ': 'Dj', 'Ш': 'Sh',
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'ѓ': 'gj', 'е': 'e', 'ж': 'zh', 'з': 'z', 'ѕ': 'dz',
        'и': 'i', 'ј': 'j', 'к': 'k', 'л': 'l', 'љ': 'lj', 'м': 'm', 'н': 'n', 'њ': 'nj', 'о': 'o', 'п': 'p',
        'р': 'r', 'с': 's', 'т': 't', 'ќ': 'kj', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'џ': 'dj', 'ш': 'sh',
        "✅": "OK", "❌": "ERR", "⏭️": "SKIP", "🎨": "RENDER", "⚠️": "WARN", "📭": "EMPTY", "📂": "READ", "✨": "DONE", "📎": "LINK", "🆔": "ID", "👨‍💻": "DEV", "📊": "STATS", "📦": "ARCHIVE", "🧹": "CLEAN"
    }
    return "".join(m.get(c, c) for c in text)

def safe_print(text):
    print(to_ascii(str(text)))

def rotate_logs():
    if not os.path.exists(LOG_FILE):
        safe_print(f"WARN Log fajlot ne postoi: {LOG_FILE}")
        return

    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Razdeluvanje na zapisite. Sekoj zapis pochnuva so "### ID Zadacha:"
    # Koristime lookahead za da go fatime pochetokot bez da go izbrisheme
    parts = re.split(r'(?=### ID Zadacha:)', content)
    
    # Prviot del mozhe da bide prazen ili header ako fajlot ne pochnuva vednash so zadacha
    header = ""
    tasks = []
    
    for part in parts:
        if not part.strip(): continue
        if part.strip().startswith("### ID Zadacha:"):
            tasks.append(part)
        else:
            header = part # Ako ima nekoj voved

    total_tasks = len(tasks)
    safe_print(f"STATS Vkupno pronajdeni zadachi vo logot: {total_tasks}")

    if total_tasks <= entries_to_keep:
        safe_print(f"OK Nema potreba od arhiviranje. Ima pomalku od {entries_to_keep} aktivni zadachi.")
        return

    # Podelba
    tasks_to_archive = tasks[:-entries_to_keep]
    tasks_to_keep = tasks[-entries_to_keep:]

    safe_print(f"ARCHIVE Arhiviram {len(tasks_to_archive)} stari zadachi...")
    safe_print(f"DONE Zadrzhuvam {len(tasks_to_keep)} najnovi zadachi...")

    # 1. Zapishuvanje vo Arhiva (Append)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    archive_header = fr"\n\n\n# --- ARHIVA: {timestamp} ---\n"
    
    with open(ARCHIVE_FILE, 'a', encoding='utf-8') as f:
        f.write(archive_header)
        for task in tasks_to_archive:
            f.write(task)
    
    safe_print(f"READ Starite zadachi se prefrleni vo: {ARCHIVE_FILE}")

    # 2. Prepishuvanje na LOG fajlot
    with open(LOG_FILE, 'w', encoding='utf-8') as f:
        if header: f.write(header)
        for task in tasks_to_keep:
            f.write(task)
            
    safe_print(f"CLEAN Glavniot log fajl e ischisten: {LOG_FILE}")

if __name__ == "__main__":
    rotate_logs()
