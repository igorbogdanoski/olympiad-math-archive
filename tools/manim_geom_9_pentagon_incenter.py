from manim import *

class Problem_geom_9_pentagon_incenter(Scene):
    def construct(self):
        # Create a regular pentagon just for visualization of the concept
        pentagon = RegularPolygon(n=5, color=BLUE).scale(2.5)
        
        # Vertices
        vertices = pentagon.get_vertices()
        A, B, C, D, E = vertices
        
        # Labels for vertices
        label_A = MathTex("A").next_to(A, UP)
        label_B = MathTex("B").next_to(B, RIGHT)
        label_C = MathTex("C").next_to(C, DR)
        label_D = MathTex("D").next_to(D, DL)
        label_E = MathTex("E").next_to(E, LEFT)
        
        # Side labels (values from problem)
        # AB=4, BC=6, CD=8, DE=7, EA=9
        # Note: The regular pentagon sides are equal, but we just label them with the problem values
        # to illustrate the setup.
        
        s1 = MathTex("4").next_to(Line(A, B).get_center(), UR, buff=0.2)
        s2 = MathTex("6").next_to(Line(B, C).get_center(), RIGHT, buff=0.2)
        s3 = MathTex("8").next_to(Line(C, D).get_center(), DOWN, buff=0.2)
        s4 = MathTex("7").next_to(Line(D, E).get_center(), LEFT, buff=0.2)
        s5 = MathTex("9").next_to(Line(E, A).get_center(), UL, buff=0.2)
        
        # Incircle (hypothetical)
        incircle = Circle(radius=1.8, color=YELLOW, stroke_opacity=0.7).move_to(pentagon.get_center())
        
        # Tangent points (approximate for visual)
        # We just want to show the concept of tangent lengths x1, x2...
        
        self.add(pentagon)
        self.add(label_A, label_B, label_C, label_D, label_E)
        self.add(s1, s2, s3, s4, s5)
        self.add(incircle)
        
        # Add equation text
        eq1 = MathTex(r"x_A + x_B = 4")
        eq2 = MathTex(r"x_B + x_C = 6")
        eq3 = MathTex(r"x_C + x_D = 8")
        eq4 = MathTex(r"x_D + x_E = 7")
        eq5 = MathTex(r"x_E + x_A = 9")
        
        equations = VGroup(eq1, eq2, eq3, eq4, eq5).arrange(DOWN, aligned_edge=LEFT).scale(0.8)
        equations.to_corner(UL)
        
        # Add solution text
        sol = MathTex(r"\Rightarrow x_B = 0").next_to(equations, DOWN, buff=0.5).set_color(RED)
        
        self.add(equations)
        self.add(sol)
