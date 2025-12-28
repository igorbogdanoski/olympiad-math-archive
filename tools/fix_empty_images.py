import os
import re
import sys
import argparse
from pathlib import Path

# Add current directory to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from render_manim import render_scene
except ImportError:
    print("❌ Error: Could not import 'render_manim.py'.")
    sys.exit(1)

# Configuration
BASE_DIR = Path(__file__).parent.parent.absolute()
DOCS_DIR = BASE_DIR / "docs"
LOG_FILE = DOCS_DIR / "assets" / "manim_code_log.md"
IMAGES_DIR = DOCS_DIR / "assets" / "images"

# Threshold for "empty" image (bytes)
# We saw empty images are ~10619 bytes. Let's set threshold at 15KB.
SIZE_THRESHOLD = 15 * 1024 

def get_code_blocks(content):
    pattern = r"### 🆔 Задача: (.*?)\s-.*?\n.*?```python\n(.*?)\n```"
    return re.findall(pattern, content, re.DOTALL)

def main():
    parser = argparse.ArgumentParser(description="Re-render empty or small Manim images.")
    parser.add_argument("--limit", type=int, default=5, help="Number of images to process in this batch.")
    args = parser.parse_args()

    if not LOG_FILE.exists():
        print(f"📭 Log file not found: {LOG_FILE}")
        return

    print(f"📂 Reading log file: {LOG_FILE}")
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    tasks = get_code_blocks(content)
    task_map = {pid.strip(): code for pid, code in tasks}
    
    print(f"🔍 Found {len(task_map)} tasks in log.")
    
    candidates = []
    
    # Scan images
    for prob_id, code in task_map.items():
        img_path = IMAGES_DIR / f"{prob_id}.png"
        
        should_render = False
        reason = ""
        
        if not img_path.exists():
            should_render = True
            reason = "Missing"
        else:
            size = img_path.stat().st_size
            if size < SIZE_THRESHOLD:
                should_render = True
                reason = f"Small size ({size} bytes)"
        
        if should_render:
            candidates.append((prob_id, code, reason))

    print(f"⚠️ Found {len(candidates)} images that need rendering.")
    
    to_process = candidates[:args.limit]
    print(f"🚀 Processing batch of {len(to_process)} images...\n")

    for i, (prob_id, code, reason) in enumerate(to_process, 1):
        print(f"[{i}/{len(to_process)}] 🎨 Rendering {prob_id} ({reason})...")
        try:
            # Remove bad file if exists
            target_image = IMAGES_DIR / f"{prob_id}.png"
            if target_image.exists():
                os.remove(target_image)
                
            success = render_scene(prob_id, code)
            if success:
                print(f"   ✅ Success: {prob_id}")
            else:
                print(f"   ❌ Failed: {prob_id}")
        except Exception as e:
            print(f"   ❌ Exception for {prob_id}: {e}")

    remaining = len(candidates) - len(to_process)
    if remaining > 0:
        print(f"\n⏳ {remaining} images remaining. Run the script again to process the next batch.")
    else:
        print("\n🎉 All empty images processed!")

if __name__ == "__main__":
    main()
