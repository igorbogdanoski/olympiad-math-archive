#!/usr/bin/env python3
"""
Export all problems from local MongoDB to JSON for production deployment
Expert migration script - exports clean JSON for mongoimport
"""
import pymongo
import json
from datetime import datetime
from bson import json_util

def export_problems():
    print("🚀 Starting expert database export...")
    
    # Connect to local MongoDB
    print("📡 Connecting to local MongoDB (localhost:27035)...")
    try:
        client = pymongo.MongoClient("mongodb://localhost:27035/", serverSelectionTimeoutMS=5000)
        client.admin.command('ping')  # Test connection
        print("✅ Connected successfully!")
    except Exception as e:
        print(f"❌ Failed to connect to local MongoDB: {e}")
        print("💡 Make sure MongoDB is running: docker ps | grep mongo")
        return False
    
    db = client["olympiad_db"]
    problems_collection = db["problems"]
    
    # Count total problems
    total_count = problems_collection.count_documents({})
    print(f"📊 Found {total_count} problems in local database")
    
    if total_count == 0:
        print("⚠️  No problems found! Cannot export empty database.")
        return False
    
    # Export problems
    print("📦 Exporting problems to JSON...")
    problems = list(problems_collection.find({}))
    
    # Convert ObjectId to string for JSON serialization
    for problem in problems:
        if '_id' in problem:
            problem['_id'] = str(problem['_id'])
        if 'created_at' in problem and isinstance(problem['created_at'], datetime):
            problem['created_at'] = problem['created_at'].isoformat()
    
    # Save to JSON file
    output_file = "problems_export.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(problems, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Exported {len(problems)} problems to {output_file}")
    
    # Statistics
    print("\n📊 Export Statistics:")
    grades = {}
    categories = {}
    for p in problems:
        grade = p.get('grade', 'Unknown')
        category = p.get('category', 'Unknown')
        grades[grade] = grades.get(grade, 0) + 1
        categories[category] = categories.get(category, 0) + 1
    
    print(f"   By Grade: {dict(sorted(grades.items()))}")
    print(f"   By Category: {categories}")
    
    # File size
    import os
    file_size = os.path.getsize(output_file) / (1024 * 1024)
    print(f"   File size: {file_size:.2f} MB")
    
    client.close()
    
    print(f"\n🎯 Next steps:")
    print(f"   1. SCP: scp problems_export.json root@76.13.129.9:/tmp/")
    print(f"   2. SSH: ssh root@76.13.129.9")
    print(f"   3. Import: mongoimport --host localhost:27035 --db olympiad_db --collection problems --file /tmp/problems_export.json --jsonArray")
    print(f"   4. Verify: mongosh --host localhost:27035 olympiad_db --eval 'db.problems.count()'")
    
    return True

if __name__ == "__main__":
    success = export_problems()
    if success:
        print("\n✅ Export complete! Ready for deployment.")
    else:
        print("\n❌ Export failed. Fix errors and try again.")
