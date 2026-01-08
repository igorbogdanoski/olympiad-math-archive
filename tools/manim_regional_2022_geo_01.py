from manim import *

class Problem_regional_2022_geo_01(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Isosceles Triangle ABC (AC=BC).
        # Point D on AC such that AD=AB.
        # Angle ABD = 15 degrees.
        # Find angles of ABC.
        
        # Let Angle BAC = alpha.
        # Since AC=BC, Angle ABC = alpha.
        # Angle C = 180 - 2*alpha.
        
        # Triangle ABD is isosceles with AD=AB.
        # So Angle ADB = Angle ABD = 15 degrees? No.
        # AD=AB means triangle ABD is isosceles with base BD.
        # So Angle ADB = Angle ABD? No.
        # Sides AD and AB are equal.
        # So angles opposite to them are equal.
        # Angle opposite to AD is Angle ABD = 15.
        # Angle opposite to AB is Angle ADB.
        # So Angle ADB = 15.
        # Then Angle DAB = 180 - 15 - 15 = 150.
        # Angle DAB is Angle A of triangle ABC.
        # So alpha = 150.
        # But sum of angles in ABC is 180.
        # If A = 150, B = 150 (since AC=BC). Sum = 300 > 180. Impossible.
        
        # Re-read: "AD=AB".
        # Triangle ABD has sides AB and AD equal.
        # So it is isosceles.
        # The vertex is A.
        # The base angles are at B and D.
        # Angle ABD = Angle ADB.
        # We are given Angle ABD = 15?
        # No, "Angle ABD = 15".
        # Wait, if AD=AB, then Angle ADB = Angle ABD.
        # So Angle ADB = 15?
        # Then Angle A = 180 - 15 - 15 = 150.
        # Same contradiction.
        
        # Maybe D is on extension? "Na krakot AC izbrana e tocka D". Usually means segment AC.
        # Maybe AC=BC is the main triangle.
        # Maybe Angle ABD is part of Angle B?
        # Angle B = Angle ABC.
        # Angle ABD = 15.
        # So Angle DBC = Angle B - 15.
        
        # Let's try another configuration.
        # Maybe AD=AB refers to base AB?
        # No, AD is segment on AC. AB is base.
        # If AD=AB, triangle ABD is isosceles at A.
        # Base angles are at B and D.
        # Angle ABD = Angle ADB.
        # If Angle ABD = 15, then Angle ADB = 15.
        # Then Angle A = 150.
        # If Angle A = 150, Angle B = 150 (since AC=BC). Impossible.
        
        # Is it possible that Angle ADB is the vertex angle?
        # No, AD=AB means A is the vertex where equal sides meet.
        # Wait. AD and AB meet at A.
        # So A is the vertex.
        # Base is BD.
        # Base angles are ABD and ADB.
        # So ABD = ADB.
        
        # Is it possible that D is such that AB=BD? No, says AD=AB.
        
        # Maybe the problem implies a specific order of vertices?
        # AC=BC. Base is AB.
        # Angle A = Angle B.
        # D on AC.
        # AD=AB.
        # This implies AC > AD = AB.
        # So AC > AB.
        # Triangle ABD is isosceles with vertex A.
        # Base angles are Angle ABD and Angle ADB.
        # Angle ABD is given as 15?
        # Wait. Angle ABD is part of Angle B (Angle ABC).
        # Angle ABC is base angle of large triangle.
        # Angle ABD is 15.
        # Angle ADB = Angle ABD = 15?
        # Then Angle A = 150.
        # Then Angle ABC = 150.
        # Contradiction.
        
        # Is it possible that Angle ADB is NOT equal to Angle ABD?
        # Only if AD != AB. But problem says AD=AB.
        
        # Maybe I am misinterpreting "AD=AB".
        # Could it be AB = BD? Or something else?
        # "AD=AB".
        
        # Let's check if Angle ABD could be the vertex angle of ABD?
        # No, B is a vertex. A is a vertex. D is a vertex.
        # Sides are AB, AD, BD.
        # AB = AD.
        # So triangle is isosceles with legs AB and AD.
        # Vertex is A.
        # Base angles are at B and D.
        # Angle ABD = Angle ADB.
        
        # Is it possible that Angle A is small?
        # If Angle A = alpha.
        # Angle B = alpha.
        # Angle C = 180 - 2alpha.
        # In Triangle ABD:
        # Angle A = alpha.
        # AB = AD.
        # So Angle ABD = Angle ADB = (180 - alpha) / 2.
        # We are given Angle ABD = 15?
        # (180 - alpha) / 2 = 15.
        # 180 - alpha = 30.
        # alpha = 150.
        # Again 150.
        
        # Is it possible that D is on the extension of AC?
        # "Na krakot AC". Usually means segment.
        
        # Maybe Angle ABD is NOT the base angle of ABD?
        # Angle ABD is the angle at B in triangle ABD.
        # Yes.
        
        # Is there any other interpretation?
        # Maybe AC=BC means C is vertex.
        # Maybe AB is not the base?
        # "Ramnokrak triagolnik ABC (AC=BC)".
        # C is vertex. AB is base.
        # Angle A = Angle B.
        
        # Maybe the text is wrong? Or my logic?
        # Let's assume the problem is solvable.
        # What if Angle ADB is the exterior angle?
        # No.
        
        # Let's search for this problem online or in context.
        # "Regional Competition 2022 Geo 01".
        # Maybe "AD=CD"? Or "BD=AB"?
        # If BD=AB, then Angle BDA = Angle BAD = alpha.
        # Angle ABD = 180 - 2alpha.
        # If ABD = 15, then 180 - 2alpha = 15 => 2alpha = 165 => alpha = 82.5.
        # Angle A = 82.5. Angle B = 82.5. Angle C = 15.
        # This works.
        
        # But text says "AD=AB".
        # Let's assume the text in the MD file is correct and I am missing something.
        # Or the text in the MD file is a typo.
        # "AD=AB".
        # If A=150, B=150, sum=300.
        # Maybe the triangle is A-C-B?
        # No, standard notation.
        
        # Let's assume it's a typo and it should be CD=AB? Unlikely.
        # Or maybe Angle DBC = 15?
        # If Angle DBC = 15.
        # Angle ABD = Angle B - 15 = alpha - 15.
        # In Triangle ABD (AB=AD):
        # Angle ABD = (180 - alpha)/2.
        # alpha - 15 = (180 - alpha)/2.
        # 2alpha - 30 = 180 - alpha.
        # 3alpha = 210.
        # alpha = 70.
        # If alpha = 70.
        # Angle A = 70. Angle B = 70. Angle C = 40.
        # Check:
        # Triangle ABD: A=70. AB=AD.
        # Base angles = (180-70)/2 = 55.
        # Angle ABD = 55.
        # Angle DBC = 70 - 55 = 15.
        # This fits "Angle DBC = 15".
        # But problem says "Angle ABD = 15".
        
        # What if Angle ABD = 15 is correct, but AD=AB is wrong?
        # Maybe AC=AB? No, AC=BC.
        
        # Let's visualize the "Impossible" case just to show the labels.
        # Or maybe I should visualize the "Angle DBC = 15" case which is a common variation (alpha=70).
        # Or maybe "Angle BAD = 15"?
        
        # Let's look at the file content again.
        # "AD=AB". "Angle ABD = 15".
        # This implies A=150.
        # If A=150, B=150.
        # This is only possible if geometry is non-Euclidean or I am misinterpreting "Ramnokrak".
        # Maybe AC=BC is NOT the main pair?
        # "Ramnokrak triagolnik ABC (AC=BC)".
        # This is explicit.
        
        # Okay, I will draw a generic isosceles triangle and label the given conditions.
        # I will not try to solve it perfectly if it's contradictory.
        # I will draw a triangle that looks isosceles.
        # I will mark AD=AB with ticks.
        # I will mark Angle ABD = 15.
        # I will put a question mark for angles.
        
        # Let's assume a shape where A is top vertex?
        # No, C is top vertex (AC=BC).
        # A and B are base.
        
        C = np.array([0, 3, 0])
        A = np.array([-1, 0, 0])
        B = np.array([1, 0, 0])
        # This is isosceles.
        
        # D on AC.
        # Let's place D somewhere on AC.
        D = A + 0.6 * (C - A)
        
        # Draw Triangle ABC
        tri = Polygon(A, B, C, color=BLUE, fill_opacity=0.1)
        
        # Draw Line BD
        line_BD = Line(B, D, color=RED)
        
        # Mark AD = AB
        # Tick on AD
        tick_AD = Line(A, D).get_center()
        # Tick on AB
        tick_AB = Line(A, B).get_center()
        
        ticks = VGroup(
            Line(tick_AD + LEFT*0.1, tick_AD + RIGHT*0.1, color=RED).rotate(PI/4),
            Line(tick_AB + UP*0.1, tick_AB + DOWN*0.1, color=RED).rotate(PI/4)
        )
        
        # Mark Angle ABD = 15
        angle_mark = Angle(Line(B, A), Line(B, D), radius=0.6, color=ORANGE)
        lbl_15 = MathTex(r"15^\circ", color=ORANGE, font_size=24).next_to(angle_mark, UP, buff=0.05)
        
        # Labels
        lbl_A = Text("A", font_size=24, color=BLACK).next_to(A, DL, buff=0.1)
        lbl_B = Text("B", font_size=24, color=BLACK).next_to(B, DR, buff=0.1)
        lbl_C = Text("C", font_size=24, color=BLACK).next_to(C, UP, buff=0.1)
        lbl_D = Text("D", font_size=24, color=BLACK).next_to(D, UL, buff=0.1)
        
        self.add(tri)
        self.add(line_BD)
        self.add(ticks)
        self.add(angle_mark, lbl_15)
        self.add(lbl_A, lbl_B, lbl_C, lbl_D)
        
        # Text
        text = MathTex("AC=BC", color=BLACK).to_corner(UL)
        text2 = MathTex("AD=AB", color=BLACK).next_to(text, DOWN, aligned_edge=LEFT)
        self.add(text, text2)
