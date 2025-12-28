from manim import *
import numpy as np

class SquareDiagonalTrisection(Scene):
    def construct(self):
        # Parameters
        side = 6
        
        # Coordinates
        # A bottom-left
        A = ORIGIN
        B = RIGHT * side
        C = RIGHT * side + UP * side
        D = UP * side
        
        # Midpoints
        M = (C + D) / 2 # Midpoint of CD
        N = (B + C) / 2 # Midpoint of BC
        
        # Intersections
        # P = AM intersect BD
        # Line AM: y = (side/ (side/2)) * x? No.
        # A=(0,0). M=(side/2, side).
        # Line AM: y = 2x.
        # Line BD: y = -x + side.
        # 2x = -x + side => 3x = side => x = side/3.
        # y = 2*side/3.
        P = np.array([side/3, 2*side/3, 0])
        
        # Q = AN intersect BD
        # A=(0,0). N=(side, side/2).
        # Line AN: y = 0.5x.
        # Line BD: y = -x + side.
        # 0.5x = -x + side => 1.5x = side => x = side / 1.5 = 2*side/3.
        # y = side/3.
        Q = np.array([2*side/3, side/3, 0])
        
        # Create points
        pA = Dot(A)
        pB = Dot(B)
        pC = Dot(C)
        pD = Dot(D)
        pM = Dot(M)
        pN = Dot(N)
        pP = Dot(P, color=RED)
        pQ = Dot(Q, color=RED)
        
        # Shapes
        square = Polygon(A, B, C, D, color=BLUE, fill_opacity=0.1)
        diag_BD = Line(B, D, color=YELLOW)
        line_AM = Line(A, M, color=GREEN)
        line_AN = Line(A, N, color=GREEN)
        
        # Labels
        lbl_A = MathTex("A").next_to(A, DOWN+LEFT)
        lbl_B = MathTex("B").next_to(B, DOWN+RIGHT)
        lbl_C = MathTex("C").next_to(C, UP+RIGHT)
        lbl_D = MathTex("D").next_to(D, UP+LEFT)
        lbl_M = MathTex("M").next_to(M, UP)
        lbl_N = MathTex("N").next_to(N, RIGHT)
        lbl_P = MathTex("P").next_to(P, UP+LEFT, buff=0.1)
        lbl_Q = MathTex("Q").next_to(Q, DOWN+RIGHT, buff=0.1)
        
        # Segments on diagonal
        seg_DP = Line(D, P, color=RED, stroke_width=4)
        seg_PQ = Line(P, Q, color=ORANGE, stroke_width=4)
        seg_QB = Line(Q, B, color=RED, stroke_width=4)
        
        # Braces
        brace_DP = Brace(seg_DP, direction=np.array([-1, 1, 0]))
        brace_PQ = Brace(seg_PQ, direction=np.array([-1, 1, 0]))
        brace_QB = Brace(seg_QB, direction=np.array([-1, 1, 0]))
        
        # Group
        scene_objects = VGroup(
            square, diag_BD, line_AM, line_AN,
            pA, pB, pC, pD, pM, pN, pP, pQ,
            lbl_A, lbl_B, lbl_C, lbl_D, lbl_M, lbl_N, lbl_P, lbl_Q,
            seg_DP, seg_PQ, seg_QB
        )
        
        scene_objects.scale(0.7)
        scene_objects.shift(LEFT * 2.5)
        
        # Text
        text = VGroup(
            MathTex(r"\text{Let } P = AM \cap BD, Q = AN \cap BD"),
            MathTex(r"\triangle ABQ \sim \triangle NDQ \text{ (Wait, } Q \text{ is closer to B)}"),
            MathTex(r"\text{Actually: } \triangle ADQ \sim \triangle NBQ"),
            MathTex(r"\frac{DQ}{BQ} = \frac{AD}{BN} = \frac{a}{a/2} = 2 \implies DQ = \frac{2}{3}BD, BQ = \frac{1}{3}BD"),
            MathTex(r"\triangle ABP \sim \triangle MDP"),
            MathTex(r"\frac{BP}{DP} = \frac{AB}{DM} = \frac{a}{a/2} = 2 \implies BP = \frac{2}{3}BD, DP = \frac{1}{3}BD"),
            MathTex(r"PQ = BD - DP - BQ"),
            MathTex(r"PQ = BD - \frac{1}{3}BD - \frac{1}{3}BD = \frac{1}{3}BD"),
            MathTex(r"\implies DP = PQ = QB")
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT).scale(0.6)
        
        self.add(scene_objects)
        self.add(text)
