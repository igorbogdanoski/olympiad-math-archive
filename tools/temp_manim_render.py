from manim import *
import numpy as np

class SolutionScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        A = np.array([-1.0, 2.0, 0])
        B = np.array([-2.5, -1.0, 0])
        C = np.array([2.0, -1.0, 0])
        D = B + 1.5 * (B - C)
        v_ab = B - A
        v_ac = C - A
        dir_a = (v_ab / np.linalg.norm(v_ab)) + (v_ac / np.linalg.norm(v_ac))
        v_ba = A - B
        v_bd = D - B
        dir_b = (v_ba / np.linalg.norm(v_ba)) + (v_bd / np.linalg.norm(v_bd))
        m = np.array([dir_a[:2], -dir_b[:2]]).T
        rhs = (B - A)[:2]
        sol = np.linalg.solve(m, rhs)
        t_val = sol
        Y_2d = A[:2] + t_val * dir_a[:2]
        Y = np.array([Y_2d[0], Y_2d[1], 0])
        triangle = Polygon(A, B, C, color=BLACK, stroke_width=4)
        ext_line = Line(C, D, color=GRAY)
        ext_line.set_dash_array([0.05, 0.05])
        bisector_a = Line(A, Y, color=BLUE, stroke_width=3)
        bisector_b = Line(B, Y, color=BLUE, stroke_width=3)
        dot_y = Dot(Y, color=RED, radius=0.12)
        cross = Cross(dot_y, color=RED, stroke_width=4).scale(0.5)
        highlight = SurroundingRectangle(dot_y, color=RED, buff=0.08)
        lbl_A = MathTex("A", color=BLACK).next_to(A, UP)
        lbl_B = MathTex("B", color=BLACK).next_to(B, DOWN)
        lbl_C = MathTex("C", color=BLACK).next_to(C, DOWN)
        lbl_Y = MathTex("Y", color=RED).next_to(Y, LEFT)
        res = MathTex("\\angle AYB = \\frac{\\gamma}{2}", color=BLACK).to_edge(DOWN)
        gamma_arc = Angle(Line(C, A), Line(C, B), radius=0.4, color=GRAY)
        ayb_arc = Angle(Line(Y, B), Line(Y, A), radius=0.4, color=RED)
        self.add(ext_line, triangle, bisector_a, bisector_b, dot_y, cross, highlight, gamma_arc, ayb_arc)
        self.add(lbl_A, lbl_B, lbl_C, lbl_Y, res)
