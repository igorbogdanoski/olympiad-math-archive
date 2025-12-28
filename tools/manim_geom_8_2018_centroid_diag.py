from manim import *
import numpy as np

class CentroidDiag(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        # Parameters
        a = 6
        b = 4
        angle = 60 * DEGREES
        
        # Points
        A = ORIGIN
        B = RIGHT * a
        D = np.array([b * np.cos(angle), b * np.sin(angle), 0])
        C = B + D
        
        # Midpoints
        M = (B + C) / 2
        N = (C + D) / 2
        
        # Intersection T (Centroid of BCD)
        # T = (B + C + D) / 3
        T = (B + C + D) / 3
        
        # Create points
        pA = Dot(A, color=BLACK)
        pB = Dot(B, color=BLACK)
        pC = Dot(C, color=BLACK)
        pD = Dot(D, color=BLACK)
        pM = Dot(M, color=BLACK)
        pN = Dot(N, color=BLACK)
        pT = Dot(T, color=RED)
        
        # Shapes
        para = Polygon(A, B, C, D, color=BLUE, fill_opacity=0.1, stroke_color=BLUE)
        diag_AC = Line(A, C, color=ORANGE)
        diag_BD = DashedLine(B, D, color=GRAY)
        
        line_DM = Line(D, M, color=GREEN)
        line_BN = Line(B, N, color=GREEN)
        
        # Labels
        lbl_A = MathTex('A', color=BLACK).next_to(A, DOWN+LEFT)
        lbl_B = MathTex('B', color=BLACK).next_to(B, DOWN+RIGHT)
        lbl_C = MathTex('C', color=BLACK).next_to(C, UP+RIGHT)
        lbl_D = MathTex('D', color=BLACK).next_to(D, UP+LEFT)
        lbl_M = MathTex('M', color=BLACK).next_to(M, RIGHT)
        lbl_N = MathTex('N', color=BLACK).next_to(N, UP)
        lbl_T = MathTex('T', color=RED).next_to(T, UP, buff=0.1)
        
        # Group
        scene_objects = VGroup(
            para, diag_AC, diag_BD,
            line_DM, line_BN,
            pA, pB, pC, pD, pM, pN, pT,
            lbl_A, lbl_B, lbl_C, lbl_D, lbl_M, lbl_N, lbl_T
        )
        
        scene_objects.scale(0.8)
        scene_objects.shift(UP * 1.0)
        
        # Text
        text = VGroup(
            MathTex(r'\text{In } \triangle BCD:', color=BLACK),
            MathTex(r'M \text{ is midpoint of } BC \implies DM \text{ is median}', color=BLACK),
            MathTex(r'N \text{ is midpoint of } CD \implies BN \text{ is median}', color=BLACK),
            MathTex(r'T = DM \cap BN \text{ is centroid of } \triangle BCD', color=BLACK),
            MathTex(r'\text{Diagonals of parallelogram bisect each other at } O', color=BLACK),
            MathTex(r'CO \text{ is median of } \triangle BCD', color=BLACK),
            MathTex(r'\text{Centroid } T \text{ lies on median } CO \subset AC', color=BLACK)
        ).arrange(DOWN).next_to(scene_objects, DOWN).scale(0.6)
        
        self.add(scene_objects)
        self.add(text)
