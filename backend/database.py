import os
import pymongo
from dotenv import load_dotenv

# Load environment variables
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path)

MONGO_URI = os.getenv("MONGO_URI", "mongodb://76.13.129.9:27035/")
DB_NAME = "olympiad_db"

_client = None

def get_database():
    global _client
    if _client is None:
        try:
            _client = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
            # Test connection
            _client.server_info()
        except Exception as e:
            print(f"❌ Database Connection Error: {e}")
            return None
    return _client[DB_NAME]
