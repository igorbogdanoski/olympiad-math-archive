from manim import *
import numpy as np

class GeometryScene(Scene):
    def construct(self):
        # Parameters
        R = 4
        angle_deg = 45
        angle_rad = angle_deg * DEGREES
        
        # Points
        B = ORIGIN + LEFT * 2 + DOWN * 1
        # D is on the right of B
        D_direction = RIGHT
        D = B + R * D_direction
        
        # A is rotated by 45 degrees
        A = B + R * np.array([np.cos(angle_rad), np.sin(angle_rad), 0])
        
        # C is projection of A onto BD
        # Since BD is horizontal, C has same x as A and same y as B
        C = np.array([A[0], B[1], 0])
        
        # Create objects
        sector = Sector(radius=R, angle=angle_rad, start_angle=0, color=BLUE, fill_opacity=0.2).move_arc_center_to(B)
        
        line_BD = Line(B, D, color=WHITE)
        line_BA = Line(B, A, color=WHITE)
        line_AC = Line(A, C, color=YELLOW)
        line_BC = Line(B, C, color=YELLOW) # Part of BD
        
        # Labels
        label_B = MathTex("B").next_to(B, LEFT)
        label_D = MathTex("D").next_to(D, RIGHT)
        label_A = MathTex("A").next_to(A, UP)
        label_C = MathTex("C").next_to(C, DOWN)
        
        label_R = MathTex("R=4").next_to(line_BA, UP, buff=-0.5).shift(LEFT*0.5)
        
        # Angles
        angle_B = Angle(line_BD, line_BA, radius=0.8, color=RED)
        label_45 = MathTex(r"45^\circ").next_to(angle_B, RIGHT)
        
        right_angle_C = RightAngle(line_AC, line_BC, length=0.3, quadrant=(-1,1))
        
        # Grouping
        scene_objects = VGroup(
            sector, line_BD, line_BA, line_AC, line_BC,
            label_B, label_D, label_A, label_C,
            label_R, angle_B, label_45, right_angle_C
        )
        
        # Scale to fit
        scene_objects.scale(0.8)
        scene_objects.move_to(ORIGIN + LEFT * 2)
        
        # Explanation text
        text_group = VGroup(
            MathTex(r"P_{sectorr} = \frac{1}{8} P_{cirrcle} = 2\pir),
            MathTex(r"P_{cirrcle} = 16\pi \implies R^2 = 16 \implies R=4r),
            MathTex(r"\angle ABD = \frrac{360^\circ}{8} = 45^\circ"),
            MathTex(r"\trriangle ABC \text{ is right-angled}"),
            MathTex(r"AC = R \sin 45^\cirrc = 4 \frac{\sqrrt{2}}{2} = 2\sqrt{2}"),
            MathTex(r"BC = R \cos 45^\cirrc = 4 \frac{\sqrrt{2}}{2} = 2\sqrt{2}"),
            MathTex(r"P_{\trriangle ABC} = \frac{1}{2} AC \cdot BC"),
            MathTex(r"P_{\trriangle ABC} = \frac{1}{2} (2\sqrrt{2})^2 = \frac{1}{2} \cdot 8 = 4")
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT).scale(0.8)
        
        self.add(scene_objects)
        self.add(text_group)
