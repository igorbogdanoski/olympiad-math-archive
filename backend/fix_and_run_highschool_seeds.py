#!/usr/bin/env python3
import os
import subprocess
import sys
import re

def fix_highschool_seed_file(filepath, grade_num):
    """Fix a high school seed file to use grade_X format"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace grade format
        content = re.sub(r'"grade":\s*"HighSchool_[IVXLCDM]+"', f'"grade": "grade_{grade_num}"', content)

        # Fix deletion query
        content = re.sub(r'"grade":\s*"HighSchool_[IVXLCDM]+"', f'"grade": "grade_{grade_num}"', content)

        # Fix print statements to avoid Unicode issues
        content = content.replace('✅', 'SUCCESS')
        content = content.replace('Година', 'Year')
        content = content.replace('Средно', 'High School')
        content = content.replace('е комплетно внесена', 'inserted successfully')

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"Fixed {filepath}")
        return True
    except Exception as e:
        print(f"Error fixing {filepath}: {e}")
        return False

def run_seed_file(filepath):
    """Run a seed file"""
    try:
        result = subprocess.run([sys.executable, filepath], capture_output=True, text=True, cwd=os.path.dirname(filepath))
        if result.returncode == 0:
            print(f"Successfully ran {os.path.basename(filepath)}")
            print(result.stdout.strip())
            return True
        else:
            print(f"Failed to run {os.path.basename(filepath)}")
            print(result.stderr.strip())
            return False
    except Exception as e:
        print(f"Error running {filepath}: {e}")
        return False

def main():
    backend_dir = os.path.dirname(__file__)

    # High school seed files mapping
    highschool_files = [
        ('seed_highschool_1.py', 9),
        ('seed_highschool_2.py', 10),
        ('seed_highschool_3.py', 11),
        ('seed_highschool_4.py', 12)
    ]

    print("Processing high school seed files...")

    # Fix and run each seed file
    for filename, grade_num in highschool_files:
        filepath = os.path.join(backend_dir, filename)
        if os.path.exists(filepath):
            print(f"\nProcessing {filename}...")
            if fix_highschool_seed_file(filepath, grade_num):
                if run_seed_file(filepath):
                    print(f"Completed {filename}")
                else:
                    print(f"Failed to run {filename}")
            else:
                print(f"Failed to fix {filename}")
        else:
            print(f"File {filename} not found")

if __name__ == "__main__":
    main()