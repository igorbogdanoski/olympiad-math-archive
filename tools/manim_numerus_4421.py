from manim import *
import numpy as np

class Problem_numerus_4421(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Parameters
        a = 2.0
        
        # Coordinates (relative to P at origin)
        P_raw = np.array([0.0, 0.0, 0.0])
        A_raw = np.array([a, 0.0, 0.0])
        B_raw = np.array([2*a, 0.0, 0.0])
        C_raw = np.array([3*a, 0.0, 0.0])
        M_raw = np.array([a, a, 0.0])
        
        # N calculation
        # N is intersection of MC and perp from B
        # MC: y = -0.5x + 1.5a
        # BN: y = 2x - 4a
        x_N = 2.2 * a
        y_N = 0.4 * a
        N_raw = np.array([x_N, y_N, 0.0])
        
        # Center view
        center = (P_raw + C_raw + M_raw) / 3
        shift = -center
        
        P = P_raw + shift
        A = A_raw + shift
        B = B_raw + shift
        C = C_raw + shift
        M = M_raw + shift
        N = N_raw + shift
        
        # Scale
        scale = 1.0
        P *= scale
        A *= scale
        B *= scale
        C *= scale
        M *= scale
        N *= scale
        
        # Elements
        line_PC = Line(P, C, color=BLACK)
        line_AM = Line(A, M, color=BLACK)
        line_MC = Line(M, C, color=BLUE)
        line_BN = Line(B, N, color=BLUE)
        line_PM = Line(P, M, color=RED)
        
        # Circle ABNM
        # Center is midpoint of MB
        center_circle = (M + B) / 2
        radius = np.linalg.norm(M - B) / 2
        circle = Circle(radius=radius, color=GREEN, fill_opacity=0.1).move_to(center_circle)
        
        # Labels
        lbl_P = Text("P", font_size=24, color=BLACK).next_to(P, DL, buff=0.1)
        lbl_A = Text("A", font_size=24, color=BLACK).next_to(A, DOWN, buff=0.1)
        lbl_B = Text("B", font_size=24, color=BLACK).next_to(B, DOWN, buff=0.1)
        lbl_C = Text("C", font_size=24, color=BLACK).next_to(C, DOWN, buff=0.1)
        lbl_M = Text("M", font_size=24, color=BLACK).next_to(M, UP, buff=0.1)
        lbl_N = Text("N", font_size=24, color=BLACK).next_to(N, UR, buff=0.1)
        
        # Right angles
        ra_A = RightAngle(Line(A, P), Line(A, M), length=0.3, color=BLACK)
        ra_N = RightAngle(Line(N, B), Line(N, C), length=0.3, color=BLACK) # BN perp MC
        
        # Equality marks
        # PA, AB, BC, MA
        def tick(p1, p2):
            return Line(p1, p2).get_center()
            
        t_PA = Text("|", font_size=16, color=BLACK).move_to(tick(P, A)).shift(DOWN*0.2)
        t_AB = Text("|", font_size=16, color=BLACK).move_to(tick(A, B)).shift(DOWN*0.2)
        t_BC = Text("|", font_size=16, color=BLACK).move_to(tick(B, C)).shift(DOWN*0.2)
        t_MA = Text("-", font_size=24, color=BLACK).move_to(tick(M, A)).rotate(90*DEGREES).shift(LEFT*0.2)
        
        # Add to scene
        self.add(circle)
        self.add(line_PC, line_AM, line_MC, line_BN, line_PM)
        self.add(lbl_P, lbl_A, lbl_B, lbl_C, lbl_M, lbl_N)
        self.add(ra_A, ra_N)
        self.add(t_PA, t_AB, t_BC, t_MA)
        
        # Add text info
        info = VGroup(
            MathTex("PA=AB=BC=MA", color=BLACK, font_size=24),
            MathTex("PM^2 = PA \\cdot PB", color=RED, font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UL)
        self.add(info)
