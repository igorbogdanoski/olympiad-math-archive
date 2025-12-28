from manim import *
import numpy as np

class GeometryScene(Scene):
    def construct(self):
        # Define points
        # a=4, b=6, c=2.4
        # A at origin
        A = np.array([0.0, 0.0, 0.0])
        
        # B at (c, 0)
        c_len = 2.4
        B = np.array([c_len, 0.0, 0.0])
        
        # C coordinates
        b_len = 6.0
        a_len = 4.0
        cos_A = (b_len**2 + c_len**2 - a_len**2) / (2 * b_len * c_len)
        sin_A = np.sqrt(1 - cos_A**2)
        C = np.array([b_len * cos_A, b_len * sin_A, 0])
        
        # Center the triangle
        center = (A + B + C) / 3
        A -= center
        B -= center
        C -= center
        
        # Scale up for visibility
        scale = 1.5
        A *= scale
        B *= scale
        C *= scale
        
        # Create triangle
        triangle = Polygon(A, B, C, color=BLUE, stroke_width=4)
        
        # Altitudes
        # h_c: from C to AB
        # Project C onto line AB.
        # Line AB direction: B-A.
        vec_AB = B - A
        unit_AB = vec_AB / np.linalg.norm(vec_AB)
        proj_C_on_AB = A + np.dot(C - A, unit_AB) * unit_AB
        h_c_line = DashedLine(C, proj_C_on_AB, color=RED)
        label_hc = MathTex("h_c").next_to(h_c_line, RIGHT, buff=0.05)
        
        # h_a: from A to BC
        vec_BC = C - B
        unit_BC = vec_BC / np.linalg.norm(vec_BC)
        proj_A_on_BC = B + np.dot(A - B, unit_BC) * unit_BC
        h_a_line = DashedLine(A, proj_A_on_BC, color=RED)
        label_ha = MathTex("h_a").next_to(h_a_line, UP, buff=0.05)
        
        # h_b: from B to AC
        vec_AC = C - A
        unit_AC = vec_AC / np.linalg.norm(vec_AC)
        proj_B_on_AC = A + np.dot(B - A, unit_AC) * unit_AC
        h_b_line = DashedLine(B, proj_B_on_AC, color=RED)
        label_hb = MathTex("h_b").next_to(h_b_line, UP, buff=0.05)
        
        # Labels
        label_A = MathTex("A").next_to(A, DL)
        label_B = MathTex("B").next_to(B, DR)
        label_C = MathTex("C").next_to(C, UP)
        
        # Side labels
        label_a = MathTex("a=4").next_to(Line(B, C), RIGHT)
        label_b = MathTex("b=6").next_to(Line(A, C), LEFT)
        label_c = MathTex("c=?").next_to(Line(A, B), DOWN)
        
        # Equation
        equation = MathTex("h_c = h_a + h_b").to_corner(UL)
        
        # Group
        scene_group = VGroup(triangle, h_a_line, h_b_line, h_c_line, label_A, label_B, label_C, label_ha, label_hb, label_hc, label_a, label_b, label_c, equation)
        scene_group.move_to(ORIGIN)
        
        # Animations
        self.play(Create(triangle), run_time=2)
        self.play(Write(label_A), Write(label_B), Write(label_C))
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.play(Create(h_a_line), Write(label_ha))
        self.play(Create(h_b_line), Write(label_hb))
        self.play(Create(h_c_line), Write(label_hc))
        self.play(Write(equation))
        
        self.wait(2)
