from manim import *
import numpy as np

class DigitDivisionScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        title = Text("Број со различни цифри", font_size=40, color=DARK_BLUE)
        title.to_edge(UP)
        self.add(title)
        
        problem_text = Text("N = 3750, и кога ќе ја избришеме 1-та цифра: 750", 
                           font_size=28, color=DARK_GRAY)
        problem_text.next_to(title, DOWN, buff=0.5)
        self.add(problem_text)
        
        original_group = VGroup()
        original_label = Text("Оригинален број:", font_size=24, color=BLACK)
        original_label.shift(LEFT * 3 + DOWN * 1.5)
        
        original_digits = VGroup()
        digits_3750 = "3750"
        x_pos = -1.5
        colors_orig = [YELLOW, GREEN, BLUE, RED]
        for i, (digit, color) in enumerate(zip(digits_3750, colors_orig)):
            d = Text(digit, font_size=48, color=color, weight=BOLD)
            d.shift(RIGHT * (x_pos + i * 0.6))
            d.shift(DOWN * 1.5)
            original_digits.add(d)
            
            if i == 0:
                box = Rectangle(height=0.8, width=0.5, color=color, stroke_width=3)
                box.move_to(d)
                original_digits.add(box)
        
        self.add(original_label, original_digits)
        
        equation = Text("3750 = 5 × 750", font_size=32, color=DARK_BLUE, weight=BOLD)
        equation.shift(DOWN * 3.2)
        self.add(equation)
        
        division_line = Line(LEFT * 3.5, RIGHT * 3.5, stroke_width=2, color=BLACK)
        division_line.shift(DOWN * 2.8)
        self.add(division_line)
        
        remaining_label = Text("Остаток по бришење на 1-та цифра:", font_size=24, color=BLACK)
        remaining_label.shift(LEFT * 3 + DOWN * 3.8)
        
        remaining_digits = VGroup()
        digits_750 = "750"
        x_pos_rem = -0.6
        colors_rem = [GREEN, BLUE, RED]
        for i, (digit, color) in enumerate(zip(digits_750, colors_rem)):
            d = Text(digit, font_size=48, color=color, weight=BOLD)
            d.shift(RIGHT * (x_pos_rem + i * 0.6))
            d.shift(DOWN * 3.8)
            remaining_digits.add(d)
        
        self.add(remaining_label, remaining_digits)
