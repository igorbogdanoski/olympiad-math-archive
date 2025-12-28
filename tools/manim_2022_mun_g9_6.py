from manim import *

class Problem_2022_mun_g9_6(Scene):
    def construct(self):
        # Scale
        scale = 0.8
        
        # Parameters
        # R = 3r
        # AB = 12
        # OM = r
        # OM is midline, so OM = AB / 2 = 6
        # r = 6
        # R = 3r = 18
        
        r = 6.0
        R = 18.0
        AB = 12.0
        
        # Coordinates
        O = ORIGIN
        
        # C at (R, 0), A at (-R, 0)
        C = RIGHT * R
        A = LEFT * R
        
        # B is on circle K1 such that BC is tangent to K2.
        # Tangent from C to K2.
        # Distance OC = R = 3r.
        # Angle OCM: sin(angle) = r / R = 1/3.
        angle_C = np.arcsin(1/3)
        
        # B is intersection of line CM with K1.
        # Line CM is at angle (180 - angle_C) or (180 + angle_C) relative to positive x-axis?
        # C is at (R, 0).
        # Let's rotate everything so C is at (R, 0).
        # Tangent line from C goes "up-left".
        # Angle of line CB relative to CA (x-axis) is angle_C? No.
        # In triangle OMC (M is tangent point), angle OMC = 90.
        # sin(OCM) = OM/OC = r/R = 1/3.
        # So angle BCA = arcsin(1/3).
        
        # B coordinates:
        # B is on K1. Angle BCA is known.
        # In right triangle ABC (angle B is 90 because AC is diameter),
        # AB = AC * sin(BCA) = 2R * (1/3) = 2/3 R.
        # We are given AB = 12.
        # 12 = 2/3 R => R = 18. Correct.
        
        # Coordinates of B
        # Angle AOB = 2 * Angle ACB (central angle theorem) ? No.
        # Angle COB = 2 * Angle CAB?
        # Let's find B directly.
        # C = (R, 0). A = (-R, 0).
        # B = (R cos(theta), R sin(theta)).
        # Vector CB = B - C.
        # Distance from O to line CB is r.
        
        # Let's use the angle alpha = arcsin(1/3).
        # B is at angle (180 - 2*alpha) from C?
        # In isosceles triangle OBC? No.
        # In right triangle ABC:
        # Angle A = 90 - alpha.
        # B = (R cos(2*alpha + pi), R sin(2*alpha + pi))?
        # Let's just place B using geometry.
        # Angle at C is alpha.
        # B = C + vector of length BC at angle (180 - alpha).
        # BC = AC * cos(alpha) = 2R * sqrt(1 - 1/9) = 2R * sqrt(8)/3.
        
        # Easier:
        # Rotate C by 2*alpha? No.
        # Angle BOC = 180 - 2*alpha.
        # B is at angle (180 - 2*alpha) relative to OC?
        # Let's check. Triangle OBC is isosceles. Angle OCB = alpha. Angle OBC = alpha.
        # Angle COB = 180 - 2*alpha.
        # So B is at angle (180 - 2*alpha) from positive x-axis?
        # Wait, C is at 0 degrees (relative to O).
        # B is at 180 - 2*alpha.
        
        alpha = np.arcsin(1/3)
        theta_B = np.pi - 2 * alpha
        
        B = np.array([R * np.cos(theta_B), R * np.sin(theta_B), 0])
        
        # Tangent point M
        # M is midpoint of BC (since OM perp BC and Triangle OBC is isosceles? No.)
        # OM is radius to tangent. OM perp BC.
        # Triangle OBC is isosceles (OB=OC=R).
        # Altitude OM bisects base BC. So M is midpoint of BC.
        M = (B + C) / 2
        
        # Shift to center
        # Already centered at O.
        
        # Apply scale
        O *= scale
        A *= scale
        B *= scale
        C *= scale
        M *= scale
        r_sc = r * scale
        R_sc = R * scale
        
        # Objects
        k1 = Circle(radius=R_sc, color=BLUE, arc_center=O)
        k2 = Circle(radius=r_sc, color=GREEN, arc_center=O)
        
        diameter = Line(A, C, color=WHITE)
        chord = Line(B, C, color=YELLOW)
        side_AB = Line(A, B, color=YELLOW)
        
        radius_OM = Line(O, M, color=RED)
        
        dot_O = Dot(O, color=WHITE)
        dot_A = Dot(A, color=WHITE)
        dot_B = Dot(B, color=WHITE)
        dot_C = Dot(C, color=WHITE)
        dot_M = Dot(M, color=RED)
        
        label_O = MathTex("O").next_to(dot_O, DOWN)
        label_A = MathTex("A").next_to(dot_A, LEFT)
        label_B = MathTex("B").next_to(dot_B, UP)
        label_C = MathTex("C").next_to(dot_C, RIGHT)
        label_M = MathTex("M").next_to(dot_M, UR)
        
        label_AB = MathTex("12").next_to(side_AB, LEFT)
        label_r = MathTex("r").next_to(radius_OM, RIGHT, buff=0.05)
        
        # Right angles
        ra_B = RightAngle(Line(B, A), Line(B, C), length=0.4) # Angle ABC is 90
        ra_M = RightAngle(Line(M, O), Line(M, C), length=0.3) # Angle OMC is 90
        
        # Text
        text = MathTex(
            r"OM \parallel AB \implies OM = \frac{AB}{2} = 6",
            r"r = 6 \implies R = 3r = 18"
        ).arrange(DOWN).to_corner(UL).scale(0.8)
        
        self.add(k1, k2)
        self.add(diameter, chord, side_AB, radius_OM)
        self.add(dot_O, dot_A, dot_B, dot_C, dot_M)
        self.add(label_O, label_A, label_B, label_C, label_M)
        self.add(label_AB, label_r)
        self.add(ra_B, ra_M)
        self.add(text)
