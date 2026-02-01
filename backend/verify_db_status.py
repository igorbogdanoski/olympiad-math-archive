import pymongo
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27035/")
DB_NAME = "olympiad_db"

def check_db():
    try:
        client = pymongo.MongoClient(MONGO_URI)
        db = client[DB_NAME]
        
        problems_count = db.problems.count_documents({})
        curriculum_count = db.curriculum.count_documents({})
        test_instances_count = db.test_instances.count_documents({})
        
        print(f"Database: {DB_NAME}")
        print(f"Problems collection: {problems_count} documents")
        print(f"Curriculum collection: {curriculum_count} documents")
        print(f"Test Instances collection: {test_instances_count} documents")
        
        if problems_count > 0:
            sample = db.problems.find_one()
            print(f"Sample problem: {sample.get('title')} ({sample.get('problem_id')})")
            
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")

if __name__ == "__main__":
    check_db()
