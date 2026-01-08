from manim import *
import numpy as np

class Problem_geom_9_centroid_plane_dist(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # 3D scene simulated in 2D
        # Plane is a line at bottom
        plane_y = -2.0
        line_plane = Line(LEFT*6, RIGHT*6, color=BLACK).shift(UP*plane_y)
        label_plane = MathTex(r"\pi").next_to(line_plane, RIGHT)
        
        # Points A, B, C in "space" (above the line)
        # x coordinates arbitrary
        # y coordinates relative to plane_y are heights 10, 15, 17 (scaled)
        scale = 0.2
        hA = 10 * scale
        hB = 15 * scale
        hC = 17 * scale
        
        A = np.array([-3, plane_y + hA, 0])
        B = np.array([0, plane_y + hB, 0])
        C = np.array([3, plane_y + hC, 0])
        
        # Projections A', B', C' on the plane
        Ap = np.array([A[0], plane_y, 0])
        Bp = np.array([B[0], plane_y, 0])
        Cp = np.array([C[0], plane_y, 0])
        
        # Centroid T
        T = (A + B + C) / 3
        
        # Projection T'
        Tp = np.array([T[0], plane_y, 0])
        
        # Center camera
        self.camera.frame_center = (A + C + line_plane.get_center())/3
        self.camera.frame_width = 10
        
        # Points
        points = {'A': A, 'B': B, 'C': C, "A'": Ap, "B'": Bp, "C'": Cp, 'T': T, "T'": Tp}
        
        # Triangle ABC
        tri = Polygon(A, B, C, color=BLUE, fill_opacity=0.1)
        
        # Projection lines
        line_AAp = DashedLine(A, Ap, color=GRAY)
        line_BBp = DashedLine(B, Bp, color=GRAY)
        line_CCp = DashedLine(C, Cp, color=GRAY)
        line_TTp = Line(T, Tp, color=RED)
        
        # Labels
        labels = VGroup()
        for name, point in points.items():
            direction = UP
            if "'" in name: direction = DOWN
            
            labels.add(MathTex(name).next_to(point, direction))
            
        # Height labels
        label_hA = MathTex("10").next_to(line_AAp, LEFT)
        label_hB = MathTex("15").next_to(line_BBp, LEFT)
        label_hC = MathTex("17").next_to(line_CCp, RIGHT)
        label_hT = MathTex("?").next_to(line_TTp, RIGHT)
        
        # Draw
        self.play(Create(line_plane), Write(label_plane))
        self.play(Create(tri))
        self.play(Create(line_AAp), Create(line_BBp), Create(line_CCp))
        self.play(Create(line_TTp))
        
        dots = VGroup(*[Dot(p) for p in points.values()])
        self.play(FadeIn(dots), FadeIn(labels))
        
        self.play(Write(label_hA), Write(label_hB), Write(label_hC), Write(label_hT))
        
        # Add text info
        info = MathTex(r"TTrr' = \frac{AA' + BB' + CC'}{3}", color=RED, font_size=36).to_corner(UL)
        self.add(info)
        
        self.wait(2)
