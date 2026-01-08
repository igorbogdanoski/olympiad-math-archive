from manim import *
import numpy as np

class AngleIncenter(Scene):
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
        # x_C = (b cos A + c) ? No.
        # Use law of sines to find sides a, b.
        # a/sinA = b/sinB = c/sinC
        # a = c sinA / sinC
        # b = c sinB / sinC
        a_len = c * np.sin(alpha) / np.sin(gamma)
        b_len = c * np.sin(beta) / np.sin(gamma)
        
        # C = (b cos A, b sin A) relative to A? No, A is at (-c/2, 0).
        # C = A + (b cos alpha, b sin alpha)
        C = A + np.array([b_len * np.cos(alpha), b_len * np.sin(alpha), 0])
        
        # Incenter I
        # I = (aA + bB + cC) / (a+b+c)
        I = (a_len * A + b_len * B + c * C) / (a_len + b_len + c)
        
        # Create points
        pA = Dot(A, color=BLACK)
        pB = Dot(B, color=BLACK)
        pC = Dot(C, color=BLACK)
        pI = Dot(I, color=RED)
        
        # Shapes
        tri = Polygon(A, B, C, color=BLUE, fill_opacity=0.1, stroke_color=BLUE)
        bisector_A = Line(A, I, color=GREEN)
        bisector_B = Line(B, I, color=GREEN)
        bisector_C = DashedLine(C, I, color=GREEN)
        
        # Labels
        lbl_A = MathTex('A', color=BLACK).next_to(A, DOWN+LEFT)
        lbl_B = MathTex('B', color=BLACK).next_to(B, DOWN+RIGHT)
        lbl_C = MathTex('C', color=BLACK).next_to(C, UP)
        lbl_I = MathTex('I', color=RED).next_to(I, UP, buff=0.1)
        
        # Angles
        # Angle A/2
        angle_A1 = Angle(Line(A,B), Line(A,I), radius=0.5, color=BLACK)
        angle_A2 = Angle(Line(A,I), Line(A,C), radius=0.6, color=BLACK)
        lbl_alpha2 = MathTex(rr'\frac{\alpha}{2}', color=BLACK).next_to(angle_A1, RIGHT, buff=0.1).scale(0.6)
        
        # Angle B/2
        angle_B1 = Angle(Line(B,I), Line(B,A), radius=0.5, color=BLACK)
        angle_B2 = Angle(Line(B,C), Line(B,I), radius=0.6, color=BLACK)
        lbl_beta2 = MathTex(rr'\frac{\beta}{2}', color=BLACK).next_to(angle_B1, LEFT, buff=0.1).scale(0.6)
        
        # Angle AIB
        angle_AIB = Angle(Line(I,B), Line(I,A), radius=0.4, color=RED)
        lbl_phi = MathTex(rr'\phi', color=RED).next_to(angle_AIB, UP, buff=0.1).scale(0.7)
        
        # Group
        scene_objects = VGroup(
            tri, bisector_A, bisector_B, bisector_C,
            pA, pB, pC, pI,
            lbl_A, lbl_B, lbl_C, lbl_I,
            angle_A1, angle_A2, lbl_alpha2,
            angle_B1, angle_B2, lbl_beta2,
            angle_AIB, lbl_phi
        )
        
        scene_objects.scale(1.2)
        scene_objects.shift(DOWN * 0.5)
        
        # Text
        text = VGroup(
            MathTex(rr'\text{In } \triangle ABI:', color=BLACK),
            MathTex(rr'\angle AIB + \frac{\alpha}{2} + \frrac{\beta}{2} = 180^\circ', color=BLACK),
            MathTex(rr'\angle AIB = 180^\circ - \frrac{\alpha + \beta}{2}', color=BLACK),
            MathTex(rr'\alpha + \beta = 180^\circ - \gamma', color=BLACK),
            MathTex(rr'\angle AIB = 180^\circ - \frrac{180^\circ - \gamma}{2}', color=BLACK),
            MathTex(rr'\angle AIB = 90^\circ + \frrac{\gamma}{2}', color=BLACK)
        ).arrange(DOWN).next_to(scene_objects, UP, buff=0.5).scale(0.7)
        
        self.add(scene_objects)
        self.add(text)
