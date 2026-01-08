from manim import *

class SquareDissection(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Title
        title = Text("Поделба на квадрат (n=6)", font_size=40, color=BLACK).to_edge(UP)
        self.play(Write(title))
        
        # Main Square
        L = 4
        big_square = Square(side_length=L, color=BLACK, stroke_width=4)
        self.play(Create(big_square))
        self.wait(1)
        
        # Construction for n=6 (L-method with k=3)
        # Big inner square (2/3 of side)
        # 5 small squares (1/3 of side)
        
        unit = L / 3
        
        # The large sub-square (2x2 units)
        sq_large = Square(side_length=2*unit, color=BLUE, fill_opacity=0.2)
        sq_large.align_to(big_square, UL)
        
        # The small squares
        small_squares = VGroup()
        # Bottom row (3 squares)
        for i in range(3):
            s = Square(side_length=unit, color=RED, fill_opacity=0.2)
            s.align_to(big_square, DL).shift(RIGHT * i * unit)
            small_squares.add(s)
            
        # Right column (2 squares remaining)
        for i in range(2):
            s = Square(side_length=unit, color=RED, fill_opacity=0.2)
            s.align_to(big_square, UR).shift(DOWN * i * unit)
            small_squares.add(s)
            
        self.play(DrawBorderThenFill(sq_large))
        self.play(DrawBorderThenFill(small_squares))
        
        # Labels
        count_text = MathTex("1 + 5 = 6 \\text{ квадрати}", color=BLACK).next_to(big_square, DOWN)
        self.play(Write(count_text))
        self.wait(2)
        
        # Transition to n=7 (Subdivision)
        self.play(FadeOut(sq_large), FadeOut(small_squares), FadeOut(count_text), FadeOut(title))
        
        title2 = Text("Правило +3 (n=4 -> n=7)", font_size=40, color=BLACK).to_edge(UP)
        self.play(Write(title2))
        
        # Reset to n=4
        lines = VGroup(
            Line(big_square.get_top(), big_square.get_bottom(), color=BLACK),
            Line(big_square.get_left(), big_square.get_right(), color=BLACK)
        )
        self.play(Create(lines))
        self.wait(1)
        
        # Subdivide top-left
        sub_lines = VGroup(
            Line(big_square.get_corner(UL), big_square.get_center(), color=BLACK).scale(0.5).shift(UL * L/4 + DR * L/4), # Wait, simpler logic
            Line(UP*L/2 + LEFT*L/2, UP*L/2, color=BLACK).move_to(big_square.get_corner(UL) + DR*L/4), # Horizontal
            Line(LEFT*L/2, LEFT*L/2 + UP*L/2, color=BLACK).move_to(big_square.get_corner(UL) + DR*L/4).rotate(PI/2) # Vertical
        )
        
        # Correct manual placement for subdivision
        center_ul = big_square.get_corner(UL) + DR * (L/4)
        h_line = Line(LEFT*L/2, ORIGIN, color=RED).move_to(center_ul)
        v_line = Line(UP*L/2, ORIGIN, color=RED).move_to(center_ul).rotate(PI/2)
        
        self.play(Create(h_line), Create(v_line))
        
        final_text = MathTex("4 - 1 + 4 = 7", color=BLACK).next_to(big_square, DOWN)
        self.play(Write(final_text))
        self.wait(2)