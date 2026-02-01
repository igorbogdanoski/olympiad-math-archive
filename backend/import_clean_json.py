#!/usr/bin/env python3
"""
Script to import clean JSON curriculum data into MongoDB.
This replaces the messy parsed data with clean, structured curriculum data.
"""

import json
import os
from pymongo import MongoClient

# MongoDB connection
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "olympiad_archive"
COLLECTION_NAME = "curricula"

def connect_db():
    try:
        client = MongoClient(MONGO_URI)
        db = client[DB_NAME]
        print(f"[OK] Connected to MongoDB: {DB_NAME}")
        return db[COLLECTION_NAME]
    except Exception as e:
        print(f"[ERROR] Connection failed: {e}")
        return None

def clean_curriculum_data(data):
    """Clean and standardize curriculum data structure"""
    if not isinstance(data, dict):
        return None

    # Handle different possible structures
    nastavna_programa = data.get("nastavna_programa", {})
    modulani_edinici = nastavna_programa.get("modulani_edinici", [])
    tematiki_celini = nastavna_programa.get("тематски_целини", modulani_edinici)

    if not tematiki_celini:
        print("[WARNING] No thematic units found in data")
        return None

    themes = []
    for unit in tematiki_celini:
        if isinstance(unit, dict):
            # Try different key names for objectives
            objectives = (
                unit.get("rezultati_od_ucenje_celi") or
                unit.get("резултати_од_учење") or
                unit.get("objectives") or
                unit.get("цели") or
                []
            )

            # Ensure objectives is a list
            if isinstance(objectives, str):
                objectives = [objectives]
            elif not isinstance(objectives, list):
                objectives = []

            # Clean objective texts
            clean_objectives = []
            for obj in objectives:
                if isinstance(obj, str) and obj.strip():
                    # Remove extra whitespace and clean text
                    clean_obj = " ".join(obj.split())
                    if len(clean_obj) > 10:  # Only include meaningful objectives
                        clean_objectives.append(clean_obj)
                elif isinstance(obj, dict) and obj.get("text"):
                    clean_objectives.append(obj["text"])

            if clean_objectives:  # Only add themes that have objectives
                theme = {
                    "id": unit.get("id") or unit.get("број") or len(themes) + 1,
                    "title": unit.get("naslov") or unit.get("наслов") or unit.get("title") or f"Тема {len(themes) + 1}",
                    "objectives": clean_objectives
                }
                themes.append(theme)

    if not themes:
        print("[WARNING] No valid themes found after cleaning")
        return None

    # Determine grade level from filename or data
    grade = (
        data.get("oddel") or
        data.get("odelenie") or
        data.get("grade") or
        data.get("одделение") or
        "Unknown"
    )

    return {
        "grade_level": str(grade),
        "themes": themes,
        "source_file": "clean_import.json",
        "last_updated": "2026-01-20",
        "data_quality": "clean"
    }

def import_json_file(file_path, collection):
    """Import a single JSON file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        cleaned_data = clean_curriculum_data(data)
        if not cleaned_data:
            print(f"[SKIP] {file_path} - No valid data after cleaning")
            return False

        # Upsert the data
        grade = cleaned_data["grade_level"]
        filter_query = {"grade_level": grade}
        result = collection.replace_one(filter_query, cleaned_data, upsert=True)

        if result.upserted_id:
            print(f"[INSERT] Successfully imported grade {grade} from {os.path.basename(file_path)}")
        else:
            print(f"[UPDATE] Successfully updated grade {grade} from {os.path.basename(file_path)}")

        print(f"  - {len(cleaned_data['themes'])} themes")
        total_objectives = sum(len(theme.get('objectives', [])) for theme in cleaned_data['themes'])
        print(f"  - {total_objectives} learning objectives")

        return True

    except Exception as e:
        print(f"[ERROR] Failed to import {file_path}: {e}")
        return False

def main():
    print("🧹 Clean JSON Curriculum Data Import Tool")
    print("=" * 50)

    collection = connect_db()
    if not collection:
        return

    # Directory containing clean JSON files
    json_dir = "../tools/clean_curriculum_data"  # Adjust path as needed

    if not os.path.exists(json_dir):
        print(f"[ERROR] Directory not found: {json_dir}")
        print("Please create the directory and place your clean JSON files there.")
        return

    json_files = [f for f in os.listdir(json_dir) if f.endswith('.json')]

    if not json_files:
        print(f"[WARNING] No JSON files found in {json_dir}")
        print("Please place your clean curriculum JSON files in this directory.")
        return

    print(f"[INFO] Found {len(json_files)} JSON files to process")
    print()

    success_count = 0
    for filename in json_files:
        file_path = os.path.join(json_dir, filename)
        if import_json_file(file_path, collection):
            success_count += 1
        print()

    print("=" * 50)
    print(f"✅ Import complete! Successfully processed {success_count}/{len(json_files)} files")
    print("\nYour curriculum data is now clean and ready for use!")
    print("The accordion UI will show themes collapsed by default for better UX.")

if __name__ == "__main__":
    main()