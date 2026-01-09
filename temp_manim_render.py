from manim import *
import numpy as np

class Mat3762Scene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        # Right triangle ABC: A at origin, B at (4,0), C at (0,3)
        A = np.array([0, 0, 0])
        B = np.array([4, 0, 0])
        C = np.array([0, 3, 0])
        # Lengths
        AB = np.linalg.norm(B - A)
        AC = np.linalg.norm(C - A)
        BC = np.linalg.norm(C - B)
        # Direction BC
        dir_BC = (C - B) / np.linalg.norm(C - B)
        # Find E: BE = AB
        E = B + dir_BC * AB
        # Find D: CD = AC
        D = C - dir_BC * AC
        # Draw triangle
        triangle = Polygon(A, B, C, color=BLUE, stroke_width=4)
        self.add(triangle)
        # Draw points
        self.add(Dot(A, color=BLACK), Dot(B, color=BLACK), Dot(C, color=BLACK), Dot(D, color=RED), Dot(E, color=RED))
        # Labels
        self.add(MathTex("A").next_to(A, DOWN+LEFT),
                 MathTex("B").next_to(B, DOWN+RIGHT),
                 MathTex("C").next_to(C, UP+LEFT),
                 MathTex("D", color=RED).next_to(D, UP),
                 MathTex("E", color=RED).next_to(E, DOWN))
        # Draw segments
        self.add(Line(B, E, color=ORANGE, stroke_width=2, stroke_opacity=0.7))
        self.add(Line(C, D, color=ORANGE, stroke_width=2, stroke_opacity=0.7))
        # Highlight angle DAE
        angle = Angle(Line(A, D), Line(A, E), radius=0.6, color=GREEN)
        self.add(angle)
        angle_label = MathTex("45^\circ", color=GREEN).move_to(A + np.array([0.5, 0.3, 0]))
        self.add(angle_label)
        self.wait(2)