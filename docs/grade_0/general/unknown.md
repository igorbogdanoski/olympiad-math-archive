---
{}
---

from manim import *

class SolutionScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Title
        title = Text("Задача 1873", font_size=48, color=BLACK).to_edge(UP)
        self.play(Write(title))
        
        # Step 1: The Equation
        eq_text = MathTex("x^2 + ax + b = 0", color=BLACK).scale(1.2)
        condition = Text("Корен: ", font_size=32, color=BLACK).next_to(eq_text, LEFT)
        root_val = MathTex("x = a+b", color=BLUE).next_to(condition, RIGHT)
        group1 = VGroup(condition, root_val).next_to(eq_text, UP)
        
        self.play(Write(eq_text))
        self.play(FadeIn(group1))
        self.wait(1)
        
        # Step 2: Substitution
        sub_eq = MathTex("(a+b)^2 + a(a+b) + b = 0", color=BLACK)
        self.play(Transform(eq_text, sub_eq))
        self.wait(1)
        
        # Step 3: Expansion
        expanded = MathTex("2a^2 + 3ab + b^2 + b = 0", color=BLACK)
        self.play(Transform(eq_text, expanded))
        self.wait(1)
        
        # Step 4: Quadratic in b
        quad_b = MathTex("b^2 + (3a+1)b + 2a^2 = 0", color=BLUE)
        self.play(Transform(eq_text, quad_b))
        self.wait(1)
        
        # Step 5: Discriminant
        disc_text = MathTex("D = (3a+1)^2 - 4(2a^2) = k^2", color=RED)
        disc_res = MathTex("a^2 + 6a + 1 = k^2", color=RED)
        
        self.play(eq_text.animate.to_edge(UP).scale(0.8), FadeOut(title), FadeOut(group1))
        self.play(Write(disc_text))
        self.wait(1)
        self.play(Transform(disc_text, disc_res))
        self.wait(1)
        
        # Step 6: Completion of Square
        sq_text = MathTex("(a+3)^2 - 8 = k^2", color=BLACK)
        diff_sq = MathTex("(a+3)^2 - k^2 = 8", color=BLACK)
        
        self.play(Transform(disc_text, sq_text))
        self.wait(0.5)
        self.play(Transform(disc_text, diff_sq))
        self.wait(1)
        
        # Step 7: Solutions
        solutions = VGroup(
            Text("Случаи за (a+3-k)(a+3+k)=8:", font_size=24, color=BLACK),
            MathTex("1) \\; a=0 \\Rightarrow b \\in \{0, -1\}", color=GREEN),
            MathTex("2) \\; a=-6 \\Rightarrow b \\in \{8, 9\}", color=GREEN)
        ).arrange(DOWN).next_to(disc_text, DOWN)
        
        self.play(Write(solutions))
        self.wait(2)
        
        # Final Box
        final_ans = MathTex("(0,0), (0,-1), (-6,8), (-6,9)", color=BLACK).scale(1.2)
        box = SurroundingRectangle(final_ans, color=BLUE)
        final_group = VGroup(final_ans, box).move_to(ORIGIN)
        
        self.play(FadeOut(eq_text), FadeOut(disc_text), FadeOut(solutions))
        self.play(Create(final_group))
        self.wait(2)