from manim import *
import numpy as np

class sigma137_p1867(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # Coordinates
        # H is origin (0,0)
        H = ORIGIN
        # C is (0, 3)
        C = UP * 3
        # A is (-2, 0)
        A = LEFT * 2
        # B is (4.5, 0)
        B = RIGHT * 4.5
        
        # E is on CH. Let's pick midpoint 
        E = UP * 1.5
        
        # E_prime (symmetric to E wrt AB)
        E_prime = DOWN * 1.5
        
        # Calculate D based on angle condition angle(CAD) = angle(BAE)
        # See thought process for derivation: D = (2.25, 1.5)
        D = np.array([2.25, 1.5, 0])
        
        # Calculate F based on collinearity D-F-E'
        # See thought process: F = (1.125, 0)
        F = np.array([1.125, 0, 0])
        
        # Mobjects
        triangle = Polygon(A, B, C, color=BLACK, stroke_width=4)
        altitude = Line(C, H, color=BLACK, stroke_width=2)
        
        # Points
        pts = VGroup(Dot(A), Dot(B), Dot(C), Dot(H), Dot(E), Dot(F), Dot(D), Dot(E_prime))
        
        # Segments for the problem
        seg_AE = Line(A, E, color=BLUE)
        seg_EF = Line(E, F, color=BLUE)
        seg_FD = Line(F, D, color=BLUE)
        
        # Additional construction lines
        seg_AE_prime = DashedLine(A, E_prime, color=RED)
        seg_E_prime_F = DashedLine(E_prime, F, color=RED)
        seg_DE_prime = DashedLine(D, E_prime, color=RED)
        line_AD = DashedLine(A, D, color=GRAY)
        
        # Labels
        lbl_A = MathTex("A").next_to(A, DL)
        lbl_B = MathTex("B").next_to(B, DR)
        lbl_C = MathTex("C").next_to(C, UP)
        lbl_H = MathTex("H").next_to(H, DL, buff=0.1)
        lbl_E = MathTex("E").next_to(E, LEFT, buff=0.1)
        lbl_F = MathTex("F").next_to(F, DOWN)
        lbl_D = MathTex("D").next_to(D, UR, buff=0.1)
        lbl_Ep = MathTex("E'").next_to(E_prime, DOWN)
        
        self.add(triangle, altitude)
        self.add(seg_AE, seg_EF, seg_FD, seg_AE_prime, seg_E_prime_F, seg_DE_prime, line_AD)
        self.add(pts)
        self.add(lbl_A, lbl_B, lbl_C, lbl_H, lbl_E, lbl_F, lbl_D, lbl_Ep)
        
        # Marks
        # Right angle at H
        self.add(RightAngle(Line(C, H), Line(H, B), length=0.3))
        
        # Target angle AEF - should look like 90 degrees
        self.add(RightAngle(Line(E, A), Line(E, F), length=0.3, color=RED))
