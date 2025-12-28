from manim import *

class Problem_geom_9_hypot_ratio_mid_circle(Scene):
    def construct(self):
        # Scale
        scale = 0.8
        
        # Coordinates
        C = ORIGIN
        A = RIGHT * 12
        B = UP * 5
        
        # Midpoints
        M = (C + B) / 2 # Midpoint of BC
        N = (C + A) / 2 # Midpoint of AC
        
        # Circle diameter MN
        center_O = (M + N) / 2
        radius = np.linalg.norm(M - N) / 2
        circle = Circle(radius=radius, color=GREEN).move_to(center_O)
        
        # Hypotenuse line
        line_AB = Line(A, B, color=BLUE)
        
        # Intersections P and Q
        # Line AB: y = -5/12 * (x - 12)
        # Circle: (x-3)^2 + (y-1.25)^2 = 3.25^2
        # Substitute y:
        # (x-3)^2 + (-5/12(x-12) - 1.25)^2 = 3.25^2
        # -5/12(x-12) - 5/4 = -5/12(x-12) - 15/12 = -5/12(x-12+3) = -5/12(x-9)
        # (x-3)^2 + 25/144 (x-9)^2 = 169/16
        # 144(x-3)^2 + 25(x-9)^2 = 169/16 * 144 = 169 * 9 = 1521
        # 144(x^2-6x+9) + 25(x^2-18x+81) = 1521
        # 144x^2 - 864x + 1296 + 25x^2 - 450x + 2025 = 1521
        # 169x^2 - 1314x + 3321 = 1521
        # 169x^2 - 1314x + 1800 = 0
        # x = (1314 +/- sqrt(1314^2 - 4*169*1800)) / 338
        # 1314^2 = 1726596
        # 4*169*1800 = 1216800
        # sqrt(509796) = 714
        # x1 = (1314 - 714) / 338 = 600 / 338 = 300 / 169 = 1.775
        # x2 = (1314 + 714) / 338 = 2028 / 338 = 6
        
        x_Q = 6
        y_Q = -5/12 * (x_Q - 12) # -5/12 * -6 = 2.5
        Q = np.array([x_Q, y_Q, 0])
        
        x_P = 300 / 169
        y_P = -5/12 * (x_P - 12)
        P = np.array([x_P, y_P, 0])
        
        # Shift to center
        center_scene = (A + B + C) / 3
        shift = -center_scene
        
        A += shift
        B += shift
        C += shift
        M += shift
        N += shift
        P += shift
        Q += shift
        circle.shift(shift)
        
        # Scale
        A *= scale
        B *= scale
        C *= scale
        M *= scale
        N *= scale
        P *= scale
        Q *= scale
        circle.scale(scale)
        
        # Objects
        triangle = Polygon(A, B, C, color=BLUE)
        
        dot_A = Dot(A, color=WHITE)
        dot_B = Dot(B, color=WHITE)
        dot_C = Dot(C, color=WHITE)
        dot_M = Dot(M, color=WHITE)
        dot_N = Dot(N, color=WHITE)
        dot_P = Dot(P, color=RED)
        dot_Q = Dot(Q, color=RED)
        
        label_A = MathTex("A").next_to(dot_A, DR)
        label_B = MathTex("B").next_to(dot_B, UL)
        label_C = MathTex("C").next_to(dot_C, DL)
        label_M = MathTex("M").next_to(dot_M, LEFT)
        label_N = MathTex("N").next_to(dot_N, DOWN)
        label_P = MathTex("P").next_to(dot_P, UP)
        label_Q = MathTex("Q").next_to(dot_Q, UR)
        
        self.add(triangle)
        self.add(circle)
        self.add(dot_A, dot_B, dot_C, dot_M, dot_N, dot_P, dot_Q)
        self.add(label_A, label_B, label_C, label_M, label_N, label_P, label_Q)
        
        # Add ratio text
        # AP : PQ : QB
        # x coords: A=12, Q=6, P=1.77, B=0
        # Wait, B is at x=0. A is at x=12.
        # P is closer to B (x=1.77). Q is at x=6.
        # Order on hypotenuse from B to A: B, P, Q, A.
        # BP distance: sqrt((1.77-0)^2 + ...)
        # Just use x-diffs since linear.
        # x_B = 0. x_P = 300/169. x_Q = 6. x_A = 12.
        # BP ~ 1.77
        # PQ ~ 6 - 1.77 = 4.23
        # QA ~ 12 - 6 = 6
        # Ratio BP : PQ : QA = 300/169 : (1014-300)/169 : 6
        # = 300 : 714 : 1014
        # Divide by 6: 50 : 119 : 169
        
        text = MathTex("BP : PQ : QA = 50 : 119 : 169").to_corner(UL).scale(0.8)
        self.add(text)
