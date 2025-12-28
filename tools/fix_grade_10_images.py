import os
import re

DOCS_DIR = os.path.join(os.getcwd(), 'docs')
GRADE_10_GEO_DIR = os.path.join(DOCS_DIR, 'grade_10', 'geometry')
ASSETS_DIR = os.path.join(DOCS_DIR, 'assets', 'images')

print(f"Checking Grade 10 Geometry files in {GRADE_10_GEO_DIR}...")

for filename in os.listdir(GRADE_10_GEO_DIR):
    if not filename.endswith('.md') or filename == 'README.md':
        continue
        
    file_path = os.path.join(GRADE_10_GEO_DIR, filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check if image tag exists
    has_image = '![Визуелизација]' in content or '![Скица]' in content or '<img' in content
    
    if not has_image:
        print(f"⚠️  {filename}: Missing image tag.")
        
        # Try to deduce image name
        # 1. From problem_id
        pid_match = re.search(r'problem_id:\s*([\w_]+)', content)
        image_name = None
        
        if pid_match:
            image_name = f"{pid_match.group(1)}.png"
        else:
            # 2. From filename (remove extension)
            # e.g. classic_sangaku_olympiad_folklore_geo_three_circles_tangent.md -> geo_three_circles_tangent.png
            # This is tricky. Let's try to find a matching image in assets that contains part of the filename.
            base_name = filename.replace('.md', '')
            # Try exact match first
            if os.path.exists(os.path.join(ASSETS_DIR, f"{base_name}.png")):
                image_name = f"{base_name}.png"
            else:
                # Try to find the suffix that matches an image
                # e.g. classic_sangaku_olympiad_folklore_geo_three_circles_tangent -> geo_three_circles_tangent
                parts = base_name.split('_')
                for i in range(len(parts)):
                    candidate = "_".join(parts[i:]) + ".png"
                    if os.path.exists(os.path.join(ASSETS_DIR, candidate)):
                        image_name = candidate
                        break
        
        if image_name and os.path.exists(os.path.join(ASSETS_DIR, image_name)):
            print(f"   Found matching image: {image_name}")
            
            # Insert image tag
            # If ## 📐 Скица exists, put it there.
            # If not, put it after ## 📝 Текст на задачата section
            
            if "## 📐 Скица" in content:
                replacement = f"## 📐 Скица\n\n![Визуелизација](../../assets/images/{image_name}){{ width=500 }}\n"
                new_content = content.replace("## 📐 Скица", replacement, 1)
            elif "## 📝 Текст на задачата" in content:
                # Find end of text section (next header)
                text_section_start = content.find("## 📝 Текст на задачата")
                next_header = content.find("\n## ", text_section_start + 1)
                
                if next_header != -1:
                    # Insert before next header
                    insertion = f"\n\n## 📐 Скица\n\n![Визуелизација](../../assets/images/{image_name}){{ width=500 }}\n"
                    new_content = content[:next_header] + insertion + content[next_header:]
                else:
                    # Append to end
                    new_content = content + f"\n\n## 📐 Скица\n\n![Визуелизација](../../assets/images/{image_name}){{ width=500 }}\n"
            else:
                print("   Could not find suitable place to insert image.")
                continue
                
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"   ✅ Added image tag to {filename}")
            
        else:
            print(f"   ❌ Could not find image for {filename}")
    else:
        print(f"✅ {filename}: Has image.")

print("Done.")
