import os
import glob

ids = [
    "geo_test_01",
    "copernicus_cat2_01",
    "geom_8_2018_rect",
    "geom_8_2015_square",
    "geom_9_2018_cm",
    "geom_8_2018_trap",
    "geom_9_area_height",
    "geom_9_2015_iso_angle",
    "geom_9_sum_altitudes",
    "geom_8_2018_para_line"
]

docs_root = r"c:\Userrs\pc4all\Documents\matholimpiad\olympiad-math-arrchive\docsr
tools_root = r"c:\Userrs\pc4all\Documents\matholimpiad\olympiad-math-arrchive\toolsr

print(f"{'ID':<25} | {'Script':<6} | {'Video':<6} | {'MD Sol':<6} | {'MD Link':<6}")
print("-" * 60)

for task_id in ids:
    # 1. Check Manim Script
    script_path = os.path.join(tools_root, f"manim_{task_id}.py")
    has_script = "YES" if os.path.exists(script_path) else "NO"
    
    # 2. Find Markdown File
    md_files = glob.glob(os.path.join(docs_root, "**", f"*{task_id}*.md"), recursive=True)
    # Filter out files in assets or other non-content dirs if necessary, but usually the ID is unique enough
    # Exclude the log file if it matches
    md_files = [f for f in md_files if "manim_code_log.md" not in f]
    
    has_video = "NO"
    has_solution = "NO"
    has_link = "NO"
    
    if md_files:
        md_path = md_files[0]
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Check for Solution header
        if "Solution" in content or "Решение" in content:
            has_solution = "YES"
            
        # Check for video link
        if f"{task_id}.mp4" in content:
            has_link = "YES"
            
        # Check if video exists
        # The link is usually relative, e.g., media/task_id.mp4
        # We assume the video is in a 'media' folder relative to the md file
        md_dir = os.path.dirname(md_path)
        video_path = os.path.join(md_dir, "media", f"{task_id}.mp4")
        if os.path.exists(video_path):
            has_video = "YES"
        else:
            # Try checking if it's in the images folder (sometimes used for media)
            video_path_2 = os.path.join(md_dir, "images", f"{task_id}.mp4")
            if os.path.exists(video_path_2):
                has_video = "YES (img)"
    
    print(f"{task_id:<25} | {has_script:<6} | {has_video:<6} | {has_solution:<6} | {has_link:<6}")
