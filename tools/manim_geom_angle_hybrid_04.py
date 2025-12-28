from manim import *

class Problem_geom_angle_hybrid_04(Scene):
    def construct(self):
        # Scale
        scale = 1.2
        
        # Coordinates
        A = np.array([-2.0, -1.0, 0])
        B = np.array([2.0, -1.0, 0])
        C = np.array([0.5, 2.5, 0])
        
        # Shift to center
        center = (A + B + C) / 3
        shift = -center
        
        A += shift
        B += shift
        C += shift
        
        # Apply scale
        A *= scale
        B *= scale
        C *= scale
        
        # Vectors
        v_AB = B - A
        v_AC = C - A
        v_BC = C - B
        v_BA = A - B
        
        # Internal bisector of A
        u_AB = v_AB / np.linalg.norm(v_AB)
        u_AC = v_AC / np.linalg.norm(v_AC)
        dir_bisect_A = u_AB + u_AC
        # Line A + t * dir_bisect_A
        
        # External bisector of B
        # Extend AB to B_ext
        u_BA = v_BA / np.linalg.norm(v_BA)
        u_BC = v_BC / np.linalg.norm(v_BC)
        # External angle is between BC and extension of AB.
        # Extension of AB is direction -u_BA = u_AB.
        u_B_ext = -u_BA
        dir_bisect_B_ext = u_BC + u_B_ext
        # Line B + s * dir_bisect_B_ext
        
        # Find intersection Y
        # A + t * dA = B + s * dB
        # t * dA - s * dB = B - A
        dA = dir_bisect_A
        dB = dir_bisect_B_ext
        
        # Solve linear system for t, s
        # dA_x * t - dB_x * s = B_x - A_x
        # dA_y * t - dB_y * s = B_y - A_y
        
        mat = np.array([[dA[0], -dB[0]], [dA[1], -dB[1]]])
        rhs = np.array([B[0] - A[0], B[1] - A[1]])
        sol = np.linalg.solve(mat, rhs)
        t = sol[0]
        
        Y = A + t * dA
        
        # Objects
        triangle = Polygon(A, B, C, color=BLUE, fill_opacity=0.1)
        
        line_AY = Line(A, Y, color=YELLOW)
        line_BY = Line(B, Y, color=YELLOW)
        
        # Extension of AB for visualization
        B_ext_pt = B + u_B_ext * 1.5
        line_AB_ext = DashedLine(B, B_ext_pt, color=GRAY)
        
        # Labels
        label_A = MathTex("A").next_to(A, DL)
        label_B = MathTex("B").next_to(B, DOWN)
        label_C = MathTex("C").next_to(C, UP)
        label_Y = MathTex("Y").next_to(Y, UP)
        
        # Angles
        angle_C = Angle(Line(C, A), Line(C, B), radius=0.4, color=GREEN)
        label_gamma = MathTex(r"\gamma").next_to(angle_C, UP, buff=0.1)
        
        angle_AYB = Angle(Line(Y, B), Line(Y, A), radius=0.4, color=RED)
        label_res = MathTex(r"\frac{\gamma}{2}").next_to(angle_AYB, LEFT, buff=0.1)
        
        # Mark bisectors
        # Angle A
        a1 = Angle(Line(A, B), Line(A, Y), radius=0.5, color=YELLOW)
        a2 = Angle(Line(A, Y), Line(A, C), radius=0.6, color=YELLOW)
        
        # Angle B ext
        b1 = Angle(Line(B, C), Line(B, Y), radius=0.5, color=YELLOW)
        b2 = Angle(Line(B, Y), Line(B, B_ext_pt), radius=0.6, color=YELLOW)
        
        self.add(triangle)
        self.add(line_AY, line_BY, line_AB_ext)
        self.add(label_A, label_B, label_C, label_Y)
        self.add(angle_C, label_gamma)
        self.add(angle_AYB, label_res)
        self.add(a1, a2, b1, b2)
        
        # Text
        text = MathTex(r"\angle AYB = \frac{\gamma}{2}").to_corner(UL)
        self.add(text)
