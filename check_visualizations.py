import os

regional_files = [
    'docs\\grade_9\\number_theory\\regional_2025_1_3ab.md',
    'docs\\grade_9\\number_theory\\regional_2025_1_2b_alternative.md',
    'docs\\grade_9\\number_theory\\regional_2025_1_2b.md',
    'docs\\grade_9\\number_theory\\regional_2025_1_2a.md',
    'docs\\grade_9\\geometry\\regional_2025_1_4b_verified.md',
    'docs\\grade_9\\geometry\\regional_2025_1_4b.md',
    'docs\\grade_9\\geometry\\regional_2025_1_4a.md',
    'docs\\grade_12\\number_theory\\regional_2025_4_3a.md',
    'docs\\grade_12\\geometry\\regional_2025_4_4b.md',
    'docs\\grade_12\\geometry\\regional_2025_4_2a.md',
    'docs\\grade_12\\combinatorics\\regional_2025_4_3b.md',
    'docs\\grade_12\\algebra\\regional_2025_4_4a.md',
    'docs\\grade_12\\algebra\\regional_2025_4_2b.md',
    'docs\\grade_12\\algebra\\regional_2025_4_1ab.md',
    'docs\\grade_9\\algebra\\regional_2025_1_1ab.md',
    'docs\\grade_11\\number_theory\\regional_2025_3_4a.md',
    'docs\\grade_11\\geometry\\regional_2025_3_3a.md',
    'docs\\grade_11\\geometry\\regional_2025_3_2ab.md',
    'docs\\grade_11\\algebra\\regional_2025_3_4b.md',
    'docs\\grade_11\\algebra\\regional_2025_3_3b.md',
    'docs\\grade_11\\algebra\\regional_2025_3_1ab.md',
    'docs\\grade_10\\number_theory\\regional_2025_2_1b.md',
    'docs\\grade_10\\geometry\\regional_2025_2_3ab.md',
    'docs\\grade_10\\algebra\\regional_2025_2_4ab.md',
    'docs\\grade_10\\algebra\\regional_2025_2_2b.md',
    'docs\\grade_10\\algebra\\regional_2025_2_2a.md',
    'docs\\grade_10\\algebra\\regional_2025_2_1a.md'
]

missing = []
for f in regional_files:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            if '### 🎨 Визуелизација' not in content:
                missing.append(f)

print("Files WITHOUT visualization section:")
for f in missing:
    print(f"  - {f}")
print(f"\nTotal missing: {len(missing)}")
