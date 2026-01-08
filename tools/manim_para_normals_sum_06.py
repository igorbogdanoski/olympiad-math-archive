from manim import *
import numpy as np

class Problem_para_normals_sum_06(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Parameters
        a = 3.0
        b = 2.0
        angle = 60 * DEGREES
        
        # Coordinates
        # D at origin
        D = np.array([0.0, 0.0, 0.0])
        
        # Line p passes through D. Let's make it horizontal.
        # So p is x-axis.
        
        # Parallelogram ABCD.
        # D is a vertex.
        # A, B, C are above p (or mixed, but problem implies lengths, so usually one side).
        # "p has unique common point D" -> Parallelogram is on one side of p?
        # Or just touches at D.
        # Let's put A, B, C above p.
        
        # A is at angle alpha from p.
        # C is at angle beta from p.
        # B = A + C (vector sum from D).
        
        # Let A = (x_A, y_A), C = (x_C, y_C).
        # B = A + C = (x_A + x_C, y_A + y_C).
        # AM = y_A. OC = y_C. BN = y_B = y_A + y_C.
        # So AM + OC = BN holds.
        
        # Let's choose coordinates.
        A = np.array([-1.5, 2.0, 0.0])
        C = np.array([2.5, 1.0, 0.0])
        B = A + C # Vector addition since D is origin
        
        # Projections onto p (x-axis)
        M = np.array([A[0], 0.0, 0.0])
        N = np.array([B[0], 0.0, 0.0])
        O = np.array([C[0], 0.0, 0.0])
        
        # Center view
        center = (A + B + C + D) / 4
        shift = -center
        
        A += shift
        B += shift
        C += shift
        D += shift
        M += shift
        N += shift
        O += shift
        
        # Scale
        scale = 1.0
        A *= scale
        B *= scale
        C *= scale
        D *= scale
        M *= scale
        N *= scale
        O *= scale
        
        # Elements
        parallelogram = Polygon(A, B, C, D, color=BLUE, fill_opacity=0.1)
        line_p = Line(LEFT*4, RIGHT*4, color=BLACK).shift(D[1]*UP) # Line through D
        
        line_AM = DashedLine(A, M, color=RED)
        line_BN = DashedLine(B, N, color=RED)
        line_CO = DashedLine(C, O, color=RED)
        
        # Labels
        lbl_A = Text("A", font_size=24, color=BLACK).next_to(A, UP, buff=0.1)
        lbl_B = Text("B", font_size=24, color=BLACK).next_to(B, UP, buff=0.1)
        lbl_C = Text("C", font_size=24, color=BLACK).next_to(C, UP, buff=0.1)
        lbl_D = Text("D", font_size=24, color=BLACK).next_to(D, DOWN, buff=0.1)
        
        lbl_M = Text("M", font_size=24, color=BLACK).next_to(M, DOWN, buff=0.1)
        lbl_N = Text("N", font_size=24, color=BLACK).next_to(N, DOWN, buff=0.1)
        lbl_O = Text("O", font_size=24, color=BLACK).next_to(O, DOWN, buff=0.1)
        
        lbl_p = Text("p", font_size=24, color=BLACK).next_to(line_p, RIGHT, buff=0.1)
        
        # Right angles
        ra_M = RightAngle(Line(M, A), Line(M, D), length=0.2, color=RED)
        ra_N = RightAngle(Line(N, B), Line(N, D), length=0.2, color=RED)
        ra_O = RightAngle(Line(O, C), Line(O, D), length=0.2, color=RED)
        
        # Add to scene
        self.add(line_p)
        self.add(parallelogram)
        self.add(line_AM, line_BN, line_CO)
        self.add(lbl_A, lbl_B, lbl_C, lbl_D, lbl_M, lbl_N, lbl_O, lbl_p)
        self.add(ra_M, ra_N, ra_O)
        
        # Add text info
        info = VGroup(
            MathTex(r"AM \\perrp p, BN \\perp p, CO \\perp p", color=BLACK, font_size=24),
            MathTex("AM + OC = BN", color=RED, font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UL)
        self.add(info)
