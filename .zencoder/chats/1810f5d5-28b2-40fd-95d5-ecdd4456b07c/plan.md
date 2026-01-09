# Bug Fix Plan

This plan guides you through systematic bug resolution. Please update checkboxes as you complete each step.

## Phase 1: Investigation

### [x] Bug Reproduction

- [x] Identified SyntaxError in `tools/process_ai_problem.py` at line 131.
- [x] Identified broken Manim code generation (`A = np.array()`) in `new_problem_input.md`.

### [ ] Root Cause Analysis

- [ ] Analyze why `image_rrel_path` and `\n\nr` were present in `process_ai_problem.py`.
- [ ] Determine why AI is generating empty `np.array()` calls for point A.

## Phase 2: Resolution

### [x] Fix Implementation

- [x] Fixed syntax error in `tools/process_ai_problem.py`.
- [x] Corrected the Manim code logic for triangle vertices using barycentric coordinates.
- [x] Ensured `line_intersection` is no longer needed in the fixed code.
- [x] Fixed UnicodeEncodeError in `process_ai_problem.py` for Windows environment.

### [x] Impact Assessment

- [x] Verified that the problem processor now runs correctly.
- [x] Checked that the generated image is correctly linked in the final Markdown.

## Phase 3: Verification & Quality Audit

### [x] Testing & Verification

- [x] Fixed `SyntaxError` in `process_ai_problem.py` (line 131)
- [x] Fixed `UnicodeEncodeError` for Windows terminal
- [x] Fixed `TypeError` in Manim code (`A = np.array()` missing arguments)
- [x] Verified high-quality image generation (1080p)
- [x] Verified successful integration and Markdown generation in `docs/`

### [x] Quality Audit (High Quality Images)

- [x] Upgraded `tools/process_ai_problem.py` to High Quality (`-qh`, 1080p)
- [x] Upgraded `tools/process_olympiad.py` to High Quality (`-qh`, 1080p)
- [x] Verified `tools/render_manim.py` is using 4K Quality (`--quality k`)
- [x] Fixed syntax errors, typos, and malformed strings in `render_manim.py` and `process_olympiad.py`

### [x] Final Cleanup

- [x] All temporary media files are cleaned up
- [x] Input file is cleared after successful processing

## Notes

- Update this plan as you discover more about the issue
- Check off completed items using [x]
- Add new steps if the bug requires additional investigation
