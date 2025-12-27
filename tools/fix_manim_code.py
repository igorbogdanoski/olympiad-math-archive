
import re

log_path = r"c:\Users\pc4all\Documents\matholimpiad\olympiad-math-archive\assets\manim_code_log.md"

with open(log_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace Line(..., stroke_dash_pattern=...) with DashedLine(...)
# Regex to capture Line(arg1, arg2, ..., stroke_dash_pattern=...)
# This is tricky with regex.
# Simpler approach: Look for stroke_dash_pattern inside Line(...)

# Pattern: Line(..., stroke_dash_pattern=[...], ...)
# We want to change Line to DashedLine and remove stroke_dash_pattern argument.

# Let's just do a simple replacement for the specific pattern I used before if any.
# But actually, in my recent generation I used DashedLine directly.
# So maybe I don't need it for this batch.

# However, to be safe, let's just check if "stroke_dash_pattern" exists in the file.
if "stroke_dash_pattern" in content:
    print("Found stroke_dash_pattern. Attempting to fix...")
    # This is a naive fix, but might work for simple cases
    # Replace "Line(" with "DashedLine(" if the line contains "stroke_dash_pattern"
    lines = content.split('\n')
    new_lines = []
    for line in lines:
        if "stroke_dash_pattern" in line and "Line(" in line:
            line = line.replace("Line(", "DashedLine(")
            # Remove the stroke_dash_pattern arg
            # Assuming it's like ", stroke_dash_pattern=[4, 4]"
            line = re.sub(r",\s*stroke_dash_pattern\s*=\s*\[[^\]]*\]", "", line)
        new_lines.append(line)
    
    new_content = '\n'.join(new_lines)
    
    with open(log_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Fixed.")
else:
    print("No issues found.")
