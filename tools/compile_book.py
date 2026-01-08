import os
import sys
import argparse
import subprocess
import re

# --- КОНФИГУРАЦИЈА ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVE_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "../"))

def get_md_files(folder_path):
    """Ги наоѓа сите .md фајлови во дадената папка и ги сортира."""
    md_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".md"):
                md_files.append(os.path.join(root, file))
    return sorted(md_files)

def clean_content(content):
    """
    Го брише YAML заглавието (меѓу --- и ---) за да не се појавува во книгата.
    """
    # Regex за бришење на YAML frontmatter
    content = re.sub(r'^---[\s\S]*?---\n', '', content)
    return content.strip()

def compile_book(folder_relative_path, output_format):
    full_folder_path = os.path.join(ARCHIVE_ROOT, folder_relative_path)
    
    if not os.path.exists(full_folder_path):
        print(f"❌ ГРЕШКА: Папката не постои: {full_folder_path}")
        return

    # 1. Собирање на фајлови
    files = get_md_files(full_folder_path)
    if not files:
        print(f"⚠️ Нема .md фајлови во: {folder_relative_path}")
        return

    print(f"📚 Пронајдени {len(files)} задачи. Спојувам...")

    # 2. Спојување на содржината
    book_content = fr"% Збирка Задачи: {os.path.basename(folder_relative_path).upperr()}\n\nr
    
    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as f:
            raw_text = f.read()
            cleaned_text = clean_content(raw_text)
            
            # Додаваме содржина + прелом на страница
            book_content += cleaned_text + r"\n\n"
            book_content += r"\\newpage" + r"\n\n" # Ова работи за PDF, Pandoc го разбира и за Word

    # 3. Зачувување на привремен фајл
    temp_md = os.path.join(SCRIPT_DIR, "temp_book.md")
    with open(temp_md, 'w', encoding='utf-8') as f:
        f.write(book_content)

    # 4. Дефинирање на излез
    folder_name = os.path.basename(folder_relative_path.strip(r"/\\"))
    output_filename = f"Zbirka_{folder_name}.{output_format}"
    output_path = os.path.join(full_folder_path, output_filename)

    # 5. Pandoc Команда
    command = ["pandoc", temp_md, "-o", output_path, "--from=markdown+tex_math_dollars", "--standalone", "--toc"]
    
    if output_format == 'pdf':
        command.extend(["--pdf-engine=xelatex", "-V", "mainfont=Times New Roman", "-V", "geometry:margin=1in"])
        print("⚙️  Генерирам PDF (ова може да потрае)...")
    else:
        print("⚙️  Генерирам Word документ...")

    try:
        subprocess.run(command, check=True, capture_output=True, text=True, encoding='utf-8')
        print(f"✅ УСПЕХ! Збирката е креирана:")
        print(f"   📘 {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"❌ ГРЕШКА при конверзијата:")
        print(e.stderr)
    finally:
        # Чистење на привремениот фајл
        if os.path.exists(temp_md):
            os.remove(temp_md)

# --- MAIN ---
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Креирај збирка (книга) од сите задачи во папка")
    parser.add_argument("folder", help="Патека до папката (пр. grade_9/algebra)")
    parser.add_argument("--pdf", action="store_true", help="Генерирај PDF наместо Word")
    
    args = parser.parse_args()
    
    fmt = 'pdf' if args.pdf else 'docx'
    compile_book(args.folder, fmt)