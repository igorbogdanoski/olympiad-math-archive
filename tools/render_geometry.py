from manim import *
import numpy as np

class Task_geo_three_circles_tangent(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        # --- AI GENERATED CODE START ---
        # 1. Setup parameters
        R = 3.0
        r = 2.0
        # Calculate x using the formula: 1/sqrt(x) = 1/sqrt(R) + 1/sqrt(r)
        sqrt_x_inv = 1/np.sqrt(R) + 1/np.sqrt(r)
        x = 1 / (sqrt_x_inv ** 2)
        
        # 2. Coordinates
        # Line at y=0
        # Circle 1 at (0, R)
        O1 = [-2, R - 2, 0] # Shifted down/left for centering
        # Circle 2 distance: 2*sqrt(Rr)
        dist_12 = 2 * np.sqrt(R * r)
        O2 = [O1[0] + dist_12, r - 2, 0]
        
        # Circle 3 distance from C1: 2*sqrt(Rx)
        dist_13 = 2 * np.sqrt(R * x)
        O3 = [O1[0] + dist_13, x - 2, 0]

        # 3. Objects
        line = Line(LEFT*4, RIGHT*4, color=BLACK).shift(DOWN*2)
        c1 = Circle(radius=R, color=BLUE).move_to(O1)
        c2 = Circle(radius=r, color=GREEN).move_to(O2)
        c3 = Circle(radius=x, color=RED).move_to(O3)
        
        # Radii lines
        l1 = Line(O1, O1 + DOWN*R, color=BLACK)
        l2 = Line(O2, O2 + DOWN*r, color=BLACK)
        l3 = Line(O3, O3 + DOWN*x, color=BLACK)

        # 4. Labels
        labels = VGroup(
            MathTex('R').next_to(l1, LEFT, buff=0.1),
            MathTex('r').next_to(l2, RIGHT, buff=0.1),
            MathTex('x', color=RED).next_to(c3, UP, buff=0.1)
        ).set_color(BLACK)

        self.add(line, c1, c2, c3, l1, l2, l3, labels)
        # --- AI GENERATED CODE END ---
