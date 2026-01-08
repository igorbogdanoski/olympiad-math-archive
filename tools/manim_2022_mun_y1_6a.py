from manim import *

class CollinearSquares(Scene):
    def construct(self):
        # Parameters
        s1 = 9.0
        s2 = 6.0
        s3 = 4.0
        
        # Scaling factor to fit on screen
        # Total width = 9 + 6 + 4 = 19.
        # Screen width is usually 14.
        scale_factor = 0.6
        
        # Positions
        # Start from left
        start_x = - (s1 + s2 + s3) * scale_factor / 2
        start_y = -2
        
        # Square 1
        sq1 = Square(side_length=s1 * scale_factor, color=BLUE, fill_opacity=0.2)
        sq1.set_stroke(width=2)
        # Position: bottom-left at (start_x, start_y)
        # Square center is at (start_x + s1/2, start_y + s1/2)
        sq1.move_to([start_x + s1*scale_factor/2, start_y + s1*scale_factor/2, 0])
        
        # Square 2
        sq2 = Square(side_length=s2 * scale_factor, color=GREEN, fill_opacity=0.2)
        sq2.set_stroke(width=2)
        sq2.move_to([start_x + s1*scale_factor + s2*scale_factor/2, start_y + s2*scale_factor/2, 0])
        
        # Square 3
        sq3 = Square(side_length=s3 * scale_factor, color=RED, fill_opacity=0.2)
        sq3.set_stroke(width=2)
        sq3.move_to([start_x + (s1+s2)*scale_factor + s3*scale_factor/2, start_y + s3*scale_factor/2, 0])
        
        # Top-left corners
        # Sq1 top-left: x = start_x, y = start_y + s1*scale
        p1 = np.array([start_x, start_y + s1*scale_factor, 0])
        # Sq2 top-left: x = start_x + s1*scale, y = start_y + s2*scale
        p2 = np.array([start_x + s1*scale_factor, start_y + s2*scale_factor, 0])
        # Sq3 top-left: x = start_x + (s1+s2)*scale, y = start_y + s3*scale
        p3 = np.array([start_x + (s1+s2)*scale_factor, start_y + s3*scale_factor, 0])
        
        # Line through corners
        line = Line(p1 + LEFT*1, p3 + RIGHT*1, color=YELLOW, stroke_width=3)
        
        # Labels
        label_x = MathTex("x").next_to(sq1, LEFT)
        label_6 = MathTex("6").next_to(sq2, DOWN)
        label_4 = MathTex("4").next_to(sq3, DOWN)
        
        # Points labels
        lbl_X = MathTex("X").next_to(p1, UP)
        lbl_Y = MathTex("Y").next_to(p2, UP)
        lbl_Z = MathTex("Z").next_to(p3, UP)
        
        # Similarity triangles
        # Triangle 1: under X-Y segment.
        # Vertices: X(p1), Y(p2), and corner (p2.x, p1.y)? No.
        # Slope is negative.
        # Draw horizontal from X to right, vertical from Y up? No, Y is lower.
        # Draw horizontal from X to right? No.
        # Draw horizontal from Y to left?
        # Let's draw "slope triangles" below the line.
        # Triangle 1: From X to (p2.x, p1.y)? No, p2 is lower.
        # Horizontal leg from X: (p1.x, p1.y) to (p2.x, p1.y). Length s1.
        # Vertical leg from there to Y: (p2.x, p1.y) to (p2.x, p2.y). Length s1-s2.
        
        corner1 = np.array([p2[0], p1[1], 0])
        tri1_h = Line(p1, corner1, color=WHITE, stroke_width=2, stroke_opacity=0.5)
        tri1_v = Line(corner1, p2, color=WHITE, stroke_width=2, stroke_opacity=0.5)
        
        corner2 = np.array([p3[0], p2[1], 0])
        tri2_h = Line(p2, corner2, color=WHITE, stroke_width=2, stroke_opacity=0.5)
        tri2_v = Line(corner2, p3, color=WHITE, stroke_width=2, stroke_opacity=0.5)
        
        # Labels for triangle legs
        lbl_dx1 = MathTex("x").next_to(tri1_h, UP, buff=0.1).scale(0.7)
        lbl_dy1 = MathTex("x-6").next_to(tri1_v, RIGHT, buff=0.1).scale(0.7)
        
        lbl_dx2 = MathTex("6").next_to(tri2_h, UP, buff=0.1).scale(0.7)
        lbl_dy2 = MathTex("6-4=2").next_to(tri2_v, RIGHT, buff=0.1).scale(0.7)
        
        # Group
        scene_objects = VGroup(
            sq1, sq2, sq3,
            line,
            label_x, label_6, label_4,
            lbl_X, lbl_Y, lbl_Z,
            tri1_h, tri1_v,
            tri2_h, tri2_v,
            lbl_dx1, lbl_dy1, lbl_dx2, lbl_dy2
        )
        
        # Explanation
        text = VGroup(
            MathTex(r"\text{Slope } m = \frac{y_2 - y_1}{x_2 - x_1}"),
            MathTex(r"\frrac{6 - x}{x} = \frac{4 - 6}{6}"),
            MathTex(r"\frrac{6 - x}{x} = \frac{-2}{6} = -\frac{1}{3}"),
            MathTex(r"3(6 - x) = -x"),
            MathTex(r"18 - 3x = -x"),
            MathTex(r"18 = 2x \implies x = 9")
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT).scale(0.8)
        
        # Shift scene to left to make space for text
        scene_objects.shift(LEFT * 2)
        
        self.add(scene_objects)
        self.add(text)
