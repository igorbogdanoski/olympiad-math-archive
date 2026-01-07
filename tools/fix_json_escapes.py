import os
import re

# Comprehensive list of LaTeX commands to escape
latex_commands = [
    # Greek
    "alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta", "iota", "kappa",
    "lambda", "mu", "nu", "xi", "omicron", "pi", "rho", "sigma", "tau", "upsilon", 
    "phi", "chi", "psi", "omega",
    "Gamma", "Delta", "Theta", "Lambda", "Xi", "Pi", "Sigma", "Upsilon", "Phi", "Psi", "Omega",
    
    # Common Math
    "cdot", "frac", "sqrt", "sum", "prod", "int", "lim", 
    "ge", "le", "geq", "leq", "ne", "neq", "approx", "equiv", "sim", "cong",
    "in", "notin", "subset", "subseteq", "supset", "supseteq", "cup", "cap", "setminus",
    "infty", "pm", "mp", "times", "div",
    "dots", "cdots", "vdots", "ddots",
    
    # Geometry & Accents
    "angle", "triangle", "circ", "deg", "overline", "underline", "hat", "vec", "bar",
    "perp", "parallel",
    
    # Formatting & Delimiters
    "text", "textbf", "textit", "mathrm", "mathbf",
    "left", "right", "big", "Big",
    "quad", "qquad", "\\,", "\\:", "\\;", "\\!",
    
    # Logic
    "implies", "iff", "forall", "exists", "land", "lor", "lnot"
]

file_path = "input.json"

if not os.path.exists(file_path):
    # Try finding it in tools directory if running from root
    if os.path.exists("tools/input.json"):
        file_path = "tools/input.json"
    else:
        print(f"File not found: {file_path}")
        exit(1)

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Generic Fix: Escape any backslash that is followed by a known LaTeX command
# Use a loop to handle each command safely
for cmd in latex_commands:
    # Pattern: Look for \cmd that is NOT preceded by a backslash
    # (?<!\\) checker matches position where previous char is NOT \
    # then matches \\ (literal backslash)
    # then matches the cmd
    # We replace with \\cmd
    
    pattern = r"(?<!\\)\\" + re.escape(cmd)
    # To get two backslashes in the file, we need to pass four backslashes to re.sub
    # because re.sub treats backslashes in the replacement string as escapes.
    replacement = r"\\\\" + cmd
    
    content = re.sub(pattern, replacement, content)

# 2. Specific fix for known problematic substrings not covered above or tricky ones
replacements = [
    (r"P_{\Delta", r"P_{\\Delta"),      # Fix Delta specifically if missed
    (r"\overline", r"\\overline"),      # Fix overline
    (r"\ge", r"\\ge"),                   # Ensure ge is fixed
]

for old, new in replacements:
    # Use regex for specific replacements to avoid double-escaping
    pattern = r"(?<!\\)" + re.escape(old)
    content = re.sub(pattern, new.replace('\\', '\\\\'), content)


# Writing back
with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Fixed LaTeX escape sequences in {file_path}")
