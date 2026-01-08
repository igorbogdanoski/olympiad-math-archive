from manim import *
import numpy as np

class Problem_numerus_4419(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Parameters
        w = 4.0
        h = w * np.tan(40 * DEGREES)
        
        # Coordinates
        C = np.array([0.0, h, 0.0])
        A = np.array([-w, 0.0, 0.0])
        B = np.array([w, 0.0, 0.0])
        
        # Calculate D
        # Line AD: y = tan(20)(x+4)
        # Line BD: y = -tan(30)(x-4)
        t20 = np.tan(20 * DEGREES)
        t30 = np.tan(30 * DEGREES)
        
        x_D = 4 * (t30 - t20) / (t30 + t20)
        y_D = t20 * (x_D + 4)
        D = np.array([x_D, y_D, 0.0])
        
        # Center the view
        center_of_mass = (A + B + C) / 3
        shift = -center_of_mass
        
        A += shift
        B += shift
        C += shift
        D += shift
        
        # Scale
        scale_factor = 1.2
        A *= scale_factor
        B *= scale_factor
        C *= scale_factor
        D *= scale_factor
        
        # Elements
        triangle_ABC = Polygon(A, B, C, color=BLUE, fill_opacity=0.1)
        line_AD = Line(A, D, color=BLACK)
        line_BD = Line(B, D, color=BLACK)
        line_CD = Line(C, D, color=RED)
        
        # Labels
        lbl_A = Text("A", font_size=24, color=BLACK).next_to(A, DL, buff=0.1)
        lbl_B = Text("B", font_size=24, color=BLACK).next_to(B, DR, buff=0.1)
        lbl_C = Text("C", font_size=24, color=BLACK).next_to(C, UP, buff=0.1)
        lbl_D = Text("D", font_size=24, color=BLACK).next_to(D, UP, buff=0.1)
        
        # Angles
        # Angle BAD = 20
        angle_BAD = Angle(Line(A, B), Line(A, D), radius=1.0, color=ORANGE)
        lbl_20_A = MathTex(r"20^\\circ", color=BLACK, font_size=20).next_to(angle_BAD, RIGHT, buff=0.1)
        
        # Angle CBD = 10
        angle_CBD = Angle(Line(B, D), Line(B, A), radius=1.0, color=ORANGE)
        lbl_10_B = MathTex(r"10^\\circ", color=BLACK, font_size=20).next_to(angle_CBD, LEFT, buff=0.1).shift(UP*0.1)
        
        # Angle ACB = 100
        angle_ACB = Angle(Line(C, B), Line(C, A), radius=0.6, color=BLUE)
        lbl_100_C = MathTex(r"100^\\circ", color=BLACK, font_size=20).next_to(angle_ACB, DOWN, buff=0.1)
        
        # Angle DCB = ?
        angle_DCB = Angle(Line(C, B), Line(C, D), radius=1.2, color=RED)
        lbl_q = MathTex("?", color=RED, font_size=24).next_to(angle_DCB, DOWN, buff=0.05)
        
        # Add to scene
        self.add(triangle_ABC)
        self.add(line_AD, line_BD, line_CD)
        self.add(lbl_A, lbl_B, lbl_C, lbl_D)
        self.add(angle_BAD, lbl_20_A)
        self.add(angle_CBD, lbl_10_B)
        self.add(angle_ACB, lbl_100_C)
        self.add(angle_DCB, lbl_q)
        
        # Add text info
        info = VGroup(
            MathTex(r"\\angle ACB = 100^\\circ", color=BLACK, font_size=24),
            MathTex(r"\\angle BAD = 20^\\circ", color=BLACK, font_size=24),
            MathTex(r"\\angle CBD = 10^\\circ", color=BLACK, font_size=24),
            MathTex(r"\\angle DCB = ?", color=RED, font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UL)
        self.add(info)
