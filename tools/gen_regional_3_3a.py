from manim import *
import os

class SolutionScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Define a generic triangle
        A = np.array([0, 3, 0])
        B = np.array([-3, -1, 0])
        C = np.array([3, -1, 0])
        
        triangle = Polygon(A, B, C, color=BLACK, stroke_width=4)
        
        # Labels for sides
        lbl_c = MathTex("c", color=BLACK).move_to((A + B) / 2 + LEFT * 0.3)
        lbl_b = MathTex("b", color=BLACK).move_to((A + C) / 2 + RIGHT * 0.3)
        lbl_a = MathTex("a", color=BLACK).move_to((B + C) / 2 + DOWN * 0.3)
        
        # Labels for angles
        alpha = MathTex(r"\alpha", color=RED).scale(0.8).next_to(A, DOWN, buff=0.2)
        beta = MathTex(r"\beta", color=RED).scale(0.8).next_to(B, UR, buff=0.2)
        gamma = MathTex(r"\gamma", color=RED).scale(0.8).next_to(C, UL, buff=0.2)
        
        # Identity to display
        identity = MathTex(r"M = a^2 + b^2 + c^2", color=BLUE).to_edge(UP, buff=0.5)
        identity2 = MathTex(r"N = \cot \alpha + \cot \beta + \cot \gamma", color=BLUE).next_to(identity, DOWN)
        
        # Final Result
        result = MathTex(r"P = \frac{M}{4N}", color=BLACK).scale(1.5).to_edge(DOWN, buff=0.5)
        box = SurroundingRectangle(result, color=BLACK, buff=0.2)
        
        # Add all elements
        self.add(triangle, lbl_a, lbl_b, lbl_c, alpha, beta, gamma)
        self.add(identity, identity2, result, box)

if __name__ == "__main__":
    os.system('manim -qh -s --disable_caching tools/gen_regional_3_3a.py SolutionScene --media_dir tools/media_gen -o regional_2025_3_3a.png')
    
    # Move file to correct location
    import shutil
    src = "tools/media_gen/images/1080p60/partial_movie_file/regional_2025_3_3a.png"
    dst = "web/public/assets/images/regional_2025_3_3a"
    os.makedirs(dst, exist_ok=True)
    shutil.copy(src, f"{dst}/regional_2025_3_3a.png")
    print(f"✅ Image copied to {dst}/regional_2025_3_3a.png")
