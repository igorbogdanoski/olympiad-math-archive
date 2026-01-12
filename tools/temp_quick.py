from manim import *

class GenScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        A = np.array([0, 3, 0])
        B = np.array([-3, -1, 0])
        C = np.array([3, -1, 0])
        
        tri = Polygon(A, B, C, color=BLACK, stroke_width=4)
        label_a = MathTex("a").move_to((B+C)/2 + DOWN*0.3)
        label_b = MathTex("b").move_to((A+C)/2 + RIGHT*0.3)
        label_c = MathTex("c").move_to((A+B)/2 + LEFT*0.3)
        
        formula = MathTex(r"P = \frac{M}{4N}", color=BLACK).scale(1.5).to_edge(DOWN)
        rect = SurroundingRectangle(formula, color=BLACK, buff=0.2)
        
        self.add(tri, label_a, label_b, label_c, formula, rect)
