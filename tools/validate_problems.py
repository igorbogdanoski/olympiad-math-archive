import os
import re
import glob
from pathlib import Path

def validate_problem(filepath):
    """Validate a problem markdown file for common issues."""
    issues = []
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    problem_id = Path(filepath).stem
    
    # Check 1: Raw Python code at the end (Manim code that should be extracted)
    if re.search(r'```python\s*$', content, re.MULTILINE):
        issues.append("ERROR: Unterminated Python code block at end of file")
    
    if re.search(r'class\s+\w+Scene\(Scene\):', content):
        if 'tools/manim_' not in filepath and not re.search(r'```', content):
            issues.append("WARN: Detected Manim Scene class outside tools directory - should be in separate file")
    
    # Check 2: Unmatched or improperly closed details tags
    details_open = content.count('<details>')
    details_close = content.count('</details>')
    if details_open != details_close:
        issues.append(f"ERROR: Mismatched details tags: {details_open} open, {details_close} close")
    
    summary_open = content.count('<summary>')
    summary_close = content.count('</summary>')
    if summary_open != summary_close:
        issues.append(f"ERROR: Mismatched summary tags: {summary_open} open, {summary_close} close")
    
    # Check 3: Missing image file
    if 'problem_id:' in content:
        match = re.search(r'problem_id:\s*(\S+)', content)
        if match:
            problem_id = match.group(1).strip()
            image_path = Path(filepath).parent.parent.parent / 'web' / 'public' / 'assets' / 'images' / problem_id / f'{problem_id}.png'
            
            # Only warn if image is expected but missing (for geometry/algebra problems)
            if any(tag in content for tag in ['geometry', 'diagram', 'visualization']):
                if not image_path.exists():
                    issues.append(f"WARN: Expected image not found at {image_path.name}")
    
    # Check 4: Placeholder text that wasn't replaced
    placeholders = [
        '<Детално решение',
        '<Детално',
        'TODO:',
        'FIXME:',
        'XXX:',
        'PLACEHOLDER'
    ]
    for placeholder in placeholders:
        if placeholder in content:
            issues.append(f"WARN: Found placeholder text: {placeholder}")
    
    # Check 5: Raw LaTeX that's not properly wrapped
    if re.search(r'\\[a-z]+\{', content):
        if not re.search(r'\$\$', content) and not re.search(r'\$[^\$]+\$', content):
            issues.append("WARN: Detected LaTeX commands but no math delimiters")
    
    # Check 6: Embedded HTML/code that should be collapsed
    if re.search(r'```(?:python|javascript|jsx|tsx)\s*\n[\s\S]{100,}```\s*$', content):
        issues.append("WARN: Large code block at end of file - consider extracting to separate Manim file")
    
    return issues

def validate_all_problems(docs_path=None):
    """Validate all problem markdown files."""
    if not docs_path:
        docs_path = Path(__file__).parent.parent / 'docs'
    
    problem_files = glob.glob(str(docs_path / '**' / '*.md'), recursive=True)
    
    total_issues = 0
    problems_with_issues = 0
    
    for filepath in sorted(problem_files):
        issues = validate_problem(filepath)
        if issues:
            problems_with_issues += 1
            rel_path = Path(filepath).relative_to(docs_path.parent)
            print(f"\n📄 {rel_path}")
            for issue in issues:
                print(f"  {issue}")
                total_issues += 1
    
    print(f"\n{'='*70}")
    print(f"Validation Summary:")
    print(f"  Total issues found: {total_issues}")
    print(f"  Problems with issues: {problems_with_issues}")
    print(f"{'='*70}\n")
    
    return total_issues == 0

if __name__ == '__main__':
    import sys
    import io
    
    if sys.stdout.encoding != 'utf-8':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    
    success = validate_all_problems()
    sys.exit(0 if success else 1)
