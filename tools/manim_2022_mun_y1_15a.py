from manim import *
import numpy as np

class GeometryScene(Scene):
    def construct(self):
        # Parameters
        # Scale down for visualization
        scale_factor = 0.02
        L, W, H = 120, 100, 80
        l, w, h = 15, 8, 8
        
        # Create large block
        big_block = Cube(side_length=1).scale([L*scale_factor, H*scale_factor, W*scale_factor])
        big_block.set_color(BLUE).set_opacity(0.5)
        
        # Create small block
        small_block = Cube(side_length=1).scale([l*scale_factor*3, h*scale_factor*3, w*scale_factor*3]) # Exaggerate size
        small_block.set_color(RED).set_opacity(0.5)
        
        # Position
        big_block.move_to(LEFT * 3)
        small_block.move_to(RIGHT * 3)
        
        # Labels Big Block
        label_big = Text("Big Block").next_to(big_block, UP)
        label_L = MathTex("120").next_to(big_block, DOWN)
        label_W = MathTex("100").next_to(big_block, RIGHT).rotate(90*DEGREES)
        label_H = MathTex("80").next_to(big_block, LEFT)
        
        # Labels Small Block
        label_small = Text("Small Block (x1000)").next_to(small_block, UP)
        label_l = MathTex("15").next_to(small_block, DOWN)
        label_w = MathTex("x").next_to(small_block, RIGHT).rotate(90*DEGREES)
        label_h = MathTex("x").next_to(small_block, LEFT)
        
        # Arrow
        arrow = Arrow(start=small_block.get_left(), end=big_block.get_right(), buff=1)
        label_melt = Text("Melting").next_to(arrow, UP).scale(0.5)
        
        # Grouping
        scene_objects = VGroup(
            big_block, label_big, label_L, label_W, label_H,
            small_block, label_small, label_l, label_w, label_h,
            arrow, label_melt
        )
        
        scene_objects.scale(0.8)
        scene_objects.move_to(UP * 1)
        
        # Explanation text
        text_group = VGroup(
            MathTex(r"V_{big} = 120 \cdot 100 \cdot 80 = 960000 \text{ cm}^3"),
            MathTex(r"V_{small} = \frrac{V_{big}}{1000} = 960 \text{ cm}^3r),
            MathTex(r"V_{small} = 15 \cdot x \cdot x = 15x^2"),
            MathTex(r"15x^2 = 960 \implies x^2 = 64 \implies x = 8"),
            MathTex(r"\text{Sum} = 15 + 8 + 8 = 31 \text{ cm}")
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(DOWN).scale(0.8)
        
        self.add(scene_objects)
        self.add(text_group)
