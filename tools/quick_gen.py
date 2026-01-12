#!/usr/bin/env python
import subprocess
import shutil
import os
from pathlib import Path

manim_code = '''from manim import *

class GenScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        A = np.array([0, 3, 0])
        B = np.array([-3, -1, 0])
        C = np.array([3, -1, 0])
        
        tri = Polygon(A, B, C, color=BLACK, stroke_width=4)
        label_a = MathTex("a").move_to((B+C)/2 + DOWN*0.3)
        label_b = MathTex("b").move_to((A+C)/2 + RIGHT*0.3)
        label_c = MathTex("c").move_to((A+B)/2 + LEFT*0.3)
        
        formula = MathTex(r"P = \\frac{M}{4N}", color=BLACK).scale(1.5).to_edge(DOWN)
        rect = SurroundingRectangle(formula, color=BLACK, buff=0.2)
        
        self.add(tri, label_a, label_b, label_c, formula, rect)
'''

# Write temp script
with open('tools/temp_quick.py', 'w') as f:
    f.write(manim_code)

# Run manim
cmd = ['manim', '-qh', '-s', '--disable_caching', 'tools/temp_quick.py', 'GenScene', '-o', 'regional_2025_3_3a.png']
result = subprocess.run(cmd, capture_output=True, text=True)

print("STDOUT:", result.stdout[-500:] if result.stdout else "")
print("STDERR:", result.stderr[-500:] if result.stderr else "")
print("Return code:", result.returncode)

# Find and move image
for root, dirs, files in os.walk('tools'):
    for file in files:
        if file == 'regional_2025_3_3a.png':
            src = os.path.join(root, file)
            dst = 'web/public/assets/images/regional_2025_3_3a/regional_2025_3_3a.png'
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy(src, dst)
            print(f"✅ Copied {src} to {dst}")
