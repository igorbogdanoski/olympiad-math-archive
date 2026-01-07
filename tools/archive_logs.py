import os
import re
import datetime

# --- КОНФИГУРАЦИЈА ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "../"))
LOG_FILE = os.path.join(BASE_DIR, "docs", "assets", "manim_code_log.md")
ARCHIVE_FILE = os.path.join(BASE_DIR, "docs", "assets", "manim_code_archive.md")

entries_to_keep = 20

def rotate_logs():
    if not os.path.exists(LOG_FILE):
        print(f"⚠️ Лог фајлот не постои: {LOG_FILE}")
        return

    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Разделување на записите. Секој запис почнува со "### 🆔 Задача:"
    # Користиме lookahead за да го фатиме почетокот без да го избришеме
    parts = re.split(r'(?=### 🆔 Задача:)', content)
    
    # Првиот дел може да биде празен или header ако фајлот не почнува веднаш со задача
    header = ""
    tasks = []
    
    for part in parts:
        if not part.strip(): continue
        if part.strip().startswith("### 🆔 Задача:"):
            tasks.append(part)
        else:
            header = part # Ако има некој вовед

    total_tasks = len(tasks)
    print(f"📊 Вкупно пронајдени задачи во логот: {total_tasks}")

    if total_tasks <= entries_to_keep:
        print(f"✅ Нема потреба од архивирање. Има помалку од {entries_to_keep} активни задачи.")
        return

    # Поделба
    tasks_to_archive = tasks[:-entries_to_keep]
    tasks_to_keep = tasks[-entries_to_keep:]

    print(f"📦 Архивирам {len(tasks_to_archive)} стари задачи...")
    print(f"✨ Задржувам {len(tasks_to_keep)} најнови задачи...")

    # 1. Запишување во Архива (Append)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    archive_header = f"\n\n\n# --- АРХИВА: {timestamp} ---\n"
    
    with open(ARCHIVE_FILE, 'a', encoding='utf-8') as f:
        f.write(archive_header)
        for task in tasks_to_archive:
            f.write(task)
    
    print(f"📂 Старите задачи се префрлени во: {ARCHIVE_FILE}")

    # 2. Препишување на LOG фајлот
    with open(LOG_FILE, 'w', encoding='utf-8') as f:
        if header: f.write(header)
        for task in tasks_to_keep:
            f.write(task)
            
    print(f"🧹 Главниот лог фајл е исчистен: {LOG_FILE}")

if __name__ == "__main__":
    rotate_logs()
