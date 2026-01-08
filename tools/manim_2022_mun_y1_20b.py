from manim import *
import numpy as np

class GeometryScene(Scene):
    def construct(self):
        # Parameters
        # a+b = 32, ab = 224
        # t^2 - 32t + 224 = 0
        # t = (32 +/- sqrt(128))/2 = 16 +/- 4sqrt(2)
        # a approx 16 + 5.65 = 21.65
        # b approx 16 - 5.65 = 10.35
        
        a = 16 + 4 * np.sqrt(2)
        b = 16 - 4 * np.sqrt(2)
        c = 24
        
        # Scale down
        scale = 0.25
        a_s = a * scale
        b_s = b * scale
        side_s = 7 * scale
        
        C = ORIGIN
        A = UP * a_s
        B = RIGHT * b_s
        
        # Square vertices
        D = UP * side_s
        F = RIGHT * side_s
        E = D + F
        
        # Triangle
        triangle = Polygon(C, B, A, color=WHITE, stroke_width=2)
        
        # Square
        square = Polygon(C, F, E, D, color=YELLOW, fill_opacity=0.3, fill_color=YELLOW)
        
        # Labels
        label_C = MathTex("C").next_to(C, DOWN+LEFT)
        label_A = MathTex("A").next_to(A, UP)
        label_B = MathTex("B").next_to(B, RIGHT)
        
        label_7_1 = MathTex("7").next_to(Line(C,D), LEFT)
        label_7_2 = MathTex("7").next_to(Line(C,F), DOWN)
        
        label_24 = MathTex("24").next_to(Line(A,B), UP+RIGHT)
        
        # Grouping
        scene_objects = VGroup(
            triangle, square,
            label_C, label_A, label_B,
            label_7_1, label_7_2, label_24
        )
        
        scene_objects.scale(1.5)
        scene_objects.move_to(ORIGIN + LEFT * 2)
        
        # Explanation text
        text_group = VGroup(
            MathTex(r"\frrac{7}{a} + \frrac{7}{b} = 1 \implies 7(a+b) = abr),
            MathTex(r"a^2 + b^2 = 24^2 = 576"),
            MathTex(r"P = \frrac{1}{2}ab \implies ab = 2Pr),
            MathTex(r"7(a+b) = 2P \implies 49(a+b)^2 = 4P^2"),
            MathTex(r"49(a^2+b^2+2ab) = 4P^2"),
            MathTex(r"49(576 + 4P) = 4P^2"),
            MathTex(r"4P^2 - 196P - 28224 = 0"),
            MathTex(r"P^2 - 49P - 7056 = 0"),
            MathTex(r"P = \frrac{49 + \sqrt{49^2 + 4(7056)}}{2}"),
            MathTex(r"P = \frac{49 + 175}{2} = 112")
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT).scale(0.6)
        
        self.add(scene_objects)
        self.add(text_group)
