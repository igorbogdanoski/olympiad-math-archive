from manim import *
import numpy as np

class Problem_geom_8_viviani_proof(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Parameters
        a = 5.0
        h = a * np.sqrt(3) / 2
        
        # Coordinates
        # A bottom-left, B bottom-right, C top
        A = np.array([-a/2, -h/3, 0.0])
        B = np.array([a/2, -h/3, 0.0])
        C = np.array([0.0, 2*h/3, 0.0])
        
        # Point S inside
        # Let's pick a point
        S = np.array([0.5, 0.0, 0.0])
        
        # Projections
        # M on AB (bottom)
        # N on BC (right)
        # P on CA (left)
        
        # M is easy: (S_x, -h/3)
        M = np.array([S[0], -h/3, 0.0])
        
        # For N and P, use projection function
        def get_projection(p, line_start, line_end):
            v = line_end - line_start
            w = p - line_start
            proj_scalar = np.dot(w, v) / np.dot(v, v)
            return line_start + proj_scalar * v
            
        N = get_projection(S, B, C)
        P = get_projection(S, C, A)
        
        # Center view
        center = (A + B + C) / 3
        shift = -center
        
        A += shift
        B += shift
        C += shift
        S += shift
        M += shift
        N += shift
        P += shift
        
        # Scale
        scale = 1.0
        A *= scale
        B *= scale
        C *= scale
        S *= scale
        M *= scale
        N *= scale
        P *= scale
        
        # Elements
        triangle = Polygon(A, B, C, color=BLUE, fill_opacity=0.1)
        
        line_SM = Line(S, M, color=RED)
        line_SN = Line(S, N, color=RED)
        line_SP = Line(S, P, color=RED)
        
        # Labels
        lbl_A = Text("A", font_size=24, color=BLACK).next_to(A, DL, buff=0.1)
        lbl_B = Text("B", font_size=24, color=BLACK).next_to(B, DR, buff=0.1)
        lbl_C = Text("C", font_size=24, color=BLACK).next_to(C, UP, buff=0.1)
        lbl_S = Text("S", font_size=24, color=BLACK).next_to(S, UP, buff=0.1)
        
        lbl_M = Text("M", font_size=24, color=BLACK).next_to(M, DOWN, buff=0.1)
        lbl_N = Text("N", font_size=24, color=BLACK).next_to(N, RIGHT, buff=0.1)
        lbl_P = Text("P", font_size=24, color=BLACK).next_to(P, LEFT, buff=0.1)
        
        # Right angles
        ra_M = RightAngle(Line(M, S), Line(M, B), length=0.2, color=RED)
        ra_N = RightAngle(Line(N, S), Line(N, C), length=0.2, color=RED)
        ra_P = RightAngle(Line(P, S), Line(P, A), length=0.2, color=RED)
        
        # Add to scene
        self.add(triangle)
        self.add(line_SM, line_SN, line_SP)
        self.add(lbl_A, lbl_B, lbl_C, lbl_S, lbl_M, lbl_N, lbl_P)
        self.add(ra_M, ra_N, ra_P)
        
        # Add text info
        info = VGroup(
            MathTex("\\triangle ABC \\text{ is equilateral}", color=BLACK, font_size=24),
            MathTex("SM \\perp AB, SN \\perp BC, SP \\perp CA", color=BLACK, font_size=24),
            MathTex("SM + SN + SP = h", color=RED, font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UL)
        self.add(info)
