from manim import *
import numpy as np

class RectProjDiff(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        # Parameters
        # c = 8
        c = 8
        # a = c/2 = 4
        a = 4
        # b = sqrt(c^2 - a^2) = sqrt(64 - 16) = sqrt(48) = 4sqrt(3) approx 6.928
        b = np.sqrt(c**2 - a**2)
        
        # Points
        # C at origin
        C = ORIGIN
        # A on y-axis? No, let's put AB on x-axis for altitude visualization.
        # C at top.
        # h = ab/c = 4 * 6.928 / 8 = 3.464
        h = a * b / c
        # p = b^2/c = 48/8 = 6
        p = b**2 / c
        # q = a^2/c = 16/8 = 2
        q = a**2 / c
        
        # D at origin
        D = ORIGIN
        A = LEFT * p
        B = RIGHT * q
        C_top = UP * h
        
        # Create points
        pA = Dot(A, color=BLACK)
        pB = Dot(B, color=BLACK)
        pC = Dot(C_top, color=BLACK)
        pD = Dot(D, color=BLACK)
        
        # Shapes
        tri = Polygon(A, B, C_top, color=BLUE, fill_opacity=0.1, stroke_color=BLUE)
        alt = DashedLine(C_top, D, color=RED)
        
        # Labels
        lbl_A = MathTex('A', color=BLACK).next_to(A, DOWN+LEFT)
        lbl_B = MathTex('B', color=BLACK).next_to(B, DOWN+RIGHT)
        lbl_C = MathTex('C', color=BLACK).next_to(C_top, UP)
        lbl_D = MathTex('D', color=BLACK).next_to(D, DOWN)
        
        lbl_p = MathTex('p', color=BLACK).next_to(Line(A,D), DOWN, buff=0.1)
        lbl_q = MathTex('q', color=BLACK).next_to(Line(D,B), DOWN, buff=0.1)
        lbl_h = MathTex('h', color=RED).next_to(alt, RIGHT, buff=0.1)
        
        lbl_a = MathTex('a', color=BLACK).next_to(Line(B,C_top), RIGHT, buff=0.1)
        lbl_b = MathTex('b', color=BLACK).next_to(Line(A,C_top), LEFT, buff=0.1)
        
        # Angles
        angle_A = Angle(Line(A,B), Line(A,C_top), radius=0.7, color=BLACK)
        lbl_30 = MathTex(rr'30^\circ', color=BLACK).next_to(angle_A, UP+RIGHT)
        
        angle_B = Angle(Line(B,C_top), Line(B,A), radius=0.7, color=BLACK)
        lbl_60 = MathTex(rr'60^\circ', color=BLACK).next_to(angle_B, UP+LEFT)
        
        right_angle = RightAngle(Line(C_top, A), Line(C_top, B), length=0.4, color=BLACK)
        
        # Group
        scene_objects = VGroup(
            tri, alt,
            pA, pB, pC, pD,
            lbl_A, lbl_B, lbl_C, lbl_D,
            lbl_p, lbl_q, lbl_h,
            lbl_a, lbl_b,
            angle_A, lbl_30, angle_B, lbl_60, right_angle
        )
        
        scene_objects.scale(0.8)
        scene_objects.shift(UP * 0.5)
        
        # Text
        text = VGroup(
            MathTex(r'p - q = a', color=BLACK),
            MathTex(rr'\frrac{b^2}{c} - \frac{a^2}{c} = a', color=BLACK),
            MathTex(rr'b^2 - a^2 = ac \implies c^2 - 2a^2 = ac', color=BLACK),
            MathTex(rr'c^2 - ac - 2a^2 = 0 \implies (c-2a)(c+a) = 0', color=BLACK),
            MathTex(rr'c = 2a \implies \angle A = 30^\cirrc, \angle B = 60^\circ', color=BLACK)
        ).arrange(DOWN).next_to(scene_objects, DOWN).scale(0.7)
        
        self.add(scene_objects)
        self.add(text)
