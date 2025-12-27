import json
import os
import sys

def validate_json(file_path):
    print(f"Checking file: {file_path}...")

    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print("JSON syntax is valid.")
        
        if not isinstance(data, list):
            print("Error: Root element must be a list of objects.")
            return

        required_fields = [
            "problem_id", 
            "grade", 
            "problem_text_mk", 
            "solution_content", 
            "analysis_hint"
        ]
        
        errors_found = False
        
        for index, item in enumerate(data):
            # Check for required fields
            for field in required_fields:
                if field not in item:
                    print(f"Error in item #{index + 1} (ID: {item.get('problem_id', 'Unknown')}): Missing field '{field}'")
                    errors_found = True
            
            # Check for duplicates (e.g., duplicate keys in source file usually cause JSON decode error, 
            # but logical duplicates like same problem_id need checking)
            # Note: Python's json.load automatically handles duplicate keys by keeping the last one, 
            # so we check for unique problem_ids across the list.
            
        # Check for duplicate problem_ids
        ids = [item.get("problem_id") for item in data if "problem_id" in item]
        if len(ids) != len(set(ids)):
            print("Error: Duplicate problem_ids found!")
            from collections import Counter
            duplicates = [item for item, count in Counter(ids).items() if count > 1]
            print(f"Duplicate IDs: {duplicates}")
            errors_found = True

        if not errors_found:
            print(f"Validation successful! Found {len(data)} problems.")
        else:
            print("Validation failed with errors.")

    except json.JSONDecodeError as e:
        print(f"JSON Syntax Error: {e}")
        print(f"Error at line {e.lineno}, column {e.colno}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Adjust path relative to where you run the script
    target_file = os.path.join(os.path.dirname(__file__), 'input.json')
    validate_json(target_file)
