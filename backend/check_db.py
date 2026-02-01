import pymongo
try:
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['olympiad_db']
    count = db['curriculum'].count_documents({})
    print(f"Total documents: {count}")
    if count > 0:
        grades = db['curriculum'].distinct('grade')
        print(f"Grades: {grades}")
except Exception as e:
    print(f"Error: {e}")
