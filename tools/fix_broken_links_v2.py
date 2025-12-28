import os
import re

DOCS_DIR = r"c:\Users\pc4all\Documents\matholimpiad\olympiad-math-archive\docs"

def fix_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return

    original_content = content
    
    rel_path = os.path.relpath(filepath, DOCS_DIR)
    parts = rel_path.split(os.sep)
    depth = len(parts) - 1 
    
    # Fix 1: grade_X/README.md linking to ../../README.md
    # Should link to ../index.md (docs/index.md)
    if depth == 1 and parts[1] == "README.md" and parts[0].startswith("grade_"):
        content = content.replace("../../README.md", "../index.md")

    # Fix 2: grade_9/README.md linking to ../../README.md
    # Same as above, covered by the logic.

    # Fix 3: grade_8/geometry/3_1597_viviani_theorem_08.md linking to ../../skill_guides/triangle_decomposition.md
    # The warning says: "contains a link '../../skill_guides/triangle_decomposition.md', but the target 'skill_guides/triangle_decomposition.md' is not found".
    # This means the file `docs/skill_guides/triangle_decomposition.md` does not exist.
    # I cannot fix missing files, but I can check if the link path is correct relative to the file.
    # File is in `docs/grade_8/geometry/`. `../../skill_guides/` goes to `docs/skill_guides/`.
    # If the file is missing, I can't do much except maybe remove the link or point to a placeholder.
    # But wait, the warning says "target 'skill_guides/triangle_decomposition.md' is not found".
    # This confirms the file is missing.
    
    # Fix 4: skill_guides/absolute_value.md linking to ../grade_10/algebra/2025_mun_y2_4a.md
    # Warning: "target 'grade_10/algebra/2025_mun_y2_4a.md' is not found".
    # This means `docs/grade_10/algebra/2025_mun_y2_4a.md` is missing.
    # Again, missing target files.
    
    # Fix 5: skill_guides/angle_chasing.md linking to cyclic_quads.md
    # Warning: "target 'skill_guides/cyclic_quads.md' is not found".
    # Missing file.

    # Fix 6: skill_guides/angle_chasing.md linking to ../grade_7/geometry/isosceles_angles.md
    # Warning: "target 'grade_7/geometry/isosceles_angles.md' is not found".
    # Missing file.

    # It seems most of the remaining warnings are about MISSING TARGET FILES, not broken relative paths.
    # The relative paths look correct (e.g. `../grade_10/...` from `skill_guides/`).
    # The issue is that the referenced files (e.g. `2025_mun_y2_4a.md`) do not exist in the `docs` folder.
    
    # However, the README links are definitely fixable.
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {rel_path}")

print("Starting link fix round 2...")
for root, dirs, files in os.walk(DOCS_DIR):
    for file in files:
        if file.endswith(".md"):
            fix_file(os.path.join(root, file))
print("Done.")
