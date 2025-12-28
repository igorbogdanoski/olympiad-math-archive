from manim import *
import numpy as np

class TriangleBisectorDifference(Scene):
    def construct(self):
        # Parameters
        # AB - BC = 5.
        # Let's scale for visualization.
        # From calculation: BC = 5 / (2 cos 80) approx 5 / (2 * 0.173) = 5 / 0.347 = 14.4.
        # AB = BC + 5 = 19.4.
        # Scale down by factor 2.
        scale = 0.4
        BC_len = 14.4 * scale
        AB_len = 19.4 * scale
        diff = 5 * scale
        
        # Coordinates
        # B at origin
        B = ORIGIN
        # A on x-axis
        A = RIGHT * AB_len
        # C at angle 20 degrees from BA? No, angle B is 20.
        # C = (BC cos 20, BC sin 20).
        C = np.array([BC_len * np.cos(20*DEGREES), BC_len * np.sin(20*DEGREES), 0])
        
        # M on AB. CM bisects C.
        # Angle C = 120. Bisector at 60 from CB.
        # Line CM angle: 20 + 60 = 80 degrees? No.
        # Line BC angle is 20 relative to BA? No.
        # If B is origin, A is (AB, 0).
        # Angle B is 20. So C is at 20 degrees.
        # Angle BCA = 120.
        # Bisector CM makes angle 60 with CB.
        # Angle of CB is 20.
        # Angle of CM is 20 + 60 = 80? No.
        # Angle B is interior.
        # Vector BA is (1, 0). Vector BC is (cos 20, sin 20).
        # Angle ABC is 20.
        # Angle BCA is 120.
        # Bisector CM splits BCA into 60, 60.
        # Angle BCM = 60.
        # In triangle MBC, angle M = 180 - 20 - 60 = 100.
        # So line CM makes angle?
        # Let's just find M as intersection of bisector and AB.
        # Bisector theorem: AM / MB = AC / BC.
        # AC / sin(20) = AB / sin(120).
        # AC = AB * sin(20) / sin(120).
        AC_len = AB_len * np.sin(20*DEGREES) / np.sin(120*DEGREES)
        ratio = AC_len / BC_len
        # M divides AB in ratio.
        # M = (A + ratio * B) / (1 + ratio).
        M = (A + ratio * B) / (1 + ratio)
        
        # Point D on AB such that BD = BC.
        # D is at distance BC from B along BA.
        D = RIGHT * BC_len
        
        # Create points
        pA = Dot(A)
        pB = Dot(B)
        pC = Dot(C)
        pM = Dot(M)
        pD = Dot(D)
        
        # Shapes
        triangle = Polygon(A, B, C, color=BLUE, fill_opacity=0.1)
        bisector = Line(C, M, color=RED)
        line_CD = Line(C, D, color=GREEN)
        
        # Labels
        lbl_A = MathTex("A").next_to(A, DOWN)
        lbl_B = MathTex("B").next_to(B, DOWN+LEFT)
        lbl_C = MathTex("C").next_to(C, UP)
        lbl_M = MathTex("M").next_to(M, DOWN)
        lbl_D = MathTex("D").next_to(D, DOWN)
        
        # Angles
        angle_B = Angle(Line(B,A), Line(B,C), radius=0.8, color=YELLOW)
        lbl_20 = MathTex("20^\circ").next_to(angle_B, RIGHT).scale(0.7)
        
        angle_A = Angle(Line(A,C), Line(A,B), radius=0.8, color=YELLOW)
        lbl_40 = MathTex("40^\circ").next_to(angle_A, LEFT).scale(0.7)
        
        # Bisector angles
        angle_BCM = Angle(Line(C,B), Line(C,M), radius=0.6, color=RED)
        angle_MCA = Angle(Line(C,M), Line(C,A), radius=0.7, color=RED)
        lbl_60 = MathTex("60^\circ").next_to(angle_BCM, DOWN).scale(0.5)
        
        # Group
        scene_objects = VGroup(
            triangle, bisector, line_CD,
            pA, pB, pC, pM, pD,
            lbl_A, lbl_B, lbl_C, lbl_M, lbl_D,
            angle_B, lbl_20, angle_A, lbl_40,
            angle_BCM, angle_MCA, lbl_60
        )
        
        scene_objects.scale(0.8)
        scene_objects.shift(DOWN * 1 + LEFT * 1)
        
        # Text
        text = VGroup(
            MathTex(r"\text{Given: } \angle A=40^\circ, \angle B=20^\circ, AB-BC=5"),
            MathTex(r"\text{Construct } D \in AB \text{ such that } BD=BC"),
            MathTex(r"\implies \triangle BCD \text{ is isosceles } (20^\circ, 80^\circ, 80^\circ)"),
            MathTex(r"AD = AB - BD = AB - BC = 5"),
            MathTex(r"\angle ADC = 180^\circ - 80^\circ = 100^\circ"),
            MathTex(r"\angle ACD = 180^\circ - 40^\circ - 100^\circ = 40^\circ"),
            MathTex(r"\implies \triangle ADC \text{ is isosceles } \implies CD = AD = 5"),
            MathTex(r"\text{In } \triangle CDM: \angle DCM = 80^\circ - 60^\circ = 20^\circ"),
            MathTex(r"\angle CDM = 80^\circ \implies \angle CMD = 80^\circ"),
            MathTex(r"\implies \triangle CDM \text{ is isosceles } \implies CM = CD = 5")
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT).scale(0.6)
        
        self.add(scene_objects)
        self.add(text)
