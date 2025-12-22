from manim import *
import numpy as np

class PitagorovaTeorema(Scene):
    def construct(self):
        # --- 0. Setup (Optional Background) ---
        try:
            background = ImageMobject("image_ea0909.png")
            background.scale_to_fit_width(config.frame_width)
            background.set_z_index(-1)
            background.set_opacity(0.5)
            self.add(background)
        except FileNotFoundError:
            pass

        # --- 1. Setup Title ---
        title = Title("Питагорова Теорема: $a^2 + b^2 = c^2$")
        # Move title up slightly to make room
        title.to_edge(UP)
        self.play(Write(title))

        # --- 2. Define Triangle Geometry (Scaled to fit screen) ---
        scale_factor = 0.8  # Scale down to 80% to fit in frame
        a_val, b_val = 3, 4
        c_val = 5
        
        a = a_val * scale_factor
        b = b_val * scale_factor
        c = c_val * scale_factor
        
        # Define points
        # Move C down and left so the whole drawing centers better
        C = np.array([-1, -1.5, 0])      
        A = C + RIGHT * b              
        B = C + UP * a                 

        # Create and draw triangle
        triangle = Polygon(C, A, B, color=WHITE, stroke_width=4)
        # Mark the right angle
        right_angle = RightAngle(Line(C, A), Line(C, B), length=0.4)
        
        self.play(Create(triangle), Create(right_angle))

        # --- 3. Add Side Labels ---
        label_a = MathTex("a").next_to(Line(C, B), LEFT, buff=0.2)
        label_b = MathTex("b").next_to(Line(C, A), DOWN, buff=0.2)
        
        # Calculate Hypotenuse center for label c
        hypotenuse_line = Line(A, B)
        label_c = MathTex("c").next_to(hypotenuse_line.get_center(), UP + RIGHT, buff=0.2)
        
        self.play(Write(label_a), Write(label_b), Write(label_c))

        # --- 4. Create Squares for legs a and b ---
        square_a = Square(side_length=a, fill_color=BLUE, fill_opacity=0.6)
        # Align square_a to the left of side a
        square_a.next_to(Line(C, B), LEFT, buff=0)

        square_b = Square(side_length=b, fill_color=RED, fill_opacity=0.6)
        # Align square_b below side b
        square_b.next_to(Line(C, A), DOWN, buff=0)

        # Labels for areas
        tex_a2 = MathTex("a^2").move_to(square_a.get_center())
        tex_b2 = MathTex("b^2").move_to(square_b.get_center())

        self.play(
            FadeIn(square_a), FadeIn(square_b),
            Write(tex_a2), Write(tex_b2)
        )
        self.wait(1)

        # --- 5. Create Square for Hypotenuse c ---
        # Calculate angle of hypotenuse
        vec_ab = B - A
        angle_ab = np.arctan2(vec_ab[1], vec_ab[0])
        
        square_c = Square(side_length=c, color=YELLOW, fill_opacity=0.3)
        
        # 1. Rotate the square to match the hypotenuse angle
        square_c.rotate(angle_ab)
        
        # 2. Move to the center of the hypotenuse
        square_c.move_to(hypotenuse_line.get_center())
        
        # 3. Shift it "outward". 
        # We calculate the vector pointing 'UP' relative to the rotation, 
        # then shift by half the side length.
        # FIXED: Use rotate_vector instead of Rotate animation
        shift_vector = rotate_vector(UP, angle_ab) * (c / 2)
        square_c.shift(shift_vector)

        tex_c2 = MathTex("c^2").move_to(square_c.get_center())

        self.play(Create(square_c), Write(tex_c2))
        self.wait(1)

        # --- 6. Animate movement (Visual Proof) ---
        
        # Group the square and its label to move them together
        group_a = VGroup(square_a, tex_a2)
        group_b = VGroup(square_b, tex_b2)

        self.play(
            # Move A to the center of C
            group_a.animate.rotate(angle_ab).move_to(square_c.get_center()).scale(0.5).shift(LEFT*0.5),
            # Move B to the center of C
            group_b.animate.rotate(angle_ab).move_to(square_c.get_center()).scale(0.5).shift(RIGHT*0.5),
            # Fade out the 'c^2' text so we can see the others arrive
            FadeOut(tex_c2),
            run_time=2
        )
        
        # Note: A perfect geometric proof (dissection) is complex. 
        # Here we just show they "merge" into the big square area concept.

        # Final Equation Update
        final_text = MathTex("3^2 + 4^2 = 5^2").next_to(title, DOWN)
        calc_text = MathTex("9 + 16 = 25").next_to(final_text, DOWN)

        self.play(Write(final_text))
        self.play(Write(calc_text))
        
        self.wait(2)