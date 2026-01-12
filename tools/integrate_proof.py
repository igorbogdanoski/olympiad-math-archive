#!/usr/bin/env python3
"""
Script for integrating AI-generated proofs into theorem files.

Usage:
python integrate_proof.py theorem_name proof_file.md [manim_file.py]
"""

import sys
import os
from pathlib import Path

def integrate_proof(theorem_name: str, proof_file: str, manim_file: str = None):
    """Integrate proof into theorem file."""

    base_dir = Path(__file__).parent.parent
    theorems_dir = base_dir / "web" / "src" / "data" / "theorems"
    proofs_dir = base_dir / "tools" / "generated_proofs"

    # Read proof
    proof_path = proofs_dir / proof_file
    if not proof_path.exists():
        print(f"❌ Proof file not found: {proof_path}")
        return False

    with open(proof_path, 'r', encoding='utf-8') as f:
        proof_content = f.read().strip()

    # Validate proof content
    validation = validate_proof(proof_content)
    if not validation['valid']:
        print("❌ Proof validation failed:")
        for error in validation['errors']:
            print(f"  - {error}")
        return False

    # Find theorem file
    theorem_file = theorems_dir / f"{theorem_name}.md"
    if not theorem_file.exists():
        print(f"❌ Theorem file not found: {theorem_file}")
        return False

    # Read theorem
    with open(theorem_file, 'r', encoding='utf-8') as f:
        theorem_content = f.read()

    # Check if proof already exists
    if '## 📝 Доказ' in theorem_content:
        print("⚠️  Proof already exists. Replacing...")
        # Remove old proof
        start = theorem_content.find('## 📝 Доказ')
        next_section = theorem_content.find('\n## ', start + 1)
        if next_section == -1:
            next_section = len(theorem_content)
        theorem_content = theorem_content[:start] + theorem_content[next_section:]

    # Find insertion point (after ## 🛠 Каде се користи?)
    insert_pos = theorem_content.find('## 🛠 Каде се користи?')
    if insert_pos == -1:
        insert_pos = theorem_content.find('---', theorem_content.find('---') + 1) + 3

    # Find end of section
    next_section = theorem_content.find('\n## ', insert_pos)
    if next_section == -1:
        insert_pos = len(theorem_content.rstrip()) + 1
        new_content = theorem_content.rstrip() + '\n\n' + proof_content + '\n'
    else:
        new_content = theorem_content[:next_section] + '\n\n' + proof_content + '\n\n' + theorem_content[next_section:]

    # Write updated theorem
    with open(theorem_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"✅ Proof integrated into {theorem_file}")

    # Handle Manim file if provided
    if manim_file:
        manim_path = proofs_dir / manim_file
        if manim_path.exists():
            # Copy to tools directory for processing
            target_manim = base_dir / "tools" / f"manim_{theorem_name}_proof.py"
            with open(manim_path, 'r', encoding='utf-8') as f:
                manim_content = f.read()

            with open(target_manim, 'w', encoding='utf-8') as f:
                f.write(manim_content)

            print(f"✅ Manim code saved to {target_manim}")
        else:
            print(f"⚠️  Manim file not found: {manim_path}")

    return True

def validate_proof(proof_content: str) -> dict:
    """Validate proof content meets requirements."""

    validation = {
        'valid': True,
        'errors': [],
        'warnings': []
    }

    # Required elements
    if not proof_content.strip():
        validation['errors'].append("Proof is empty")
        validation['valid'] = False

    if '## 📝 Доказ' not in proof_content:
        validation['errors'].append("Missing '## 📝 Доказ' header")

    if '### Чекор 1:' not in proof_content:
        validation['errors'].append("Missing at least one step")

    if '### Заклучок:' not in proof_content:
        validation['errors'].append("Missing conclusion")

    # LaTeX check
    latex_count = len(proof_content.split('$$')) - 1
    if latex_count < 2:
        validation['warnings'].append("Few LaTeX formulas found")

    return validation

def main():
    if len(sys.argv) < 3:
        print("Usage: python integrate_proof.py theorem_name proof_file.md [manim_file.py]")
        print("\nExample:")
        print("python integrate_proof.py pythagorean_theorem pythagorean_proof.md pythagorean_manim.py")
        sys.exit(1)

    theorem_name = sys.argv[1]
    proof_file = sys.argv[2]
    manim_file = sys.argv[3] if len(sys.argv) > 3 else None

    print(f"🔄 Integrating proof for theorem: {theorem_name}")
    print(f"📄 Proof file: {proof_file}")
    if manim_file:
        print(f"🎬 Manim file: {manim_file}")

    success = integrate_proof(theorem_name, proof_file, manim_file)

    if success:
        print("\n✅ Integration complete!")
        print("Next steps:")
        print("1. Review the updated theorem file")
        print("2. Test the web page generation")
        print("3. If Manim code provided, run visualization")
    else:
        print("\n❌ Integration failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()