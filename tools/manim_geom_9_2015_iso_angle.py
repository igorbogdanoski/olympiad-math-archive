from manim import *
import numpy as np

class GeometryScene(Scene):
    def construct(self):
        # Define parameters
        # Base angle alpha = 36 degrees
        alpha_deg = 36
        alpha = alpha_deg * DEGREES
        
        # Base length c = 6
        c_len = 6.0
        half_c = c_len / 2
        
        # Height h_c = (c/2) * tan(alpha)
        h_c_len = half_c * np.tan(alpha)
        
        # Points
        A = np.array([-half_c, -1, 0])
        B = np.array([half_c, -1, 0])
        C = np.array([0, -1 + h_c_len, 0])
        
        # Triangle
        triangle = Polygon(A, B, C, color=BLUE, stroke_width=4)
        
        # Altitude CD
        D = (A + B) / 2
        altitude = DashedLine(C, D, color=RED)
        label_hc = MathTex("h_c").next_to(altitude, RIGHT, buff=0.05)
        
        # Angle bisector AE
        # Angle A is 36 deg. Bisector is at 18 deg from AB.
        # Vector AB is (1, 0).
        # Vector AE direction is (cos 18, sin 18).
        bisector_angle = alpha / 2
        dir_AE = np.array([np.cos(bisector_angle), np.sin(bisector_angle), 0])
        
        # Intersect ray A + t * dir_AE with segment BC
        # Line BC: P = B + u * (C - B)
        # A + t * d = B + u * (C - B)
        # A - B = u * (C - B) - t * d
        # Solve linear system for t, u
        # x: Ax - Bx = u(Cx - Bx) - t dx
        # y: Ay - By = u(Cy - By) - t dy
        
        # Ax - Bx = -c_len
        # Ay - By = 0
        # Cx - Bx = -half_c
        # Cy - By = h_c_len
        
        # -c = u(-c/2) - t dx
        # 0 = u(h_c) - t dy
        
        # t = u * h_c / dy
        # -c = -u*c/2 - (u * h_c / dy) * dx
        # c = u (c/2 + h_c * dx / dy)
        # u = c / (c/2 + h_c * dx / dy)
        
        dx = dir_AE[0]
        dy = dir_AE[1]
        
        u = c_len / (c_len/2 + h_c_len * dx / dy)
        E = B + u * (C - B)
        
        bisector = DashedLine(A, E, color=GREEN)
        label_l = MathTex("l_\\alpha").next_to(bisector, UP, buff=0.05)
        
        # Labels
        label_A = MathTex("A").next_to(A, DL)
        label_B = MathTex("B").next_to(B, DR)
        label_C = MathTex("C").next_to(C, UP)
        label_D = MathTex("D").next_to(D, DOWN)
        label_E = MathTex("E").next_to(E, UR)
        
        # Angles
        angle_A = Angle(Line(A, B), Line(A, C), radius=0.5)
        label_angle_A = MathTex("36^\\circ").next_to(angle_A, RIGHT)
        
        # Equation
        equation = MathTex("l_\\alpha = 2 h_c").to_corner(UL)
        
        # Group
        scene_group = VGroup(triangle, altitude, bisector, label_A, label_B, label_C, label_D, label_E, label_hc, label_l, angle_A, label_angle_A, equation)
        scene_group.move_to(ORIGIN)
        
        # Animations
        self.play(Create(triangle), run_time=2)
        self.play(Write(label_A), Write(label_B), Write(label_C))
        self.play(Create(altitude), Write(label_hc), Write(label_D))
        self.play(Create(bisector), Write(label_l), Write(label_E))
        self.play(Create(angle_A), Write(label_angle_A))
        self.play(Write(equation))
        
        self.wait(2)
