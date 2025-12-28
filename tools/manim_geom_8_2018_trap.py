from manim import *
import numpy as np

class Problem_geom_8_2018_trap(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Coordinates
        # M at origin
        M = np.array([0, 0, 0])
        
        # Parameters
        a = 6.0
        b = 2.0
        h = (a - b) / 2 # = 2.0
        
        A = np.array([-a/2, 0, 0])
        B = np.array([a/2, 0, 0])
        
        N = np.array([0, h, 0])
        D = np.array([-b/2, h, 0])
        C = np.array([b/2, h, 0])
        
        # Center camera
        center = (A + B + C + D)/4
        self.camera.frame_center = center
        self.camera.frame_width = a + 2
        
        # Points
        points = {'A': A, 'B': B, 'C': C, 'D': D, 'M': M, 'N': N}
        
        # Trapezoid
        trap = Polygon(A, B, C, D, color=BLUE, fill_opacity=0.1)
        
        # Line MN
        line_MN = Line(M, N, color=RED)
        
        # Labels
        labels = VGroup()
        for name, point in points.items():
            direction = UP
            if name == 'A': direction = DOWN + LEFT
            if name == 'B': direction = DOWN + RIGHT
            if name == 'C': direction = UP + RIGHT
            if name == 'D': direction = UP + LEFT
            if name == 'M': direction = DOWN
            if name == 'N': direction = UP
            
            labels.add(MathTex(name).next_to(point, direction))
            
        # Equality marks
        # AM = MB
        tick_AM = Line(A, M).get_center()
        tick_MB = Line(M, B).get_center()
        t_AM = Text("|", font_size=16, color=BLACK).move_to(tick_AM)
        t_MB = Text("|", font_size=16, color=BLACK).move_to(tick_MB)
        
        # DN = NC
        tick_DN = Line(D, N).get_center()
        tick_NC = Line(N, C).get_center()
        t_DN = Text("||", font_size=12, color=BLACK).move_to(tick_DN)
        t_NC = Text("||", font_size=12, color=BLACK).move_to(tick_NC)
        
        # Angles
        angle_A = Angle(Line(A, B), Line(A, D), radius=0.8, color=GREEN)
        label_A = MathTex(r"\alpha").next_to(angle_A, UP + RIGHT)
        
        angle_B = Angle(Line(B, C), Line(B, A), radius=0.8, color=GREEN)
        label_B = MathTex(r"\beta").next_to(angle_B, UP + LEFT)
        
        # Draw
        self.play(Create(trap))
        self.play(Create(line_MN))
        
        dots = VGroup(*[Dot(p) for p in points.values()])
        self.play(FadeIn(dots), FadeIn(labels))
        
        self.play(Create(t_AM), Create(t_MB), Create(t_DN), Create(t_NC))
        self.play(Create(angle_A), Write(label_A))
        self.play(Create(angle_B), Write(label_B))
        
        # Add text info
        info = VGroup(
            MathTex(r"MN = \frac{a-b}{2}", color=RED, font_size=24),
            MathTex(r"\alpha + \beta = 90^\circ", color=GREEN, font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UL)
        self.add(info)
        
        self.wait(2)
