from manim import *

class Problem_numerus_4367(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Equilateral Triangle ABC
        # Side length 6
        # A at (-3, -1.5), B at (3, -1.5)
        # Height = 6 * sqrt(3)/2 = 3*sqrt(3) approx 5.2
        
        h = 3 * np.sqrt(3)
        A = np.array([-3, -2, 0])
        B = np.array([3, -2, 0])
        C = np.array([0, -2 + h, 0])
        
        tri = Polygon(A, B, C, color=BLUE, fill_opacity=0.1)
        
        # Midpoints
        P = (A + B) / 2
        M = (A + C) / 2
        
        # Lines
        line_CP = Line(C, P, color=RED) # Perpendicular bisector
        line_BM = Line(B, M, color=GREEN) # Median
        
        # Intersection Q
        # Q is centroid. Q = (A+B+C)/3
        Q = (A + B + C) / 3
        
        # Labels
        lbl_A = Text("A", font_size=24, color=BLACK).next_to(A, DL, buff=0.1)
        lbl_B = Text("B", font_size=24, color=BLACK).next_to(B, DR, buff=0.1)
        lbl_C = Text("C", font_size=24, color=BLACK).next_to(C, UP, buff=0.1)
        lbl_P = Text("P", font_size=24, color=BLACK).next_to(P, DOWN, buff=0.1)
        lbl_M = Text("M", font_size=24, color=BLACK).next_to(M, UL, buff=0.1)
        lbl_Q = Text("Q", font_size=24, color=BLACK).next_to(Q, LEFT, buff=0.1)
        
        # Mark Angle PQB
        # P-Q-B? No, angle at Q? "angle PQB". Vertex is Q.
        # Wait, "angle PQB" usually means vertex is Q.
        # But in triangle BPQ, angle at P is 90, angle at B is 30.
        # Angle at Q is 60.
        # Let's mark angle PQB.
        # Angle(line QP, line QB).
        
        angle_mark = Angle(Line(Q, P), Line(Q, B), radius=0.4, color=ORANGE)
        lbl_angle = MathTex("?", color=ORANGE).next_to(angle_mark, UP, buff=0.1)
        
        # Add elements
        self.add(tri)
        self.add(line_CP, line_BM)
        self.add(lbl_A, lbl_B, lbl_C, lbl_P, lbl_M, lbl_Q)
        self.add(angle_mark, lbl_angle)
        
        # Add text
        text = MathTex(r"\triangle ABC \text{ is Equilateral}", color=BLACK).to_corner(UL)
        self.add(text)
