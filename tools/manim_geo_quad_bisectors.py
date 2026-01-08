from manim import *
import numpy as np

class Problem_geo_quad_bisectors(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Parameters
        # Convex quadrilateral ABCD with AC = BD.
        # Perpendicular bisectors of AD and BC intersect at P on AB.
        # Prove Angle DAB = Angle ABC.
        
        # This implies ABCD is an isosceles trapezoid or P is center of circumcircle?
        # If P is on AB, and PA = PD (since P on perp bisector of AD)
        # and PB = PC (since P on perp bisector of BC).
        # Also P is on AB.
        # So P is between A and B (or outside).
        # PA + PB = AB (if P is between).
        # We have PD = PA and PC = PB.
        # Also given AC = BD.
        # In triangles PAC and PBD:
        # PA = PD
        # PC = PB
        # AC = BD
        # So Triangle PAC is congruent to Triangle PBD (SSS).
        # Thus Angle APC = Angle BPD.
        # Also Angle APD is isosceles triangle angle.
        # Angle BPC is isosceles triangle angle.
        
        # Actually, if P is on AB, then A, P, B are collinear.
        # Triangle PAD is isosceles (PA=PD). Angle PAD = Angle PDA.
        # Triangle PBC is isosceles (PB=PC). Angle PBC = Angle PCB.
        
        # From congruence PAC = PBD:
        # Angle PAC = Angle PBD? No, Angle PAC corresponds to Angle PBD?
        # Vertices: P-A-C and P-D-B?
        # PA = PD. AC = DB. PC = PB.
        # So P-A-C corresponds to P-D-B.
        # So Angle PAC = Angle PDB.
        # And Angle PCA = Angle PBD.
        # And Angle APC = Angle DPB.
        
        # We want to prove Angle DAB = Angle ABC.
        # Angle DAB is Angle P AD (since P is on AB).
        # Angle ABC is Angle P BC (since P is on AB).
        
        # Wait, P is on AB.
        # Angle DAB is just Angle A of the quad.
        # Angle ABC is just Angle B of the quad.
        
        # Let's construct a symmetric figure.
        # Isosceles trapezoid works.
        # Let AB be horizontal.
        # AD = BC? Not necessarily given.
        # But AC = BD is given.
        # If it's an isosceles trapezoid, then AD=BC and angles are equal.
        
        # Let's try to construct such a quad.
        # Let P be origin (0,0).
        # A at (-2, 0), B at (3, 0).
        # P is on AB.
        # PA = 2. PB = 3.
        # D must be such that PD = PA = 2.
        # C must be such that PC = PB = 3.
        # Also AC = BD.
        # Let D = (2 cos alpha, 2 sin alpha).
        # Let C = (3 cos beta, 3 sin beta).
        # AC distance: A=(-2,0). |C - A| = |(3 cos beta + 2, 3 sin beta)|.
        # BD distance: B=(3,0). |D - B| = |(2 cos alpha - 3, 2 sin alpha)|.
        # |AC|^2 = (3c + 2)^2 + (3s)^2 = 9c^2 + 12c + 4 + 9s^2 = 13 + 12 cos beta.
        # |BD|^2 = (2c - 3)^2 + (2s)^2 = 4c^2 - 12c + 9 + 4s^2 = 13 - 12 cos alpha.
        # We need |AC| = |BD| => 13 + 12 cos beta = 13 - 12 cos alpha.
        # cos beta = -cos alpha.
        # beta = 180 - alpha (or 180 + alpha).
        # Since convex, alpha and beta should be in (0, 180).
        # So beta = 180 - alpha.
        # This means C and D are symmetric wrt y-axis (perp to AB at P? No).
        # D = (2 cos alpha, 2 sin alpha).
        # C = (3 cos(180-alpha), 3 sin(180-alpha)) = (-3 cos alpha, 3 sin alpha).
        # Wait, x_C = -3 cos alpha. x_D = 2 cos alpha.
        # y_C = 3 sin alpha. y_D = 2 sin alpha.
        
        # Angle DAB?
        # Vector AD = D - A = (2c + 2, 2s).
        # Vector AB = (5, 0).
        # Angle at A is arg(AD).
        # tan A = 2s / (2c + 2) = s / (c + 1) = tan(alpha/2).
        # So Angle A = alpha/2.
        
        # Angle ABC?
        # Vector BC = C - B = (-3c - 3, 3s).
        # Vector BA = (-5, 0).
        # Angle at B is arg(BC) relative to BA?
        # Vector BA is angle 180.
        # Vector BC angle is 180 - beta/2?
        # Let's check slope.
        # slope BC = 3s / (-3(c+1)) = -s/(c+1) = -tan(alpha/2).
        # So angle of BC is 180 - alpha/2.
        # Angle ABC is 180 - (180 - alpha/2) = alpha/2?
        # Or just alpha/2.
        # Yes, Angle A = Angle B = alpha/2.
        
        # So we construct this specific case.
        # alpha = 120 degrees.
        # A = (-2, 0). B = (3, 0). P = (0, 0).
        # D = (2 cos 120, 2 sin 120) = (-1, sqrt(3)).
        # C = (-3 cos 120, 3 sin 120) = (1.5, 1.5*sqrt(3) approx 2.6).
        # Wait, beta = 180 - 120 = 60.
        # C = (3 cos 60, 3 sin 60) = (1.5, 2.6).
        
        # Let's verify AC = BD.
        # A=(-2,0), C=(1.5, 2.6). dx=3.5, dy=2.6. d^2 = 12.25 + 6.75 = 19.
        # B=(3,0), D=(-1, 1.73). dx=4, dy=1.73. d^2 = 16 + 3 = 19.
        # Matches.
        
        alpha = 120 * DEGREES
        beta = 60 * DEGREES
        
        P = np.array([0.0, 0.0, 0.0])
        A = np.array([-2.0, 0.0, 0.0])
        B = np.array([3.0, 0.0, 0.0])
        D = np.array([2.0 * np.cos(alpha), 2.0 * np.sin(alpha), 0.0])
        C = np.array([3.0 * np.cos(beta), 3.0 * np.sin(beta), 0.0])
        
        # Center view
        center = (A + B + C + D) / 4
        shift = -center
        
        A += shift
        B += shift
        C += shift
        D += shift
        P += shift
        
        # Scale
        scale = 1.2
        A *= scale
        B *= scale
        C *= scale
        D *= scale
        P *= scale
        
        # Elements
        quad = Polygon(A, B, C, D, color=BLUE, fill_opacity=0.1)
        diag_AC = DashedLine(A, C, color=GRAY)
        diag_BD = DashedLine(B, D, color=GRAY)
        
        # Perpendicular bisectors
        # Midpoint AD
        M_AD = (A + D) / 2
        # Vector AD = D - A. Perp vector (-dy, dx).
        perp_AD_vec = np.array([-(D[1]-A[1]), D[0]-A[0], 0.0])
        perp_AD_vec /= np.linalg.norm(perp_AD_vec)
        line_perp_AD = Line(M_AD - perp_AD_vec*3, M_AD + perp_AD_vec*3, color=RED)
        
        # Midpoint BC
        M_BC = (B + C) / 2
        perp_BC_vec = np.array([-(C[1]-B[1]), C[0]-B[0], 0.0])
        perp_BC_vec /= np.linalg.norm(perp_BC_vec)
        line_perp_BC = Line(M_BC - perp_BC_vec*3, M_BC + perp_BC_vec*3, color=RED)
        
        # Labels
        lbl_A = Text("A", font_size=24, color=BLACK).next_to(A, DL, buff=0.1)
        lbl_B = Text("B", font_size=24, color=BLACK).next_to(B, DR, buff=0.1)
        lbl_C = Text("C", font_size=24, color=BLACK).next_to(C, UR, buff=0.1)
        lbl_D = Text("D", font_size=24, color=BLACK).next_to(D, UL, buff=0.1)
        lbl_P = Text("P", font_size=24, color=BLACK).next_to(P, DOWN, buff=0.1)
        
        # Angles
        angle_A = Angle(Line(A, D), Line(A, B), radius=0.6, color=ORANGE)
        angle_B = Angle(Line(B, A), Line(B, C), radius=0.6, color=ORANGE)
        
        # Add to scene
        self.add(quad)
        self.add(diag_AC, diag_BD)
        self.add(line_perp_AD, line_perp_BC)
        self.add(lbl_A, lbl_B, lbl_C, lbl_D, lbl_P)
        self.add(angle_A, angle_B)
        
        # Add text info
        info = VGroup(
            MathTex("AC = BD", color=BLACK, font_size=24),
            MathTex(r"P = s_{AD} \\cap s_{BC} \\in AB", color=RED, font_size=24),
            MathTex(r"\\angle DAB = \\angle ABC", color=BLACK, font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UL)
        self.add(info)
