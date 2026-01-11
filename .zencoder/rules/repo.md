---
description: Repository Information Overview
alwaysApply: true
---

# Olympiad Math Archive - Repository Information

## Summary

The Olympiad Math Archive is a multi-project educational platform for Macedonian mathematics olympiad problems, solutions, and pedagogical guides. It combines a web-based Astro.js frontend for content delivery, Python-based automation tools for problem processing and visualization (Manim), and geometry diagram generation (Asymptote). The repository is organized by grade level (1-12) and mathematical topics (algebra, geometry, combinatorics, number theory).

## Repository Structure

- **`web/`** - Astro.js static site generator for the web platform
- **`tools/`** - Python utilities for problem processing, indexing, PDF generation, and Manim animations
- **`geometry-diagrams/`** - Asymptote-based geometry diagram generation
- **`docs/`** - Markdown problem content organized by grade and subject
- **`site/`** - Generated static HTML output
- **`problems/`** - Raw problem database
- **`templates/`** - Markdown templates for problem structure
- **`media/`** - Image and LaTeX assets

### Main Repository Components
- **Web Application**: Astro.js-based static site with full-text search and math rendering
- **Content Management**: Python scripts for parsing, indexing, and building problems into JSON
- **Automation Tools**: Manim scene generation, batch processing, PDF export
- **Documentation System**: MkDocs configuration with Material theme for local development

---

## Projects

### Web Application (Astro.js)

**Configuration File**: `web/package.json`

#### Language & Runtime
**Language**: JavaScript/TypeScript  
**Runtime**: Node.js (npm)  
**Framework**: Astro 4.0  
**Build System**: Astro CLI  
**CSS Framework**: Tailwind CSS 3.4

#### Dependencies
**Main Dependencies**:
- `astro` (4.0.0) - Static site generator
- `@astrojs/tailwind` (5.1.0) - Tailwind CSS integration
- `katex` (0.16.9) - LaTeX math rendering
- `fuse.js` (7.0.0) - Client-side full-text search
- `tailwindcss` (3.4.0) - Utility-first CSS

**Development Dependencies**:
- `@playwright/test` (1.57.0) - Browser automation testing

#### Build & Installation

```bash
cd web
npm install
npm run dev          # Start development server (port 4321)
npm run build        # Create production build
npm run preview      # Preview production build
npm run astro        # Run Astro CLI commands
```

#### Application Structure
- **Entry Points**: `web/src/pages/` (Astro file-based routing)
- **Main Pages**: 
  - `index.astro` - Homepage with problem browsing
  - `tasks/[id].astro` - Individual problem detail pages
  - `skills/[skill].astro` - Skill-based filtering and learning guides
  - `theorems/[id].astro` - Mathematical theorem library
  - `teachers.astro` - Teacher resources page

- **Layout**: `web/src/layouts/Layout.astro` - Main page template
- **Data**: `web/src/data/problems.json` (3.06 MB) - Generated problem database
- **Components**: `web/src/components/` - Reusable UI components

#### Testing

**Framework**: Playwright  
**Test Location**: `web/tests/`  
**Configuration**: `web/playwright.config.js`  

**Test Configuration Details**:
- Base URL: `http://localhost:4321`
- Timeout: 90 seconds per test
- Screenshot on failure only
- HTML report generation
- Chromium browser tested

**Run Command**:

```bash
npx playwright test
```

---

### Python Tools & Automation

**Main Scripts**: `tools/` directory  
**Language**: Python 3.8+  
**Key Dependencies**: Manim, Streamlit, pandas, requests, pytest

#### Core Utilities

- **`app.py`** - Streamlit web interface for problem exploration and PDF generation
- **`build_problem.py`** - Converts JSON problem input to Markdown with Manim integration
- **`indexer.py`** - Parses all Markdown files in `docs/` and generates `problems.json`
- **`process_olympiad.py`** - Advanced batch processor for large problem sets
- **`batch_manim.py`** - Parallel rendering of multiple Manim scenes
- **`generate_site.py`** - Builds static HTML from Markdown problems
- **`build_website.py`** - Website generation pipeline

#### Manim Animation Scripts
Numerous `manim_*.py` files for specific geometric and algebraic problem visualizations, including:
- Geometry proofs and constructions
- Theorem illustrations
- Interactive mathematical animations

#### Installation & Setup

