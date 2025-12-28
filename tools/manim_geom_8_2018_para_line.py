from manim import *
import numpy as np

class Problem_geom_8_2018_para_line(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Coordinates
        # D at origin
        D = np.array([0, 0, 0])
        
        # Line p is horizontal axis
        # But let's tilt it slightly to make it look general, or tilt the parallelogram.
        # Easier to keep line horizontal and tilt parallelogram.
        
        # Parallelogram ABCD
        # D at origin.
        # A = (2, 2)
        # C = (4, 1)
        # B = A + C - D = (6, 3)
        
        scale = 1.5
        A = np.array([-2, 2, 0]) * scale
        C = np.array([3, 1, 0]) * scale
        B = (A + C - D)
        
        # Shift everything so D is not at center, but line p is visible
        # Line p passes through D.
        # Let's make line p horizontal.
        
        # Projections
        # M is projection of A on p (y=0)
        M = np.array([A[0], 0, 0])
        # N is projection of B on p
        N = np.array([B[0], 0, 0])
        # O is projection of C on p
        O = np.array([C[0], 0, 0])
        
        # Center camera
        center = (A + B + C + D + M + N)/6
        self.camera.frame_center = center
        self.camera.frame_width = 14
        
        # Points
        points = {'A': A, 'B': B, 'C': C, 'D': D, 'M': M, 'N': N, 'O': O}
        
        # Parallelogram
        para = Polygon(A, B, C, D, color=BLUE, fill_opacity=0.1)
        
        # Line p
        line_p = Line(D + LEFT*5, D + RIGHT*8, color=BLACK)
        label_p = MathTex("p").next_to(line_p, RIGHT)
        
        # Perpendiculars
        perp_AM = DashedLine(A, M, color=RED)
        perp_BN = DashedLine(B, N, color=RED)
        perp_CO = DashedLine(C, O, color=RED)
        
        # Labels
        labels = VGroup()
        for name, point in points.items():
            direction = UP
            if name == 'D': direction = DOWN
            if name == 'M': direction = DOWN
            if name == 'N': direction = DOWN
            if name == 'O': direction = DOWN
            if name == 'A': direction = UP
            if name == 'B': direction = UP
            if name == 'C': direction = UP
            
            labels.add(MathTex(name).next_to(point, direction))
            
        # Right angles
        ra_M = RightAngle(Line(M, A), Line(M, D), length=0.3, color=BLACK)
        ra_N = RightAngle(Line(N, B), Line(N, D), length=0.3, color=BLACK)
        ra_O = RightAngle(Line(O, C), Line(O, D), length=0.3, color=BLACK)
        
        # Draw
        self.play(Create(line_p), Write(label_p))
        self.play(Create(para))
        self.play(Create(perp_AM), Create(perp_BN), Create(perp_CO))
        
        dots = VGroup(*[Dot(p) for p in points.values()])
        self.play(FadeIn(dots), FadeIn(labels))
        
        self.play(Create(ra_M), Create(ra_N), Create(ra_O))
        
        # Add text info
        info = MathTex("AM + OC = BN", color=RED, font_size=36).to_corner(UL)
        self.add(info)
        
        self.wait(2)
