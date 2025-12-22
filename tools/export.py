import subprocess
import os
import sys
import argparse

# --- КОНФИГУРАЦИЈА ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVE_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "../"))

def check_if_file_open(filename):
    """Проверува дали фајлот е веќе отворен (за да избегнеме грешка)."""
    if os.path.exists(filename):
        try:
            with open(filename, 'a'):
                pass
        except IOError:
            return True
    return False

def export_file(input_path, output_format):
    """
    Главна функција за конверзија.
    input_path: Патека до .md фајлот
    output_format: 'docx' или 'pdf'
    """
    
    # 1. Проверка на влезниот фајл
    if not os.path.exists(input_path):
        print(f"❌ ГРЕШКА: Влезниот фајл не постои: {input_path}")
        return

    # 2. Дефинирање на излезниот фајл
    output_path = input_path.replace(".md", f".{output_format}")
    
    # 3. Проверка дали излезниот фајл е заклучен (отворен во Word/Adobe)
    if check_if_file_open(output_path):
        print(f"❌ ГРЕШКА: Фајлот '{os.path.basename(output_path)}' е отворен!")
        print(f"   👉 Затворете го програмот (Word/PDF Reader) и пробајте повторно.")
        return

    # 4. Креирање на командата за Pandoc
    command = ["pandoc", input_path, "-o", output_path, "--from=markdown+tex_math_dollars", "--standalone"]

    if output_format == 'pdf':
        # Подесувања за PDF (со поддршка за кирилица)
        command.extend([
            "--pdf-engine=xelatex",
            "-V", "mainfont=Times New Roman",
            "-V", "geometry:margin=1in",
            "-V", "fontsize=12pt"
        ])
        print(f"🚀 Конвертирам во PDF: {os.path.basename(input_path)}...")
    else:
        # Подесувања за Word (нема потреба од посебни фонтови)
        print(f"🚀 Конвертирам во Word: {os.path.basename(input_path)}...")

    # 5. Извршување
    try:
        subprocess.run(command, check=True, capture_output=True, text=True, encoding='utf-8')
        print(f"✅ УСПЕХ! Креиран фајл:")
        print(f"   📂 {output_path}")
    except FileNotFoundError:
        print("❌ ГРЕШКА: Pandoc не е инсталиран.")
        print("   Инсталирај го од: https://pandoc.org/install.html")
    except subprocess.CalledProcessError as e:
        print(f"❌ ГРЕШКА при конверзијата:")
        print(e.stderr)
        if output_format == 'pdf':
            print("💡 Совет: PDF конверзијата бара LaTeX. Ако немате LaTeX, користете Word.")

# --- MAIN ---
if __name__ == "__main__":
    # Поставување на аргументи од командна линија
    parser = argparse.ArgumentParser(description="Конвертор за Олимписка Архива (MD -> Word/PDF)")
    parser.add_argument("file", help="Релативна патека до .md фајлот (пр. grade_9/algebra/task.md)")
    parser.add_argument("--pdf", action="store_true", help="Генерирај PDF наместо Word")
    
    args = parser.parse_args()

    # Спојување на патеката
    full_path = os.path.join(ARCHIVE_ROOT, args.file)
    
    # Одлука за формат
    fmt = 'pdf' if args.pdf else 'docx'
    
    export_file(full_path, fmt)