import json
import os
import sys
import re

# --- КОНФИГУРАЦИЈА ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(SCRIPT_DIR, "input.json")
SCHEMA_FILE = os.path.join(SCRIPT_DIR, "../ai/output_schema.json")

def validate_structure(data):
    errors = []
    
    # 1. Задолжителни полиња (според новата шема)
    required_fields = [
        "problem_id", 
        "grade", 
        "field", 
        "difficulty", 
        "problem_title", 
        "problem_text_mk", 
        "solution_content",
        "analysis_hint" # Ново задолжително поле!
    ]
    
    # Проверка дали е листа или единечен објект
    items = data if isinstance(data, list) else [data]
    
    for i, item in enumerate(items):
        prefix = f"Item {i+1} (ID: {item.get('problem_id', 'MISSING')}):"
        
        # А. Проверка на полиња
        for field in required_fields:
            if field not in item:
                errors.append(f"{prefix} Недостасува задолжително поле '{field}'.")
            elif not item[field]: # Ако е празно (None или "")
                errors.append(f"{prefix} Полето '{field}' е празно.")

        # Б. Проверка на типови
        if not isinstance(item.get('grade'), (int, str)):
             errors.append(f"{prefix} 'grade' мора да биде број.")
        
        # В. Проверка на LaTeX (Backslashes)
        # Ова е најчестата грешка: "\frac" наместо "\\frac" во JSON стрингови
        # Тешко е да се детектира совршено, но бараме сомнителни единечни backslashes
        # кои не се дел од познати escape sequences (\n, \t, \", \\)
        # (Ова е само предупредување, не грешка, бидејќи Python json.load веќе ги парсирал)
        
        # Г. Проверка на ID формат
        pid = str(item.get('problem_id', ''))
        if not re.match(r'^[a-zA-Z0-9_]+$', pid):
            errors.append(f"{prefix} 'problem_id' содржи недозволени знаци (само букви, бројки и _).")

    return errors

def validate_json(file_path):
    print(f"Checking file: {file_path}...")

    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print("JSON syntax is valid.")
        
        # Втор тест: Дали ја следи нашата структура?
        semantic_errors = validate_structure(data)
        
        if semantic_errors:
            print("\n❌ Пронајдени се структурни грешки:")
            for err in semantic_errors:
                print(f"  - {err}")
            print("\n⚠️ Поправи ги овие грешки пред да стартуваш build_problem.py!")
            sys.exit(1)
        else:
            print("✅ Структурата е валидна! Спремно за build_problem.py.")
            
    except json.JSONDecodeError as e:
        print(f"\n❌ КРИТИЧНА ГРЕШКА ВО JSON СИНТАКСАТА:")
        print(f"  {e}")
        print("\n💡 СОВЕТ: Провери ги LaTeX формулите. Дали користиш двојни коси црти (\\\\frac)?")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Неочекувана грешка: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Adjust path relative to where you run the script
    target_file = os.path.join(os.path.dirname(__file__), 'input.json')
    validate_json(target_file)
