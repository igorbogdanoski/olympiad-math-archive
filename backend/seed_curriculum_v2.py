import pymongo
import json
import os

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["olympiad_db"]
collection = db["curriculum"]

# Load JSON data
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
json_path = os.path.join(base_dir, "web", "src", "data", "curriculum_standards_processed.json")

if not os.path.exists(json_path):
    print(f"Error: {json_path} not found")
    exit(1)

with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

mathematics = data.get("subjects", {}).get("mathematics", {})

# Clear existing data
collection.delete_many({})

# Insert each grade
for grade_key, grade_data in mathematics.items():
    # Convert JSON structure to Mongo structure
    mongo_doc = {
        "grade": grade_key,
        "grade_level": grade_key,
        "source": "curriculum_standards_processed.json",
        "themes": []
    }

    themes = grade_data.get("themes", [])
    for t in themes:
        theme = {
            "title": t.get("name", ""),
            "code": t.get("code", ""),
            "objectives": t.get("objectives", []),
            "standards": t.get("standards", []),
            "standards_with_codes": t.get("standards_with_codes", []),
            "activities": t.get("activities", [])
        }
        mongo_doc["themes"].append(theme)

    collection.insert_one(mongo_doc)
    print(f"Inserted {grade_key} with {len(mongo_doc['themes'])} themes")

print("All grades seeded from processed JSON!")
