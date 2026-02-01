import pymongo
import json

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["olympiad_db"]
collection = db["curriculum"]

doc = collection.find_one({"grade": "grade_8"})
if doc:
    # Remove _id for JSON serialization
    if "_id" in doc:
        del doc["_id"]
    print(json.dumps(doc, indent=2)[:3000])
else:
    print("No document found for grade_8")
