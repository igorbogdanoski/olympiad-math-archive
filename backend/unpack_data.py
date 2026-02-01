import json
import os
from database import get_database

def fix_data():
    print("🔧 Започнувам поправка на податоците...")
    db = get_database()
    collection = db["problems"]
    
    # 1. Прво бришеме сè (за да го тргнеме тој голем грешен запис)
    delete_result = collection.delete_many({})
    print(f"🧹 Избришани {delete_result.deleted_count} стари записи.")

    file_path = "/app/backend/full_data.json"
    
    if not os.path.exists(file_path):
        print("❌ Грешка: Фајлот full_data.json го нема во backend папката!")
        return

    print("📂 Читање на фајлот...")
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 2. Логика за отпакување
    tasks_to_insert = []

    if isinstance(data, dict):
        print("💡 Детектиран е РЕЧНИК (Dictionary). Ги земам вредностите...")
        # Проверуваме дали задачите се директно вредностите
        # (Ова ги претвора вредностите од речникот во Листа)
        tasks_to_insert = list(data.values())
        
        # Мала проверка: дали првиот елемент личи на задача?
        if tasks_to_insert and isinstance(tasks_to_insert[0], dict):
             print(f"   -> Најдов {len(tasks_to_insert)} потенцијални задачи.")
        else:
             print("⚠️ Вредностите во речникот не се објекти/задачи. Проверувам 'items' клуч...")
             if "items" in data:
                 tasks_to_insert = data["items"]
             elif "problems" in data:
                 tasks_to_insert = data["problems"]

    elif isinstance(data, list):
        print("💡 Детектирана е ЛИСТА.")
        tasks_to_insert = data

    # 3. Внесување во база
    if tasks_to_insert:
        # Безбедносна проверка: внесуваме само ако се речници
        valid_tasks = [t for t in tasks_to_insert if isinstance(t, dict)]
        
        if valid_tasks:
            try:
                collection.insert_many(valid_tasks)
                print(f"✅ УСПЕШНО! Внесени се {len(valid_tasks)} задачи поединечно!")
            except Exception as e:
                print(f"❌ Грешка при внесување: {e}")
        else:
            print("⚠️ Не најдов валидни податоци за внес.")
    else:
        print("❌ Не успеав да ги извлечам задачите од структурата.")

if __name__ == "__main__":
    fix_data()
