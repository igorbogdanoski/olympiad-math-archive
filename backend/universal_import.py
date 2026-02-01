import json
import os
from database import get_database

def import_data():
    print("🔌 Поврзување со базата...")
    db = get_database()
    
    file_path = "full_data.json"
    
    if not os.path.exists(file_path):
        print(f"❌ ГРЕШКА: Фајлот {file_path} не постои! Дали го ископиравте?")
        return

    print(f"📂 Читање на {file_path}...")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        # СЦЕНАРИО 1: Фајлот е директна листа на одделенија
        if isinstance(data, list):
            print(f"✅ Детектиран формат: ЛИСТА со {len(data)} елементи.")
            collection = db["curriculum"]
            collection.delete_many({}) # Чистење на старото
            collection.insert_many(data)
            print(f"🎉 Успешно внесени {len(data)} записи во 'curriculum'!")

        # СЦЕНАРИО 2: Фајлот е речник (Dictionary) со повеќе категории
        elif isinstance(data, dict):
            print(f"✅ Детектиран формат: РЕЧНИК.")
            print(f"🔑 Пронајдени клучеви: {list(data.keys())}")
            
            # Проверка за Наставна Програма
            if "curriculum" in data:
                coll = db["curriculum"]
                coll.delete_many({})
                coll.insert_many(data["curriculum"])
                print(f"📚 Внесени {len(data['curriculum'])} елементи во 'curriculum'.")
            elif "grades" in data:
                coll = db["grades"] # Или curriculum, зависи од вашата база
                coll.delete_many({})
                coll.insert_many(data["grades"])
                print(f"📚 Внесени {len(data['grades'])} елементи во 'grades'.")
                
            # Проверка за Задачи (Problems)
            if "problems" in data:
                coll = db["problems"]
                coll.delete_many({})
                coll.insert_many(data["problems"])
                print(f"🧮 Внесени {len(data['problems'])} задачи во 'problems'.")
                
        print("\n🏁 Импортот заврши! Освежете ја веб-страната.")

    except Exception as e:
        print(f"❌ Се случи грешка при импортот: {e}")

if __name__ == "__main__":
    import_data()
