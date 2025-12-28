from manim import *
import numpy as np

class Problem_geom_8_2018_rect(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Coordinates
        # Scale down
        s = 0.3
        AB = 18 * s
        BC = 12 * s
        
        A = np.array([-AB/2, -BC/2, 0])
        B = np.array([AB/2, -BC/2, 0])
        C = np.array([AB/2, BC/2, 0])
        D = np.array([-AB/2, BC/2, 0])
        
        # E on AB. AE = 1/3 AB.
        # Vector AB = (AB, 0).
        E = A + (B - A) / 3
        
        # F on BC. BF = 2/3 BC.
        # Vector BC = (0, BC).
        F = B + 2 * (C - B) / 3
        
        # G midpoint of AD.
        G = (A + D) / 2
        
        # Center camera
        self.camera.frame_center = (A + B + C + D)/4
        self.camera.frame_width = AB + 2
        
        # Points
        points = {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'G': G}
        
        # Rectangle
        rect = Polygon(A, B, C, D, color=BLUE, fill_opacity=0.1)
        
        # Triangle EFG
        tri_EFG = Polygon(E, F, G, color=RED, fill_opacity=0.3)
        
        # Labels
        labels = VGroup()
        for name, point in points.items():
            direction = UP
            if name == 'A': direction = DOWN + LEFT
            if name == 'B': direction = DOWN + RIGHT
            if name == 'C': direction = UP + RIGHT
            if name == 'D': direction = UP + LEFT
            if name == 'E': direction = DOWN
            if name == 'F': direction = RIGHT
            if name == 'G': direction = LEFT
            
            labels.add(MathTex(name).next_to(point, direction))
            
        # Draw
        self.play(Create(rect))
        self.play(Create(tri_EFG))
        
        dots = VGroup(*[Dot(p) for p in points.values()])
        self.play(FadeIn(dots), FadeIn(labels))
        
        # Add text info
        info = VGroup(
            MathTex("AB=18, BC=12", color=BLACK, font_size=24),
            MathTex("AE = AB/3", color=BLACK, font_size=24),
            MathTex("BF = 2BC/3", color=BLACK, font_size=24),
            MathTex("G = mid(AD)", color=BLACK, font_size=24),
            MathTex("Area(EFG) = ?", color=RED, font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UL)
        self.add(info)
        
        self.wait(2)
