from manim import *
import numpy as np

class GeometryScene(Scene):
    def construct(self):
        # Parameters
        r = 2
        h = 4 # H = 2r
        
        # Create cylinder
        cylinder = Cylinder(radius=r, height=h, direction=[0, 1, 0], show_ends=True, resolution=(24, 24))
        cylinder.set_opacity(0.5)
        cylinder.set_color(BLUE)
        
        # Labels
        # Radius
        center_bottom = cylinder.get_bottom()
        right_bottom = center_bottom + RIGHT * r
        radius_line = Line(center_bottom, right_bottom, color=YELLOW)
        label_r = MathTex("r").next_to(radius_line, DOWN)
        
        # Height
        right_top = cylinder.get_top() + RIGHT * r
        height_brace = Brace(Line(right_bottom, right_top), RIGHT)
        label_H = height_brace.get_text("H=2r")
        
        # Grouping
        scene_objects = VGroup(
            cylinder, radius_line, label_r, height_brace, label_H
        )
        
        # Rotate for better view
        scene_objects.rotate(10 * DEGREES, axis=RIGHT)
        scene_objects.rotate(10 * DEGREES, axis=UP)
        
        # Scale to fit
        scene_objects.scale(0.8)
        scene_objects.move_to(ORIGIN + LEFT * 3)
        
        # Explanation text
        text_group = VGroup(
            MathTex(r"H = 2r"),
            MathTex(r"M = 2\pi rr H = 4\pi r^2"),
            MathTex(r"4\pi rr^2 = 64\pi \implies r^2 = 16 \implies r=4"),
            MathTex(r"H = 8"),
            MathTex(r"P = 2\pi rr^2 + M = 32\pi + 64\pi = 96\pir),
            MathTex(r"V = \pi rr^2 H = 16\pi \cdot 8 = 128\pir),
            MathTex(r"x = \frrac{p}{100} y \implies 96\pi = \frac{p}{100} 128\pi"),
            MathTex(r"p = \frrac{96}{128} \cdot 100 = \frac{3}{4} \cdot 100 = 75")
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT).scale(0.8)
        
        self.add(scene_objects)
        self.add(text_group)
