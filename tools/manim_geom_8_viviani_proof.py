from manim import *
import numpy as np

class VivianiProof(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        # Parameters
        side = 6
        h = side * np.sqrt(3) / 2
        
        # Points
        A = LEFT * side / 2 + DOWN * h / 3
        B = RIGHT * side / 2 + DOWN * h / 3
        C = UP * 2 * h / 3
        
        # Point S inside
        S = np.array([0.5, 0.2, 0])
        
        # Projections
        # Side AB (y = -h/3)
        P_AB = np.array([S[0], A[1], 0])
        
        # Side BC
        # Line BC direction vector v = C - B.
        v_BC = C - B
        # Normal vector n = (-v_BC[1], v_BC[0])
        n_BC = np.array([-v_BC[1], v_BC[0], 0])
        n_BC = n_BC / np.linalg.norm(n_BC)
        # Vector from B to S
        v_BS = S - B
        # Distance d = v_BS . n_BC (signed)
        d_BC = np.dot(v_BS, n_BC)
        # P_BC = S - d_BC * n_BC
        P_BC = S - d_BC * n_BC
        
        # Side AC
        # Line AC direction vector v = C - A.
        v_AC = C - A
        # Normal vector n (pointing inward/outward)
        n_AC = np.array([v_AC[1], -v_AC[0], 0])
        n_AC = n_AC / np.linalg.norm(n_AC)
        v_AS = S - A
        d_AC = np.dot(v_AS, n_AC)
        P_AC = S - d_AC * n_AC
        
        # Create points
        pA = Dot(A, color=BLACK)
        pB = Dot(B, color=BLACK)
        pC = Dot(C, color=BLACK)
        pS = Dot(S, color=RED)
        
        # Shapes
        tri = Polygon(A, B, C, color=BLUE, fill_opacity=0.1, stroke_color=BLUE)
        
        # Perpendiculars
        line_SM = Line(S, P_AB, color=GREEN)
        lbl_M = MathTex('M', color=BLACK).next_to(P_AB, DOWN, buff=0.1)
        
        line_SN = Line(S, P_BC, color=GREEN)
        lbl_N = MathTex('N', color=BLACK).next_to(P_BC, UP+RIGHT, buff=0.1)
        
        line_SP = Line(S, P_AC, color=GREEN)
        lbl_P = MathTex('P', color=BLACK).next_to(P_AC, UP+LEFT, buff=0.1)
        
        # Altitude
        alt_C = DashedLine(C, np.array([0, A[1], 0]), color=ORANGE)
        lbl_h = MathTex('h', color=ORANGE).next_to(alt_C, LEFT, buff=0.1)
        
        # Labels
        lbl_A = MathTex('A', color=BLACK).next_to(A, DOWN+LEFT)
        lbl_B = MathTex('B', color=BLACK).next_to(B, DOWN+RIGHT)
        lbl_C = MathTex('C', color=BLACK).next_to(C, UP)
        lbl_S = MathTex('S', color=RED).next_to(S, UP, buff=0.1)
        
        lbl_x = MathTex('x', color=GREEN).next_to(line_SM, RIGHT, buff=0.05).scale(0.7)
        lbl_y = MathTex('y', color=GREEN).next_to(line_SN, DOWN, buff=0.05).scale(0.7)
        lbl_z = MathTex('z', color=GREEN).next_to(line_SP, DOWN, buff=0.05).scale(0.7)
        
        # Group
        scene_objects = VGroup(
            tri, alt_C,
            line_SM, line_SN, line_SP,
            pA, pB, pC, pS,
            lbl_A, lbl_B, lbl_C, lbl_S,
            lbl_M, lbl_N, lbl_P, lbl_h,
            lbl_x, lbl_y, lbl_z
        )
        
        scene_objects.scale(0.8)
        scene_objects.shift(UP * 0.5)
        
        # Text
        text = VGroup(
            MathTex(r'P_{ABC} = P_{SAB} + P_{SBC} + P_{SCA}', color=BLACK),
            MathTex(rr'\frac{a \cdot h}{2} = \frrac{a \cdot x}{2} + \frac{a \cdot y}{2} + \frrac{a \cdot z}{2}', color=BLACK),
            MathTex(r'h = x + y + z', color=BLACK),
            MathTex(r'SM + SN + SP = h', color=BLACK)
        ).arrange(DOWN).next_to(scene_objects, DOWN).scale(0.7)
        
        self.add(scene_objects)
        self.add(text)
