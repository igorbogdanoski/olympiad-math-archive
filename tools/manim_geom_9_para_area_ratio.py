from manim import *

class Problem_geom_9_para_area_ratio(Scene):
    def construct(self):
        # Scale
        scale = 1.5
        
        # Coordinates
        # A at origin
        A = ORIGIN
        # B at (4, 0)
        B = RIGHT * 4
        # D at (1, 2)
        D = np.array([1.0, 2.0, 0.0])
        # C at B + D
        C = B + D
        
        # Shift to center
        center = (A + C) / 2
        shift = -center
        A += shift
        B += shift
        C += shift
        D += shift
        
        # Scale
        A *= scale
        B *= scale
        C *= scale
        D *= scale
        
        # Parallelogram
        parallelogram = Polygon(A, B, C, D, color=BLUE)
        
        # Diagonal BD
        diag_BD = Line(B, D, color=GRAY)
        
        # Point M on BD such that MD = 3BM => BM = 1/4 BD
        M = B + 0.25 * (D - B)
        
        # Line AM extended to intersect BC at N
        # We found N is on BC such that BN = 1/3 BC
        N = B + (1/3) * (C - B)
        
        line_AN = Line(A, N, color=YELLOW)
        
        # Triangle MND
        tri_MND = Polygon(M, N, D, color=RED, fill_opacity=0.3)
        
        # Points
        dot_A = Dot(A, color=WHITE)
        dot_B = Dot(B, color=WHITE)
        dot_C = Dot(C, color=WHITE)
        dot_D = Dot(D, color=WHITE)
        dot_M = Dot(M, color=RED)
        dot_N = Dot(N, color=RED)
        
        # Labels
        label_A = MathTex("A").next_to(dot_A, DL)
        label_B = MathTex("B").next_to(dot_B, DR)
        label_C = MathTex("C").next_to(dot_C, UR)
        label_D = MathTex("D").next_to(dot_D, UL)
        label_M = MathTex("M").next_to(dot_M, UP)
        label_N = MathTex("N").next_to(dot_N, RIGHT)
        
        # Ratio text
        text_ratio = MathTex("MD = 3 BM").to_corner(UL)
        text_area = MathTex(r"\frac{Area(MND)}{Area(ABCD)} = \frac{1}{8}").next_to(text_ratio, DOWN).set_color(YELLOW)
        
        self.add(parallelogram, diag_BD)
        self.add(line_AN)
        self.add(tri_MND)
        self.add(dot_A, dot_B, dot_C, dot_D, dot_M, dot_N)
        self.add(label_A, label_B, label_C, label_D, label_M, label_N)
        self.add(text_ratio, text_area)
