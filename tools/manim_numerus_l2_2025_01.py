from manim import *
import numpy as np

class Problem_numerus_L2_2025_01(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Parameters
        d = 4.0
        r = 2.5
        x_deg = 65
        x_rad = x_deg * DEGREES
        
        # s = r + 2d cos x
        s = r + 2 * d * np.cos(x_rad)
        
        # Coordinates
        D = np.array([0.0, 0.0, 0.0])
        B = np.array([d, 0.0, 0.0])
        
        # C: Angle BDC = 180 - x
        # Vector DC angle is 180 - x
        C = np.array([r * np.cos(PI - x_rad), r * np.sin(PI - x_rad), 0.0])
        
        # A: Angle DBA = x
        # Vector BA angle is 180 + x (since A is below DB)
        # A = B + s * (cos(180+x), sin(180+x))
        A = B + np.array([s * np.cos(PI + x_rad), s * np.sin(PI + x_rad), 0.0])
        
        # Center view
        center = (A + B + C + D) / 4
        shift = -center
        
        A += shift
        B += shift
        C += shift
        D += shift
        
        # Scale
        scale = 0.8
        A *= scale
        B *= scale
        C *= scale
        D *= scale
        
        # Elements
        quad = Polygon(A, B, C, D, color=BLUE, fill_opacity=0.1)
        diag_BD = Line(B, D, color=BLACK)
        diag_AC = DashedLine(A, C, color=GRAY)
        
        # Labels
        lbl_A = Text("A", font_size=24, color=BLACK).next_to(A, DOWN, buff=0.1)
        lbl_B = Text("B", font_size=24, color=BLACK).next_to(B, RIGHT, buff=0.1)
        lbl_C = Text("C", font_size=24, color=BLACK).next_to(C, UP, buff=0.1)
        lbl_D = Text("D", font_size=24, color=BLACK).next_to(D, LEFT, buff=0.1)
        
        # Angles
        # Angle BDC = 180 - x
        angle_BDC = Angle(Line(D, B), Line(D, C), radius=0.6, color=ORANGE)
        # lbl_BDC = MathTex(r"180^\\circ - x", color=BLACK, font_size=16).next_to(angle_BDC, UP, buff=0.1)
        
        # Angle DBA = x
        angle_DBA = Angle(Line(B, A), Line(B, D), radius=0.6, color=ORANGE)
        # lbl_DBA = MathTex("x", color=BLACK, font_size=16).next_to(angle_DBA, LEFT, buff=0.1)
        
        # Angle DCB = 47
        angle_DCB = Angle(Line(C, B), Line(C, D), radius=0.6, color=BLUE)
        lbl_47 = MathTex(r"47^\\circ", color=BLACK, font_size=20).next_to(angle_DCB, DOWN, buff=0.1)
        
        # Angle BAD = ?
        angle_BAD = Angle(Line(A, D), Line(A, B), radius=0.6, color=RED)
        lbl_q = MathTex("?", color=RED, font_size=24).next_to(angle_BAD, UP, buff=0.1)
        
        # Equality marks AD = BC
        tick_AD = Line(A, D).get_center()
        tick_BC = Line(B, C).get_center()
        
        t_AD = Text("|", font_size=16, color=BLACK).move_to(tick_AD).shift(LEFT*0.1)
        t_BC = Text("|", font_size=16, color=BLACK).move_to(tick_BC).shift(RIGHT*0.1)
        
        # Add to scene
        self.add(quad)
        self.add(diag_BD)
        self.add(lbl_A, lbl_B, lbl_C, lbl_D)
        self.add(angle_BDC, angle_DBA)
        self.add(angle_DCB, lbl_47)
        self.add(angle_BAD, lbl_q)
        self.add(t_AD, t_BC)
        
        # Add text info
        info = VGroup(
            MathTex("AD = BC", color=BLACK, font_size=24),
            MathTex(r"\\angle DBA + \\angle BDC = 180^\\circ", color=BLACK, font_size=24),
            MathTex(r"\\angle DCB = 47^\\circ", color=BLACK, font_size=24),
            MathTex(r"\\angle BAD = ?", color=RED, font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UL)
        self.add(info)
