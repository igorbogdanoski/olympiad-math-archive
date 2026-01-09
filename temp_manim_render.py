from manim import *
import numpy as np

class ZigZagTriangleScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        # --- CONFIGURATION (20-80-80 Triangle) ---
        L = 6.0  # base length
        angle_A = 20 * DEGREES
        # Place B and C on x-axis
        B = np.array([-L/2, 0, 0])
        C = np.array([L/2, 0, 0])
        # Height from A to BC using angle at A
        h = (L/2) / np.tan(10 * np.pi / 180)
        A = np.array([0, h, 0])
        # Draw triangle
        triangle = Polygon(A, B, C, color=BLUE, stroke_width=4)
        self.add(triangle)
        # Draw points
        self.add(Dot(A, color=BLACK), Dot(B, color=BLACK), Dot(C, color=BLACK))
        # Labels
        self.add(MathTex("A").next_to(A, UP),
                 MathTex("B").next_to(B, DOWN+LEFT),
                 MathTex("C").next_to(C, DOWN+RIGHT))
        # Draw zig-zag chain (5 equal segments)
        # Calculate points along AB and AC
        n = 5
        points_AB = [A + (B - A) * (i / n) for i in range(1, n)]
        points_AC = [A + (C - A) * (i / n) for i in range(1, n)]
        # Draw segments
        for i in range(n-1):
            self.add(Line(points_AB[i], points_AC[i], color=ORANGE, stroke_width=2))
        # Draw chain dots
        for pt in points_AB + points_AC:
            self.add(Dot(pt, color=ORANGE, radius=0.07))
        self.wait(2)
