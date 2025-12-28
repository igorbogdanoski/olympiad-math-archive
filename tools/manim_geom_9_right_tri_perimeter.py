from manim import *

class Problem_geom_9_right_tri_perimeter(Scene):
    def construct(self):
        # Sides
        a = 5
        b = 12
        c = 13
        
        # Scale
        scale = 0.5
        a_s = a * scale
        b_s = b * scale
        c_s = c * scale
        
        # Vertices
        C = ORIGIN
        A = RIGHT * b_s
        B = UP * a_s
        
        triangle = Polygon(C, A, B, color=BLUE, stroke_width=4)
        
        # Right angle
        right_angle = RightAngle(Line(C, A), Line(C, B), length=0.4, color=WHITE)
        
        # Incircle
        r = 2
        r_s = r * scale
        I = np.array([r_s, r_s, 0])
        incircle = Circle(radius=r_s, color=GREEN)
        incircle.move_to(I)
        
        # Labels
        label_P = MathTex("P = 30").to_corner(UL)
        label_r = MathTex("r = 2").next_to(label_P, DOWN, aligned_edge=LEFT)
        label_c = MathTex("c = ?").next_to(Line(A, B).get_center(), UR)
        
        # Side labels (optional, maybe just c)
        # label_a = MathTex("a").next_to(Line(C, B).get_center(), LEFT)
        # label_b = MathTex("b").next_to(Line(C, A).get_center(), DOWN)
        
        # Center everything
        VGroup(triangle, right_angle, incircle, label_c).move_to(ORIGIN)
        
        self.add(triangle, right_angle, incircle)
        self.add(label_P, label_r, label_c)
        
        # Show calculation result
        result = MathTex("c = 13").next_to(label_c, RIGHT, buff=0.5).set_color(YELLOW)
        self.add(result)
