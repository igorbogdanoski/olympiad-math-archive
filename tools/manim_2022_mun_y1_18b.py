from manim import *
import numpy as np

class GeometryScene(Scene):
    def construct(self):
        # Parameters
        side = 4 # Visual scale for 17
        scale = side / 17
        
        # Coordinates
        A = ORIGIN
        B = RIGHT * side
        C = RIGHT * side + UP * side
        D = UP * side
        
        # Rhombus
        # Height is 15. Scaled height = 15 * scale
        h_scaled = 15 * scale
        # N x-coord is 8. Scaled = 8 * scale
        n_x_scaled = 8 * scale
        
        N = np.array([n_x_scaled, h_scaled, 0])
        M = N + RIGHT * side
        
        # Polygons
        square = Polygon(A, B, C, D, color=WHITE, stroke_width=2)
        rhombus = Polygon(A, B, M, N, color=BLUE, stroke_width=2, fill_opacity=0.3, fill_color=BLUE)
        
        # Gray Area (Square minus Rhombus)
        # Part 1: Top rectangle
        # Vertices: (0, 15), (17, 15), (17, 17), (0, 17)
        P1 = np.array([0, h_scaled, 0])
        P2 = np.array([side, h_scaled, 0])
        gray_rect = Polygon(P1, P2, C, D, color=GRAY, fill_opacity=0.5, fill_color=GRAY, stroke_width=0)
        
        # Part 2: Left triangle
        # Vertices: A(0,0), N(8,15), P1(0,15)
        gray_tri = Polygon(A, N, P1, color=GRAY, fill_opacity=0.5, fill_color=GRAY, stroke_width=0)
        
        # Labels
        label_A = MathTex("A").next_to(A, DOWN+LEFT)
        label_B = MathTex("B").next_to(B, DOWN+RIGHT)
        label_C = MathTex("C").next_to(C, UP+RIGHT)
        label_D = MathTex("D").next_to(D, UP+LEFT)
        
        label_N = MathTex("N").next_to(N, UP+LEFT)
        label_M = MathTex("M").next_to(M, UP+RIGHT)
        
        # Dimensions
        brace_side = Brace(square, LEFT)
        label_17 = brace_side.get_text("17")
        
        # Height line
        height_line = DashedLine(N, np.array([n_x_scaled, 0, 0]), color=YELLOW)
        label_h = MathTex("15").next_to(height_line, RIGHT)
        
        # Projection of N on AB
        N_proj = np.array([n_x_scaled, 0, 0])
        brace_proj = Brace(Line(A, N_proj), DOWN)
        label_8 = brace_proj.get_text("8")
        
        # Grouping
        scene_objects = VGroup(
            gray_rect, gray_tri,
            square, rhombus,
            label_A, label_B, label_C, label_D, label_N, label_M,
            brace_side, label_17,
            height_line, label_h,
            brace_proj, label_8
        )
        
        scene_objects.scale(0.8)
        scene_objects.move_to(ORIGIN + LEFT * 2)
        
        # Explanation text
        text_group = VGroup(
            MathTex(r"P_{square} = 289 \implies a = 17"),
            MathTex(r"P_{rhombus} = 255 \implies a \cdot h = 255"),
            MathTex(r"17 \cdot h = 255 \implies h = 15"),
            MathTex(r"AN^2 = h^2 + x^2 \implies 17^2 = 15^2 + x^2"),
            MathTex(r"289 = 225 + x^2 \implies x^2 = 64 \implies x = 8"),
            MathTex(r"P_{gray} = P_{rect} + P_{tri}"),
            MathTex(r"P_{rect} = 17 \cdot (17-15) = 17 \cdot 2 = 34"),
            MathTex(r"P_{tri} = \frac{1}{2} \cdot 8 \cdot 15 = 60"),
            MathTex(r"P_{total} = 34 + 60 = 94")
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT).scale(0.8)
        
        self.add(scene_objects)
        self.add(text_group)
