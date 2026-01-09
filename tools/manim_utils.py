import re

def fix_manim_common_errors(code):
    """
    Applies a set of regex rules and string replacements to fix common AI-generated 
    Manim errors, particularly for geometry diagrams.
    """
    if not code:
        return code

    # 1. Fix DashedLine/stroke_dash_pattern issues
    # AI often tries to use stroke_dash_pattern inside Line() which is not standard or buggy
    # Replace Line(..., stroke_dash_pattern=...) with DashedLine(...)
    code = re.sub(
        r'Line\((.*?),\s*stroke_dash_pattern\s*=\s*\[.*?\](.*?)\)',
        r'DashedLine(\1\2)',
        code,
        flags=re.DOTALL
    )
    
    # 2. Fix typos in parameters
    code = code.replace("l_style=DASHED", "")
    code = code.replace("l_style = DASHED", "")
    code = code.replace("DASHED", "True") # Sometimes used as a bool
    
    # 3. Fix comma issues from removals
    code = code.replace(", ,", ",")
    code = code.replace(",,", ",")
    code = code.replace("(,", "(")
    code = code.replace(",)", ")")

    # 4. Fix Dot label issues
    # AI often does Dot(point).add_label("A") but standard is Dot(point).add_annotation or just creating text
    # No direct fix but common hallucination: Dot(point).set_label("A") -> should be avoided in prompt
    
    # 5. Fix common geometric hallucinations
    # Angle(line1, line2, ...) often fails if lines don't meet at origin or as expected
    # Ensure they use RightAngle if needed
    
    # 6. Ensure WHITE background doesn't lead to invisible BLACK text
    # Most labels should be BLACK
    if 'self.camera.background_color = WHITE' in code:
        if 'color=BLACK' not in code and 'MathTex' in code:
            # Inject default color if missing for MathTex
            # This is a bit risky but usually AI forgets color=BLACK
            # code = code.replace('MathTex(', 'MathTex(color=BLACK, ')
            pass

    return code

def sanitize_for_latex_free(code):
    """
    Converts MathTex to Text and removes LaTeX specific commands 
    to allow rendering on systems without a working TeX installation.
    """
    # Simple replacement of the class
    code = code.replace("MathTex", "Text")
    
    # Remove LaTeX symbols like $, \, etc.
    code = code.replace("$", "")
    # Remove \text{...} but keep contents
    code = re.sub(r'\\text\{(.*?)\}', r'\1', code)
    # Replace other common LaTeX commands
    code = code.replace(r'\\alpha', 'alpha')
    code = code.replace(r'\\beta', 'beta')
    code = code.replace(r'\\gamma', 'gamma')
    code = code.replace(r'\\theta', 'theta')
    code = code.replace(r'\\angle', 'angle ')
    code = code.replace(r'\\triangle', 'triangle ')
    
    return code
