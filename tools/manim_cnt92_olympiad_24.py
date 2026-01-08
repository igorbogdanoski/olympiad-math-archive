from manim import *

class Problem_cnt92_olympiad_24(Scene):
    def construct(self):
        # Scale
        scale = 0.5
        
        # Parameters
        a = 12.0
        b = 12.0
        angle_deg = 30
        angle_rad = angle_deg * DEGREES
        
        # Coordinates
        A = ORIGIN
        B = RIGHT * a
        D = np.array([b * np.cos(angle_rad), b * np.sin(angle_rad), 0])
        C = B + D
        
        # Shift to center
        center = (A + B + C + D) / 4
        shift = -center
        
        A += shift
        B += shift
        C += shift
        D += shift
        
        # Apply scale
        A *= scale
        B *= scale
        C *= scale
        D *= scale
        
        # Objects
        parallelogram = Polygon(A, B, C, D, color=BLUE, fill_opacity=0.2)
        
        # Labels
        label_a = MathTex("a=12").next_to(Line(A, B), DOWN)
        label_b = MathTex("b=12").next_to(Line(B, C), RIGHT)
        
        # Angle
        angle_arc = Angle(Line(A, B), Line(A, D), radius=0.5, color=YELLOW)
        label_angle = MathTex(r"30^\\circ").next_to(angle_arc, RIGHT, buff=0.1)
        
        # Height
        # Drop perp from D to AB
        # D is (x, y). AB is on x-axis (after rotation? No, A and B are not on x axis after shift)
        # Let's use the original coordinates relative to A before shift/scale for logic, but that's hard.
        # Easier: Project D onto line AB.
        
        # Vector AB
        v_AB = B - A
        u_AB = v_AB / np.linalg.norm(v_AB)
        # Vector AD
        v_AD = D - A
        # Projection length
        proj_len = np.dot(v_AD, u_AB)
        # Projection point H
        H = A + u_AB * proj_len
        
        height_line = DashedLine(D, H, color=RED)
        label_h = MathTex("h").next_to(height_line, LEFT, buff=0.05)
        
        # Area text
        area_val = 12 * 12 * np.sin(angle_rad)
        text_calc = MathTex(
            r"a + b = 24 \implies \max(ab) \text{ when } a=b=12",
            r"S = a \cdot b \cdot \sin(30^\circ)",
            r"S = 12 \cdot 12 \cdot 0.5 = 72"
        ).arrange(DOWN).to_corner(UL)
        
        self.add(parallelogram)
        self.add(label_a, label_b)
        self.add(angle_arc, label_angle)
        self.add(height_line, label_h)
        self.add(text_calc)
