import json
from database import get_database

def import_curriculum():
    print("🔌 Поврзување со базата...")
    db = get_database()
    collection = db["curriculum"]

    # Чистиме старо за да нема дупликати
    collection.delete_many({})

    print("📂 Читање на full_data.json...")
    with open("/app/backend/full_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # Трансформација: Од {"6": {...}} во [{"grade": "6", ...}]
    docs_to_insert = []
    for grade_key, content in data.items():
        # Правиме копија за да не го расипеме оригиналот
        doc = content.copy()
        # Го додаваме клучот како поле "grade"
        doc["grade"] = str(grade_key)
        docs_to_insert.append(doc)

    if docs_to_insert:
        collection.insert_many(docs_to_insert)
        print(f"✅ УСПЕШНО! Внесени се наставните програми за {len(docs_to_insert)} одделенија.")
        print("👉 Одете на веб-страната и проверете го менито 'Одделение'.")
    else:
        print("⚠️ Не најдов податоци за внес.")

if __name__ == "__main__":
    import_curriculum()
