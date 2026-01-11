from manim import *

class IrrationalEquationScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        title = Text("Iracionalna Ravnenka so Smena", color=DARK_BLUE, font_size=36).to_edge(UP)
        self.add(title)
        
        original = MathTex(r"\sqrt{5 + \sqrt[3]{x}} + \sqrt{5 - \sqrt[3]{x}} = \sqrt[3]{x}", color=BLACK, font_size=32).shift(UP*2.5)
        self.add(original)
        
        step1_label = Text("Smena:", color=DARK_BLUE, font_size=24).shift(UP*1.5 + LEFT*3)
        step1_eq = MathTex(r"t = \sqrt[3]{x}", color=BLUE, font_size=28).next_to(step1_label, RIGHT, buff=0.3)
        self.add(step1_label, step1_eq)
        
        step2_label = Text("Posle smena:", color=DARK_BLUE, font_size=24).shift(UP*0.7 + LEFT*3)
        step2_eq = MathTex(r"\sqrt{5 + t} + \sqrt{5 - t} = t", color=BLUE, font_size=28).next_to(step2_label, RIGHT, buff=0.3)
        self.add(step2_label, step2_eq)
        
        step3_label = Text("Domein:", color=DARK_BLUE, font_size=24).shift(DOWN*0.1 + LEFT*3)
        step3_eq = MathTex(r"t \in [0, 5]", color=RED, font_size=28).next_to(step3_label, RIGHT, buff=0.3)
        self.add(step3_label, step3_eq)
        
        step4_label = Text("Resenie:", color=DARK_BLUE, font_size=24).shift(DOWN*0.9 + LEFT*3)
        step4_eq = MathTex(r"t = 4", color=GREEN, font_size=28).next_to(step4_label, RIGHT, buff=0.3)
        self.add(step4_label, step4_eq)
        
        step5_label = Text("Povratak:", color=DARK_BLUE, font_size=24).shift(DOWN*1.7 + LEFT*3)
        step5_eq = MathTex(r"x = 4^3 = 64", color=GREEN, font_size=28).next_to(step5_label, RIGHT, buff=0.3)
        self.add(step5_label, step5_eq)
