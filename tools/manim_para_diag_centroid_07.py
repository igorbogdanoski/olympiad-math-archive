from manim import *
import numpy as np

class Problem_para_diag_centroid_07(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Parameters
        a = 4.0
        b = 2.5
        angle = 60 * DEGREES
        
        # Coordinates
        A = np.array([0.0, 0.0, 0.0])
        B = np.array([a, 0.0, 0.0])
        D = np.array([b * np.cos(angle), b * np.sin(angle), 0.0])
        C = B + D
        
        # Midpoints
        M = (B + C) / 2 # Midpoint of BC
        N = (C + D) / 2 # Midpoint of CD
        
        # Intersection of DM and BN
        # Line DM: D to M
        # Line BN: B to N
        # Let's calculate intersection P
        # P is centroid of triangle BCD?
        # In triangle BCD:
        # DM is median to BC? No, M is midpoint of BC. So DM is median from D.
        # BN is median to CD? No, N is midpoint of CD. So BN is median from B.
        # So P is centroid of triangle BCD.
        # Centroid lies on median from C to BD.
        # Median from C to BD passes through midpoint of BD.
        # Midpoint of BD is same as midpoint of AC (diagonals bisect).
        # So P lies on AC.
        
        P = (B + C + D) / 3
        
        # Center view
        center = (A + C) / 2
        shift = -center
        
        A += shift
        B += shift
        C += shift
        D += shift
        M += shift
        N += shift
        P += shift
        
        # Scale
        scale = 1.0
        A *= scale
        B *= scale
        C *= scale
        D *= scale
        M *= scale
        N *= scale
        P *= scale
        
        # Elements
        parallelogram = Polygon(A, B, C, D, color=BLUE, fill_opacity=0.1)
        diag_AC = Line(A, C, color=BLACK)
        diag_BD = DashedLine(B, D, color=GRAY)
        
        line_DM = Line(D, M, color=RED)
        line_BN = Line(B, N, color=RED)
        
        # Labels
        lbl_A = Text("A", font_size=24, color=BLACK).next_to(A, DL, buff=0.1)
        lbl_B = Text("B", font_size=24, color=BLACK).next_to(B, DR, buff=0.1)
        lbl_C = Text("C", font_size=24, color=BLACK).next_to(C, UR, buff=0.1)
        lbl_D = Text("D", font_size=24, color=BLACK).next_to(D, UL, buff=0.1)
        lbl_M = Text("M", font_size=24, color=BLACK).next_to(M, RIGHT, buff=0.1)
        lbl_N = Text("N", font_size=24, color=BLACK).next_to(N, UP, buff=0.1)
        lbl_P = Text("P", font_size=24, color=BLACK).next_to(P, UP, buff=0.1)
        
        # Mark midpoints
        # BM = MC
        tick_BM = Line(B, M).get_center()
        tick_MC = Line(M, C).get_center()
        t_BM = Text("|", font_size=16, color=BLACK).move_to(tick_BM).shift(RIGHT*0.1)
        t_MC = Text("|", font_size=16, color=BLACK).move_to(tick_MC).shift(RIGHT*0.1)
        
        # CN = ND
        tick_CN = Line(C, N).get_center()
        tick_ND = Line(N, D).get_center()
        t_CN = Text("||", font_size=16, color=BLACK).move_to(tick_CN).shift(UP*0.1)
        t_ND = Text("||", font_size=16, color=BLACK).move_to(tick_ND).shift(UP*0.1)
        
        # Add to scene
        self.add(parallelogram)
        self.add(diag_AC, diag_BD)
        self.add(line_DM, line_BN)
        self.add(lbl_A, lbl_B, lbl_C, lbl_D, lbl_M, lbl_N, lbl_P)
        self.add(t_BM, t_MC, t_CN, t_ND)
        
        # Add text info
        info = VGroup(
            MathTex(r"M \\in BC, BM=MC", color=BLACK, font_size=24),
            MathTex(r"N \\in CD, CN=ND", color=BLACK, font_size=24),
            MathTex(r"DM \\cap BN = P \\in AC", color=RED, font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UL)
        self.add(info)
