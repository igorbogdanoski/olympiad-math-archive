from manim import *
import numpy as np

class Problem_geom_9_incenter_intersect(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Coordinates
        # k2 center O at origin
        O = np.array([0, 0, 0])
        r2 = 2.5
        
        # k1 passes through O.
        # Let k1 center be O1.
        # k1 and k2 intersect at A and B.
        # O is on k1.
        # Let A and B be symmetric wrt x-axis.
        # Let O1 be on x-axis.
        # Distance OO1 = r1.
        # Intersection points A, B satisfy:
        # x^2 + y^2 = r2^2 (k2)
        # (x-d)^2 + y^2 = r1^2 (k1)
        # Since O is on k1, d = r1.
        # (x-r1)^2 + y^2 = r1^2
        # x^2 - 2xr1 + r1^2 + y^2 = r1^2
        # r2^2 - 2xr1 + r1^2 = r1^2
        # 2xr1 = r2^2 => x = r2^2 / (2r1)
        
        # Let r1 = r2 = 2.5 for simplicity? No, O is on k1.
        # Let r2 = 2.5.
        # Let r1 = 2.0.
        r1 = 2.0
        O1 = np.array([-r1, 0, 0]) # O is at origin, O1 at -r1.
        # Wait, O is on k1. So distance(O, O1) = r1.
        # If O1 is at (-r1, 0), then O(0,0) is on k1. Correct.
        
        # Intersection A and B
        # x = r2^2 / (2r1) ? No.
        # k2: x^2 + y^2 = r2^2
        # k1: (x+r1)^2 + y^2 = r1^2
        # x^2 + 2xr1 + r1^2 + y^2 = r1^2
        # r2^2 + 2xr1 = 0 => x = -r2^2 / (2r1)
        
        x_int = - (r2**2) / (2*r1)
        # Check if valid
        # r2 = 2.5, r1 = 2.0 => x = -6.25 / 4 = -1.5625.
        # |x| < r2 (2.5) and |x+r1| < r1?
        # x+r1 = -1.56 + 2 = 0.44. Valid.
        
        y_int = np.sqrt(r2**2 - x_int**2)
        A = np.array([x_int, y_int, 0])
        B = np.array([x_int, -y_int, 0])
        
        # C on arc AB of k1 not containing O.
        # O is at (0,0). O1 is at (-2,0).
        # Arc AB containing O is the "right" arc.
        # Arc AB not containing O is the "left" arc.
        # C should be on the left side.
        # Angle of C wrt O1.
        # A angle: atan2(y, x+r1).
        # Let's pick C at angle 180 (far left).
        C = O1 + np.array([-r1, 0, 0]) # (-4, 0)
        
        # Line OC intersects k2 at D.
        # O is origin. C is (-4, 0).
        # Line OC is x-axis (negative).
        # Intersects k2 at (-r2, 0).
        D = np.array([-r2, 0, 0])
        
        # Center camera
        center = (O + O1)/2
        self.camera.frame_center = center
        self.camera.frame_width = 10
        
        # Points
        points = {'A': A, 'B': B, 'C': C, 'D': D, 'O': O}
        
        # Circles
        circle_k2 = Circle(radius=r2, color=BLUE).move_to(O)
        circle_k1 = Circle(radius=r1, color=GREEN).move_to(O1)
        
        # Triangle ABC
        tri_ABC = Polygon(A, B, C, color=ORANGE, fill_opacity=0.1)
        
        # Line OC
        line_OC = Line(O, C, color=RED)
        
        # Incenter D check
        # D is incenter of ABC?
        # Bisector of C passes through D? Yes, by symmetry C and D are on x-axis, A and B symmetric.
        # Bisector of A passes through D?
        # Angle CAD = Angle DAB?
        
        # Labels
        labels = VGroup()
        for name, point in points.items():
            direction = UP
            if name == 'O': direction = RIGHT
            if name == 'C': direction = LEFT
            if name == 'D': direction = DOWN + RIGHT
            if name == 'A': direction = UP
            if name == 'B': direction = DOWN
            
            labels.add(MathTex(name).next_to(point, direction))
            
        label_k1 = MathTex("k_1").next_to(circle_k1, UP + LEFT)
        label_k2 = MathTex("k_2").next_to(circle_k2, UP + RIGHT)
        
        # Draw
        self.play(Create(circle_k1), Write(label_k1))
        self.play(Create(circle_k2), Write(label_k2))
        
        dots = VGroup(*[Dot(p) for p in points.values()])
        self.play(FadeIn(dots), FadeIn(labels))
        
        self.play(Create(tri_ABC))
        self.play(Create(line_OC))
        
        # Highlight D
        self.play(Indicate(dots[3])) # D
        
        # Add text info
        info = MathTex(r"D = I_{ABC}", color=RED, font_size=36).to_corner(UL)
        self.add(info)
        
        self.wait(2)
