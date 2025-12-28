from manim import *

class Problem_2022_mun_g9_10(Scene):
    def construct(self):
        # Scale
        scale = 0.25
        
        # Parameters
        r = 13.0
        c1 = 24.0
        c2 = 10.0
        
        d1 = np.sqrt(r**2 - (c1/2)**2) # 5
        d2 = np.sqrt(r**2 - (c2/2)**2) # 12
        
        # Coordinates
        O = ORIGIN
        
        # Chords are horizontal
        # Chord 1 at y = d1
        y1 = d1
        x1 = c1 / 2
        A1 = np.array([-x1, y1, 0])
        B1 = np.array([x1, y1, 0])
        
        # Chord 2 at y = d2
        y2 = d2
        x2 = c2 / 2
        A2 = np.array([-x2, y2, 0])
        B2 = np.array([x2, y2, 0])
        
        # Shift to center
        # Center is O.
        # Let's shift everything so that the chords are centered vertically?
        # No, keep O at origin.
        
        # Apply scale
        O *= scale
        A1 *= scale
        B1 *= scale
        A2 *= scale
        B2 *= scale
        r_sc = r * scale
        
        # Objects
        circle = Circle(radius=r_sc, color=BLUE, arc_center=O)
        
        chord1 = Line(A1, B1, color=YELLOW)
        chord2 = Line(A2, B2, color=YELLOW)
        
        # Distances
        # Line from O to midpoint of chord1
        M1 = (A1 + B1) / 2
        line_d1 = Line(O, M1, color=RED)
        
        # Line from O to midpoint of chord2
        M2 = (A2 + B2) / 2
        line_d2 = Line(O, M2, color=RED)
        
        # Radius to end of chord
        radius_line1 = Line(O, B1, color=GREEN)
        radius_line2 = Line(O, B2, color=GREEN)
        
        # Labels
        label_O = MathTex("O").next_to(O, DOWN)
        label_c1 = MathTex("c_1=24").next_to(chord1, UP, buff=0.05).scale(0.8)
        label_c2 = MathTex("c_2=10").next_to(chord2, UP, buff=0.05).scale(0.8)
        
        label_d1 = MathTex("d_1=5").next_to(line_d1, RIGHT, buff=0.05).scale(0.8)
        # d2 overlaps d1.
        # Let's label d2 on the left or use a brace
        brace_d2 = Brace(Line(O, M2), LEFT)
        label_d2 = brace_d2.get_text("$d_2=12$").scale(0.8)
        
        # Distance between chords
        brace_dist = Brace(Line(M1, M2), RIGHT)
        label_dist = brace_dist.get_text("$x=7$").scale(0.8)
        
        # Text
        text = MathTex(
            r"d_1 = \sqrt{13^2 - 12^2} = 5",
            r"d_2 = \sqrt{13^2 - 5^2} = 12",
            r"x = |d_2 - d_1| = 7"
        ).arrange(DOWN).to_corner(DL).scale(0.8)
        
        self.add(circle)
        self.add(chord1, chord2)
        self.add(line_d2) # Draw longer first
        self.add(line_d1)
        self.add(radius_line1, radius_line2)
        self.add(label_O, label_c1, label_c2)
        self.add(label_d1, brace_d2, label_d2)
        self.add(brace_dist, label_dist)
        self.add(text)
