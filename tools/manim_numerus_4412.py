from manim import *

class Problem_numerus_4412(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Circle k with center O and radius r
        r = 2.5
        O = ORIGIN
        circle = Circle(radius=r, color=BLUE)
        
        # Points A and B on circle
        # C is on ray AB such that BC = r.
        # B is between A and C.
        # Line CO intersects circle at M. O is between M and C.
        # Angle ACM = 25 degrees.
        
        # Let's work backwards from the angle.
        # Let C be at some distance.
        # Angle OCM = 25 degrees.
        # Let C be on the x-axis for simplicity? No, let's put O at origin.
        # Line M-O-C. Let this be the horizontal line.
        # M at (-r, 0), O at (0,0), C at (d, 0).
        # Then angle ACM is angle between AC and MC.
        # Wait, M, O, C are collinear. So angle ACM is just angle between AC and the line MOC.
        # Let line MOC be the x-axis.
        # M = (-r, 0)
        # C = (d, 0) with d > r.
        # A and B are on the circle.
        # C, B, A are collinear.
        # BC = r.
        # Distance OB = r.
        # In triangle OBC, OB = BC = r. So triangle OBC is isosceles.
        # Angle BCO = 25 degrees (given as ACM).
        # So Angle BOC = 25 degrees.
        # Angle OBC = 180 - 25 - 25 = 130 degrees.
        # Angle OBA = 180 - 130 = 50 degrees (supplementary).
        # Triangle OAB is isosceles (OA=OB=r).
        # So Angle OAB = 50 degrees.
        # Angle AOB = 180 - 50 - 50 = 80 degrees.
        # We need Angle AOM.
        # M is on the line CO, on the opposite side of O from C.
        # So Angle AOM is exterior to AOB?
        # Angle MOC is 180.
        # Angle AOM = 180 - Angle AOC.
        # Angle AOC = Angle AOB + Angle BOC = 80 + 25 = 105.
        # Angle AOM = 180 - 105 = 75 degrees.
        # Wait, let's check the diagram.
        # M is on circle. O is between M and C.
        # So M is at (-r, 0), O(0,0), C(d,0).
        # A is at angle...
        # Angle BOC = 25. B is on circle.
        # B = (r * cos(25), r * sin(25)).
        # Wait, C is on x-axis. B is on circle.
        # Angle BCO = 25.
        # If C is at (d, 0), B is at (x_b, y_b).
        # This is getting complicated to calculate coordinates directly.
        # Let's use the angles we derived.
        
        # Derived angles:
        # Angle(CO, CB) = 25.
        # Let line CO be horizontal.
        # C is to the right. O is origin. M is to the left.
        # Line CBA is at 25 degrees to the horizontal.
        # Let's rotate everything so CO is horizontal.
        
        M = np.array([-r, 0, 0])
        C_dist = 6 # Arbitrary, but needs to fit BC=r.
        # Actually, position of C is determined by BC=r.
        # In triangle OBC, OB=r, BC=r. Angle BCO = 25.
        # So C is determined.
        # Let's place O at origin.
        # C at (d, 0).
        # B on circle. Angle BCO = 25.
        # B is intersection of circle and line from C at 155 degrees (180-25)?
        # No, angle BCO is 25.
        # Let's place C at (5, 0).
        # Line CB makes angle 180-25 = 155 with positive x-axis?
        # Or just 25 degrees slope?
        # Let's place C at (5,0).
        # Line passing through C with angle 155 degrees.
        # It intersects circle at B and A.
        # We need BC = r.
        # This implies a specific distance for C.
        # Let's construct by angles.
        
        # 1. Draw Circle O.
        # 2. Draw Line M-O-C horizontal.
        # 3. Draw Line from O at 25 degrees (Angle BOC).
        #    Wait, triangle OBC is isosceles with OB=BC=r.
        #    So Angle BOC = Angle BCO = 25.
        #    So B is at angle 25 degrees from C (relative to O).
        #    Wait, Angle(OC, OB) = 25?
        #    Yes.
        #    So B = (r * cos(25), r * sin(25))? No, C is on x-axis.
        #    Angle BOC = 25.
        #    So B is at angle 25 or -25. Let's say 25.
        #    B = (r * cos(25deg), r * sin(25deg)).
        #    C is on x-axis.
        #    BC must be r.
        #    Distance B to C.
        #    C = (x_c, 0).
        #    (x_c - r cos25)^2 + (0 - r sin25)^2 = r^2.
        #    x_c^2 - 2 x_c r cos25 + r^2 = r^2.
        #    x_c (x_c - 2 r cos25) = 0.
        #    x_c = 2 r cos25.
        
        val_cos25 = np.cos(25*DEGREES)
        x_c = 2 * r * val_cos25
        C = np.array([x_c, 0, 0])
        
        # B is at angle 25 from OC?
        # Let's check triangle OBC.
        # OB = r. BC = r.
        # Angle BCO = 25.
        # Angle BOC = 25.
        # Angle OBC = 130.
        # Yes.
        # So B is at angle 180 - 25 = 155 from C? No.
        # B is at angle 25 from O?
        # If B is at angle alpha, C is at angle 0.
        # Angle BOC = alpha.
        # So B is at 25 degrees.
        B = np.array([r * np.cos(25*DEGREES), r * np.sin(25*DEGREES), 0])
        
        # A is on the line CB extended.
        # Line CB passes through C and B.
        # A is the other intersection with circle.
        # Line CB direction:
        # Vector CB = B - C.
        # Extend to find A.
        # Or use symmetry/geometry.
        # Angle AOB = 2 * Angle ACB? No.
        # Triangle OAB is isosceles.
        # Angle OBA = 180 - Angle OBC = 180 - 130 = 50.
        # Angle OAB = 50.
        # Angle AOB = 180 - 50 - 50 = 80.
        # So A is at angle 25 + 80 = 105 degrees.
        A = np.array([r * np.cos(105*DEGREES), r * np.sin(105*DEGREES), 0])
        
        # M is intersection of CO and circle, O between M and C.
        # C is at (x_c, 0). O is (0,0).
        # M is at (-r, 0).
        M = np.array([-r, 0, 0])
        
        # Draw elements
        lbl_O = Text("O", font_size=24, color=BLACK).next_to(O, DOWN, buff=0.1)
        lbl_A = Text("A", font_size=24, color=BLACK).next_to(A, UP, buff=0.1)
        lbl_B = Text("B", font_size=24, color=BLACK).next_to(B, UR, buff=0.1)
        lbl_C = Text("C", font_size=24, color=BLACK).next_to(C, RIGHT, buff=0.1)
        lbl_M = Text("M", font_size=24, color=BLACK).next_to(M, LEFT, buff=0.1)
        
        line_MOC = Line(M, C, color=BLACK)
        line_ABC = Line(A, C, color=BLACK)
        line_OA = Line(O, A, color=BLUE)
        line_OB = Line(O, B, color=BLUE)
        
        # Angle Mark for ACM (25 deg)
        angle_ACM = Angle(Line(C, O), Line(C, B), radius=1, color=RED)
        lbl_25 = MathTex("25^\circ", color=RED, font_size=24).next_to(angle_ACM, LEFT, buff=0.1)
        
        # Target Angle AOM
        angle_AOM = Angle(Line(O, A), Line(O, M), radius=0.5, color=GREEN)
        lbl_target = MathTex("?", color=GREEN).next_to(angle_AOM, UL, buff=0.05)
        
        self.add(circle)
        self.add(line_MOC, line_ABC, line_OA, line_OB)
        self.add(lbl_O, lbl_A, lbl_B, lbl_C, lbl_M)
        self.add(angle_ACM, lbl_25)
        self.add(angle_AOM, lbl_target)
        
        # Add text
        text = MathTex("BC = r", color=BLACK).to_corner(UL)
        self.add(text)

