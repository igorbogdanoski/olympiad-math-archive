from manim import *
import numpy as np

class GeometryScene(Scene):
    def construct(self):
        # Parameters
        # Parallelogram BADC
        # B bottom-left, A top-left, D top-right, C bottom-right?
        # Usually ABCD is counter-clockwise.
        # BADC implies B->A->D->C.
        # So BA // CD and BC // AD? No.
        # In BADC, sides are BA, AD, DC, CB.
        # So BA // DC and AD // CB.
        # Angle B = 40.
        # Angle CAD = 57.
        # Find ACD.
        
        angle_B = 40 * DEGREES
        # Let B = (0,0)
        B = ORIGIN
        # A is somewhere. Let side BA length = 3.
        # Angle B is interior angle at B.
        # If BADC is parallelogram, then angle at B + angle at A = 180?
        # Adjacent angles sum to 180.
        # Angle A = 180 - 40 = 140.
        # Angle CAD is part of Angle A.
        # Angle A = Angle BAC + Angle CAD.
        # 140 = Angle BAC + 57.
        # Angle BAC = 140 - 57 = 83.
        
        # Coordinates
        # B at origin
        # C on x-axis? No, usually AB is horizontal or BC is horizontal.
        # Let's assume BC is horizontal.
        # C = (5, 0).
        # A = (3 * cos(40), 3 * sin(40)). No, angle B is ABC.
        # If BC is horizontal, A is at angle 40? No, angle B is usually interior.
        # Let's assume standard orientation.
        # B = (0,0). C = (5,0).
        # A = (3*cos(40), 3*sin(40))? No, angle B is ABC.
        # If BADC is parallelogram, vertices are B, A, D, C in order around perimeter?
        # Or B, A, D, C are vertices.
        # Sides: BA, AD, DC, CB.
        # So BA // CD and AD // BC.
        # Angle B (ABC) = 40.
        # Angle A (BAD) = 180 - 40 = 140.
        # Angle D (ADC) = 40.
        # Angle C (DCB) = 140.
        
        # Given: Angle CAD = 57.
        # Find Angle ACD.
        # In triangle ADC:
        # Angle D = 40.
        # Angle CAD = 57.
        # Angle ACD = 180 - (40 + 57) = 180 - 97 = 83.
        
        # Let's verify with alternate interior angles.
        # AD // BC.
        # Transversal AC.
        # Angle CAD = Angle ACB (alternate interior).
        # So Angle ACB = 57.
        # Angle C (whole) = 140.
        # Angle ACD = Angle C - Angle ACB = 140 - 57 = 83.
        # Matches.
        
        # Coordinates for Manim
        # B = (0,0)
        # C = (5,0)
        # Angle B = 40? No, Angle B is ABC.
        # If AD // BC, and Angle B = 40.
        # Then A is at (x, y) such that vector BA makes angle?
        # Wait, if BC is horizontal, and Angle ABC = 40.
        # Then A is on a ray from B at 40 degrees? No, usually B is bottom left.
        # If A is top left, B is bottom left.
        # Then Angle ABC is angle at B.
        # If BC is horizontal, AB makes angle 40? No, interior angle is 40.
        # If A is "above" B, and C is "right" of B.
        # Then angle is 180-40? No.
        # Let's assume standard parallelogram shape /_
        # B bottom left. C bottom right.
        # A top left. D top right.
        # Angle at B is acute (40).
        # So A is shifted right? No, shifted left?
        # If A is (x, h), B is (0,0).
        # Vector BA is (-x, -h). Vector BC is (w, 0).
        # Angle is 40.
        # Let's place B at origin. C at (5,0).
        # A at (3 * cos(40), 3 * sin(40)).
        # Then Angle ABC is 40? No, that would be if A is to the right.
        # If A is to the right, it's acute.
        # D = A + C = (3cos40 + 5, 3sin40).
        # This is a parallelogram.
        # Angle B = 40.
        # Angle A = 140.
        # Angle D = 40.
        # Angle C = 140.
        
        # Check CAD = 57.
        # A = (2.29, 1.92). D = (7.29, 1.92). C = (5, 0).
        # Vector AC = C - A = (2.71, -1.92).
        # Vector AD = D - A = (5, 0).
        # Angle CAD is angle between AC and AD.
        # tan(CAD) = 1.92 / 2.71 = 0.708.
        # atan(0.708) = 35 degrees.
        # We need CAD = 57.
        # So we need to adjust the shape.
        # Angle D is fixed at 40.
        # Angle CAD depends on the aspect ratio (lengths of sides).
        # In triangle ADC, by Sine Rule:
        # CD / sin(57) = AC / sin(40) = AD / sin(83).
        # We can set AD = 5 (visual length).
        # Then CD = 5 * sin(57) / sin(83).
        # And AC = 5 * sin(40) / sin(83).
        
        AD_len = 5
        CD_len = AD_len * np.sin(57*DEGREES) / np.sin(83*DEGREES)
        
        # Construct points
        # D at (0,0) for easier calculation, then move.
        # Let D = (0,0).
        # A = (-5, 0). (AD is horizontal).
        # C is at angle -140 (or 220) from D? No, Angle D is 40.
        # Line DC makes angle 180+40? No.
        # Let's place D at top right.
        # A at top left.
        # AD is horizontal.
        # Angle ADC = 40.
        # So DC goes down-left at angle 40 relative to DA?
        # Angle between DA (Left) and DC.
        # Let's use standard coordinates.
        # A = (0, 3). D = (5, 3).
        # Angle ADC = 40.
        # DC vector: length CD_len, angle -140 degrees (from positive x).
        # C = D + CD_len * (cos(-140), sin(-140)).
        # B = A + (C - D).
        
        D = np.array([2.5, 2, 0])
        A = D + LEFT * AD_len
        C = D + CD_len * np.array([np.cos((180+40)*DEGREES), np.sin((180+40)*DEGREES), 0])
        B = A + (C - D)
        
        # Create objects
        parallelogram = Polygon(A, B, C, D, color=BLUE, stroke_width=2)
        diagonal_AC = Line(A, C, color=YELLOW)
        
        # Labels
        label_A = MathTex("A").next_to(A, UP)
        label_B = MathTex("B").next_to(B, DOWN)
        label_C = MathTex("C").next_to(C, DOWN)
        label_D = MathTex("D").next_to(D, UP)
        
        # Angles
        # Angle B = 40
        angle_B_arc = Angle(Line(B,C), Line(B,A), radius=0.5, color=RED)
        label_40 = MathTex("40^\circ").next_to(angle_B_arc, UP+RIGHT)
        
        # Angle CAD = 57
        angle_CAD_arc = Angle(Line(A,D), Line(A,C), radius=0.7, color=GREEN)
        label_57 = MathTex("57^\circ").next_to(angle_CAD_arc, RIGHT+DOWN)
        
        # Angle ACD = ?
        angle_ACD_arc = Angle(Line(C,A), Line(C,D), radius=0.6, color=ORANGE)
        label_q = MathTex("?").next_to(angle_ACD_arc, UP+LEFT)
        
        # Grouping
        scene_objects = VGroup(
            parallelogram, diagonal_AC,
            label_A, label_B, label_C, label_D,
            angle_B_arc, label_40,
            angle_CAD_arc, label_57,
            angle_ACD_arc, label_q
        )
        
        scene_objects.scale(0.8)
        scene_objects.move_to(ORIGIN + LEFT * 2)
        
        # Explanation text
        text_group = VGroup(
            MathTex(r"\text{Parallelogram } BADC \implies AD \parallel BC, AB \parallel CD"),
            MathTex(r"\angle D = \angle B = 40^\circ \text{ (Opposite angles)}"),
            MathTex(r"\text{In } \triangle ADC:"),
            MathTex(r"\angle CAD + \angle D + \angle ACD = 180^\circ"),
            MathTex(r"57^\circ + 40^\circ + \angle ACD = 180^\circ"),
            MathTex(r"97^\circ + \angle ACD = 180^\circ"),
            MathTex(r"\angle ACD = 180^\circ - 97^\circ = 83^\circ")
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT).scale(0.8)
        
        self.add(scene_objects)
        self.add(text_group)
