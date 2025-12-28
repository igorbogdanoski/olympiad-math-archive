from manim import *
import numpy as np

class SquareEquilateralTriangle(Scene):
    def construct(self):
        # Parameters
        side = 6
        
        # Coordinates
        # A bottom-left, B bottom-right
        A = LEFT * side / 2 + DOWN * side / 2
        B = RIGHT * side / 2 + DOWN * side / 2
        C = RIGHT * side / 2 + UP * side / 2
        D = LEFT * side / 2 + UP * side / 2
        
        # E is vertex of equilateral triangle ABE inside square
        # Height of equilateral triangle = side * sqrt(3) / 2
        h = side * np.sqrt(3) / 2
        E = (A + B) / 2 + UP * h
        
        # Create points
        pA = Dot(A)
        pB = Dot(B)
        pC = Dot(C)
        pD = Dot(D)
        pE = Dot(E)
        
        # Shapes
        square = Polygon(A, B, C, D, color=BLUE, fill_opacity=0.1)
        triangle_ABE = Polygon(A, B, E, color=GREEN, fill_opacity=0.1)
        triangle_DEC = Polygon(D, E, C, color=RED, fill_opacity=0.1)
        
        # Lines connecting E to D and C
        line_ED = Line(E, D, color=RED)
        line_EC = Line(E, C, color=RED)
        
        # Labels
        lbl_A = MathTex("A").next_to(A, DOWN+LEFT)
        lbl_B = MathTex("B").next_to(B, DOWN+RIGHT)
        lbl_C = MathTex("C").next_to(C, UP+RIGHT)
        lbl_D = MathTex("D").next_to(D, UP+LEFT)
        lbl_E = MathTex("E").next_to(E, DOWN)
        
        # Angles
        # Angle DEC
        angle_DEC = Angle(Line(E,C), Line(E,D), radius=0.5, color=YELLOW)
        lbl_DEC = MathTex("?").next_to(angle_DEC, UP)
        
        # Angle DAE = 30
        angle_DAE = Angle(Line(A,E), Line(A,D), radius=0.8, color=WHITE)
        lbl_30 = MathTex("30^\circ").next_to(angle_DAE, UP+RIGHT).scale(0.7)
        
        # Angle AEB = 60
        angle_AEB = Angle(Line(A,B), Line(A,E), radius=0.6, color=WHITE)
        # This is actually angle EAB.
        # Let's mark angle EAB = 60
        angle_EAB = Angle(Line(A,B), Line(A,E), radius=0.6, color=WHITE)
        lbl_60 = MathTex("60^\circ").next_to(angle_EAB, UP+RIGHT).scale(0.7)
        
        # Group
        scene_objects = VGroup(
            square, triangle_ABE, triangle_DEC,
            lbl_A, lbl_B, lbl_C, lbl_D, lbl_E,
            angle_DEC, lbl_DEC,
            angle_DAE, lbl_30,
            angle_EAB, lbl_60
        )
        
        scene_objects.scale(0.7)
        scene_objects.shift(LEFT * 2)
        
        # Text
        text = VGroup(
            MathTex(r"\triangle ABE \text{ is equilateral} \implies AB=AE=BE, \angle A = 60^\circ"),
            MathTex(r"ABCD \text{ is square} \implies AB=AD, \angle DAB = 90^\circ"),
            MathTex(r"\implies AE = AD \text{ (} \triangle ADE \text{ is isosceles)}"),
            MathTex(r"\angle DAE = 90^\circ - 60^\circ = 30^\circ"),
            MathTex(r"\angle ADE = \angle AED = \frac{180^\circ - 30^\circ}{2} = 75^\circ"),
            MathTex(r"\text{Similarly, } \angle BEC = 75^\circ"),
            MathTex(r"\angle DEC = 360^\circ - (60^\circ + 75^\circ + 75^\circ)"),
            MathTex(r"= 360^\circ - 210^\circ = 150^\circ")
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT).scale(0.65)
        
        self.add(scene_objects)
        self.add(text)
