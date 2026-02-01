import os
import re
import uuid
import shutil
import tempfile
import sys
import subprocess
from celery import Celery
from playwright.sync_api import sync_playwright
import markdown

# Celery konfig
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
celery_app = Celery('tasks', broker=REDIS_URL, backend=REDIS_URL)

def process_latex(text: str):
    text = re.sub(r'\$\$(.*?)\$\$', r'\\\[ \1 \\\]', text, flags=re.DOTALL)
    text = re.sub(r'\$([^\$]+)\$', r'\\\( \1 \\\)', text)
    return text

def render_content(text: str):
    if not text: return ""
    # Support for GeoGebra [geogebra:ID]
    text = re.sub(
        r'\[geogebra:([a-zA-Z0-9]+)\]', 
        r'<div class="geogebra-container" style="margin: 20px 0; border-radius: 12px; overflow: hidden; border: 1px solid #e2e8f0;"><iframe src="https://www.geogebra.org/material/iframe/id/\1/width/800/height/600/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/false/ctl/false" width="100%" height="400px" style="border:0px;"></iframe></div>', 
        text
    )
    processed_text = process_latex(text)
    return markdown.markdown(processed_text, extensions=['extra', 'nl2br', 'sane_lists'])

@celery_app.task
def generate_pdf_task(html_content, pdf_filename):
    pdf_path = os.path.join("worksheets", pdf_filename)
    os.makedirs("worksheets", exist_ok=True)
    
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(args=["--no-sandbox"])
            page = browser.new_page()
            page.set_content(html_content, wait_until="networkidle")
            
            try:
                page.wait_for_function("window.mathjaxFinished === true", timeout=15000)
            except:
                pass
            
            page.pdf(
                path=pdf_path, 
                format="A4", 
                margin={"top": "20mm", "bottom": "20mm", "left": "20mm", "right": "20mm"},
                print_background=True
            )
            browser.close()
        return {"status": "completed", "pdf_url": f"/worksheets/{pdf_filename}"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}

@celery_app.task
def generate_video_task(code, video_id):
    temp_dir = tempfile.mkdtemp()
    module_path = os.path.join(temp_dir, "lesson_script.py")
    os.makedirs("videos", exist_ok=True)
    
    with open(module_path, "w", encoding="utf-8") as f:
        f.write(code)

    try:
        output_dir = os.path.abspath("videos")
        cmd = [
            sys.executable, "-m", "manim",
            module_path, "LessonScene",
            "--format=mp4", "--quality", "m",
            "--media_dir", temp_dir, "--disable_caching"
        ]
        
        subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
        
        found_file = None
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                if file.endswith(".mp4") and "LessonScene" in file:
                    found_file = os.path.join(root, file)
                    break
            if found_file: break
            
        if found_file:
            final_filename = f"{video_id}.mp4"
            shutil.move(found_file, os.path.join(output_dir, final_filename))
            return {"status": "completed", "video_url": f"/videos/{final_filename}"}
        
        return {"status": "failed", "error": "Video file not found"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)
