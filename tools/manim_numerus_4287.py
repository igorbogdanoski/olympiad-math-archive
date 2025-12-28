from manim import *

class Problem_numerus_4287(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Parallelogram ABCD.
        # Bisector of Angle CBA intersects ray AD at M.
        # DM = 5.
        # Perimeter = 42.
        
        # Let sides be a and b. AB = CD = a, BC = AD = b.
        # Bisector of B intersects AD extended at M.
        # AD is parallel to BC.
        # Transversal BM cuts parallel lines AD and BC.
        # Alternate interior angles: Angle AMB = Angle MBC.
        # Since BM is bisector, Angle ABM = Angle MBC.
        # Therefore, Angle AMB = Angle ABM.
        # Triangle ABM is isosceles with AB = AM.
        
        # M is on ray AD.
        # Case 1: M is on segment AD?
        # Or M is outside?
        # "polupravata AD" means ray starting at A passing through D.
        # So M can be beyond D.
        # AM = AD + DM (if D is between A and M) or AM = AD - DM (if M is between A and D).
        # Usually "intersects ray AD at M such that DM=5" implies order A-D-M or A-M-D.
        # If M is between A and D, then AM = AD - 5.
        # If D is between A and M, then AM = AD + 5.
        
        # Let's check geometry.
        # Angle B is obtuse or acute?
        # If B is acute, bisector goes inside.
        # If B is obtuse, bisector goes inside.
        # Ray AD is parallel to BC.
        # Bisector of B will intersect line AD.
        # Since ABM is isosceles (AB=AM), AM = a.
        # Also AD = b.
        # So AM = a.
        # Relationship between a and b?
        # Perimeter = 2(a+b) = 42 => a+b = 21.
        
        # Case 1: M is on extension of AD (A-D-M).
        # Then AM = AD + DM = b + 5.
        # So a = b + 5.
        # Substitute into a+b=21: (b+5) + b = 21 => 2b = 16 => b = 8.
        # Then a = 13.
        # Sides are 13 and 8.
        
        # Case 2: M is on segment AD (A-M-D).
        # Then AM = AD - DM = b - 5.
        # So a = b - 5.
        # Substitute: (b-5) + b = 21 => 2b = 26 => b = 13.
        # Then a = 8.
        # Sides are 8 and 13.
        
        # Both cases yield sides 8 and 13.
        # The problem asks for "lengths of sides".
        # So the answer is 8 and 13.
        
        # Visualization:
        # Let's draw one case, e.g., A-D-M.
        # a = 13, b = 8.
        # AB = 13, BC = 8.
        # AM = 13. AD = 8. DM = 5.
        # Triangle ABM is isosceles (13, 13, base BM).
        
        # Coordinates:
        # A at origin (0,0).
        # B at (13, 0)? No, let's make AB horizontal.
        # A(0,0), B(13,0).
        # D at (x, y). AD = 8.
        # M is on line AD. AM = 13.
        # M is at (13/8 * x, 13/8 * y).
        # Also BM bisects B.
        # Angle ABM = Angle MBC.
        # Line BC is parallel to AD.
        # So Angle MBC = Angle AMB (alternate).
        # So Angle ABM = Angle AMB.
        # Triangle ABM is isosceles with AB=AM=13.
        # So M must be at distance 13 from A.
        # We already used that.
        # We need to choose an angle for A.
        # Let Angle A = 60 degrees.
        # D = (8 cos 60, 8 sin 60) = (4, 4sqrt(3)).
        # M = (13 cos 60, 13 sin 60) = (6.5, 6.5sqrt(3)).
        # C = D + (B-A) = (4+13, 4sqrt(3)) = (17, 4sqrt(3)).
        
        # Let's scale down to fit screen.
        scale = 0.4
        
        A = np.array([0.0, 0.0, 0.0])
        B = np.array([13.0, 0.0, 0.0])
        D = np.array([4.0, 6.92, 0.0]) # 4sqrt(3) approx 6.92
        C = np.array([17.0, 6.92, 0.0])
        M = np.array([6.5, 11.25, 0.0]) # Wait, M is on ray AD.
        # Ray AD direction is (4, 6.92). Unit vector (0.5, 0.866).
        # AM length 13.
        # M = 13 * (0.5, 0.866) = (6.5, 11.25).
        
        # Shift to center
        center = (A + C) / 2
        shift = -center
        
        A += shift
        B += shift
        C += shift
        D += shift
        M += shift
        
        # Apply scale
        A *= scale
        B *= scale
        C *= scale
        D *= scale
        M *= scale
        
        # Create shapes
        parallelogram = Polygon(A, B, C, D, color=BLUE, fill_opacity=0.1)
        
        # Line AM (Ray AD extended)
        line_AM = Line(A, M, color=BLACK)
        
        # Line BM (Bisector)
        line_BM = Line(B, M, color=RED)
        
        # Labels
        lbl_A = Text("A", font_size=24, color=BLACK).next_to(A, DL, buff=0.1)
        lbl_B = Text("B", font_size=24, color=BLACK).next_to(B, DR, buff=0.1)
        lbl_C = Text("C", font_size=24, color=BLACK).next_to(C, UR, buff=0.1)
        lbl_D = Text("D", font_size=24, color=BLACK).next_to(D, UL, buff=0.1)
        lbl_M = Text("M", font_size=24, color=BLACK).next_to(M, UP, buff=0.1)
        
        # Dimensions
        lbl_DM = MathTex("DM=5", color=BLACK, font_size=24).next_to(Line(D, M), LEFT, buff=0.1)
        
        # Angle marks
        angle_ABM = Angle(Line(B, A), Line(B, M), radius=0.8, color=ORANGE)
        angle_MBC = Angle(Line(B, M), Line(B, C), radius=0.7, color=ORANGE)
        
        # Text
        text_perim = MathTex("L = 42", color=BLACK).to_corner(UL)
        
        self.add(line_AM) # Draw ray first
        self.add(parallelogram)
        self.add(line_BM)
        self.add(lbl_A, lbl_B, lbl_C, lbl_D, lbl_M)
        self.add(lbl_DM)
        self.add(angle_ABM, angle_MBC)
        self.add(text_perim)
