from manim import *
import numpy as np

class Problem_sigma_adv_04(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Coordinates
        scale = 2.0
        A = np.array([-2, -1.5, 0]) * scale
        B = np.array([2, -1.5, 0]) * scale
        C = np.array([2, 1.5, 0]) * scale
        D = np.array([-2, 1.5, 0]) * scale
        
        # Point P on CD
        # Let's place it not in center to be general
        P = np.array([0.5, 1.5, 0]) * scale
        
        # Center camera
        self.camera.frame_center = (A + C)/2
        self.camera.frame_width = 10
        
        # Points
        points = {'A': A, 'B': B, 'C': C, 'D': D, 'P': P}
        
        # Rectangle
        rect = Polygon(A, B, C, D, color=BLUE, fill_opacity=0.1)
        
        # Triangle ABP
        tri = Polygon(A, B, P, color=RED, fill_opacity=0.3)
        
        # Labels
        labels = VGroup()
        for name, point in points.items():
            direction = UP
            if name == 'A': direction = DOWN + LEFT
            if name == 'B': direction = DOWN + RIGHT
            if name == 'C': direction = UP + RIGHT
            if name == 'D': direction = UP + LEFT
            if name == 'P': direction = UP
            
            labels.add(MathTex(name).next_to(point, direction))
            
        # Areas
        # Centroid of ABP
        G_tri = (A + B + P) / 3
        label_S = MathTex("S").move_to(G_tri)
        
        # Centroid of ADP
        G_1 = (A + D + P) / 3
        label_S1 = MathTex("S_1").move_to(G_1)
        
        # Centroid of BCP
        G_2 = (B + C + P) / 3
        label_S2 = MathTex("S_2").move_to(G_2)
        
        # Draw
        self.play(Create(rect))
        self.play(Create(tri))
        
        dots = VGroup(*[Dot(p) for p in points.values()])
        self.play(FadeIn(dots), FadeIn(labels))
        
        self.play(Write(label_S), Write(label_S1), Write(label_S2))
        
        # Add text info
        info = MathTex(r"S = S_1 + S_2 = \frac{1}{2} S_{ABCD}", color=RED, font_size=36).to_corner(UL)
        self.add(info)
        
        self.wait(2)
