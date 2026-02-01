import pymongo
import json
from bson import json_util

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['olympiad_db']
print("Collections:", db.list_collection_names())
col = db['curriculum']
doc = col.find_one()
if doc:
    print("Found a document in curriculum:")
    print(json.dumps(doc, indent=2, default=json_util.default))
else:
    print("No documents found in curriculum collection.")
