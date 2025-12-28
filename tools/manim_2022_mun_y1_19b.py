from manim import *
import numpy as np

class GeometryScene(Scene):
    def construct(self):
        # Parameters
        # Shape derived:
        # A(0,0), B(10,0), C(10, 2h), D(6, 2h), E(6, h), F(0, h)
        # h is arbitrary for visualization, let's say h=1.5
        h = 1.5
        
        A = np.array([0, 0, 0])
        B = np.array([5, 0, 0]) # Scale 10 -> 5
        C = np.array([5, 2*h, 0])
        D = np.array([3, 2*h, 0]) # Scale 6 -> 3
        E = np.array([3, h, 0])
        F = np.array([0, h, 0])
        
        # Polygon
        shape = Polygon(A, B, C, D, E, F, color=WHITE, stroke_width=2)
        
        # Dividing line MN
        # Let's assume MN is a vertical line that splits area in half.
        # Total area visual = 3*h + 2*2h = 7h.
        # Half area = 3.5h.
        # Left part area = 3*h.
        # So we need 0.5h more from the right part.
        # Right part is rectangle of width 2, height 2h.
        # We need area 0.5h. Height is 2h. Width needed = 0.5h / 2h = 0.25.
        # So split is at x = 3 + 0.25 = 3.25.
        # M on AB at x=3.25. N on CD? No, N on DE? No.
        # If vertical line:
        # M on AB. N on DE? No, DE is vertical.
        # N on CD? No.
        # Let's just draw a generic dividing line.
        # Or maybe MN connects midpoints of AF and CD?
        # The problem doesn't specify M and N.
        # It says "If the segment MN divides...".
        # This implies MN is a specific segment that achieves this.
        # And then asks for area of MNCF.
        # This implies MNCF is one of the halves.
        
        # Let's draw a line and label the regions.
        # Let's draw a line from M on AB to N on DE/CD/EF.
        # Let's put M on AB and N on EF.
        # Just illustrative.
        
        M = np.array([2.5, 0, 0])
        N = np.array([2.5, 2*h, 0]) # Just a line
        
        line_MN = Line(M, np.array([2.5, h, 0]), color=YELLOW) # Partial line for visual
        
        # Labels
        label_A = MathTex("A").next_to(A, DOWN+LEFT)
        label_B = MathTex("B").next_to(B, DOWN+RIGHT)
        label_C = MathTex("C").next_to(C, UP+RIGHT)
        label_D = MathTex("D").next_to(D, UP+LEFT)
        label_E = MathTex("E").next_to(E, DOWN+RIGHT)
        label_F = MathTex("F").next_to(F, UP+LEFT)
        
        # Dimensions
        label_10 = MathTex("10").next_to(Line(A,B), DOWN)
        label_6 = MathTex("6").next_to(Line(F,E), UP)
        
        # Area labels
        label_total = MathTex("P_{total} = 130").to_edge(UP)
        
        # Shading MNCF
        # Assuming MNCF is the left part (or right part).
        # If MNCF is a figure, it must be a closed loop.
        # M-N-C-F?
        # If M is on AB and N is on CD?
        # Then MNCF is M-B-C-N? No.
        # M-N-C-F implies vertices order.
        # If M is on AB, N is on EF?
        # Then MNCF is M-A-F-N? Or M-B-C-D-E-N?
        # If the figure is MNCF, then M, N, C, F are vertices.
        # This implies M and N are such that MNCF is a valid polygon.
        # Maybe M is on AB and N is on CD?
        # Then MNCF is a quadrilateral?
        # If so, Area(MNCF) = 65.
        
        # Let's just visualize the concept "Divided in half".
        
        # Grouping
        scene_objects = VGroup(
            shape, label_A, label_B, label_C, label_D, label_E, label_F,
            label_10, label_6, label_total
        )
        
        scene_objects.scale(0.8)
        scene_objects.move_to(ORIGIN)
        
        # Explanation text
        text_group = VGroup(
            MathTex(r"P_{total} = 130"),
            MathTex(r"P_{MNCF} = \frac{1}{2} P_{total}"),
            MathTex(r"P_{MNCF} = \frac{130}{2} = 65")
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT).scale(0.8)
        
        self.add(scene_objects)
        self.add(text_group)
