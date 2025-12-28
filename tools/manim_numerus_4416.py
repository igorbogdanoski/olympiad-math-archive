from manim import *

class Problem_numerus_4416(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Problem:
        # n-gon has 1011 times more diagonals than sides.
        # D_n = n(n-3)/2.
        # D_n = 1011 * n.
        # n(n-3)/2 = 1011 * n.
        # n-3 = 2022.
        # n = 2025.
        
        # m-gon A1...Am.
        # n = 405 * m.
        # 2025 = 405 * m.
        # m = 2025 / 405 = 5.
        # So m = 5. It is a regular pentagon.
        
        # Find angle A2 A1 A3.
        # In regular pentagon A1 A2 A3 A4 A5.
        # Angle A2 A1 A3.
        # Vertices are A1, A2, A3, A4, A5.
        # Angle A2 A1 A3 is angle subtended by side A2 A3 at vertex A1?
        # No, vertices are ordered A1, A2, A3...
        # Angle A2 A1 A3 is the angle between side A1 A2 and diagonal A1 A3.
        
        # Regular pentagon internal angle = (5-2)*180/5 = 3*180/5 = 108 degrees.
        # Triangle A1 A2 A3 is isosceles (A1 A2 = A2 A3).
        # Angle at A2 is 108.
        # Angles at A1 and A3 are (180 - 108)/2 = 72/2 = 36 degrees.
        # So Angle A2 A1 A3 = 36 degrees.
        
        # Visualization:
        # Draw a regular pentagon.
        # Label vertices A1 to A5.
        # Draw diagonal A1 A3.
        # Mark angle A2 A1 A3.
        
        pentagon = RegularPolygon(n=5, color=BLUE, fill_opacity=0.1).scale(2)
        
        # Vertices
        # Manim starts from right and goes counter-clockwise?
        # Let's get vertices.
        vertices = pentagon.get_vertices()
        # Let's label them A1 to A5.
        # A1 at top?
        # RegularPolygon usually starts at 0 degrees (Right).
        # Let's rotate it so A1 is at top.
        pentagon.rotate(PI/2 + PI/5) # Adjust rotation to have a vertex at top
        # Actually, let's just use the vertices as they are.
        
        A1 = vertices[0]
        A2 = vertices[1]
        A3 = vertices[2]
        A4 = vertices[3]
        A5 = vertices[4]
        
        # Labels
        lbl_A1 = Text("A1", font_size=24, color=BLACK).next_to(A1, UR, buff=0.1)
        lbl_A2 = Text("A2", font_size=24, color=BLACK).next_to(A2, UL, buff=0.1)
        lbl_A3 = Text("A3", font_size=24, color=BLACK).next_to(A3, DL, buff=0.1)
        lbl_A4 = Text("A4", font_size=24, color=BLACK).next_to(A4, DR, buff=0.1)
        lbl_A5 = Text("A5", font_size=24, color=BLACK).next_to(A5, RIGHT, buff=0.1)
        
        # Diagonal A1 A3
        diag = Line(A1, A3, color=RED)
        
        # Angle Mark
        angle_mark = Angle(Line(A1, A2), Line(A1, A3), radius=0.8, color=ORANGE)
        lbl_angle = MathTex("?", color=ORANGE).next_to(angle_mark, DOWN, buff=0.1)
        
        # Text
        text_n = MathTex("n = 2025", color=BLACK).to_corner(UL)
        text_m = MathTex("m = 5", color=BLACK).next_to(text_n, DOWN, aligned_edge=LEFT)
        
        self.add(pentagon)
        self.add(lbl_A1, lbl_A2, lbl_A3, lbl_A4, lbl_A5)
        self.add(diag)
        self.add(angle_mark, lbl_angle)
        self.add(text_n, text_m)
