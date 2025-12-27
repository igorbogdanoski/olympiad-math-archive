import subprocess
import os
import sys

# --- КОНФИГУРАЦИЈА ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVE_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "../"))

def export_to_pdf(file_path):
    """
    Конвертира Markdown фајл во PDF користејќи Pandoc со поддршка за Кирилица.
    """
    if not os.path.exists(file_path):
        print(f"❌ ГРЕШКА: Фајлот не постои: {file_path}")
        return

    pdf_file_path = file_path.replace(".md", ".pdf")

    # Determine directories
    file_dir = os.path.dirname(file_path)
    file_name = os.path.basename(file_path)
    pdf_name = os.path.basename(pdf_file_path).replace(".pdf", "_v2.pdf")

    # --- КЛУЧНИОТ ДЕЛ ЗА КИРИЛИЦА ---
    # Користиме 'xelatex' и му задаваме фонт што има кирилица (Times New Roman).
    # Ако си на Linux, смени го фонтот во 'DejaVu Serif' или 'Liberation Serif'.
    # За Windows, 'Times New Roman' или 'Arial' се најсигурни.
    
    command = [
        "pandoc",
        file_name,               # Use filename only
        "-o", pdf_name,          # Output filename only
        "--pdf-engine=xelatex", 
        "--from=markdown+tex_math_dollars",
        "--standalone",
        "-V", "geometry:margin=1in",     # Маргини
        "-V", "mainfont=Times New Roman", # <--- ОВА Е РЕШЕНИЕТО ЗА КИРИЛИЦА
        "-V", "lang=mk",                 # Јазик (за хифенација)
        "-V", "fontsize=12pt"            # Големина на фонт
    ]

    try:
        print(f"🚀 Конвертирам: {file_name}...")
        # Run in the directory of the file so relative paths work
        result = subprocess.run(command, cwd=file_dir, check=True, capture_output=True, text=True, encoding='utf-8')
        
        # Print stderr (warnings) if any
        if result.stderr:
            print("⚠️  Pandoc Warnings/Output:")
            print(result.stderr)
        
        print(f"✅ УСПЕХ! PDF фајлот е креиран:")
        print(f"   📄 {pdf_file_path}")
        
    except FileNotFoundError:
        print("❌ ГРЕШКА: Pandoc не е инсталиран.")
    except subprocess.CalledProcessError as e:
        print(f"❌ ГРЕШКА при конверзијата (LaTeX Error):")
        # Често грешката е дека фали фонт или пакет
        print(e.stderr)
        print("\n💡 СОВЕТ: Ако грешката е за фонтови, пробај да генерираш Word (.docx) наместо PDF.")
    except Exception as e:
        print(f"❌ Неочекувана грешка: {e}")

# --- MAIN ---
if __name__ == "__main__":
    if len(sys.argv) > 1:
        relative_path = sys.argv[1]
        full_path = os.path.join(ARCHIVE_ROOT, relative_path)
        export_to_pdf(full_path)
    else:
        print("\n⚠️  УПАТСТВО:")
        print("python export_to_pdf.py <патека_до_фајлот>")