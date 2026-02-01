import json
import os
from pymongo import MongoClient

# MongoDB Connection
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27035/")
DB_NAME = "olympiad_db"
COLLECTION_NAME = "problems"

def import_problems():
    # Path to problems.json
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(base_dir, "web", "src", "data", "problems.json")
    
    if not os.path.exists(json_path):
        print(f"❌ Error: {json_path} not found")
        return

    print(f"Reading {json_path}...")
    with open(json_path, 'r', encoding='utf-8') as f:
        problems = json.load(f)

    print(f"Found {len(problems)} problems. Connecting to MongoDB...")
    
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

    # Clear existing problems (optional, but requested for 'full migration')
    print("Clearing existing problems...")
    collection.delete_many({})

    mongo_docs = []
    for p in problems:
        meta = p.get("meta", {})
        
        # Skip repository info entry if it exists
        if meta.get("description") == "Repository Information Overview":
            continue
            
        content = p.get("body", "")
        solution = ""
        
        # Split body into content and solution if possible
        if "## Решение" in content:
            parts = content.split("## Решение", 1)
            content_markdown = parts[0].strip()
            solution = parts[1].strip()
        elif "## Solution" in content:
            parts = content.split("## Solution", 1)
            content_markdown = parts[0].strip()
            solution = parts[1].strip()
        else:
            content_markdown = content

        doc = {
            "problem_id": meta.get("problem_id", p.get("filename", "unknown")),
            "title": meta.get("title", "Untitled Problem"),
            "content_markdown": content_markdown,
            "solution": solution,
            "topic": p.get("category", meta.get("type", "General")),
            "difficulty": int(p.get("difficulty", meta.get("difficulty", 3))),
            "grade": str(p.get("grade", meta.get("grade", "unknown"))),
            "source_path": p.get("path", ""),
            "primary_skill": meta.get("primary_skill", ""),
            "tags": meta.get("tags", []),
            "curriculum_codes": meta.get("curriculum_codes", []),
            "related_skills": meta.get("related_skills", []),
            "related_theorems": meta.get("related_theorems", []),
            "source": meta.get("source", "")
        }
        mongo_docs.append(doc)

    if mongo_docs:
        print(f"Inserting {len(mongo_docs)} problems into {DB_NAME}.{COLLECTION_NAME}...")
        result = collection.insert_many(mongo_docs)
        print(f"✅ Successfully inserted {len(result.inserted_ids)} problems!")
    else:
        print("⚠️ No valid problems found to insert.")

    client.close()

if __name__ == "__main__":
    import_problems()
