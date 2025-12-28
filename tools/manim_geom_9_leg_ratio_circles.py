from manim import *

class Problem_geom_9_leg_ratio_circles(Scene):
    def construct(self):
        # Define the triangle sides
        a = 3
        b = 4
        c = 5
        
        # Scale for better visibility
        scale_factor = 1.5
        a *= scale_factor
        b *= scale_factor
        c *= scale_factor
        
        # Vertices
        # C at origin (right angle)
        C = ORIGIN
        A = RIGHT * b  # (4, 0) scaled
        B = UP * a     # (0, 3) scaled
        
        triangle = Polygon(A, B, C, color=BLUE, stroke_width=4)
        
        # Right angle marker
        right_angle = RightAngle(Line(C, A), Line(C, B), length=0.4, color=WHITE)
        
        # Incircle
        # Inradius r = (a+b-c)/2
        r = (a + b - c) / 2
        # Incenter I is at (r, r) because C is at origin and legs are along axes
        I = np.array([r, r, 0])
        incircle = Circle(radius=r, color=GREEN)
        incircle.move_to(I)
        
        # Circumcircle
        # Circumradius R = c/2
        R = c / 2
        # Circumcenter O is midpoint of hypotenuse AB
        O = (A + B) / 2
        circumcircle = Circle(radius=R, color=RED)
        circumcircle.move_to(O)
        
        # Labels
        label_C = MathTex("C").next_to(C, DL)
        label_A = MathTex("A").next_to(A, DR)
        label_B = MathTex("B").next_to(B, UL)
        
        # Radii lines
        # Radius of incircle
        radius_r_line = Line(I, [I[0], 0, 0], color=GREEN_E)
        label_r = MathTex("r").next_to(radius_r_line, LEFT, buff=0.1).scale(0.7)
        
        # Radius of circumcircle
        radius_R_line = Line(O, A, color=RED_E)
        label_R = MathTex("R").next_to(radius_R_line, UP, buff=0.1).scale(0.7)
        
        # Group everything
        VGroup(triangle, right_angle, incircle, circumcircle, 
               label_C, label_A, label_B, 
               radius_r_line, label_r, radius_R_line, label_R).move_to(ORIGIN)
        
        self.add(triangle, right_angle)
        self.add(incircle, circumcircle)
        self.add(label_C, label_A, label_B)
        self.add(radius_r_line, label_r)
        self.add(radius_R_line, label_R)
        
        # Add text for ratio
        text = MathTex(r"r : R = 2 : 5").to_edge(UP)
        self.add(text)
