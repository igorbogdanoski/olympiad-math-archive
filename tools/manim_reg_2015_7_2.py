from manim import *

class IsoscelesTriangleScene(Scene):
    def construct(self):
        # Define triangle points
        A = np.array([-2, 0, 0])
        B = np.array([2, 0, 0])
        # Calculate C so that triangle is isosceles with base AB and top angle 108°
        base = B - A
        base_length = np.linalg.norm(base)
        # Height from base for 36°-36°-108° triangle
        height = base_length / (2 * np.tan(np.radians(36)))
        C = np.array([0, height, 0])

        # Triangle
        triangle = Polygon(A, B, C, color=BLUE)
        self.play(Create(triangle))

        # Midpoint D of AB
        D = (A + B) / 2
        # Height CD
        height_line = Line(C, D, color=YELLOW)
        self.play(Create(height_line))

        # Angle bisector AL
        # Find L on BC such that AL is angle bisector of angle at A
        # For isosceles triangle, AL is also median, so L is midpoint of BC
        L = (B + C) / 2
        bisector = Line(A, L, color=GREEN)
        self.play(Create(bisector))

        # Extend CD to E such that CE = 2*CD
        E = D + 2 * (C - D)
        ext_line = Line(C, E, color=RED, stroke_width=6)
        self.play(Create(ext_line))

        # Labels
        self.add(Dot(A), Dot(B), Dot(C), Dot(D), Dot(L), Dot(E))
        self.add(Text("A").next_to(A, DOWN),
                 Text("B").next_to(B, DOWN),
                 Text("C").next_to(C, UP),
                 Text("D").next_to(D, DOWN),
                 Text("L").next_to(L, RIGHT),
                 Text("E").next_to(E, UP))

        self.wait(2)
