from manim import *

class Problem_2022_mun_g9_5(Scene):
    def construct(self):
        # Scale
        scale = 2.0
        
        # Parameters
        # A = 20.22 m = 202.2 dm
        # a = 3.37 dm
        # Ratio k = A/a = 202.2 / 3.37 = 60
        # Number of tiles = 6 * k^2 = 6 * 3600 = 21600
        
        # Visualization
        # Draw a hexagon and show it's made of 6 triangles.
        # Show one of the large triangles subdivided into smaller ones.
        
        # Hexagon
        R = 1.5
        hexagon = RegularPolygon(n=6, radius=R, color=BLUE)
        
        # Center
        O = ORIGIN
        
        # Triangles
        vertices = hexagon.get_vertices()
        triangles = VGroup()
        for i in range(6):
            p1 = vertices[i]
            p2 = vertices[(i+1)%6]
            tri = Polygon(O, p1, p2, color=WHITE, stroke_width=1)
            triangles.add(tri)
            
        # Subdivide one triangle (e.g., the top one)
        # Let's just show a few small triangles to imply tiling
        # Top triangle vertices: O, v1, v2 (indices depend on orientation)
        # RegularPolygon starts at right (0 deg) by default? No, usually first vertex at 0 or 90.
        # Let's check vertices.
        
        # Let's pick the triangle formed by O and first two vertices.
        t_p1 = vertices[0]
        t_p2 = vertices[1]
        
        # Draw a small triangle at the corner O
        # Scale factor for drawing: let's say we show 4 rows instead of 60
        n_rows = 4
        small_tris = VGroup()
        
        # Vector along sides
        v1 = (t_p1 - O) / n_rows
        v2 = (t_p2 - O) / n_rows
        
        for i in range(n_rows):
            for j in range(i + 1):
                # Position
                pos = O + i * v1 + j * (v2 - v1) # This logic might be slightly off for equilateral grid
                # Correct logic:
                # Row i has i+1 triangles pointing up and i triangles pointing down?
                # Wait, let's just draw lines parallel to sides.
                pass
        
        # Lines parallel to sides
        lines = VGroup()
        for i in range(1, n_rows):
            # Parallel to p1-p2
            start = O + i * v1
            end = O + i * v2
            lines.add(Line(start, end, color=YELLOW, stroke_width=1))
            
            # Parallel to O-p2
            start = O + i * v1
            end = t_p1 + i * (t_p2 - t_p1) / n_rows # This is parallel to p1-p2? No.
            # Parallel to O-p2 means direction v2.
            # Starts from O-p1 side.
            start = O + i * v1
            end = t_p2 + (n_rows - i) * (t_p1 - t_p2) / n_rows # Hard to calculate.
            
        # Easier: Just draw the grid lines for one triangle
        grid_lines = VGroup()
        # Directions: v1, v2, v2-v1
        
        # Parallel to side 2 (O-p2)
        for i in range(1, n_rows):
            start = O + i * v1
            end = t_p2 + (i) * (t_p1 - t_p2) / n_rows # Interpolate between p2 and p1?
            # Line from (i/n)A to (i/n)B + (1-i/n)C ?
            # Let's use barycentric coords logic visually.
            # Lines parallel to p1-p2
            l1 = Line(O + i*v1, O + i*v2, color=YELLOW, stroke_width=1)
            grid_lines.add(l1)
            
            # Lines parallel to O-p2
            # Start at O + i*v1, go direction v2?
            # End at line p1-p2.
            # p1 + k*(p2-p1)
            start = O + i * v1
            end = t_p1 + i * (t_p2 - t_p1) / n_rows # No
            
            # Let's just draw the big triangle and label it
            pass

        # Let's keep it simple.
        # Show Hexagon divided into 6 triangles.
        # Label side A.
        # Show a small triangle next to it with side a.
        
        label_A = MathTex(r"A = 20.22 \\text{ m}").next_to(hexagon, UP)
        
        # Small triangle
        small_tri = RegularPolygon(n=3, radius=0.2, color=YELLOW).next_to(hexagon, RIGHT, buff=1)
        label_a = MathTex(r"a = 3.37 \\text{ dm}").next_to(small_tri, DOWN)
        
        # Text
        text = MathTex(
            r"A = 202.2 \text{ dm}",
            r"k = \frrac{A}{a} = \frac{202.2}{3.37} = 60",
            r"N_{\triangle} = k^2 = 3600",
            r"N_{total} = 6 \cdot 3600 = 21600"
        ).arrange(DOWN).to_corner(UL).scale(0.8)
        
        self.add(hexagon, triangles)
        self.add(label_A)
        self.add(small_tri, label_a)
        self.add(text)
