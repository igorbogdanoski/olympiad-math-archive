from manim import *

class Task_4411(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
        
        # A = 40, B = 60, C = 80
        # Coordinates
        # A at origin
        A = ORIGIN
        # B on x-axis. c = 6 (arbitrary)
        c_len = 6
        B = RIGHT * c_len
        
        # C coordinates
        # b = c * sin(60) / sin(80)
        b_len = c_len * np.sin(60*DEGREES) / np.sin(80*DEGREES)
        C_pt = np.array([b_len * np.cos(40*DEGREES), b_len * np.sin(40*DEGREES), 0])
        
        # Shift to center
        center = (A + B + C_pt) / 3
        A = A - center
        B = B - center
        C_pt = C_pt - center
        
        tri = Polygon(A, B, C_pt, color=BLUE)
        lbl_A = MathTex("A").next_to(A, DOWN+LEFT)
        lbl_B = MathTex("B").next_to(B, DOWN+RIGHT)
        lbl_C = MathTex("C").next_to(C_pt, UP)
        
        # Bisector of AC
        # Midpoint E
        E = (A + C_pt) / 2
        # Direction AC
        vec_AC = C_pt - A
        # Perpendicular direction
        perp_vec = np.array([-vec_AC[1], vec_AC[0], 0])
        perp_vec = perp_vec / np.linalg.norm(perp_vec)
        
        # Draw bisector line s
        s_start = E + perp_vec * 4
        s_end = E - perp_vec * 4
        bisector = Line(s_start, s_end, color=GREEN)
        lbl_s = MathTex("s", color=GREEN).next_to(s_start, UP)
        
        # Intersection D with AB
        # D is intersection of bisector and AB
        # We can calculate it or use line_intersection
        D = line_intersection(
            [s_start, s_end],
            [A, B]
        )
        dot_D = Dot(D, color=RED)
        lbl_D = MathTex("D").next_to(D, DOWN)
        
        self.add(tri, lbl_A, lbl_B, lbl_C)
        self.add(bisector, lbl_s)
        self.add(dot_D, lbl_D)
        
        # Mark right angle at E
        ra = RightAngle(Line(E, C_pt), Line(E, s_start), length=0.3, quadrant=(-1,1))
        self.add(ra)


config.media_width = '100%'
config.verbosity = 'ERROR'
