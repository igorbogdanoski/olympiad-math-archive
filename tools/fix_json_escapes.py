import os
import re

# Definiši listu LaTeX komandi koje treba "escape"-ovati
# Ovi stringovi počinju sa \ u fajlu, ali JSON parser ih vidi kao escape sekvence.
# Ako je escape nevalidan (npr \c), parser puca.
# Ako je validan (npr \f), parser ga guta, što ne želimo. Želimo \\frac.

latex_commands = [
    "cdot", "frac", "ge", "dots", "in", "le", "sum", "sqrt", 
    "alpha", "beta", "gamma", "pi", "left", "right", "implies",
    "text", "hat", "angle", "triangle", "circ", "deg"
]

file_path = "input.json"

if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
    exit(1)

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Pattern: Backslash followed by one of the commands, NOT already preceded by a backslash
# Note: In regex string, \\ is a single backslash.
# We want to match `\` followed by `cmd`.
# But checking "not preceded by backslash" is tricky if we just replace `\` with `\\`.

# Easiest way: just replace `\cmd` with `\\cmd`.
# But what if it is already `\\cmd`?
# Regex lookbehind? `(?<!\\)\\cmd`

for cmd in latex_commands:
    # Pattern: (?<!\\)\\(cmd)\b
    # Meaning: A backslash, followed by the command, NOT preceded by another backslash.
    # Note: We need to escape the backslash in the regex string too.
    
    # Python regex string for backslash is \\
    # Python string for backslash is \\
    # So to match a literal backslash in regex, we need \\\\
    
    pattern = r"(?<!\\)\\" + cmd
    replacement = r"\\\\" + cmd
    
    content = re.sub(pattern, replacement, content)

# Specific fixes for things seen in the file
# 1. "a \cdot" -> "a \\cdot"
# 2. "6 \cdot" -> "6 \\cdot"
# 3. "\frac" -> "\\frac"
# 4. "\ge" -> "\\ge"
# 5. "\dots" -> "\\dots"
# 6. "\in" -> "\\in"

# Let's handle the specific lines mentioned by just replacing specific known bad substrings
# This is safer than generic regex if we are unsure.

replacements = [
    (r"$a \cdot 10^k", r"$a \\cdot 10^k"),
    (r"$6 \cdot 10^k", r"$6 \\cdot 10^k"),
    (r"$6 \cdot 100", r"$6 \\cdot 100"),
    (r"N = 6 \cdot 10^k", r"N = 6 \\cdot 10^k"),
    (r"= 6 \cdot 10^k", r"= 6 \\cdot 10^k"),
    (r"= \frac{", r"= \\frac{"),
    (r"k \ge 2", r"k \\ge 2"),
    (r"100, \dots", r"100, \\dots"),
    (r"\in \{", r"\\in \{"),
    (r"5 \cdot 10", r"5 \\cdot 10"),
    (r"a \cdot 5", r"a \\cdot 5"),
    (r"$5 \cdot 10^k", r"$5 \\cdot 10^k")
]

for old, new in replacements:
    content = content.replace(old, new)


with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed LaTeX escape sequences in input.json")
