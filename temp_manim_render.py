from manim import *


class IsoscelesTriangleScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        # Define triangle points
        base_half = 2
        height = 3.3
        A = np.array([-base_half, 0, 0])
        B = np.array([base_half, 0, 0])
        C = np.array([0, height, 0])
        D = (A + B) / 2  # Midpoint of AB
        E = D + 2 * (C - D)  # Extension of CD

        # Draw triangle
        triangle = Polygon(A, B, C, color=BLUE)
        self.add(triangle)

        # Draw height CD
        height_line = Line(C, D, color=YELLOW)
        self.add(height_line)

        # Draw angle bisector AL (L is midpoint of BC)
        L = (B + C) / 2
        bisector = Line(A, L, color=GREEN)
        self.add(bisector)

        # Draw extension CE
        ext_line = Line(C, E, color=RED, stroke_width=6)
        self.add(ext_line)

        # Draw points
        self.add(Dot(A), Dot(B), Dot(C), Dot(D), Dot(L), Dot(E))
        self.add(Text("A").next_to(A, DOWN),
                 Text("B").next_to(B, DOWN),
                 Text("C").next_to(C, UP),
                 Text("D").next_to(D, DOWN),
                 Text("L").next_to(L, RIGHT),
                 Text("E").next_to(E, UP))

        self.wait(2)