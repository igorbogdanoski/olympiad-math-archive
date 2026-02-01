#!/usr/bin/env python3
import os
import subprocess
import sys

# Roman numerals to grade format mapping
roman_to_grade = {
    '"I"': '"grade_1"',
    '"II"': '"grade_2"',
    '"III"': '"grade_3"',
    '"IV"': '"grade_4"',
    '"V"': '"grade_5"',
    '"VI"': '"grade_6"',
    '"VII"': '"grade_7"',
    '"VIII"': '"grade_8"',
    '"IX"': '"grade_9"',
    '"X"': '"grade_10"',
    '"XI"': '"grade_11"',
    '"XII"': '"grade_12"'
}

def fix_seed_file(filepath):
    """Fix a seed file to use grade_X format instead of Roman numerals"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace Roman numerals with grade format
        for roman, grade in roman_to_grade.items():
            content = content.replace(f'"grade": {roman}', f'"grade": {grade}')

        # Fix print statements to avoid Unicode issues
        content = content.replace('🗑️', 'Deleting')
        content = content.replace('💾', 'Inserting')
        content = content.replace('✅', 'SUCCESS')
        content = content.replace('👉', 'Check')

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

    # Find all complete seed files
    complete_seeds = []
    for filename in os.listdir(backend_dir):
        if filename.startswith('seed_grade_') and filename.endswith('_complete.py'):
            complete_seeds.append(os.path.join(backend_dir, filename))

    complete_seeds.sort()  # Sort by grade number

    print(f"Found {len(complete_seeds)} complete seed files")

    # Fix and run each seed file
    for seed_file in complete_seeds:
        print(f"\nProcessing {os.path.basename(seed_file)}...")
        if fix_seed_file(seed_file):
            if run_seed_file(seed_file):
                print(f"Completed {os.path.basename(seed_file)}")
            else:
                print(f"Failed to run {os.path.basename(seed_file)}")
        else:
            print(f"Failed to fix {os.path.basename(seed_file)}")

if __name__ == "__main__":
    main()