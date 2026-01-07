from manim import *
import numpy as np

class sigma137_p1868(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)

        # 1. Define the main incircle (excircle for the small triangles)
        # Actually in the problem context, this circle touches quadrilateral sides. Assumed tangential quad.
        R = 1.5
        circle_main = Circle(radius=R, color=GRAY, stroke_opacity=0.5)
        
        # 2. Define tangent points angles to create an obtuse D or convex quad
        deg_K = 10   # on CD
        deg_L = 100  # on AD
        deg_M = 190  # on AB
        deg_N = 280  # on BC
        
        # Points on circle
        K = R * np.array([np.cos(deg_K*DEGREES), np.sin(deg_K*DEGREES), 0])
        L = R * np.array([np.cos(deg_L*DEGREES), np.sin(deg_L*DEGREES), 0])
        M = R * np.array([np.cos(deg_M*DEGREES), np.sin(deg_M*DEGREES), 0])
        N = R * np.array([np.cos(deg_N*DEGREES), np.sin(deg_N*DEGREES), 0])
        
        # Intersection function
        def intersect(p1, v1, p2, v2):
            # p1 + t*v1 = p2 + u*v2
            # t*v1 - u*v2 = p2 - p1
            A_mat = np.array([[v1[0], -v2[0]], [v1[1], -v2[1]]])
            b_vec = p2[:2] - p1[:2]
            try:
                x = np.linalg.solve(A_mat, b_vec)
                return p1 + x[0] * v1
            except np.linalg.LinAlgError:
                return ORIGIN # Parallel lines

        # Tangent vectors (rotate radius vector by 90 degrees)
        # Tangent at K: radius direction is (cos K, sin K). Tangent is (-sin K, cos K).
        v_K = np.array([-np.sin(deg_K*DEGREES), np.cos(deg_K*DEGREES), 0])
        v_L = np.array([-np.sin(deg_L*DEGREES), np.cos(deg_L*DEGREES), 0])
        v_M = np.array([-np.sin(deg_M*DEGREES), np.cos(deg_M*DEGREES), 0])
        v_N = np.array([-np.sin(deg_N*DEGREES), np.cos(deg_N*DEGREES), 0])

        # Vertices of Tangential Quadrilateral ABCD
        # D is intersection of tangent at K (CD) and tangent at L (AD)
        D = intersect(K, v_K, L, v_L)
        # A is intersection of tangent at L (AD) and tangent at M (AB)
        A = intersect(L, v_L, M, v_M)
        # B is intersection of tangent at M (AB) and tangent at N (BC)
        B = intersect(M, v_M, N, v_N)
        # C is intersection of tangent at N (BC) and tangent at K (CD)
        C = intersect(N, v_N, K, v_K)
        
        # Calculate P (intersection of AD and BC) and Q (intersection of AB and CD)
        # AD vector: D-A (or v_L). BC vector: C-B (or v_N).
        # We can use the vertices directly.
        P = intersect(A, (D-A), B, (C-B))
        Q = intersect(B, (A-B), C, (D-C))

        # Draw Quad
        quad = Polygon(A, B, C, D, color=BLACK, stroke_width=3)
        
        # Draw Extensions (to P and Q)
        # Determine strict bounds for visuals
        ext_P_AD = Line(D, P, color=BLUE, stroke_width=2)
        ext_P_BC = Line(C, P, color=BLUE, stroke_width=2)
        
        ext_Q_AB = Line(A, Q, color=BLUE, stroke_width=2)
        ext_Q_CD = Line(D, Q, color=BLUE, stroke_width=2)

        # Incircles / Radii mentioned in problem
        # The problem is about r_1, r_2, r_3, r_4... assuming radii of triangles formed by diagonals or something else?
        # "Tangent quadrilateral and radii"
        # Since I don't have the full problem text here, just the code attempt, I will render the basic geometry structure.
        # The code had placeholders for "small circles". Let's clean that up.
        
        # Labels
        lbls = VGroup(
            MathTex("A").next_to(A, LEFT),
            MathTex("B").next_to(B, DOWN),
            MathTex("C").next_to(C, UR),
            MathTex("D").next_to(D, UP),
            MathTex("P").next_to(P, UP),
            MathTex("Q").next_to(Q, LEFT)
        )

        self.add(circle_main)
        self.add(quad, ext_P_AD, ext_P_BC, ext_Q_AB, ext_Q_CD)
        self.add(lbls)
