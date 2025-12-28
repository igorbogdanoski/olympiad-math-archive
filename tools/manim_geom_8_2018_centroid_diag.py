from manim import *
import numpy as np

class Problem_geom_8_2018_centroid_diag(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Coordinates
        scale = 2.5
        A = np.array([-2, -1, 0]) * scale
        B = np.array([1, -1, 0]) * scale
        D = np.array([-1, 1, 0]) * scale
        C = B + D - A # Parallelogram
        
        # Midpoints
        M = (B + C) / 2
        N = (C + D) / 2
        
        # Intersection of DM and BN
        # DM line: P = D + t(M-D)
        # BN line: P = B + u(N-B)
        # This is the centroid of BCD.
        G = (B + C + D) / 3
        
        # Center camera
        self.camera.frame_center = (A + C)/2
        self.camera.frame_width = 12
        
        # Points
        points = {'A': A, 'B': B, 'C': C, 'D': D, 'M': M, 'N': N, 'G': G}
        
        # Parallelogram
        para = Polygon(A, B, C, D, color=BLUE, fill_opacity=0.1)
        
        # Diagonal AC
        diag_AC = Line(A, C, color=GRAY)
        
        # Lines DM and BN
        line_DM = Line(D, M, color=RED)
        line_BN = Line(B, N, color=RED)
        
        # Labels
        labels = VGroup()
        for name, point in points.items():
            direction = UP
            if name == 'A': direction = DOWN + LEFT
            if name == 'B': direction = DOWN + RIGHT
            if name == 'C': direction = UP + RIGHT
            if name == 'D': direction = UP + LEFT
            if name == 'M': direction = RIGHT
            if name == 'N': direction = UP
            if name == 'G': direction = DOWN
            
            labels.add(MathTex(name).next_to(point, direction))
            
        # Equality marks
        # BM = MC
        tick_BM = Line(B, M).get_center()
        tick_MC = Line(M, C).get_center()
        t_BM = Text("|", font_size=16, color=BLACK).move_to(tick_BM)
        t_MC = Text("|", font_size=16, color=BLACK).move_to(tick_MC)
        
        # CN = ND
        tick_CN = Line(C, N).get_center()
        tick_ND = Line(N, D).get_center()
        t_CN = Text("||", font_size=12, color=BLACK).move_to(tick_CN).rotate(90*DEGREES)
        t_ND = Text("||", font_size=12, color=BLACK).move_to(tick_ND).rotate(90*DEGREES)
        
        # Draw
        self.play(Create(para))
        self.play(Create(diag_AC))
        self.play(Create(line_DM), Create(line_BN))
        
        dots = VGroup(*[Dot(p) for p in points.values()])
        self.play(FadeIn(dots), FadeIn(labels))
        
        self.play(Create(t_BM), Create(t_MC), Create(t_CN), Create(t_ND))
        
        # Highlight G on AC
        dot_G = Dot(G, color=RED)
        self.play(Indicate(dot_G))
        
        # Add text info
        info = MathTex(r"G \in AC", color=RED, font_size=36).to_corner(UL)
        self.add(info)
        
        self.wait(2)
