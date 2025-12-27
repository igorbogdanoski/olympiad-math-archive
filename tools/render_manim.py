import re
import os
import subprocess
import shutil
from pathlib import Path

# Configuration
PROJECT_ROOT = Path(__file__).parent.parent
LOG_FILE = PROJECT_ROOT / "assets" / "manim_code_log.md"
IMAGES_DIR = PROJECT_ROOT / "assets" / "images"
TEMP_SCENE_FILE = PROJECT_ROOT / "temp_manim_render.py"

def parse_log_file():
    """Parses the log file and returns a list of (problem_id, code) tuples."""
    if not LOG_FILE.exists():
        print(f"Log file not found: {LOG_FILE}")
        return []

    content = LOG_FILE.read_text(encoding="utf-8")
    
    # Regex to find problem entries
    # Matches: ### 🆔 Задача: <ID> ... ```python <code> ```
    pattern = re.compile(
        r"### 🆔 Задача:\s*([a-zA-Z0-9_\-]+).*?```python\s+(.*?)```",
        re.DOTALL
    )
    
    entries = []
    for match in pattern.finditer(content):
        problem_id = match.group(1).strip()
        code = match.group(2)
        entries.append((problem_id, code))
    
    return entries

def clean_code(code):
    """
    Cleans up the extracted code to ensure it's a valid Manim script.
    """
    if "# --- AI GENERATED CODE START ---" in code:
        parts = code.split("# --- AI GENERATED CODE START ---")
        preamble = parts[0]
        generated = parts[1]
        
        # Check if generated code contains a full class definition
        if re.search(r"class\s+\w+\(Scene\):", generated):
            # Use the generated code as the source of truth
            # But ensure imports are there
            new_code = ""
            if "from manim import" not in generated:
                new_code += "from manim import *\n\n"
            new_code += generated
            code = new_code
        else:
            # Assume it's a method body or method definition
            # We need to wrap it in the class from preamble or a default one
            
            # 1. Get imports
            imports = "from manim import *\n"
            
            # 2. Get the body
            # Remove 'def construct(self):' line if present to avoid duplication when we wrap
            generated_lines = generated.split('\n')
            body_lines = []
            for line in generated_lines:
                if "def construct(self):" in line:
                    continue
                body_lines.append(line)
                
            # 3. Construct new file content
            final_code = imports
            final_code += f"\nclass ProblemScene(Scene):\n"
            final_code += "    def construct(self):\n"
            final_code += "        self.camera.background_color = WHITE\n"
            final_code += "        Text.set_default(color=BLACK)\n"
            final_code += "        MathTex.set_default(color=BLACK)\n"
            final_code += "        Mobject.set_default(color=BLACK)\n"
            
            for line in body_lines:
                # Fix indentation: Add 8 spaces
                if line.strip():
                    final_code += "        " + line.strip() + "\n"
            
            code = final_code

    # Common fixes for AI hallucinations
    # Remove background_line_style from Axes/NumberPlane as it causes TypeError in recent Manim versions
    code = re.sub(r"background_line_style\s*=\s*\{[^}]*\},?", "", code)
    
    return code

def render_scene(problem_id, code):
    """Renders the scene and saves the image."""
    print(f"Processing {problem_id}...")
    
    # Check if image already exists
    image_path = IMAGES_DIR / f"{problem_id}.png"
    if image_path.exists():
        print(f"  Image already exists: {image_path}")
        return

    # Clean code
    try:
        code = clean_code(code)
    except Exception as e:
        print(f"  ❌ Error cleaning code: {e}")
        return

    # Write to temp file
    TEMP_SCENE_FILE.write_text(code, encoding="utf-8")
    
    # Run Manim
    # We need to find the scene name. 
    # If we wrapped it, it's ProblemScene.
    # If it was a full class, we need to find the class name.
    scene_name = "ProblemScene"
    match = re.search(r"class\s+(\w+)\(Scene\):", code)
    if match:
        scene_name = match.group(1)

    cmd = [
        "python", "-m", "manim", "-ql", "-s", 
        "--disable_caching",
        str(TEMP_SCENE_FILE), scene_name
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        # Find output
        # Manim default output: media/images/temp_manim_render/<SceneName>_ManimCE_v0.19.1.png
        media_dir = PROJECT_ROOT / "media" / "images" / "temp_manim_render"
        output_file = media_dir / f"{scene_name}_ManimCE_v0.19.1.png"
        
        if output_file.exists():
            # Move to assets
            IMAGES_DIR.mkdir(parents=True, exist_ok=True)
            shutil.copy(output_file, image_path)
            print(f"  ✅ Generated: {image_path}")
        else:
            print("  ❌ Output file not found.")
            # Try to find any png in that folder
            found_files = list(media_dir.glob("*.png"))
            if found_files:
                print(f"  ⚠️ Found other files: {found_files}")
                shutil.copy(found_files[0], image_path)
                print(f"  ✅ Generated (fallback): {image_path}")
            else:
                print(result.stdout)
            
    except subprocess.CalledProcessError as e:
        print(f"  ❌ Manim failed for {problem_id}")
        # print(e.stdout) # Too verbose
        print(e.stderr)

def main():
    entries = parse_log_file()
    print(f"Found {len(entries)} entries.")
    
    for problem_id, code in entries:
        # Clean ID (remove extra text if any)
        problem_id = problem_id.split()[0] 
        render_scene(problem_id, code)
        
    # Cleanup
    if TEMP_SCENE_FILE.exists():
        os.remove(TEMP_SCENE_FILE)

if __name__ == "__main__":
    main()
