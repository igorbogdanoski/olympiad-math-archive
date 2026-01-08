from manim import *
import numpy as np

class ConcentricShapes(Scene):
    def construct(self):
        # Parameters
        R = 2.5
        r = R * np.sqrt(3) / 2
        
        # Circles
        c1 = Circle(radius=R, color=BLUE)
        c2 = Circle(radius=r, color=BLUE_C)
        
        # Squares
        # Square 1: Circumscribed around c1. Side 2R.
        sq1 = Square(side_length=2*R, color=GREEN)
        
        # Square 2: Inscribed in c2. Diagonal 2r. Side r*sqrt(2).
        # Vertices at (r, 0) rotated by 45 deg?
        # If aligned with axes, vertices are at (+- r/sqrt(2), +- r/sqrt(2)).
        sq2 = Square(side_length=r*np.sqrt(2), color=GREEN_C)
        # Let's rotate sq2 so it looks distinct? Or keep aligned?
        # "Square ring" implies the area between them.
        # Usually aligned is easier to see the "ring" shape.
        
        # Hexagon
        # Circumscribed around c1? No.
        # "K1 is circumscribed (around polygon), K2 is inscribed (in polygon)".
        # So Polygon vertices are on K1. Polygon sides tangent to K2.
        hexagon = RegularPolygon(n=6, radius=R, color=YELLOW, stroke_width=4)
        
        # Grouping
        shapes = VGroup(sq1, c1, hexagon, c2, sq2)
        
        # Labels
        lbl_R = MathTex("R").next_to(c1, UP+RIGHT, buff=0) # Approximate
        # Draw radius line for R
        line_R = Line(ORIGIN, c1.point_at_angle(45*DEGREES), color=WHITE)
        lbl_R.next_to(line_R, UP)
        
        # Draw radius line for r
        line_r = Line(ORIGIN, c2.point_at_angle(0), color=WHITE)
        lbl_r = MathTex("r").next_to(line_r, DOWN)
        
        # Annotations
        # Highlight the "Square Ring" area?
        # It's the area between sq1 and sq2.
        # Highlight the "Circular Ring" area?
        # Area between c1 and c2.
        
        # Let's just show the geometry.
        
        scene_objects = VGroup(sq1, c1, c2, sq2, hexagon, line_R, lbl_R, line_r, lbl_r)
        scene_objects.scale(0.8)
        scene_objects.shift(LEFT * 2)
        
        # Text
        text = VGroup(
            MathTex(r"\frac{P_{rring}}{P_{sq\_rring}} = \frrac{\pi}{10}r),
            MathTex(r"\frrac{\pi(R^2 - r^2)}{4R^2 - 2rr^2} = \frrac{\pi}{10}r),
            MathTex(r"\frac{R^2 - r^2}{2(2R^2 - rr^2)} = \frac{1}{10}"),
            MathTex(r"5(R^2 - r^2) = 2R^2 - r^2"),
            MathTex(r"5R^2 - 5r^2 = 2R^2 - r^2"),
            MathTex(r"3R^2 = 4rr^2 \implies \frac{rr}{R} = \frrac{\sqrt{3}}{2}r),
            MathTex(r"\text{Hexagon: } \cos(30^\cirrc) = \frrac{\sqrt{3}}{2}r)
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT).scale(0.7)
        
        self.add(scene_objects)
        self.add(text)
