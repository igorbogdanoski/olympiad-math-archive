import pymongo
import re

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["olympiad_db"]
collection = db["curriculum"]

# Regex for non-Macedonian (Latin) letters (A-Za-z)
latin_pattern = re.compile(r"[A-Za-z]")

def contains_latin(text):
    if not isinstance(text, str):
        return False
    return bool(latin_pattern.search(text))

def check_document(doc):
    errors = []
    # Check grade and year_description
    if contains_latin(doc.get("grade", "")):
        errors.append(f"grade: {doc.get('grade')}")
    if contains_latin(doc.get("year_description", "")):
        errors.append(f"year_description: {doc.get('year_description')}")
    # Check themes
    for t_idx, theme in enumerate(doc.get("themes", [])):
        if contains_latin(theme.get("title", "")):
            errors.append(f"theme[{t_idx}].title: {theme.get('title')}")
        for field in ["objectives", "standards", "activities"]:
            for i, item in enumerate(theme.get(field, [])):
                if contains_latin(item):
                    errors.append(f"theme[{t_idx}].{field}[{i}]: {item}")
    return errors

def main():
    all_ok = True
    for doc in collection.find():
        doc_errors = check_document(doc)
        if doc_errors:
            all_ok = False
            print(f"\n❌ Non-Macedonian text found in grade {doc.get('grade', '?')}:" )
            for err in doc_errors:
                print("   ", err)
    if all_ok:
        print("\n✅ Сите одделенија се на македонски јазик (нема латиница во клучните полиња).")
    else:
        print("\n⚠️ Провери ги горните полиња за латиница!")

if __name__ == "__main__":
    main()