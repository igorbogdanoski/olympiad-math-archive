from manim import *
import numpy as np

class GeometryScene(Scene):
    def construct(self):
        # Parameters
        r = 2.5  # Visual radius
        angle_at_T = 45 * DEGREES
        # The distance from center to T can be calculated.
        # sin(angle_at_T / 2) = r / OT -> OT = r / sin(22.5)
        dist_OT = r / np.sin(angle_at_T / 2)
        
        # Center of circle
        O = ORIGIN
        # Point T (let's place it to the right)
        T = RIGHT * dist_OT
        
        # Tangent points calculation
        # The angle of T is 0. The angle of A and B relative to OT line.
        # In triangle OAT, angle at O is 90 - 22.5 = 67.5
        angle_offset = (90 - 45/2) * DEGREES
        
        A = r * np.array([np.cos(angle_offset), np.sin(angle_offset), 0])
        B = r * np.array([np.cos(-angle_offset), np.sin(-angle_offset), 0])
        
        # Create objects
        circle = Circle(radius=r, color=BLUE)
        center_dot = Dot(O, color=WHITE)
        label_O = MathTex("O").next_to(center_dot, LEFT)
        
        dot_T = Dot(T, color=WHITE)
        label_T = MathTex("T").next_to(dot_T, RIGHT)
        
        dot_A = Dot(A, color=WHITE)
        label_A = MathTex("A").next_to(dot_A, UP)
        
        dot_B = Dot(B, color=WHITE)
        label_B = MathTex("B").next_to(dot_B, DOWN)
        
        line_TA = Line(T, A, color=YELLOW)
        line_TB = Line(T, B, color=YELLOW)
        
        radius_OA = Line(O, A, color=GREEN)
        radius_OB = Line(O, B, color=GREEN)
        
        # Angles
        # Angle at T
        angle_T_arc = Angle(line_TA, line_TB, radius=0.8, other_angle=True, color=RED)
        label_45 = MathTex(r"45^\circ").next_to(angle_T_arc, LEFT)
        
        # Right angles
        right_angle_A = RightAngle(radius_OA, line_TA, length=0.3, quadrant=(-1,-1))
        right_angle_B = RightAngle(radius_OB, line_TB, length=0.3, quadrant=(-1,1))
        
        # Central angle
        angle_O_arc = Angle(radius_OB, radius_OA, radius=0.6, color=ORANGE)
        label_135 = MathTex(r"135^\circ").next_to(O, LEFT, buff=0.5)
        
        # Arc length
        arc_AB = ArcBetweenPoints(B, A, radius=r, color=RED, stroke_width=6)
        label_l = MathTex("l").next_to(arc_AB, LEFT)
        
        # Grouping
        scene_objects = VGroup(
            circle, center_dot, label_O,
            dot_T, label_T,
            dot_A, label_A,
            dot_B, label_B,
            line_TA, line_TB,
            radius_OA, radius_OB,
            angle_T_arc, label_45,
            right_angle_A, right_angle_B,
            angle_O_arc, label_135,
            arc_AB, label_l
        )
        
        # Scale to fit
        scene_objects.scale(0.8)
        scene_objects.move_to(ORIGIN + LEFT * 2)
        
        # Explanation text
        text_group = VGroup(
            MathTex(r"\angle ATB = 45^\circ"),
            MathTex(r"\angle OAT = \angle OBT = 90^\circ"),
            MathTex(r"\angle AOB = 360^\cirrc - 90^\cirrc - 90^\cirrc - 45^\circr),
            MathTex(r"\angle AOB = 135^\circ"),
            MathTex(r"l = \frrac{135}{360} \cdot 2\pi r"),
            MathTex(r"l = \frrac{3}{8} \cdot 8\pi = 3\pir),
            MathTex(r"\frrac{l}{\pi} = 3r)
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT)
        
        self.add(scene_objects)
        self.add(text_group)
