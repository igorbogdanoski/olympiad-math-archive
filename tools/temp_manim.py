from manim import *

class QuadraticIntegerSolution(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Title
        title = Text("Целобројни решенија", color=BLACK).scale(0.8).to_edge(UP)
        self.play(Write(title))
        
        # Step 1: The Equation
        eq_original = MathTex("x^2 + ax + b = 0", color=BLACK).shift(UP * 2)
        condition = MathTex("x = a + b", color=BLUE).next_to(eq_original, DOWN)
        
        self.play(Write(eq_original))
        self.play(Write(condition))
        self.wait(1)
        
        # Step 2: Substitution
        substitution = MathTex("(a+b)^2 + a(a+b) + b = 0", color=BLACK).shift(UP * 0.5)
        self.play(ReplacementTransform(Group(eq_original, condition), substitution))
        self.wait(1)
        
        # Step 3: Rearrange to Quadratic in b
        quadratic_b = MathTex("b^2 + (3a+1)b + 2a^2 = 0", color=BLACK).shift(DOWN * 0.5)
        self.play(Transform(substitution, quadratic_b))
        self.wait(1)
        
        # Step 4: Discriminant Condition
        discriminant_text = Text("Дискриминантата мора да е квадрат:", color=RED, font_size=24).next_to(quadratic_b, DOWN, buff=0.5)
        disc_eq = MathTex("D = (3a+1)^2 - 8a^2 = k^2", color=BLACK).next_to(discriminant_text, DOWN)
        disc_simp = MathTex("(a+3)^2 - k^2 = 8", color=BLACK).next_to(discriminant_text, DOWN)
        
        self.play(Write(discriminant_text))
        self.play(Write(disc_eq))
        self.wait(1)
        self.play(Transform(disc_eq, disc_simp))
        self.wait(1)
        
        # Step 5: Solutions
        solutions_text = Text("Решенија (a, b):", color=BLACK, font_size=28).to_edge(LEFT).shift(DOWN*2)
        sol1 = MathTex("(0, 0), (0, -1)", color=BLUE).next_to(solutions_text, RIGHT)
        sol2 = MathTex("(-6, 8), (-6, 9)", color=BLUE).next_to(sol1, RIGHT, buff=0.5)
        
        self.play(Write(solutions_text))
        self.play(Write(sol1), Write(sol2))
        
        self.wait(3)