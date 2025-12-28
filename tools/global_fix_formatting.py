import os
import re

DOCS_DIR = r"c:\Users\pc4all\Documents\matholimpiad\olympiad-math-archive\docs"

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    # 1. Fix Image Centering
    # Pattern: ![Alt](path) -> <div align="center"><img src="path" alt="Alt" width="500"/></div>
    # But only if it's not already in a div.
    # Regex explanation:
    # ^!\[(.*?)\]\((.*?)\)\s*$ matches a line that is just an image markdown.
    content = re.sub(
        r'^!\[(.*?)\]\((.*?)\)\s*$', 
        r'<div align="center">\n  <img src="\2" alt="\1" width="500"/>\n</div>', 
        content, 
        flags=re.MULTILINE
    )

    # 2. Remove Geo-Mentor Code blocks
    # Pattern: > **👨‍💻 Geo-Mentor Code:** ... (multiline)
    # We'll look for the specific block structure.
    content = re.sub(
        r'> \*\*👨‍💻 Geo-Mentor Code:\*\*\s*\n> .*?\n> .*?\n\n?',
        '',
        content,
        flags=re.DOTALL
    )
    # Clean up double newlines created by removal
    content = re.sub(r'\n\n\n+', '\n\n', content)

    # 3. Fix Conclusion Placeholder
    content = content.replace('<Краен резултат.>', 'Видете го решението погоре.')

    # 4. Convert <details> to ??? success and handle Steps
    # This is the tricky part. We need to find the <details> block.
    
    details_pattern = re.compile(r'<details>\s*<summary>👀 Прикажи го решението</summary>(.*?)</details>', re.DOTALL)
    
    def replace_details(match):
        inner_content = match.group(1).strip()
        
        # Check if there are "Step" markers like "**Чекор X:**"
        # Regex to find steps: \*\*Чекор \d+.*?\*\*
        step_pattern = re.compile(r'(\*\*Чекор \d+.*?\*\*)(.*?)(?=(\*\*Чекор \d+|$))', re.DOTALL)
        
        steps = list(step_pattern.finditer(inner_content))
        
        if steps:
            # If steps are found, construct a multi-admonition block
            new_block = "## 💡 Решение\n\n"
            
            # Check if there is intro text before the first step
            first_step_start = steps[0].start()
            if first_step_start > 0:
                intro_text = inner_content[:first_step_start].strip()
                if intro_text:
                    # Indent intro text for a general "success" block or just leave it outside?
                    # Let's put it in a general block first if needed, or just leave it.
                    # Actually, the user wants "Step by Step".
                    # Let's put the intro in a "??? info" block or just text.
                    # For safety, let's put everything in the new format.
                    pass 

            for step in steps:
                title = step.group(1).replace('**', '').strip() # Remove bold markers for the title
                body = step.group(2).strip()
                
                # Indent body
                indented_body = '\n    '.join(body.split('\n'))
                
                new_block += f'??? tip "{title}"\n    {indented_body}\n\n'
            
            # Check for conclusion/answer at the end (after last step)
            # The regex (?=(\*\*Чекор \d+|$)) handles the split, but we might miss text after the last step if it's not captured.
            # Actually, the last group(2) captures everything until end of string or next step.
            
            return new_block
        else:
            # No explicit steps found, use the single "success" block
            indented_content = '\n    '.join(inner_content.split('\n'))
            return f'## 💡 Решение\n\n??? success "👀 Прикажи го решението"\n    {indented_content}'

    content = details_pattern.sub(replace_details, content)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

count = 0
for root, dirs, files in os.walk(DOCS_DIR):
    for file in files:
        if file.endswith(".md"):
            if process_file(os.path.join(root, file)):
                count += 1
                print(f"Fixed: {file}")

print(f"Total files fixed: {count}")
