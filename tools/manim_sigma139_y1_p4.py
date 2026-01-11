from manim import *

class SolutionScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        axes = Axes(
            x_range=[-1, 6, 1],
            y_range=[-3, 5, 1],
            axis_config={"color": BLACK},
            x_length=7,
            y_length=6
        ).shift(UP*0.5)
        
        labels = axes.get_axis_labels(x_label="x", y_label="y").set_color(BLACK)
        
        b_val = 2.5
        
        O = axes.c2p(0, 0)
        P = axes.c2p(0, b_val)
        Q = axes.c2p(b_val, 0)
        R = axes.c2p(4, 0)
        S = axes.c2p(4, b_val - 4)
        
        line = axes.plot(lambda x: -x + b_val, color=BLUE)
        line_label = MathTex("y = -x + b", color=BLUE).next_to(line, UR).shift(LEFT*2)
        
        vline = Line(axes.c2p(4, 2), axes.c2p(4, -3), color=BLACK)
        
        tri_QOP = Polygon(O, Q, P, fill_opacity=0.3, fill_color=GREEN, color=GREEN, stroke_width=2)
        tri_QRS = Polygon(Q, R, S, fill_opacity=0.3, fill_color=RED, color=RED, stroke_width=2)
        
        label_O = MathTex("O", color=BLACK, font_size=32).next_to(O, DL, buff=0.15)
        label_P = MathTex("P(0,b)", color=BLACK, font_size=28).next_to(P, LEFT, buff=0.15)
        label_Q = MathTex("Q(b,0)", color=BLACK, font_size=28).next_to(Q, DL, buff=0.15)
        label_R = MathTex("R(4,0)", color=BLACK, font_size=28).next_to(R, UR, buff=0.15)
        label_S = MathTex("S", color=BLACK, font_size=32).next_to(S, RIGHT, buff=0.15)
        
        self.add(axes, labels, line, line_label, vline)
        self.add(label_O, label_P, label_Q, label_R, label_S)
        self.add(tri_QOP, tri_QRS)
        
        brace_b = Brace(Line(O, Q), DOWN, color=BLACK)
        text_b = brace_b.get_text("b").set_color(BLACK)
        
        brace_4mb = Brace(Line(Q, R), UP, color=BLACK)
        text_4mb = brace_4mb.get_text("4-b").set_color(BLACK)
        
        self.add(brace_b, text_b, brace_4mb, text_4mb)
        
        calc1 = MathTex(r"\frac{P_{\triangle QRS}}{P_{\triangle QOP}} = \frac{9}{25}", color=BLACK, font_size=36).to_corner(UL).shift(DOWN*0.5)
        calc2 = MathTex(r"\left(\frac{4-b}{b}\right)^2 = \left(\frac{3}{5}\right)^2", color=BLACK, font_size=36).next_to(calc1, DOWN, buff=0.3)
        calc3 = MathTex(r"b = 2.5", color=RED, font_size=40).next_to(calc2, DOWN, buff=0.3)
        
        self.add(calc1, calc2, calc3)
