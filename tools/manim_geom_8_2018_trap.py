from manim import *
import numpy as np

class TrapezoidMidpoints(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        # Parameters
        a = 8
        b = 4
        # MN = (a-b)/2 = 2
        # Let's choose A=60, B=30 so A+B=90
        # M at origin
        M = ORIGIN
        A = LEFT * a / 2
        B = RIGHT * a / 2
        
        # N position
        # u = 1, v = sqrt(3)
        u = 1
        v = np.sqrt(3)
        N = np.array([u, v, 0])
        
        # C and D
        C = N + RIGHT * b / 2
        D = N + LEFT * b / 2
        
        # Create points
        pA = Dot(A, color=BLACK)
        pB = Dot(B, color=BLACK)
        pC = Dot(C, color=BLACK)
        pD = Dot(D, color=BLACK)
        pM = Dot(M, color=BLACK)
        pN = Dot(N, color=BLACK)
        
        # Shapes
        trap = Polygon(A, B, C, D, color=BLUE, fill_opacity=0.1, stroke_color=BLUE)
        seg_MN = Line(M, N, color=RED)
        
        # Labels
        lbl_A = MathTex('A', color=BLACK).next_to(A, DOWN+LEFT)
        lbl_B = MathTex('B', color=BLACK).next_to(B, DOWN+RIGHT)
        lbl_C = MathTex('C', color=BLACK).next_to(C, UP+RIGHT)
        lbl_D = MathTex('D', color=BLACK).next_to(D, UP+LEFT)
        lbl_M = MathTex('M', color=BLACK).next_to(M, DOWN)
        lbl_N = MathTex('N', color=BLACK).next_to(N, UP)
        
        # Dimensions
        lbl_a = MathTex('a', color=BLACK).next_to(Line(A,B), DOWN, buff=0.3)
        lbl_b = MathTex('b', color=BLACK).next_to(Line(D,C), UP, buff=0.1)
        lbl_MN = MathTex(r'\frac{a-b}{2}', color=RED).next_to(seg_MN, RIGHT).scale(0.7)
        
        # Angles
        angle_A = Angle(Line(A,B), Line(A,D), radius=0.7, color=BLACK)
        lbl_alpha = MathTex(r'\alpha', color=BLACK).next_to(angle_A, UP+RIGHT, buff=0.1)
        
        angle_B = Angle(Line(B,C), Line(B,A), radius=0.7, color=BLACK)
        lbl_beta = MathTex(r'\beta', color=BLACK).next_to(angle_B, UP+LEFT, buff=0.1)
        
        # Construction: Translate AD to CE
        E = A + RIGHT * b
        pE = Dot(E, color=GREEN)
        line_CE = DashedLine(C, E, color=GREEN)
        lbl_E = MathTex('E', color=BLACK).next_to(E, DOWN)
        
        # Triangle CEB median
        line_CK = DashedLine(C, np.array([b/2, 0, 0]), color=RED)
        lbl_K = MathTex('K', color=BLACK).next_to(np.array([b/2, 0, 0]), DOWN)
        
        # Group
        scene_objects = VGroup(
            trap, seg_MN,
            pA, pB, pC, pD, pM, pN,
            lbl_A, lbl_B, lbl_C, lbl_D, lbl_M, lbl_N,
            lbl_a, lbl_b, lbl_MN,
            angle_A, lbl_alpha, angle_B, lbl_beta,
            pE, line_CE, lbl_E,
            line_CK, lbl_K
        )
        
        scene_objects.scale(0.7)
        scene_objects.shift(UP * 1.5)
        
        # Text
        text = VGroup(
            MathTex(r'\text{Construct } CE \parallel AD, E \in AB', color=BLACK),
            MathTex(r'AE = CD = b \implies EB = a - b', color=BLACK),
            MathTex(r'\text{Consider } \triangle CEB. \text{ Let } K \text{ be midpoint of } EB.', color=BLACK),
            MathTex(r'CK \text{ is median. } CK = MN = \frac{a-b}{2}', color=BLACK),
            MathTex(r'CK = \frac{1}{2} EB \implies \triangle CEB \text{ is right-angled at } C', color=BLACK),
            MathTex(r'\angle CEB = \angle A \text{ (corresponding)}', color=BLACK),
            MathTex(r'\angle A + \angle B = 90^\circ', color=BLACK)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(scene_objects, DOWN).scale(0.6)
        
        self.add(scene_objects)
        self.add(text)
