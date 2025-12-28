from manim import *
import numpy as np

class GeometryScene(Scene):
    def construct(self):
        # Define line p as x-axis (y=-2)
        p_y = -2
        line_p = Line(LEFT * 6 + UP * p_y, RIGHT * 6 + UP * p_y, color=WHITE)
        label_p = MathTex("p").next_to(line_p, RIGHT)
        
        # Define D on p
        D = np.array([-2, p_y, 0])
        
        # Define A, B, C
        # A = D + v1
        # C = D + v2
        # B = D + v1 + v2
        
        v1 = np.array([1, 2, 0])
        v2 = np.array([4, 1, 0])
        
        A = D + v1
        C = D + v2
        B = D + v1 + v2
        
        # Parallelogram
        parallelogram = Polygon(A, B, C, D, color=BLUE, stroke_width=4)
        
        # Perpendiculars
        # M is proj of A on p
        M = np.array([A[0], p_y, 0])
        # N is proj of B on p
        N = np.array([B[0], p_y, 0])
        # O is proj of C on p
        O = np.array([C[0], p_y, 0])
        
        line_AM = DashedLine(A, M, color=RED)
        line_BN = DashedLine(B, N, color=RED)
        line_CO = DashedLine(C, O, color=RED)
        
        label_AM = MathTex("AM").next_to(line_AM, LEFT, buff=0.05).scale(0.7)
        label_BN = MathTex("BN").next_to(line_BN, RIGHT, buff=0.05).scale(0.7)
        label_CO = MathTex("OC").next_to(line_CO, RIGHT, buff=0.05).scale(0.7)
        
        # Labels
        label_A = MathTex("A").next_to(A, UP)
        label_B = MathTex("B").next_to(B, UP)
        label_C = MathTex("C").next_to(C, UP)
        label_D = MathTex("D").next_to(D, DOWN)
        label_M = MathTex("M").next_to(M, DOWN)
        label_N = MathTex("N").next_to(N, DOWN)
        label_O = MathTex("O").next_to(O, DOWN)
        
        # Diagonals (optional, for proof hint)
        diag_AC = DashedLine(A, C, color=GRAY)
        diag_BD = DashedLine(B, D, color=GRAY)
        
        # Equation
        equation = MathTex("AM + OC = BN").to_corner(UL)
        
        # Group
        scene_group = VGroup(line_p, parallelogram, line_AM, line_BN, line_CO, label_A, label_B, label_C, label_D, label_M, label_N, label_O, label_AM, label_BN, label_CO, equation)
        scene_group.move_to(ORIGIN)
        
        # Animations
        self.play(Create(line_p), Write(label_p))
        self.play(Create(parallelogram), Write(label_D))
        self.play(Write(label_A), Write(label_B), Write(label_C))
        
        self.play(Create(line_AM), Write(label_M), Write(label_AM))
        self.play(Create(line_CO), Write(label_O), Write(label_CO))
        self.play(Create(line_BN), Write(label_N), Write(label_BN))
        
        self.play(Create(diag_AC), Create(diag_BD))
        
        self.play(Write(equation))
        
        self.wait(2)
