from manim import *
import numpy as np

class Problem_geom_8_2015_square(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Parameters
        a = 4.0
        
        # Coordinates
        # A top-left, B top-right, C bottom-right, D bottom-left
        A = np.array([-a/2, a/2, 0.0])
        B = np.array([a/2, a/2, 0.0])
        C = np.array([a/2, -a/2, 0.0])
        D = np.array([-a/2, -a/2, 0.0])
        
        # Midpoints
        M = (C + D) / 2 # Midpoint of CD
        N = (B + C) / 2 # Midpoint of BC
        
        # Intersections
        # P is intersection of AM and BD
        # Q is intersection of AN and BD
        # From analysis: P is 1/3 from D, Q is 2/3 from D (or 1/3 from B)
        P = D + (B - D) / 3
        Q = D + 2 * (B - D) / 3
        
        # Elements
        square = Polygon(A, B, C, D, color=BLUE, fill_opacity=0.1)
        diag_BD = Line(B, D, color=BLACK)
        line_AM = Line(A, M, color=RED)
        line_AN = Line(A, N, color=RED)
        
        # Labels
        lbl_A = Text("A", font_size=24, color=BLACK).next_to(A, UL, buff=0.1)
        lbl_B = Text("B", font_size=24, color=BLACK).next_to(B, UR, buff=0.1)
        lbl_C = Text("C", font_size=24, color=BLACK).next_to(C, DR, buff=0.1)
        lbl_D = Text("D", font_size=24, color=BLACK).next_to(D, DL, buff=0.1)
        lbl_M = Text("M", font_size=24, color=BLACK).next_to(M, DOWN, buff=0.1)
        lbl_N = Text("N", font_size=24, color=BLACK).next_to(N, RIGHT, buff=0.1)
        
        # Mark equal segments on BD
        # DP, PQ, QB
        tick_DP = Line(D, P).get_center()
        tick_PQ = Line(P, Q).get_center()
        tick_QB = Line(Q, B).get_center()
        
        t_DP = Text("|", font_size=16, color=BLACK).move_to(tick_DP).rotate(45*DEGREES).shift(UP*0.1)
        t_PQ = Text("|", font_size=16, color=BLACK).move_to(tick_PQ).rotate(45*DEGREES).shift(UP*0.1)
        t_QB = Text("|", font_size=16, color=BLACK).move_to(tick_QB).rotate(45*DEGREES).shift(UP*0.1)
        
        # Add to scene
        self.add(square)
        self.add(diag_BD)
        self.add(line_AM, line_AN)
        self.add(lbl_A, lbl_B, lbl_C, lbl_D, lbl_M, lbl_N)
        self.add(t_DP, t_PQ, t_QB)
        
        # Add text info
        info = VGroup(
            MathTex("M \\in CD, CM=MD", color=BLACK, font_size=24),
            MathTex("N \\in BC, BN=NC", color=BLACK, font_size=24),
            MathTex("DP = PQ = QB", color=RED, font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UL)
        self.add(info)
