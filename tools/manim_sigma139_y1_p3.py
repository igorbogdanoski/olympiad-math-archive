from manim import *

class SolutionScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        title = Text("Упростување на изразот", color=BLACK).to_edge(UP)
        self.add(title)
        
        sub_text = MathTex(r"x = \frac{1}{a}, \quad y = \frac{1}{b}", color=BLUE).shift(UP*2)
        self.add(sub_text)
        
        expr = MathTex(
            r"\left( \frac{x}{x-y} - \frac{y}{x+y} \right) \cdot (x-y) \cdot \frac{1}{x^2+y^2} = \frac{2}{3}",
            color=BLACK
        ).next_to(sub_text, DOWN, buff=0.5)
        self.add(expr)
        
        step1 = MathTex(
            r"\frac{x(x+y) - y(x-y)}{x^2-y^2} = \frac{x^2+y^2}{x^2-y^2}",
            color=RED
        ).next_to(expr, DOWN, buff=0.5)
        self.add(step1)
        
        step2 = MathTex(
            r"\frac{x^2+y^2}{(x-y)(x+y)} \cdot (x-y) \cdot \frac{1}{x^2+y^2} = \frac{1}{x+y}",
            color=GREEN
        ).next_to(step1, DOWN, buff=0.5)
        self.add(step2)
        
        final_eq = MathTex(r"\frac{1}{x+y} = \frac{2}{3} \implies x+y = \frac{3}{2}", color=BLACK).next_to(step2, DOWN, buff=0.5)
        self.add(final_eq)
        
        result = MathTex(r"\frac{1}{a} + \frac{1}{b} = \frac{3}{2} \implies a+b=3", color=BLUE).next_to(final_eq, DOWN, buff=0.5)
        self.add(result)
