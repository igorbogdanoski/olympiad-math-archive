import pymongo
import json

client = pymongo.MongoClient("mongodb://localhost:27035/")
db = client["mathquest_db"]
problems_col = db["problems"]

sample = problems_col.find_one()
if sample:
    # Remove _id for cleaner printing
    sample.pop('_id', None)
    print(json.dumps(sample, indent=2, ensure_ascii=False))
else:
    print("No problems found.")
