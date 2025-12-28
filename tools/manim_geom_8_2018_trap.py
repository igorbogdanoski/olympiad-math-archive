from manim import *
import numpy as np

class GeometryScene(Scene):
    def construct(self):
        # Define points
        # M at origin (0,0)
        M = np.array([0, 0, 0])
        
        # a = 6, b = 2.
        # P = (-2, 0), Q = (2, 0)
        # N = (0, 2)
        P = np.array([-2, 0, 0])
        Q = np.array([2, 0, 0])
        N = np.array([0, 2, 0])
        
        # A = (-3, 0), B = (3, 0)
        A = np.array([-3, 0, 0])
        B = np.array([3, 0, 0])
        
        # D = (-1, 2), C = (1, 2)
        D = np.array([-1, 2, 0])
        C = np.array([1, 2, 0])
        
        # Create objects
        trapezoid = Polygon(A, B, C, D, color=BLUE, stroke_width=4)
        segment_MN = Line(M, N, color=RED)
        
        # Auxiliary lines
        line_NP = DashedLine(N, P, color=YELLOW)
        line_NQ = DashedLine(N, Q, color=YELLOW)
        
        # Labels
        label_A = MathTex("A").next_to(A, DL)
        label_B = MathTex("B").next_to(B, DR)
        label_C = MathTex("C").next_to(C, UR)
        label_D = MathTex("D").next_to(D, UL)
        label_M = MathTex("M").next_to(M, DOWN)
        label_N = MathTex("N").next_to(N, UP)
        label_P = MathTex("P").next_to(P, DOWN)
        label_Q = MathTex("Q").next_to(Q, DOWN)
        
        # Right angle at N in triangle NPQ
        right_angle = RightAngle(Line(N, P), Line(N, Q), length=0.4)
        
        # Group
        scene_group = VGroup(trapezoid, segment_MN, line_NP, line_NQ, label_A, label_B, label_C, label_D, label_M, label_N, label_P, label_Q, right_angle)
        scene_group.move_to(ORIGIN)
        
        # Animations
        self.play(Create(trapezoid), run_time=2)
        self.play(Write(label_A), Write(label_B), Write(label_C), Write(label_D))
        self.play(Create(segment_MN), Write(label_M), Write(label_N))
        self.play(Create(line_NP), Create(line_NQ))
        self.play(Write(label_P), Write(label_Q))
        self.play(FadeIn(right_angle))
        
        self.wait(2)
