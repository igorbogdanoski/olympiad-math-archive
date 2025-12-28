from manim import *
import numpy as np

class Problem_numerus_4332(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Parameters
        # a = 8, b = 4
        # h_a = 3, h_b = 6
        # sin C = 3/4
        
        sin_C = 0.75
        cos_C = np.sqrt(1 - sin_C**2) # approx 0.66
        
        # Coordinates
        # C at origin
        C = np.array([0.0, 0.0, 0.0])
        
        # B on x-axis. a = 8.
        B = np.array([8.0, 0.0, 0.0])
        
        # A at distance b=4 from C, angle C.
        # A = (b cos C, b sin C) = (4 * cos_C, 4 * 0.75) = (4 * cos_C, 3)
        A = np.array([4 * cos_C, 3.0, 0.0])
        
        # Center view
        center = (A + B + C) / 3
        shift = -center
        
        A += shift
        B += shift
        C += shift
        
        # Scale
        scale = 0.8
        A *= scale
        B *= scale
        C *= scale
        
        # Elements
        triangle = Polygon(A, B, C, color=BLUE, fill_opacity=0.1)
        
        # Heights
        # Height from A to BC (h_a)
        # BC is on x-axis (before rotation/shift).
        # Wait, after shift, BC is not horizontal.
        # Let's re-calculate projection.
        
        # Projection of A onto BC
        # Vector CB = B - C
        # Vector CA = A - C
        # Proj = C + dot(CA, CB)/dot(CB, CB) * CB
        def get_projection(p, line_start, line_end):
            v = line_end - line_start
            w = p - line_start
            proj_scalar = np.dot(w, v) / np.dot(v, v)
            return line_start + proj_scalar * v
            
        H_a = get_projection(A, C, B)
        line_ha = DashedLine(A, H_a, color=RED)
        
        # Height from B to AC (h_b)
        H_b = get_projection(B, C, A)
        # Note: H_b might be outside segment AC if angle C is obtuse?
        # sin C = 3/4. C can be acute or obtuse.
        # If C is obtuse, cos C is negative.
        # Let's assume acute for standard drawing unless specified.
        # If C is acute, H_b is on ray CA.
        # Check if H_b is on segment AC.
        # Projection scalar = dot(CB, CA) / |CA|^2
        # = (a * b * cos C) / b^2 = a/b * cos C = 2 * cos C.
        # cos C = sqrt(7)/4 approx 0.66.
        # 2 * 0.66 = 1.32 > 1.
        # So H_b is outside segment AC.
        # We need to extend line AC.
        
        line_AC_ext = DashedLine(C, H_b, color=GRAY)
        line_hb = DashedLine(B, H_b, color=RED)
        
        # Labels
        lbl_A = Text("A", font_size=24, color=BLACK).next_to(A, UP, buff=0.1)
        lbl_B = Text("B", font_size=24, color=BLACK).next_to(B, RIGHT, buff=0.1)
        lbl_C = Text("C", font_size=24, color=BLACK).next_to(C, DL, buff=0.1)
        
        lbl_ha = MathTex("h_a=3", color=RED, font_size=20).next_to(line_ha, RIGHT, buff=0.1)
        lbl_hb = MathTex("h_b=6", color=RED, font_size=20).next_to(line_hb, UP, buff=0.1)
        
        lbl_a = MathTex("a", color=BLACK, font_size=20).next_to(Line(C, B), DOWN, buff=0.1)
        lbl_b = MathTex("b", color=BLACK, font_size=20).next_to(Line(C, A), LEFT, buff=0.1)
        
        # Right angles
        ra_ha = RightAngle(Line(H_a, A), Line(H_a, C), length=0.2, color=RED)
        ra_hb = RightAngle(Line(H_b, B), Line(H_b, C), length=0.2, color=RED)
        
        # Add to scene
        self.add(triangle)
        self.add(line_AC_ext)
        self.add(line_ha, line_hb)
        self.add(lbl_A, lbl_B, lbl_C)
        self.add(lbl_ha, lbl_hb)
        self.add(lbl_a, lbl_b)
        self.add(ra_ha, ra_hb)
        
        # Add text info
        info = VGroup(
            MathTex("a - b = 4", color=BLACK, font_size=24),
            MathTex("h_a = 3, h_b = 6", color=BLACK, font_size=24),
            MathTex("P = ?", color=RED, font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UL)
        self.add(info)