```bash
pip install -r geometry-diagrams/requirements.txt
pip install manim streamlit  # Core dependencies for tools
python tools/build_problem.py  # Build a single problem
python tools/indexer.py        # Re-index all problems
python tools/app.py            # Launch Streamlit interface
```

#### Build & Compilation

```bash
python tools/process_olympiad.py    # Process batch of problems
python tools/batch_manim.py         # Render all Manim scenes
python tools/generate_site.py       # Generate static site
```

---

### Geometry Diagrams (Asymptote)

**Configuration File**: `geometry-diagrams/requirements.txt`  
**Type**: Geometry diagram generation using Asymptote  
**Language**: Asymptote (.asy files)

#### Requirements
- **Asymptote compiler** (asy) - Vector graphics generation
- **Python 3.8+** - For automation scripts
- **LaTeX distribution** - Required by Asymptote

#### Key Dependencies
- `requests>=2.28.0` - HTTP requests
- `pandas>=1.5.0` - Data processing
- `python-dotenv>=0.19.0` - Environment configuration
- `pytest>=7.0.0` - Testing framework
- `black>=22.0.0` - Code formatting

#### Structure
- **`diagrams/`** - Asymptote source files (.asy) for geometric constructions
- **`scripts/`** - Python automation and batch compilation tools
- **`docs/`** - Documentation and contribution guidelines

#### Usage

```bash
asy diagrams/example.asy          # Compile single diagram
python scripts/batch_compile.py   # Generate all diagrams
python scripts/generate_worksheet.py --problem-id 1234
```

---

### Documentation & Content Management

**Configuration File**: `mkdocs.yml`

#### Specification & Tools
**Type**: MkDocs static documentation site  
**Theme**: Material Design for MkDocs  
**Language Support**: Macedonian (mk)  
**Content Format**: Markdown (.md)

#### Key Resources

**Problem Structure**:
- Organized by grade level: `docs/pre_olympiad/`, `docs/grade_6/` through `docs/grade_12/`
- Organized by subject: `algebra/`, `geometry/`, `combinatorics/`, `number_theory/`, `logic/`

**Skill Guides** (`docs/skill_guides/`):
- Pedagogical methodologies (invariants, coloring, telescoping, etc.)
- Theory with practical examples and linked problems

**Metadata Format** (YAML front matter in each problem):
```yaml
grade: 9
category: algebra
difficulty: 5
problem_id: 2025_mun_g9_1
primary_skill: quadratic_equations
```

#### Build & Compilation

```bash
mkdocs serve  # Local development server
mkdocs build  # Generate static site
```

#### Features
- Dark/light theme toggle
- Full-text search with highlighting
- Math formula support via MathJax
- Code copy functionality
- Collapsible solution sections using details/summary HTML

---

## Key Entry Points & Workflows

**Web Generation Pipeline**:
1. Problem input in `docs/` (Markdown with YAML metadata)
2. `tools/indexer.py` parses and generates `problems.json`
3. `web/src/pages/` routes display problems via Astro
4. Static HTML generated with `npm run build`

**Problem Creation Workflow**:
1. Create `.md` file following `templates/problem_template.md`
2. Run `tools/build_problem.py` to validate and process
3. Generate Manim visualization with `tools/process_olympiad.py`
4. Run `tools/indexer.py` to update searchable index

**Visualization Generation**:
1. Manim scripts create MP4 animations
2. Asymptote generates vector diagrams (.pdf)
3. Images stored in `web/public/assets/images/`
4. Referenced in problem markdown via frontmatter

---

## Testing & Validation

**Web Testing**: Playwright for end-to-end browser testing (Chromium)

**Python Testing**: pytest framework available for custom tests

**Validation Tools**:
- `tools/check_assets.py` - Finds problems without illustrations
- `tools/validate_json.py` - Validates JSON structure
- JSON linting for problem metadata

**Quality Checks**:
- Markdown syntax validation
- LaTeX formula verification
- Image asset presence checking
- Link integrity verification through indexing

---

## Build Commands Summary

### Web
```bash
npm run dev       # Development server
npm run build     # Production build
npm run preview   # Preview production
```

### Python Tools
```bash
python tools/indexer.py              # Regenerate problems.json
python tools/build_problem.py        # Build single problem
python tools/process_olympiad.py     # Batch process problems
python tools/batch_manim.py          # Render animations
```

### Documentation
```bash
mkdocs serve     # Local docs server
mkdocs build     # Generate static docs
```

---

*Last Updated: January 2026*
