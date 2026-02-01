<<<<<<< HEAD
import pymongo
import json
import os

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["olympiad_db"]
collection = db["curriculum"]

# Load JSON data
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
json_path = os.path.join(base_dir, "web", "src", "data", "curriculum_standards.json")
with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

mathematics = data["mathematics"]

# Clear existing data
collection.delete_many({})

# Insert each grade
for grade_key, grade_data in mathematics.items():
    # Convert JSON structure to Mongo structure
    mongo_doc = {
        "grade": grade_key,
        "year_description": f"Grade {grade_key.replace('grade_', '')}",
        "source": "curriculum_standards.json",
        "themes": []
    }

    topics = grade_data.get("topics", [])
    for topic in topics:
        theme = {
            "title": topic.get("name", ""),
            "objectives": topic.get("objectives", topic.get("learning_objectives", [])),
            "standards": topic.get("standards", []),
            "activities": topic.get("activities", [])
        }
        mongo_doc["themes"].append(theme)

    collection.insert_one(mongo_doc)
    print(f"Inserted {grade_key}")

print("All grades seeded from JSON!")
=======
from database import get_database
db = get_database()
collection = db["curriculum"]

sample_data = {
    "grade": "9",
    "themes": [{"title": "Алгебра", "activities": ["Квадратни равенки"]}]
}

collection.update_one({"grade": "9"}, {"$set": sample_data}, upsert=True)
print("✅ Успешно внесени податоци за 9-то одделение!")
>>>>>>> 2cfe4e73e9ab08775608bd53fa4d5ed4ddf2ab80
