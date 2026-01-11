from manim import *

class SolutionScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Define points
        O = LEFT * 1.5
        R = 2.5
        O1 = O + RIGHT * R # O1 is on k1
        
        # Circles
        k1 = Circle(radius=R, color=BLUE).move_to(O)
        r = 2.0
        k2 = Circle(radius=r, color=GREEN).move_to(O1)
        
        # Point A on k2
        angle_A = 120 * DEGREES
        A = O1 + np.array([r*np.cos(angle_A), r*np.sin(angle_A), 0])
        
        # Point M (midpoint of AO1)
        M = (A + O1) / 2
        
        # Line MO vector
        vec_MO = O - M
        angle_MO = np.arctan2(vec_MO[1], vec_MO[0])
        
        # Chord AB parallel to MO
        # Normal to MO
        normal_angle = angle_MO + PI/2
        # Distance from O1 to chord AB?
        # We need to find B such that AB || MO.
        # Let's just draw a line through A parallel to MO and find intersection B
        # Line: P = A + t * vec_MO
        # Intersect with circle |P - O1|^2 = r^2
        # Let P - O1 = (A - O1) + t * vec_MO
        # Let U = A - O1, V = vec_MO
        # |U + tV|^2 = r^2 => |U|^2 + 2t(U.V) + t^2|V|^2 = r^2
        # r^2 + 2t(U.V) + t^2|V|^2 = r^2
        # 2t(U.V) + t^2|V|^2 = 0
        # t(2(U.V) + t|V|^2) = 0
        # t = 0 (Point A) or t = -2(U.V) / |V|^2 (Point B)
        
        U = A - O1
        V = vec_MO
        t_B = -2 * np.dot(U, V) / np.dot(V, V)
        B = A + t_B * V
        
        # Midpoint S
        S = (A + B) / 2
        
        # Dots
        dot_O = Dot(O, color=BLACK, radius=0.08)
        dot_O1 = Dot(O1, color=BLACK, radius=0.08)
        dot_A = Dot(A, color=BLACK, radius=0.08)
        dot_B = Dot(B, color=BLACK, radius=0.08)
        dot_M = Dot(M, color=BLACK, radius=0.08)
        dot_S = Dot(S, color=BLACK, radius=0.08)
        
        # Labels
        lbl_O = MathTex("O", color=BLACK).next_to(O, LEFT, buff=0.15)
        lbl_O1 = MathTex("O_1", color=BLACK).next_to(O1, UP, buff=0.15)
        lbl_A = MathTex("A", color=BLACK).next_to(A, UP, buff=0.15)
        lbl_B = MathTex("B", color=BLACK).next_to(B, DOWN, buff=0.15)
        lbl_M = MathTex("M", color=BLACK).next_to(M, LEFT, buff=0.15)
        lbl_S = MathTex("S", color=BLACK).next_to(S, RIGHT, buff=0.15)
        
        # Lines
        line_AO1 = Line(A, O1, color=GRAY, stroke_width=2)
        line_MO = Line(M, O, color=RED, stroke_width=3)
        line_AB = Line(A, B, color=RED, stroke_width=3)
        line_O1S = Line(O1, S, color=GRAY, stroke_width=2, stroke_opacity=0.6)
        line_OS = Line(O, S, color=BLUE, stroke_width=4)
        
        # Add elements to scene
        self.add(k1, k2)
        self.add(dot_O, dot_O1, dot_A, dot_B, dot_M, dot_S)
        self.add(lbl_O, lbl_O1, lbl_A, lbl_B, lbl_M, lbl_S)
        self.add(line_AO1, line_MO, line_AB, line_O1S, line_OS)
