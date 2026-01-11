#!/usr/bin/env python3
"""
Скрипта што го отстранува Manim код од MD датотеките.
Manim кодот треба да биде во tools/manim_*.py, не во MD.
"""

import os
import re
from pathlib import Path

def has_manim_code(content):
    """Проверува дали MD датотеката содржи Manim код."""
    return bool(re.search(r'^from manim import|^class\s+\w+Scene', content, re.MULTILINE))

def remove_manim_code(content):
    """Го отстранува Manim кодот од MD содржината."""
    # Отстранува Python кодот што почнува од "from manim"
    pattern = r'(?:^|\n)(from manim.*?)(?:\n\n---|\Z)'
    cleaned = re.sub(pattern, '\n', content, flags=re.MULTILINE | re.DOTALL)
    return cleaned.strip() + '\n'

def process_files():
    """Обработува сите MD датотеки со Manim код."""
    docs_dir = Path('c:/Users/pc4all/Documents/matholimpiad/olympiad-math-archive/docs')
    
    cleaned_files = []
    
    for md_file in docs_dir.rglob('*.md'):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if has_manim_code(content):
                cleaned_content = remove_manim_code(content)
                
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(cleaned_content)
                
                cleaned_files.append(str(md_file))
                print(f"OK: Ocisten: {md_file.name}")
        except Exception as e:
            print(f"ERROR: Greska vo {md_file.name}: {e}")
    
    print(f"\nVkupno ocisten: {len(cleaned_files)}")
    return cleaned_files

if __name__ == '__main__':
    print("CLEANUP: Pocnalo otstranuvan je na Manim kodon od MD datotekite...\n")
    cleaned = process_files()
    print("\nZavrseno!")
