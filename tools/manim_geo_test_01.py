from manim import *
import numpy as np

class Problem_geo_test_01(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Coordinates
        # C at origin? No, let D be at origin.
        D = np.array([0, 0, 0])
        
        # AD = 4, BD = 9.
        # Let AB be on x-axis.
        # A = (-4, 0), B = (9, 0).
        A = np.array([-4, 0, 0])
        B = np.array([9, 0, 0])
        
        # CD = sqrt(4*9) = 6.
        # C = (0, 6).
        C = np.array([0, 6, 0])
        
        # Center camera
        center = (A + B + C)/3
        self.camera.frame_center = center
        self.camera.frame_width = 16
        
        # Points
        points = {'A': A, 'B': B, 'C': C, 'D': D}
        
        # Triangle ABC
        tri = Polygon(A, B, C, color=BLUE, fill_opacity=0.1)
        
        # Altitude CD
        alt_CD = Line(C, D, color=RED)
        
        # Labels
        labels = VGroup()
        for name, point in points.items():
            direction = UP
            if name == 'A': direction = DOWN + LEFT
            if name == 'B': direction = DOWN + RIGHT
            if name == 'C': direction = UP
            if name == 'D': direction = DOWN
            
            labels.add(MathTex(name).next_to(point, direction))
            
        # Right angles
        # At C
        ra_C = RightAngle(Line(C, A), Line(C, B), length=0.5, color=BLACK)
        # At D
        ra_D = RightAngle(Line(D, C), Line(D, B), length=0.5, color=BLACK)
        
        # Length labels
        brace_AD = Brace(Line(A, D), DOWN)
        label_AD = brace_AD.get_text("4")
        
        brace_BD = Brace(Line(D, B), DOWN)
        label_BD = brace_BD.get_text("9")
        
        label_CD = MathTex("h = ?").next_to(alt_CD, RIGHT)
        
        # Draw
        self.play(Create(tri))
        self.play(Create(alt_CD))
        
        dots = VGroup(*[Dot(p) for p in points.values()])
        self.play(FadeIn(dots), FadeIn(labels))
        
        self.play(Create(ra_C), Create(ra_D))
        self.play(Create(brace_AD), Write(label_AD))
        self.play(Create(brace_BD), Write(label_BD))
        self.play(Write(label_CD))
        
        # Add text info
        info = MathTex(r"h^2 = p \cdot q", color=RED, font_size=36).to_corner(UL)
        self.add(info)
        
        self.wait(2)
