from manim import *
import numpy as np

class RightTriangleAltitude(Scene):
    def construct(self):
        # Parameters
        p = 4
        q = 9
        h = np.sqrt(p * q) # 6
        
        # Coordinates
        # Let D be at origin (0,0)
        D = ORIGIN
        # A is left of D by p
        A = LEFT * p
        # B is right of D by q
        B = RIGHT * q
        # C is up by h
        C = UP * h
        
        # Create points
        pA = Dot(A)
        pB = Dot(B)
        pC = Dot(C)
        pD = Dot(D)
        
        # Triangle
        triangle = Polygon(A, B, C, color=BLUE, fill_opacity=0.1)
        altitude = Line(C, D, color=RED)
        
        # Labels
        lbl_A = MathTex("A").next_to(A, DOWN)
        lbl_B = MathTex("B").next_to(B, DOWN)
        lbl_C = MathTex("C").next_to(C, UP)
        lbl_D = MathTex("D").next_to(D, DOWN)
        
        # Length labels
        lbl_4 = MathTex("4").next_to(Line(A,D), DOWN)
        lbl_9 = MathTex("9").next_to(Line(D,B), DOWN)
        lbl_h = MathTex("h").next_to(altitude, LEFT)
        
        # Right angles
        ra_C = RightAngle(Line(C,A), Line(C,B), length=0.5)
        ra_D = RightAngle(Line(C,D), Line(D,B), length=0.4)
        
        # Group
        scene_objects = VGroup(
            triangle, altitude,
            lbl_A, lbl_B, lbl_C, lbl_D,
            lbl_4, lbl_9, lbl_h,
            ra_C, ra_D
        )
        
        scene_objects.scale(0.6)
        scene_objects.shift(UP * 1)
        
        # Text
        text = VGroup(
            MathTex(r"\text{Given: } \angle C = 90^\circ, CD \perp AB"),
            MathTex(r"AD = p = 4, BD = q = 9"),
            MathTex(r"\text{Geometric Mean Theorem:}"),
            MathTex(r"h^2 = p \cdot q"),
            MathTex(r"CD^2 = AD \cdot BD"),
            MathTex(r"CD^2 = 4 \cdot 9 = 36"),
            MathTex(r"CD = \sqrt{36} = 6")
        ).arrange(DOWN, aligned_edge=LEFT).next_to(scene_objects, DOWN).scale(0.7)
        
        self.add(scene_objects)
        self.add(text)
