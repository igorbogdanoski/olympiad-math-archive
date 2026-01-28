import json
import os
from database import get_database

def restore_system():
    print("🔌 Поврзување со базата...")
    db = get_database()
    
    # --- ДЕЛ 1: КРЕИРАЊЕ НА МЕНИЈАТА (CURRICULUM) ---
    print("🏗️ Креирање на структурата на наставните програми...")
    curriculum_coll = db["curriculum"]
    curriculum_coll.delete_many({}) # Чистиме сè старо

    # Ова е стандардната структура за да се појават менијата
    structure = [
        {
            "grade": "6",
            "themes": [
                {"title": "Броеви", "standards": ["Природни броеви", "Деливост", "Дропки"]},
                {"title": "Геометрија", "standards": ["Агли", "Триаголник", "Кружница"]}
            ]
        },
        {
            "grade": "7",
            "themes": [
                {"title": "Алгебра", "standards": ["Степени", "Полиноми"]},
                {"title": "Геометрија", "standards": ["Вектори", "Трансформации"]}
            ]
        },
        {
            "grade": "8",
            "themes": [
                {"title": "Алгебра", "standards": ["Линеарни равенки", "Функции"]},
                {"title": "Геометрија", "standards": ["Питагорова теорема", "Призма и Пирамида"]}
            ]
        },
        {
            "grade": "9",
            "themes": [
                {"title": "Алгебра", "standards": ["Квадратни равенки", "Системи равенки"]},
                {"title": "Геометрија", "standards": ["Тригонометрија", "Сличност"]}
            ]
        }
    ]
    curriculum_coll.insert_many(structure)
    print("✅ Менијата за 6, 7, 8 и 9 одделение се креирани!")

    # --- ДЕЛ 2: ВНЕСУВАЊЕ НА ЗАДАЧИТЕ ОД АРХИВАТА ---
    print("📂 Вчитување на задачите од архивата...")
    file_path = "full_data.json" # Претпоставуваме дека е веќе копиран во backend
    
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            problems_coll = db["problems"]
            # Ако е листа, внеси ги директно
            if isinstance(data, list):
                problems_coll.insert_many(data)
                print(f"✅ Внесени {len(data)} задачи од архивата!")
            # Ако е речник, пробај да најдеш клуч
            elif isinstance(data, dict):
                # Пробуваме разни клучеви каде што може да се скриени задачите
                if "problems" in data:
                    problems_coll.insert_many(data["problems"])
                    print(f"✅ Внесени {len(data['problems'])} задачи!")
                else:
                    # Ако нема клуч, можеби целиот dict е една задача?
                    problems_coll.insert_one(data)
                    print("✅ Внесена 1 комплексна задача/архива.")
        except Exception as e:
            print(f"⚠️ Грешка при читање на задачите: {e}")
    else:
        print(f"⚠️ Фајлот {file_path} не е најден во backend папката. Менијата ќе работат, но ќе нема задачи.")

    print("\n🏁 РЕСТАВРИРАЊЕТО ЗАВРШИ! Освежи ја веб-страната.")

if __name__ == "__main__":
    restore_system()
