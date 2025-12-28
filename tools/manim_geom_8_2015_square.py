from manim import *
import numpy as np

class GeometryScene(Scene):
    def construct(self):
        # Define points
        # Square ABCD.
        s = 4.0
        A = np.array([-s/2, -s/2, 0])
        B = np.array([s/2, -s/2, 0])
        C = np.array([s/2, s/2, 0])
        D = np.array([-s/2, s/2, 0])
        
        # Diagonals
        diagonal_AC = Line(A, C, color=GRAY)
        diagonal_BD = Line(B, D, color=GRAY)
        
        # Intersection O
        O = np.array([0, 0, 0])
        
        # M midpoint of CD
        M = (C + D) / 2
        
        # N midpoint of BC
        N = (B + C) / 2
        
        # Segments AM, AN
        segment_AM = Line(A, M, color=YELLOW)
        segment_AN = Line(A, N, color=YELLOW)
        
        # Create objects
        square = Polygon(A, B, C, D, color=BLUE, stroke_width=4)
        
        # Labels
        label_A = MathTex("A").next_to(A, DL)
        label_B = MathTex("B").next_to(B, DR)
        label_C = MathTex("C").next_to(C, UR)
        label_D = MathTex("D").next_to(D, UL)
        label_O = MathTex("O").next_to(O, UP, buff=0.1)
        label_M = MathTex("M").next_to(M, UP)
        label_N = MathTex("N").next_to(N, RIGHT)
        
        # Group
        scene_group = VGroup(square, diagonal_AC, diagonal_BD, segment_AM, segment_AN, label_A, label_B, label_C, label_D, label_O, label_M, label_N)
        scene_group.move_to(ORIGIN)
        
        # Animations
        self.play(Create(square), run_time=2)
        self.play(Create(diagonal_AC), Create(diagonal_BD))
        self.play(Write(label_A), Write(label_B), Write(label_C), Write(label_D), Write(label_O))
        self.play(Create(segment_AM), Create(segment_AN))
        self.play(Write(label_M), Write(label_N))
        
        self.wait(2)
