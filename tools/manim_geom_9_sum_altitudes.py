from manim import *

class Problem_geom_9_sum_altitudes(Scene):
    def construct(self):
        # Scale
        scale = 1.5
        
        # Triangle ABC
        A = UP * 2 + LEFT * 1
        B = DOWN * 1.5 + LEFT * 2.5
        C = DOWN * 1.5 + RIGHT * 2.5
        
        # Point M inside
        M = (A + B + C) / 3 + DOWN * 0.2 + RIGHT * 0.1
        
        # Shift to center
        center = (A + B + C) / 3
        shift = -center
        
        A += shift
        B += shift
        C += shift
        M += shift
        
        # Scale
        A *= scale
        B *= scale
        C *= scale
        M *= scale
        
        # Objects
        tri = Polygon(A, B, C, color=BLUE)
        
        dot_A = Dot(A, color=WHITE)
        dot_B = Dot(B, color=WHITE)
        dot_C = Dot(C, color=WHITE)
        dot_M = Dot(M, color=RED)
        
        label_A = MathTex("A").next_to(dot_A, UP)
        label_B = MathTex("B").next_to(dot_B, DL)
        label_C = MathTex("C").next_to(dot_C, DR)
        label_M = MathTex("M").next_to(dot_M, UP)
        
        # Perpendiculars from M to sides
        # Side a (BC)
        # Project M onto BC
        # Line BC direction
        v_BC = C - B
        u_BC = v_BC / np.linalg.norm(v_BC)
        v_BM = M - B
        proj_M_BC = B + np.dot(v_BM, u_BC) * u_BC
        perp_x = Line(M, proj_M_BC, color=YELLOW)
        label_x = MathTex("x").next_to(perp_x, RIGHT, buff=0.1).scale(0.8)
        
        # Side b (AC)
        v_AC = C - A
        u_AC = v_AC / np.linalg.norm(v_AC)
        v_AM = M - A
        proj_M_AC = A + np.dot(v_AM, u_AC) * u_AC
        perp_y = Line(M, proj_M_AC, color=YELLOW)
        label_y = MathTex("y").next_to(perp_y, UP, buff=0.1).scale(0.8)
        
        # Side c (AB)
        v_AB = B - A
        u_AB = v_AB / np.linalg.norm(v_AB)
        v_AM = M - A
        proj_M_AB = A + np.dot(v_AM, u_AB) * u_AB
        perp_z = Line(M, proj_M_AB, color=YELLOW)
        label_z = MathTex("z").next_to(perp_z, LEFT, buff=0.1).scale(0.8)
        
        # Altitudes
        # h_a from A to BC
        v_BC = C - B
        u_BC = v_BC / np.linalg.norm(v_BC)
        v_BA = A - B
        proj_A_BC = B + np.dot(v_BA, u_BC) * u_BC
        alt_ha = DashedLine(A, proj_A_BC, color=GREEN)
        label_ha = MathTex("h_a").next_to(alt_ha, RIGHT, buff=0.1).scale(0.8)
        
        # h_b from B to AC
        v_AC = C - A
        u_AC = v_AC / np.linalg.norm(v_AC)
        v_AB = B - A
        proj_B_AC = A + np.dot(v_AB, u_AC) * u_AC
        alt_hb = DashedLine(B, proj_B_AC, color=GREEN)
        label_hb = MathTex("h_b").next_to(alt_hb, DOWN, buff=0.1).scale(0.8)
        
        # h_c from C to AB
        v_AB = B - A
        u_AB = v_AB / np.linalg.norm(v_AB)
        v_AC = C - A
        proj_C_AB = A + np.dot(v_AC, u_AB) * u_AB
        alt_hc = DashedLine(C, proj_C_AB, color=GREEN)
        label_hc = MathTex("h_c").next_to(alt_hc, DOWN, buff=0.1).scale(0.8)
        
        self.add(tri)
        self.add(alt_ha, alt_hb, alt_hc)
        self.add(perp_x, perp_y, perp_z)
        self.add(dot_A, dot_B, dot_C, dot_M)
        self.add(label_A, label_B, label_C, label_M)
        self.add(label_x, label_y, label_z)
        self.add(label_ha, label_hb, label_hc)
        
        # Add formula
        formula = MathTex(r"\frac{x}{h_a} + \frac{y}{h_b} + \frac{z}{h_c} = 1").to_corner(UL)
        self.add(formula)
