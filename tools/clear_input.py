import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(SCRIPT_DIR, "input.json")

def clear_input():
    try:
        with open(INPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump([], f, indent=2)
        print(f"✅ Успешно исчистен: {INPUT_FILE}")
        print("   Сега е подготвен за нова серија задачи.")
    except Exception as e:
        print(f"❌ Грешка при чистење: {e}")

if __name__ == "__main__":
    clear_input()
