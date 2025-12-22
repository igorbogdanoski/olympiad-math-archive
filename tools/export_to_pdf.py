import subprocess
import os
import sys

# --- КОНФИГУРАЦИЈА ---
# Ја наоѓаме патеката каде што е скриптата, па одиме едно ниво погоре (во главната папка)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVE_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "../"))

def export_to_pdf(file_path):
    """
    Конвертира Markdown фајл во PDF користејќи Pandoc.
    """
    # Проверка дали фајлот постои
    if not os.path.exists(file_path):
        print(f"❌ ГРЕШКА: Фајлот не постои: {file_path}")
        return

    # Името на PDF фајлот ќе биде исто, само со .pdf екстензија
    pdf_file_path = file_path.replace(".md", ".pdf")

    # Командата за Pandoc
    # --pdf-engine=xelatex е најдобар за кирилица и математички формули
    command = [
        "pandoc",
        file_path,
        "-o", pdf_file_path,
        "--pdf-engine=xelatex", 
        "--from=markdown+tex_math_dollars",
        "--standalone",
        "-V", "geometry:margin=1in" # Опционално: маргини
    ]

    try:
        print(f"🚀 Конвертирам: {os.path.basename(file_path)}...")
        # Извршување на командата
        subprocess.run(command, check=True, capture_output=True, text=True, encoding='utf-8')
        
        print(f"✅ УСПЕХ! PDF фајлот е креиран:")
        print(f"   📄 {pdf_file_path}")
        
    except FileNotFoundError:
        print("❌ ГРЕШКА: Pandoc не е инсталиран или не е во PATH.")
        print("   Инсталирај го од: https://pandoc.org/install.html")
    except subprocess.CalledProcessError as e:
        print(f"❌ ГРЕШКА при конверзијата (Pandoc error):")
        print(e.stderr)
    except Exception as e:
        print(f"❌ Неочекувана грешка: {e}")

# --- ГЛАВЕН ДЕЛ (MAIN) ---
if __name__ == "__main__":
    # Проверуваме дали корисникот внел аргумент (патека до фајлот)
    if len(sys.argv) > 1:
        # Го земаме аргументот (патеката што ја напиша во терминал)
        relative_path = sys.argv[1]
        
        # Ја спојуваме со главната папка за да добиеме целосна патека
        full_path = os.path.join(ARCHIVE_ROOT, relative_path)
        
        export_to_pdf(full_path)
    else:
        # Ако не внел ништо, му кажуваме како се користи
        print("\n⚠️  УПАТСТВО ЗА КОРИСТЕЊЕ:")
        print("---------------------------------------------------")
        print("Користи: python export_to_pdf.py <патека_до_фајлот>")
        print("\nПример:")
        print("python export_to_pdf.py grade_9/algebra/numerus_4333_4333.md")
        print("---------------------------------------------------\n")