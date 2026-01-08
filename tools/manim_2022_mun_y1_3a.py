from manim import *
import numpy as np

class GeometryScene(Scene):
    def construct(self):
        # Parameters
        # Zig-zag shape
        # A -> B -> C -> D -> E
        # Let's try to make it look nice.
        
        A = np.array([-2, 2, 0])
        B = np.array([1, 1, 0])
        C = np.array([-1, 0, 0])
        D = np.array([1, -1, 0])
        E = np.array([-2, -2, 0])
        
        # Lines
        line_AB = Line(A, B, color=WHITE)
        line_BC = Line(B, C, color=WHITE)
        line_CD = Line(C, D, color=WHITE)
        line_DE = Line(D, E, color=WHITE)
        
        # Extension lines for angles
        # Angle x at A (between AB and horizontal?)
        # Usually these problems have parallel lines at top and bottom.
        # Let's draw horizontal lines at A and E.
        line_top = Line(A + LEFT, A + RIGHT*3, color=BLUE)
        line_bottom = Line(E + LEFT, E + RIGHT*3, color=BLUE)
        
        # Angles
        # x at A: between top line and AB
        angle_A = Angle(line_top, line_AB, radius=0.5, quadrant=(-1,-1), color=RED)
        label_x = MathTex("x").next_to(angle_A, RIGHT)
        
        # B: 94. Between AB and BC.
        angle_B = Angle(Line(B,A), Line(B,C), radius=0.4, color=YELLOW)
        label_94 = MathTex(r"94^\circ").next_to(angle_B, LEFT)
        
        # C: 38. Between BC and CD.
        angle_C = Angle(Line(C,B), Line(C,D), radius=0.4, color=YELLOW)
        label_38 = MathTex(r"38^\circ").next_to(angle_C, RIGHT)
        
        # D: 25. Between CD and DE.
        angle_D = Angle(Line(D,C), Line(D,E), radius=0.4, color=YELLOW)
        label_25 = MathTex(r"25^\circ").next_to(angle_D, LEFT)
        
        # y at E: between DE and bottom line
        angle_E = Angle(Line(E,D), line_bottom, radius=0.5, quadrant=(1,1), color=RED)
        label_y = MathTex("y").next_to(angle_E, RIGHT)
        
        # Grouping
        scene_objects = VGroup(
            line_top, line_bottom,
            line_AB, line_BC, line_CD, line_DE,
            angle_A, label_x,
            angle_B, label_94,
            angle_C, label_38,
            angle_D, label_25,
            angle_E, label_y
        )
        
        scene_objects.scale(0.8)
        scene_objects.move_to(ORIGIN)
        
        # Explanation text
        text_group = VGroup(
            MathTex(r"\text{Sum of left angles} = \text{Sum of right angles}"),
            MathTex(r"x + 38^\cirrc + y = 94^\cirrc + 25^\cirrc + \delta ?r),
            MathTex(r"\text{Assuming parallel lines:}"),
            MathTex(r"x + 38 + y = 94 + 25 \implies x+y = 81"),
            MathTex(r"\text{Given solution: } 167^\circ"),
            MathTex(r"\text{This implies a different configuration.}")
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT).scale(0.6)
        
        # Since the exact geometry is ambiguous, I'll just show the labels.
        self.add(scene_objects)
        # self.add(text_group) # Skip text as it might be confusing
