import pymongo
from datetime import datetime

# Connection to the remote database
client = pymongo.MongoClient("mongodb://76.13.129.9:27035/")
db = client["olympiad_db"]
collection = db["problems"]

problems = [
    {
        "problem_id": "2026_g9_t2_s4",
        "title": "Равенка на кружница",
        "grade": 9,
        "category": "geometry",
        "difficulty": 3,
        "content": "Одреди ја равенката на кружница со центар во точката $C(2, -3)$ и радиус $r = 5$.",
        "solution": "Општата равенка на кружница со центар $(x_0, y_0)$ и радиус $r$ е $(x - x_0)^2 + (y - y_0)^2 = r^2$. Замениме ги вредностите: $(x - 2)^2 + (y - (-3))^2 = 5^2$, што дава $(x - 2)^2 + (y + 3)^2 = 25$.",
        "curriculum_codes": ["MAT-O-G9-T2-S4"],
        "tags": ["аналитичка геометрија", "кружница"],
        "created_at": datetime.now()
    }
]

print(f"Connecting to remote database at 76.13.129.9:27035...")
try:
    for p in problems:
        collection.delete_many({"problem_id": p["problem_id"]})
    result = collection.insert_many(problems)
    print(f"Successfully inserted {len(result.inserted_ids)} problems for Grade 9 Theme 2.")
except Exception as e:
    print(f"Error: {e}")
