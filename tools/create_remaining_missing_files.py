import os

targets = [
    'grade_9/algebra/cnt92_v2_27.md',
    'grade_9/algebra/num_li2_09.md',
    'grade_9/algebra/sigma_adv_07.md',
    'grade_8/geometry/cyclic_chase.md',
    'grade_6/logic/problem_example.md',
    'grade_9/algebra/cnt92_v2_16.md',
    'algebra/linear_equations.md',
    'grade_9/geometry/sigma_adv_05.md',
    'grade_9/geometry/sigma_adv_13.md',
    'pre_olympiad/grade_6/geometry/numerus_4367_4367.md'
]

docs_root = os.path.join(os.getcwd(), 'docs')

for target in targets:
    file_path = os.path.join(docs_root, target)
    dir_path = os.path.dirname(file_path)
    
    if not os.path.exists(dir_path):
        print(f"Creating directory: {dir_path}")
        os.makedirs(dir_path, exist_ok=True)
        
    if not os.path.exists(file_path):
        print(f"Creating file: {file_path}")
        
        # Determine title from filename
        filename = os.path.basename(file_path)
        title = filename.replace('.md', '').replace('_', ' ').title()
        
        # Calculate relative path to index.md
        # Count how many directories deep we are relative to docs/
        rel_path = os.path.relpath(dir_path, docs_root)
        if rel_path == '.':
            depth = 0
        else:
            depth = len(rel_path.split(os.sep))
        
        back_link = "../" * (depth + 1) + "index.md"
        # If depth is 0 (in docs root), back_link is ../index.md which is wrong if index.md is in docs/
        # Wait, index.md is in docs/. So if file is in docs/subdir, link is ../index.md.
        # If file is in docs/subdir/subsubdir, link is ../../index.md.
        # If file is in docs/, link is index.md (but we are linking "Back to Home").
        
        if depth == 0:
             back_link = "index.md" # Self reference? No, usually index.md is the home.
        else:
             back_link = "../" * depth + "index.md"

        content = f"""# {title}

🚧 **Work in Progress**

This content is currently missing and will be added soon.

[🏠 Back to Home]({back_link})
"""
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    else:
        print(f"File already exists (unexpected): {file_path}")

print("Done creating remaining missing files.")
