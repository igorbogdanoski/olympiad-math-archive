from manim import *
import numpy as np

class GeometryScene(Scene):
    def construct(self):
        # Define points
        # Square ABCD. A=(-2, -2), B=(2, -2), C=(2, 2), D=(-2, 2)
        # Side length = 4.
        
        s = 4.0
        A = np.array([-s/2, -s/2, 0])
        B = np.array([s/2, -s/2, 0])
        C = np.array([s/2, s/2, 0])
        D = np.array([-s/2, s/2, 0])
        
        # Equilateral triangle ABE inside.
        # E is at (0, -s/2 + s * np.sqrt(3)/2, 0)
        E = np.array([0, -s/2 + s * np.sqrt(3)/2, 0])
        
        # Create objects
        square = Polygon(A, B, C, D, color=BLUE, stroke_width=4)
        triangle_ABE = Polygon(A, B, E, color=GREEN, stroke_width=3)
        
        segment_DE = Line(D, E, color=YELLOW)
        segment_CE = Line(C, E, color=YELLOW)
        
        # Labels
        label_A = MathTex("A").next_to(A, DL)
        label_B = MathTex("B").next_to(B, DR)
        label_C = MathTex("C").next_to(C, UR)
        label_D = MathTex("D").next_to(D, UL)
        label_E = MathTex("E").next_to(E, UP)
        
        # Mark equality
        # AB = AE = BE = AD = BC
        # Mark AB, AE, BE with single tick
        # Mark AD, BC with single tick
        
        ticks = VGroup()
        for p1, p2 in [(A, B), (A, E), (B, E), (A, D), (B, C)]:
            mid = (p1 + p2) / 2
            vec = p2 - p1
            perp = np.array([-vec[1], vec[0], 0])
            perp = perp / np.linalg.norm(perp) * 0.15
            tick = Line(mid - perp, mid + perp, color=WHITE)
            ticks.add(tick)

        # Target angle DEC
        angle_DEC = Angle(Line(E, D), Line(E, C), radius=0.5, color=RED)
        label_angle = MathTex("?").next_to(angle_DEC, UP, buff=0.1)
        
        # Group
        scene_group = VGroup(square, triangle_ABE, segment_DE, segment_CE, label_A, label_B, label_C, label_D, label_E, ticks, angle_DEC, label_angle)
        scene_group.move_to(ORIGIN)
        
        # Animations
        self.play(Create(square), run_time=2)
        self.play(Create(triangle_ABE), run_time=1.5)
        self.play(Create(segment_DE), Create(segment_CE))
        self.play(Write(label_A), Write(label_B), Write(label_C), Write(label_D), Write(label_E))
        self.play(Create(ticks))
        self.play(Create(angle_DEC), Write(label_angle))
        
        self.wait(2)
