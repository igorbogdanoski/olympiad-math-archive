from manim import *
import numpy as np

class Problem_numerus_4375(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Parameters
        a = 3.0
        
        # Coordinates
        B = np.array([0.0, 0.0, 0.0])
        C = np.array([a, 0.0, 0.0])
        
        # D is on bisector (20 deg) with length a
        angle_bisector = 20 * DEGREES
        D = np.array([a * np.cos(angle_bisector), a * np.sin(angle_bisector), 0.0])
        
        # A is on line at 40 deg.
        # Triangle ABD is isosceles with DA = DB = a.
        # A is intersection of line y = x tan 40 and circle center D radius a.
        # Or simply, Triangle ABD is isosceles with base AB?
        # Angle ABD = 20. Angle BAD = 20.
        # So DA = DB = a.
        # A is at distance a from D, on line 40 deg.
        # Let's find A.
        # A = (r cos 40, r sin 40).
        # |A - D|^2 = a^2.
        # |(r cos 40 - a cos 20, r sin 40 - a sin 20)|^2 = a^2.
        # r^2 + a^2 - 2ra(cos 40 cos 20 + sin 40 sin 20) = a^2.
        # r^2 - 2ra cos(40-20) = 0.
        # r^2 - 2ra cos 20 = 0.
        # r = 2a cos 20.
        r_A = 2 * a * np.cos(20 * DEGREES)
        A = np.array([r_A * np.cos(40 * DEGREES), r_A * np.sin(40 * DEGREES), 0.0])
        
        # Center view
        center = (A + B + C) / 3
        shift = -center
        
        A += shift
        B += shift
        C += shift
        D += shift
        
        # Scale
        scale = 1.0
        A *= scale
        B *= scale
        C *= scale
        D *= scale
        
        # Elements
        triangle_ABC = Polygon(A, B, C, color=BLUE, fill_opacity=0.1)
        line_BD = Line(B, D, color=BLACK)
        line_AD = Line(A, D, color=BLACK)
        line_CD = Line(C, D, color=RED)
        
        # Labels
        lbl_A = Text("A", font_size=24, color=BLACK).next_to(A, UP, buff=0.1)
        lbl_B = Text("B", font_size=24, color=BLACK).next_to(B, DL, buff=0.1)
        lbl_C = Text("C", font_size=24, color=BLACK).next_to(C, DR, buff=0.1)
        lbl_D = Text("D", font_size=24, color=BLACK).next_to(D, RIGHT, buff=0.1)
        
        # Angles
        # Angle CBA = 40
        angle_CBA = Angle(Line(B, C), Line(B, A), radius=0.8, color=BLUE)
        lbl_40 = MathTex(r"40^\\circ", color=BLACK, font_size=20).next_to(angle_CBA, RIGHT, buff=0.1).shift(UP*0.1)
        
        # Angle BAD = 20
        angle_BAD = Angle(Line(A, B), Line(A, D), radius=0.8, color=ORANGE)
        lbl_20_A = MathTex(r"20^\\circ", color=BLACK, font_size=20).next_to(angle_BAD, DOWN, buff=0.1)
        
        # Angle ACD = ?
        angle_ACD = Angle(Line(C, D), Line(C, A), radius=0.8, color=RED)
        lbl_q = MathTex("?", color=RED, font_size=24).next_to(angle_ACD, UP, buff=0.1)
        
        # Equality marks
        # BD = BC
        tick_BD = Line(B, D).get_center()
        tick_BC = Line(B, C).get_center()
        
        t_BD = Text("|", font_size=16, color=BLACK).move_to(tick_BD).rotate(10*DEGREES).shift(UP*0.1)
        t_BC = Text("|", font_size=16, color=BLACK).move_to(tick_BC).shift(DOWN*0.1)
        
        # Add to scene
        self.add(triangle_ABC)
        self.add(line_BD, line_AD, line_CD)
        self.add(lbl_A, lbl_B, lbl_C, lbl_D)
        self.add(angle_CBA, lbl_40)
        self.add(angle_BAD, lbl_20_A)
        self.add(angle_ACD, lbl_q)
        self.add(t_BD, t_BC)
        
        # Add text info
        info = VGroup(
            MathTex("BD = BC", color=BLACK, font_size=24),
            MathTex(r"\\angle BAD = 20^\\circ", color=BLACK, font_size=24),
            MathTex(r"\\angle ACD = ?", color=RED, font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UL)
        self.add(info)
