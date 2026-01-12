#!/usr/bin/env python
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()
sys.path.insert(0, str(BASE_DIR / "tools"))

from process_olympiad import PlatinumProcessor

processor = PlatinumProcessor(BASE_DIR)

files_to_process = [
    BASE_DIR / "docs" / "grade_9" / "number_theory" / "regional_2025_1_3ab.md",
    BASE_DIR / "docs" / "grade_10" / "number_theory" / "regional_2025_2_1b.md",
    BASE_DIR / "docs" / "grade_10" / "algebra" / "regional_2025_2_2a.md",
    BASE_DIR / "docs" / "grade_10" / "algebra" / "regional_2025_2_1a.md",
]

input_files = [str(f) for f in files_to_process if f.exists()]

if input_files:
    print(f"Processing {len(input_files)} files...")
    processor.process_batch(input_files)
else:
    print("No valid files found!")
