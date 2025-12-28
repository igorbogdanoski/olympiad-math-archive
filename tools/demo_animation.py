from manim import *

class Task_2022_mun_y3_20b(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # Wall
        wall = Rectangle(width=6, height=0.5, color=GREY, fill_opacity=1).move_to(UP*2)
        wall_text = Text("Wall", font_size=24, color=WHITE).move_to(wall.get_center())
        
        # Fence
        # x=1.5, y=3 (scaled 8 and 16)
        fence = VMobject()
        fence.set_points_as_corners([LEFT*1.5 + UP*1.75, LEFT*1.5 + DOWN*1.25, RIGHT*1.5 + DOWN*1.25, RIGHT*1.5 + UP*1.75])
        fence.set_color(RED).set_stroke(width=4)
        
        # Labels
        lx1 = MathTex('x').next_to(fence, LEFT)
        lx2 = MathTex('x').next_to(fence, RIGHT)
        ly = MathTex('y').next_to(fence, DOWN)
        area = MathTex('P = xy').move_to(ORIGIN)
        
        # Animation
        self.play(DrawBorderThenFill(wall))
        self.play(Write(wall_text))
        self.wait(0.5)
        self.play(Create(fence))
        self.play(Write(lx1), Write(lx2), Write(ly))
        self.wait(0.5)
        self.play(Write(area))
        self.wait(2)
