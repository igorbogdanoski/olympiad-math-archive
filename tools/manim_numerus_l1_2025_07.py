from manim import *
import numpy as np

class Problem_numerus_L1_2025_07(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Parameters
        a = 2.5
        
        # Coordinates
        # C at origin
        C = np.array([0.0, 0.0, 0.0])
        
        # A on x-axis
        A = np.array([a, 0.0, 0.0])
        
        # B at angle 40 deg
        angle_C = 40 * DEGREES
        B = np.array([a * np.cos(angle_C), a * np.sin(angle_C), 0.0])
        
        # Square ACDE external
        # A(a,0), C(0,0).
        # Vector CA = (a,0).
        # Rotate -90 deg for CD?
        # If B has y > 0, then external square should have y < 0.
        # So D is at (0, -a).
        D = np.array([0.0, -a, 0.0])
        E = np.array([a, -a, 0.0])
        
        # Center view
        center = (A + B + C + D + E) / 5
        shift = -center
        
        A += shift
        B += shift
        C += shift
        D += shift
        E += shift
        
        # Scale
        scale = 0.8
        A *= scale
        B *= scale
        C *= scale
        D *= scale
        E *= scale
        
        # Elements
        triangle_ABC = Polygon(A, B, C, color=BLUE, fill_opacity=0.1)
        square_ACDE = Polygon(A, C, D, E, color=GREEN, fill_opacity=0.1)
        
        line_AD = Line(A, D, color=BLACK) # Diagonal of square
        line_BD = Line(B, D, color=RED)
        line_AB = Line(A, B, color=BLACK)
        
        # Labels
        lbl_A = Text("A", font_size=24, color=BLACK).next_to(A, RIGHT, buff=0.1)
        lbl_B = Text("B", font_size=24, color=BLACK).next_to(B, UP, buff=0.1)
        lbl_C = Text("C", font_size=24, color=BLACK).next_to(C, LEFT, buff=0.1)
        lbl_D = Text("D", font_size=24, color=BLACK).next_to(D, LEFT, buff=0.1)
        lbl_E = Text("E", font_size=24, color=BLACK).next_to(E, RIGHT, buff=0.1)
        
        # Angles
        # Angle C = 40
        angle_ACB = Angle(Line(C, A), Line(C, B), radius=0.6, color=BLUE)
        lbl_40 = MathTex(r"40^\\circ", color=BLACK, font_size=20).next_to(angle_ACB, UR, buff=0.1)
        
        # Angle ADB = ?
        angle_ADB = Angle(Line(D, A), Line(D, B), radius=1.0, color=RED)
        lbl_q = MathTex("?", color=RED, font_size=24).next_to(angle_ADB, UP, buff=0.1)
        
        # Add to scene
        self.add(triangle_ABC)
        self.add(square_ACDE)
        self.add(line_BD)
        self.add(lbl_A, lbl_B, lbl_C, lbl_D, lbl_E)
        self.add(angle_ACB, lbl_40)
        self.add(angle_ADB, lbl_q)
        
        # Add text info
        info = VGroup(
            MathTex("AC=BC", color=BLACK, font_size=24),
            MathTex(r"\\angle C = 40^\\circ", color=BLACK, font_size=24),
            MathTex(r"ACDE \\text{ is square}", color=GREEN, font_size=24),
            MathTex(r"\\angle ADB = ?", color=RED, font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UL)
        self.add(info)
