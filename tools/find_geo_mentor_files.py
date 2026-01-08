import os

ARCHIVE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))

def find_problematic_files():
    print("🔍 Searching for files with 'Geo-Mentor' but no image link...")
    
    count = 0
    for root, dirs, files in os.walk(ARCHIVE_ROOT):
        if "tools" in root or "assets" in root: continue
        
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    has_geo_mentor = "Geo-Mentor" in content
                    has_image_link = "![Визуелизација]" in content
                    has_placeholder = "<!-- Ова место е резервирано за автоматската слика од Manim -->" in content
                    
                    if has_geo_mentor:
                        status = "✅ Has Image" if has_image_link else "❌ NO Image"
                        print(f"📄 {status}: {file}")
                        if not has_image_link:
                            count += 1
                        
                except Exception as e:
                    print(f"❌ Error reading {file}: {e}")

    print(fr"\nFound {count} files.")

if __name__ == "__main__":
    find_problematic_files()
