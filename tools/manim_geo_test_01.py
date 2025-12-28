from manim import *
import numpy as np

class GeometryScene(Scene):
    def construct(self):
        # Define points
        # Right triangle ABC with C at top (0, 2, 0)
        # Altitude CD. D is on AB.
        # Let D be origin (0,0,0) for simplicity?
        # No, let's center the drawing.
        
        # We know AD = 4, BD = 9. h = sqrt(4*9) = 6.
        # If D is at origin, A is at (-4, 0), B is at (9, 0).
        # C is at (0, 6).
        # Let's check slopes: CA slope = 6/4 = 1.5. CB slope = 6/-9 = -2/3.
        # Product = -1. Correct, C is right angle.
        
        D = np.array([0.0, 0.0, 0.0])
        A = np.array([-4.0, 0.0, 0.0])
        B = np.array([9.0, 0.0, 0.0])
        C = np.array([0.0, 6.0, 0.0])
        
        # Shift everything to center
        center_shift = -(A + B + C) / 3
        A += center_shift
        B += center_shift
        C += center_shift
        D += center_shift
        
        # Scale down to fit screen
        scale_factor = 0.7
        A *= scale_factor
        B *= scale_factor
        C *= scale_factor
        D *= scale_factor
        
        # Create objects
        triangle = Polygon(A, B, C, color=BLUE, stroke_width=4)
        altitude = Line(C, D, color=RED, stroke_width=3)
        
        # Labels
        label_A = MathTex("A").next_to(A, LEFT)
        label_B = MathTex("B").next_to(B, RIGHT)
        label_C = MathTex("C").next_to(C, UP)
        label_D = MathTex("D").next_to(D, DOWN)
        
        label_h = MathTex("h").next_to(altitude, RIGHT, buff=0.1)
        label_4 = MathTex("4").next_to(Line(A, D), DOWN)
        label_9 = MathTex("9").next_to(Line(D, B), DOWN)
        
        # Right angle markers
        right_angle_C = RightAngle(Line(C, A), Line(C, B), length=0.4)
        right_angle_D = RightAngle(Line(C, D), Line(D, B), length=0.3)
        
        # Group
        scene_group = VGroup(triangle, altitude, label_A, label_B, label_C, label_D, label_h, label_4, label_9, right_angle_C, right_angle_D)
        scene_group.move_to(ORIGIN)
        
        # Animations
        self.play(Create(triangle), run_time=2)
        self.play(Create(altitude), run_time=1)
        self.play(FadeIn(right_angle_C), FadeIn(right_angle_D))
        self.play(Write(label_A), Write(label_B), Write(label_C), Write(label_D))
        self.play(Write(label_h), Write(label_4), Write(label_9))
        
        self.wait(2)
