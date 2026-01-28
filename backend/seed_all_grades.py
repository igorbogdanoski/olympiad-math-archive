from database import get_database
db = get_database()
collection = db["curriculum"]

sample_data = {
    "grade": "9",
    "themes": [{"title": "Алгебра", "activities": ["Квадратни равенки"]}]
}

collection.update_one({"grade": "9"}, {"$set": sample_data}, upsert=True)
print("✅ Успешно внесени податоци за 9-то одделение!")
