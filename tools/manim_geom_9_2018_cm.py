from manim import *
import numpy as np

class GeometryScene(Scene):
    def construct(self):
        # Define points
        # Triangle ABC. A at origin. B on x-axis.
        # Angles A=40, B=20.
        # AB - BC = 5.
        # Sine rule: a/sin40 = b/sin20 = c/sin120.
        # a = c * sin40 / sin120.
        # c - a = 5 => c (1 - sin40/sin120) = 5.
        # c = 5 / (1 - sin(40)/sin(120)).
        
        deg2rad = np.pi / 180
        sin40 = np.sin(40 * deg2rad)
        sin20 = np.sin(20 * deg2rad)
        sin120 = np.sin(120 * deg2rad)
        
        c = 5.0 / (1 - sin40 / sin120)
        # Scale down for display
        scale = 0.5
        c_scaled = c * scale
        
        A = np.array([-c_scaled/2, -2, 0]) # Center somewhat
        B = A + np.array([c_scaled, 0, 0])
        
        # C coordinates
        # b = c * sin20 / sin120
        b_scaled = c_scaled * sin20 / sin120
        C = A + np.array([b_scaled * np.cos(40 * deg2rad), b_scaled * np.sin(40 * deg2rad), 0])
        
        # M is bisector of C.
        # Angle C is 120. Bisector makes 60 with AC and BC.
        # M is on AB.
        # M divides AB in ratio b:a.
        # a_scaled = c_scaled * sin40 / sin120
        # M = (a_scaled * A + b_scaled * B) / (a_scaled + b_scaled)
        a_scaled = c_scaled * sin40 / sin120
        M = (a_scaled * A + b_scaled * B) / (a_scaled + b_scaled)
        
        # D on AB such that BD = BC = a.
        # D is at distance a from B towards A.
        # D = B - (a_scaled, 0, 0)
        D = B - np.array([a_scaled, 0, 0])
        
        # Create objects
        triangle = Polygon(A, B, C, color=BLUE, stroke_width=4)
        bisector_CM = Line(C, M, color=RED)
        segment_CD = Line(C, D, color=YELLOW)
        
        # Labels
        label_A = MathTex("A").next_to(A, DL)
        label_B = MathTex("B").next_to(B, DR)
        label_C = MathTex("C").next_to(C, UP)
        label_M = MathTex("M").next_to(M, DOWN)
        label_D = MathTex("D").next_to(D, DOWN)
        
        # Angles
        angle_A = Angle(Line(A, B), Line(A, C), radius=0.5)
        label_angle_A = MathTex("40^\\circ").next_to(angle_A, RIGHT)
        
        angle_B = Angle(Line(B, C), Line(B, A), radius=0.7)
        label_angle_B = MathTex("20^\\circ").next_to(angle_B, LEFT)
        
        # Group
        scene_group = VGroup(triangle, bisector_CM, segment_CD, label_A, label_B, label_C, label_M, label_D, angle_A, label_angle_A, angle_B, label_angle_B)
        scene_group.move_to(ORIGIN)
        
        # Animations
        self.play(Create(triangle), run_time=2)
        self.play(Create(angle_A), Write(label_angle_A), Create(angle_B), Write(label_angle_B))
        self.play(Write(label_A), Write(label_B), Write(label_C))
        self.play(Create(bisector_CM), Write(label_M))
        self.play(Create(segment_CD), Write(label_D))
        
        self.wait(2)
