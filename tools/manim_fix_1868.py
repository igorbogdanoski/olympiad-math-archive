from manim import *
import numpy as np

class sigma137_p1868(MovingCameraScene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # Zoom out to see P and Q
        # The frame default width is 14. Scale 2.5 means width 35.
        self.camera.frame.scale(2.5)
        self.camera.frame.shift(UP * 2)

        # 1. Define the main incircle
        R = 1.5
        circle_main = Circle(radius=R, color=GRAY, stroke_opacity=0.5)
        
        # 2. Define tangent points angles (irregular to ensure no parallel sides)
        # Avoid 180 degree differences between L and N, or K and M
        deg_K = 10    # on CD
        deg_L = 80    # on AD
        deg_M = 200   # on AB
        deg_N = 300   # on BC
        
        # Helper: Point on circle from angle
        def pt_on_circ(d):
            return R * np.array([np.cos(d*DEGREES), np.sin(d*DEGREES), 0])
            
        K = pt_on_circ(deg_K)
        L = pt_on_circ(deg_L)
        M = pt_on_circ(deg_M)
        N = pt_on_circ(deg_N)
        
        # Tangent direction vectors (rotate radius by 90)
        def tan_vec(d):
            return np.array([-np.sin(d*DEGREES), np.cos(d*DEGREES), 0])
            
        v_K = tan_vec(deg_K)
        v_L = tan_vec(deg_L)
        v_M = tan_vec(deg_M)
        v_N = tan_vec(deg_N)
        
        # Intersection function
        def intersect(p1, v1, p2, v2):
            det = v1[0]*(-v2[1]) - v1[1]*(-v2[0])
            if abs(det) < 1e-6:
                return ORIGIN # Parallel
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            t = (dx*(-v2[1]) - dy*(-v2[0])) / det
            return p1 + t * v1

        # Vertices of Tangential Quadrilateral ABCD
        # Order of tangents around circle: K, L, M, N
        # D is between K and L
        D = intersect(K, v_K, L, v_L)
        # A is between L and M
        A = intersect(L, v_L, M, v_M)
        # B is between M and N
        B = intersect(M, v_M, N, v_N)
        # C is between N and K
        C = intersect(N, v_N, K, v_K)
        
        # P is intersection of AD and BC
        P = intersect(L, v_L, N, v_N)
        
        # Q is intersection of AB and CD
        Q = intersect(M, v_M, K, v_K)

        # Draw Quad
        quad = Polygon(A, B, C, D, color=BLACK, stroke_width=3)
        
        # Draw Extensions (to P and Q)
        lines_ext = VGroup()
        if np.linalg.norm(P) > 1e-3:
            lines_ext.add(Line(A, P, color=BLUE, stroke_width=2))
            lines_ext.add(Line(B, P, color=BLUE, stroke_width=2))
            lines_ext.add(Line(C, P, color=BLUE, stroke_width=2))
            lines_ext.add(Line(D, P, color=BLUE, stroke_width=2))

        if np.linalg.norm(Q) > 1e-3:
            lines_ext.add(Line(A, Q, color=BLUE_E, stroke_width=2))
            lines_ext.add(Line(B, Q, color=BLUE_E, stroke_width=2))
            lines_ext.add(Line(C, Q, color=BLUE_E, stroke_width=2))
            lines_ext.add(Line(D, Q, color=BLUE_E, stroke_width=2))

        # Labels
        lbls = VGroup(
            MathTex("A").next_to(A, LEFT),
            MathTex("B").next_to(B, DOWN),
            MathTex("C").next_to(C, RIGHT),
            MathTex("D").next_to(D, UP),
        )
        if np.linalg.norm(P) > 1e-3:
            lbls.add(MathTex("P").next_to(P, UP))
        if np.linalg.norm(Q) > 1e-3:
            lbls.add(MathTex("Q").next_to(Q, LEFT))

        self.add(circle_main)
        self.add(quad, lines_ext)
        self.add(lbls)
