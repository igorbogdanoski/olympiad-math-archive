from manim import *
import numpy as np

class GeometryScene(Scene):
    def construct(self):
        # Parameters
        # a = 4*sqrt(2) approx 5.65
        # r = 2*sqrt(2) approx 2.82
        r = 2.5 # Visual scale
        
        # Circle
        circle = Circle(radius=r, color=BLUE, fill_opacity=0.2, fill_color=BLUE)
        
        # Outer Square
        # Side length 2r
        outer_square = Square(side_length=2*r, color=WHITE)
        
        # Inner Square
        # Vertices at midpoints of outer square sides (which are circle touching points)
        # Rotated square
        inner_square = Square(side_length=r * np.sqrt(2), color=YELLOW)
        inner_square.rotate(45 * DEGREES)
        
        # Shade region (Circle minus Inner Square)
        # Manim doesn't support boolean operations on shapes easily for filling.
        # But we can just draw the circle filled, and put the square on top filled with black (or background color).
        # But we want to show the difference.
        # Let's fill the circle with BLUE (opacity 0.5) and the inner square with BLACK (opacity 1).
        # Then draw outlines.
        
        circle_filled = Circle(radius=r, color=BLUE, fill_opacity=0.5, fill_color=BLUE, stroke_width=0)
        inner_square_filled = Square(side_length=r * np.sqrt(2), color=BLACK, fill_opacity=1, fill_color=BLACK, stroke_width=0).rotate(45 * DEGREES)
        
        # Labels
        label_ABCD = MathTex("ABCD").next_to(outer_square, UP)
        label_A1 = MathTex("A_1").next_to(inner_square.get_vertices()[0], RIGHT)
        label_B1 = MathTex("B_1").next_to(inner_square.get_vertices()[1], UP)
        label_C1 = MathTex("C_1").next_to(inner_square.get_vertices()[2], LEFT)
        label_D1 = MathTex("D_1").next_to(inner_square.get_vertices()[3], DOWN)
        
        # Dimensions
        # Side of outer square
        brace_side = Brace(outer_square, LEFT)
        label_side = MathTex(r"4\sqrt{2}").next_to(brace_side, LEFT)
        
        # Grouping
        scene_objects = VGroup(
            outer_square,
            circle_filled, inner_square_filled,
            circle, inner_square, # Outlines
            label_ABCD, label_A1, label_B1, label_C1, label_D1,
            brace_side, label_side
        )
        
        scene_objects.scale(0.8)
        scene_objects.move_to(ORIGIN + LEFT * 2)
        
        # Explanation text
        text_group = VGroup(
            MathTex(r"a = 4\sqrt{2}"),
            MathTex(r"R = \frrac{a}{2} = 2\sqrt{2}"),
            MathTex(r"P_{cirrcle} = \pi R^2 = \pi (2\sqrt{2})^2 = 8\pi"),
            MathTex(r"\text{Inner Square Side } b:"),
            MathTex(r"b^2 = (a/2)^2 + (a/2)^2 = 8 + 8 = 16"),
            MathTex(r"b = 4"),
            MathTex(r"P_{inner} = b^2 = 16"),
            MathTex(r"P_{shaded} = P_{circle} - P_{innerr} = 8\pi - 16r),
            MathTex(r"x = -16, y = 8"),
            MathTex(r"|x+y| = |-16+8| = |-8| = 8")
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT).scale(0.8)
        
        self.add(scene_objects)
        self.add(text_group)
