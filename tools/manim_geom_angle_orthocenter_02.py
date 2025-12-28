from manim import *
import numpy as np

class AngleOrthocenter(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        # Parameters
        c = 6
        alpha_deg = 50
        beta_deg = 70
        gamma_deg = 180 - alpha_deg - beta_deg # 60
        
        alpha = alpha_deg * DEGREES
        beta = beta_deg * DEGREES
        gamma = gamma_deg * DEGREES
        
        # Points
        A = LEFT * c / 2
        B = RIGHT * c / 2
        
        # C coordinates
        a_len = c * np.sin(alpha) / np.sin(gamma)
        b_len = c * np.sin(beta) / np.sin(gamma)
        C = A + np.array([b_len * np.cos(alpha), b_len * np.sin(alpha), 0])
        
        # Altitudes
        # D on BC (from A)
        # Vector BC
        v_BC = C - B
        # Project BA onto BC
        v_BA = A - B
        proj = np.dot(v_BA, v_BC) / np.dot(v_BC, v_BC) * v_BC
        D = B + proj
        
        # E on AC (from B)
        # Vector AC
        v_AC = C - A
        # Project AB onto AC
        v_AB = B - A
        proj = np.dot(v_AB, v_AC) / np.dot(v_AC, v_AC) * v_AC
        E = A + proj
        
        # Orthocenter H (Intersection of AD and BE)
        # Line AD: A + t(D-A)
        # Line BE: B + u(E-B)
        # Use geometry utils or manual intersection
        # Manual:
        # x = Ax + t(Dx-Ax) = Bx + u(Ex-Bx)
        # y = Ay + t(Dy-Ay) = By + u(Ey-By)
        # t(Dx-Ax) - u(Ex-Bx) = Bx - Ax
        # t(Dy-Ay) - u(Ey-By) = By - Ay
        # Solve for t, u
        denom = (D[0]-A[0])*(E[1]-B[1]) - (D[1]-A[1])*(E[0]-B[0])
        t = ((B[0]-A[0])*(E[1]-B[1]) - (B[1]-A[1])*(E[0]-B[0])) / denom
        H = A + t * (D - A)
        
        # Create points
        pA = Dot(A, color=BLACK)
        pB = Dot(B, color=BLACK)
        pC = Dot(C, color=BLACK)
        pH = Dot(H, color=RED)
        pD = Dot(D, color=BLACK)
        pE = Dot(E, color=BLACK)
        
        # Shapes
        tri = Polygon(A, B, C, color=BLUE, fill_opacity=0.1, stroke_color=BLUE)
        alt_AD = Line(A, D, color=GREEN)
        alt_BE = Line(B, E, color=GREEN)
        
        # Labels
        lbl_A = MathTex('A', color=BLACK).next_to(A, DOWN+LEFT)
        lbl_B = MathTex('B', color=BLACK).next_to(B, DOWN+RIGHT)
        lbl_C = MathTex('C', color=BLACK).next_to(C, UP)
        lbl_H = MathTex('H', color=RED).next_to(H, DOWN+LEFT, buff=0.1)
        lbl_D = MathTex('D', color=BLACK).next_to(D, RIGHT, buff=0.1)
        lbl_E = MathTex('E', color=BLACK).next_to(E, LEFT, buff=0.1)
        
        # Angles
        right_D = RightAngle(Line(D, A), Line(D, C), length=0.3, color=BLACK)
        right_E = RightAngle(Line(E, B), Line(E, C), length=0.3, color=BLACK)
        
        angle_C = Angle(Line(C,A), Line(C,B), radius=0.5, color=BLACK)
        lbl_gamma = MathTex(r'\gamma', color=BLACK).next_to(angle_C, DOWN, buff=0.1)
        
        angle_AHB = Angle(Line(H,B), Line(H,A), radius=0.4, color=RED)
        lbl_phi = MathTex(r'\phi', color=RED).next_to(angle_AHB, UP, buff=0.1)
        
        # Cyclic Quad CDHE
        quad = Polygon(C, D, H, E, color=ORANGE, fill_opacity=0.1)
        
        # Group
        scene_objects = VGroup(
            tri, alt_AD, alt_BE,
            pA, pB, pC, pH, pD, pE,
            lbl_A, lbl_B, lbl_C, lbl_H, lbl_D, lbl_E,
            right_D, right_E,
            angle_C, lbl_gamma,
            angle_AHB, lbl_phi,
            quad
        )
        
        scene_objects.scale(1.2)
        scene_objects.shift(DOWN * 0.5)
        
        # Text
        text = VGroup(
            MathTex(r'\text{Quadrilateral } CDHE:', color=BLACK),
            MathTex(r'\angle CDH = 90^\circ, \angle CEH = 90^\circ', color=BLACK),
            MathTex(r'\angle C + \angle CDH + \angle DHE + \angle CEH = 360^\circ', color=BLACK),
            MathTex(r'\gamma + 90^\circ + \angle DHE + 90^\circ = 360^\circ', color=BLACK),
            MathTex(r'\angle DHE = 180^\circ - \gamma', color=BLACK),
            MathTex(r'\angle AHB = \angle DHE \text{ (vertically opposite)}', color=BLACK),
            MathTex(r'\angle AHB = 180^\circ - \gamma', color=BLACK)
        ).arrange(DOWN).next_to(scene_objects, UP, buff=0.5).scale(0.7)
        
        self.add(scene_objects)
        self.add(text)
