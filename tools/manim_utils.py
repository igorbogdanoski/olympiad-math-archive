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
    Converts MathTex to Text and transforms LaTeX math expressions
    to readable plain text while preserving mathematical meaning.
    """

    def convert_math_content(math_string):
        """Convert LaTeX math content to readable plain text"""
        content = math_string.strip()

        # Remove outer $ delimiters if present
        if content.startswith('$') and content.endswith('$'):
            content = content[1:-1]

        # Convert common LaTeX symbols to readable Unicode or ASCII
        replacements = [
            (r'\\alpha', 'α'), (r'\\beta', 'β'), (r'\\gamma', 'γ'), (r'\\delta', 'δ'),
            (r'\\theta', 'θ'), (r'\\lambda', 'λ'), (r'\\mu', 'μ'), (r'\\pi', 'π'),
            (r'\\sigma', 'σ'), (r'\\phi', 'φ'), (r'\\omega', 'ω'),
            (r'\\sqrt\{([^}]+)\}', r'sqrt(\1)'),
            (r'\\frac\{([^}]+)\}\{([^}]+)\}', r'(\1)/(\2)'),
            (r'\\text\{([^}]+)\}', r'\1'),
            (r'\\cos', 'cos'), (r'\\sin', 'sin'), (r'\\tan', 'tan'),
            (r'\\cot', 'cot'), (r'\\sec', 'sec'), (r'\\csc', 'csc'),
            (r'\\log', 'log'), (r'\\ln', 'ln'), (r'\\lim', 'lim'),
            (r'\\int', '∫'), (r'\\sum', '∑'), (r'\\prod', '∏'),
            (r'\\infty', '∞'), (r'\\leq', '≤'), (r'\\geq', '≥'),
            (r'\\neq', '≠'), (r'\\approx', '≈'), (r'\\pm', '±'),
            (r'\\times', '×'), (r'\\div', '÷'), (r'\\cdot', '•'),
            (r'\\ldots', '...'), (r'\\cdots', '...'),
            (r'\\angle', '∠'), (r'\\triangle', '△'),
            (r'\\perp', '⊥'), (r'\\parallel', '∥'),
            (r'\\degree', '°'), (r'\\circ', '°'),
            (r'\\left\(', '('), (r'\\right\)', ')'),
            (r'\\left\[', '['), (r'\\right\]', ']'),
            (r'\\{', '{'), (r'\\}', '}'),
            (r'\\_', '_'), (r'\\,', ' '),
        ]

        for latex, plain in replacements:
            content = re.sub(latex, plain, content)

        # Clean up multiple spaces
        content = re.sub(r'\s+', ' ', content).strip()

        # Remove any remaining backslashes before single letters
        content = re.sub(r'\\([a-zA-Z])', r'\1', content)

        return content

    # Replace MathTex with Text
    code = code.replace("MathTex", "Text")

    # Convert Text string arguments (MathTex was already converted to Text)
    # Handle double quotes: Text("...") -> Text("readable...")
    code = re.sub(
        r'Text\(\s*"([^"]*)"\s*\)',
        lambda m: f'Text("{convert_math_content(m.group(1))}")',
        code
    )

    # Handle single quotes: Text('...') -> Text('readable...')
    code = re.sub(
        r"Text\(\s*'([^']*)'\s*\)",
        lambda m: f"Text('{convert_math_content(m.group(1))}')",
        code
    )

    # Handle triple quotes
    code = re.sub(
        r'Text\(\s*"""(.*?)"""\s*\)',
        lambda m: f'Text("""{convert_math_content(m.group(1))}""")',
        code,
        flags=re.DOTALL
    )

    code = re.sub(
        r"Text\(\s*'''(.*?)'''\s*\)",
        lambda m: f"Text('''{convert_math_content(m.group(1))}''')",
        code,
        flags=re.DOTALL
    )

    return code
