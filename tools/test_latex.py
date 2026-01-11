from manim import *

class TestLaTeX(Scene):
    def construct(self):
        # Simple test with basic math
        eq = MathTex(r"x^2 + y^2 = z^2")
        self.play(Write(eq))
        self.wait(1)

        # Test with complex numbers (like in our problem)
        eq2 = MathTex(r"\left| z^3 + \frac{1}{z^3} \right| \leq 2")
        self.play(Transform(eq, eq2))
        self.wait(1)