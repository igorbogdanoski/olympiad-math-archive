from manim import *
import numpy as np

class IsoscelesAngle(Scene):
    def construct(self):
        # Parameters
        alpha_deg = 36
        alpha = alpha_deg * DEGREES
        # Base length c = 6
        c = 6
        # Height h_c = c/2 * tan(alpha)
        h_c = c/2 * np.tan(alpha)
        
        # Points
        # M at origin
        M = ORIGIN
        A = LEFT * c / 2
        B = RIGHT * c / 2
        C = UP * h_c
        
        # Bisector AD
        # D is on BC.
        # Angle DAB = alpha/2 = 18 deg.
        # Line AD slope: tan(18).
        # Line BC equation:
        # B = (c/2, 0), C = (0, h_c).
        # Slope BC = -h_c / (c/2) = -2h_c/c = -tan(alpha).
        # y - 0 = -tan(alpha) * (x - c/2).
        # Line AD equation: y - 0 = tan(alpha/2) * (x + c/2).
        # Intersection D.
        # tan(alpha/2)(x + c/2) = -tan(alpha)(x - c/2).
        # Let t = tan(alpha/2). tan(alpha) = 2t/(1-t^2).
        # t(x + c/2) = -2t/(1-t^2) * (x - c/2).
        # x + c/2 = -2/(1-t^2) * (x - c/2).
        # (x + c/2)(1-t^2) = -2(x - c/2).
        # x(1-t^2) + c/2(1-t^2) = -2x + c.
        # x(3-t^2) = c - c/2(1-t^2) = c(1 - 0.5 + 0.5t^2) = c(0.5 + 0.5t^2).
        # x = c(1+t^2) / (2(3-t^2)).
        # y = t * (x + c/2).
        
        t = np.tan(alpha/2)
        x_D = c * (1 + t**2) / (2 * (3 - t**2))
        y_D = t * (x_D + c/2)
        D = np.array([x_D, y_D, 0])
        
        # Create points
        pA = Dot(A)
        pB = Dot(B)
        pC = Dot(C)
        pM = Dot(M)
        pD = Dot(D)
        
        # Shapes
        tri = Polygon(A, B, C, color=BLUE, fill_opacity=0.1)
        height = DashedLine(C, M, color=RED)
        bisector = Line(A, D, color=GREEN)
        
        # Labels
        lbl_A = MathTex("A").next_to(A, DOWN+LEFT)
        lbl_B = MathTex("B").next_to(B, DOWN+RIGHT)
        lbl_C = MathTex("C").next_to(C, UP)
        lbl_M = MathTex("M").next_to(M, DOWN)
        lbl_D = MathTex("D").next_to(D, UP+RIGHT)
        
        lbl_hc = MathTex("h_c").next_to(height, LEFT, buff=0.1)
        lbl_la = MathTex("l_a").next_to(bisector, UP, buff=0.1)
        
        # Angles
        angle_A = Angle(Line(A,B), Line(A,C), radius=0.7)
        lbl_alpha = MathTex(r"\alpha").next_to(angle_A, UP+RIGHT)
        
        angle_bisect1 = Angle(Line(A,B), Line(A,D), radius=1.0)
        angle_bisect2 = Angle(Line(A,D), Line(A,C), radius=1.1)
        
        # Group
        scene_objects = VGroup(
            tri, height, bisector,
            pA, pB, pC, pM, pD,
            lbl_A, lbl_B, lbl_C, lbl_M, lbl_D,
            lbl_hc, lbl_la,
            angle_A, lbl_alpha,
            angle_bisect1, angle_bisect2
        )
        
        scene_objects.scale(1.5)
        scene_objects.move_to(ORIGIN)
        
        # Text
        text = VGroup(
            MathTex(r"h_c = \frac{l_a}{2}"),
            MathTex(r"\cos \alpha = \sin(1.5 \alpha)"),
            MathTex(r"\alpha = 36^\circ")
        ).arrange(DOWN).next_to(scene_objects, DOWN)
        
        self.add(scene_objects)
        self.add(text)
