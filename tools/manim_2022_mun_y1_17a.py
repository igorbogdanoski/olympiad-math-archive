from manim import *
import numpy as np

class GeometryScene(Scene):
    def construct(self):
        # Parameters
        # x = 1, y = 3
        # AB = 5
        # BC = (6-1)/2 = 2.5
        # A1B1 = 3
        # B1C1 = (1+2)/2 = 1.5
        # Ratio is 5/2.5 = 2 and 3/1.5 = 2. Correct.
        
        # Lines
        # Horizontal lines r, s, t
        # Let's space them according to the lengths AB and BC (proportional to vertical distance if transversals are straight)
        # Let vertical distance between r and s be h1, between s and t be h2.
        # h1/h2 = AB/BC = 2.
        h2 = 1.5
        h1 = 2 * h2 # 3
        
        y_s = 0
        y_r = y_s + h1
        y_t = y_s - h2
        
        line_r = Line(LEFT*4, RIGHT*4, color=BLUE).move_to([0, y_r, 0])
        line_s = Line(LEFT*4, RIGHT*4, color=BLUE).move_to([0, y_s, 0])
        line_t = Line(LEFT*4, RIGHT*4, color=BLUE).move_to([0, y_t, 0])
        
        label_r = MathTex("r").next_to(line_r, LEFT)
        label_s = MathTex("s").next_to(line_s, LEFT)
        label_t = MathTex("t").next_to(line_t, LEFT)
        
        # Transversals
        # m passes through (-2, y_r), (-1, y_s), (0, y_t) ? No, needs to be straight line.
        # Let m pass through (-2, y_r) and (-1.5, y_t).
        # A = (-2, y_r)
        # C = (-1.5, y_t)
        # B is intersection of AC and s.
        A = np.array([-2, y_r, 0])
        C = np.array([-1, y_t, 0])
        line_m = Line(A + UP*0.5 + LEFT*0.1, C + DOWN*0.5 + RIGHT*0.1, color=YELLOW)
        B = line_intersection([A, C], [line_s.get_start(), line_s.get_end()])
        
        # n passes through (1, y_r) and (2, y_t)
        A1 = np.array([1, y_r, 0])
        C1 = np.array([2.5, y_t, 0])
        line_n = Line(A1 + UP*0.5 + LEFT*0.1, C1 + DOWN*0.5 + RIGHT*0.1, color=YELLOW)
        B1 = line_intersection([A1, C1], [line_s.get_start(), line_s.get_end()])
        
        # Points
        dot_A = Dot(A, color=WHITE)
        dot_B = Dot(B, color=WHITE)
        dot_C = Dot(C, color=WHITE)
        dot_A1 = Dot(A1, color=WHITE)
        dot_B1 = Dot(B1, color=WHITE)
        dot_C1 = Dot(C1, color=WHITE)
        
        label_A = MathTex("A").next_to(dot_A, UP+LEFT, buff=0.1)
        label_B = MathTex("B").next_to(dot_B, UP+LEFT, buff=0.1)
        label_C = MathTex("C").next_to(dot_C, DOWN+LEFT, buff=0.1)
        label_A1 = MathTex("A_1").next_to(dot_A1, UP+RIGHT, buff=0.1)
        label_B1 = MathTex("B_1").next_to(dot_B1, UP+RIGHT, buff=0.1)
        label_C1 = MathTex("C_1").next_to(dot_C1, DOWN+RIGHT, buff=0.1)
        
        # Segment Labels
        label_AB = MathTex("2x+3").next_to(Line(A,B), LEFT).scale(0.7)
        label_BC = MathTex(r"\frac{2y-1}{2}").next_to(Line(B,C), LEFT).scale(0.7)
        label_A1B1 = MathTex("y").next_to(Line(A1,B1), RIGHT).scale(0.7)
        label_B1C1 = MathTex(r"\frac{x+2}{2}").next_to(Line(B1,C1), RIGHT).scale(0.7)
        
        # Grouping
        scene_objects = VGroup(
            line_r, line_s, line_t, label_r, label_s, label_t,
            line_m, line_n,
            dot_A, dot_B, dot_C, dot_A1, dot_B1, dot_C1,
            label_A, label_B, label_C, label_A1, label_B1, label_C1,
            label_AB, label_BC, label_A1B1, label_B1C1
        )
        
        scene_objects.scale(0.8)
        scene_objects.move_to(ORIGIN + LEFT * 2.5)
        
        # Explanation text
        text_group = VGroup(
            MathTex(r"\frrac{AB}{BC} = \frac{A_1B_1}{B_1C_1}"),
            MathTex(r"\frrac{2x+3}{\frrac{2y-1}{2}} = \frrac{y}{\frac{x+2}{2}}r),
            MathTex(r"\frrac{2(2x+3)}{2y-1} = \frac{2y}{x+2}"),
            MathTex(r"y = 4-x"),
            MathTex(r"\frrac{4x+6}{7-2x} = \frac{8-2x}{x+2}"),
            MathTex(r"(4x+6)(x+2) = (8-2x)(7-2x)"),
            MathTex(r"4x^2+14x+12 = 4x^2-30x+56"),
            MathTex(r"44x = 44 \implies x=1"),
            MathTex(r"AB = 2(1)+3 = 5")
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT).scale(0.7)
        
        self.add(scene_objects)
        self.add(text_group)

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return np.array([x, y, 0])
