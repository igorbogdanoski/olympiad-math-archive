import os
import pymongo

MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017/")
DB_NAME = "olympiad_db"

def get_database():
    client = pymongo.MongoClient(MONGO_URI)
    return client[DB_NAME]
