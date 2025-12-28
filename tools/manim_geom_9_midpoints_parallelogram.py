from manim import *

class Problem_geom_9_midpoints_parallelogram(Scene):
    def construct(self):
        # Define quadrilateral ABCD
        A = np.array([-3, -2, 0])
        B = np.array([3, -2, 0])
        C = np.array([2, 2, 0])
        D = np.array([-2, 3, 0])
        
        quad = Polygon(A, B, C, D, color=BLUE)
        
        # Midpoints E and K
        E = (A + B) / 2
        K = (C + D) / 2
        
        # Segments AK, CE, BK, DE
        line_AK = Line(A, K, color=GRAY, stroke_opacity=0.5)
        line_CE = Line(C, E, color=GRAY, stroke_opacity=0.5)
        line_BK = Line(B, K, color=GRAY, stroke_opacity=0.5)
        line_DE = Line(D, E, color=GRAY, stroke_opacity=0.5)
        
        # Midpoints of these segments
        # P = mid(AK)
        P = (A + K) / 2
        # Q = mid(CE)
        Q = (C + E) / 2
        # R = mid(BK)
        R = (B + K) / 2
        # S = mid(DE)
        S = (D + E) / 2
        
        # The parallelogram vertices are P, S, R, Q based on my analysis
        # P(-1.5, 0.25), S(-1, 0.5), R(1.5, 0.25), Q(1, 0)
        parallelogram = Polygon(P, S, R, Q, color=YELLOW, fill_opacity=0.2)
        
        # Labels
        label_A = MathTex("A").next_to(A, DL)
        label_B = MathTex("B").next_to(B, DR)
        label_C = MathTex("C").next_to(C, UR)
        label_D = MathTex("D").next_to(D, UL)
        label_E = MathTex("E").next_to(E, DOWN)
        label_K = MathTex("K").next_to(K, UP)
        
        # Dots
        dots = VGroup(
            Dot(A), Dot(B), Dot(C), Dot(D),
            Dot(E, color=RED), Dot(K, color=RED),
            Dot(P, color=YELLOW), Dot(Q, color=YELLOW), 
            Dot(R, color=YELLOW), Dot(S, color=YELLOW)
        )
        
        self.add(quad)
        self.add(line_AK, line_CE, line_BK, line_DE)
        self.add(parallelogram)
        self.add(dots)
        self.add(label_A, label_B, label_C, label_D, label_E, label_K)
        
        # Add labels for the parallelogram vertices? Maybe too crowded.
        # Let's just label the parallelogram itself or the midpoints if needed.
        # The problem asks to prove they are vertices of a parallelogram.
        # Visualizing the yellow parallelogram is enough.
