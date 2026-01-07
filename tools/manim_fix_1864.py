from manim import *
import numpy as np

class sigma137_p1864(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # Triangle vertices - Make it Scalene (Acute)
        # Old: A(0,3), B(-3,-2), C(3,-2) (Isosceles)
        # New: Shift A and C to make it scalene
        A = UP * 2.5 + LEFT * 0.5  # (-0.5, 2.5)
        B = LEFT * 3.5 + DOWN * 2  # (-3.5, -2)
        C = RIGHT * 3 + DOWN * 2    # (3, -2)
        
        # Point P inside
        # Avoid symmetry axis. Centroid is roughly (-0.3, -0.5).
        # Let's place P somewhere clearly distinct.
        # Maybe slightly to the right and up.
        P = RIGHT * 1.0 + DOWN * 0.5
        
        # Projections
        # Function to find projection of P onto line XY
        def get_projection(P, X, Y):
            XY = Y - X
            XP = P - X
            t = np.dot(XP, XY) / np.dot(XY, XY)
            return X + t * XY
            
        A1 = get_projection(P, B, C)
        B1 = get_projection(P, C, A)
        C1 = get_projection(P, A, B)
        
        # Mobjects
        triangle = Polygon(A, B, C, color=BLACK, stroke_width=4)
        
        # Perpendiculars from P
        line_PA1 = DashedLine(P, A1, color=BLUE)
        line_PB1 = DashedLine(P, B1, color=BLUE)
        line_PC1 = DashedLine(P, C1, color=BLUE)
        
        # Segments PA, PB, PC
        seg_PA = Line(P, A, color=RED, stroke_width=3)
        seg_PB = Line(P, B, color=RED, stroke_width=3)
        seg_PC = Line(P, C, color=RED, stroke_width=3)
        
        # Labels
        lbl_A = MathTex("A").next_to(A, UP)
        lbl_B = MathTex("B").next_to(B, DL)
        lbl_C = MathTex("C").next_to(C, DR)
        lbl_P = MathTex("P").next_to(P, UL, buff=0.1)
        lbl_A1 = MathTex("A_1").next_to(A1, DOWN)
        
        lbl_B1 = MathTex("B_1").next_to(B1, UR, buff=0.1)
        lbl_C1 = MathTex("C_1").next_to(C1, UL, buff=0.1)
        
        # Right angle markers
        ra_A1 = RightAngle(Line(P, A1), Line(B, C), length=0.3)
        ra_B1 = RightAngle(Line(P, B1), Line(C, A), length=0.3)
        ra_C1 = RightAngle(Line(P, C1), Line(A, B), length=0.3)

        self.add(triangle)
        self.add(line_PA1, line_PB1, line_PC1)
        self.add(seg_PA, seg_PB, seg_PC)
        self.add(lbl_A, lbl_B, lbl_C, lbl_P, lbl_A1, lbl_B1, lbl_C1)
        self.add(ra_A1, ra_B1, ra_C1)
