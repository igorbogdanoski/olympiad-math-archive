# GeoGebra Auto-Matcher System

## Преглед
AI-powered систем за автоматско мапирање на математички задачи со соодветни GeoGebra интерактивни аплети користејќи Google Gemini.

## Структура

### 1. GeoGebra Library (`geogebra_library.json`)
База на достапни GeoGebra материјали со метаподатоци:
- **ID**: Уникатен GeoGebra material ID
- **Наслов**: Македонски и англиски наслов
- **Теми**: Листа на математички теми (geometry, algebra, etc.)
- **Одделение**: Препорачан опсег на одделенија
- **БРО Стандарди**: Поврзани curriculum standards

**Тренутна состојба**: 10 примерни материјали

### 2. Matcher Engine (`geogebra_matcher.py`)
Python класа што користи Gemini 1.5 Pro за intelligent matching:

#### Клучни функции:
- `match_problem()` - Мапира еден problem со GeoGebra applet
- `batch_process()` - Batch процесирање на множество problems
- `_extract_topics_from_text()` - NLP topic detection
- `_format_library_for_prompt()` - Prepare context за AI

#### AI Prompting Strategy:
```python
Inputs:
- Problem text (Macedonian)
- Metadata (grade, topic, difficulty, БРО standard)
- Library of available materials

AI Task:
- Analyze problem semantically
- Match to best GeoGebra applet
- Return confidence score + reasoning
```

### 3. Batch Processing (`batch_geogebra_matching.py`)
Автоматски обработува сите проблеми од problems.json:
1. Load problems (1100 total)
2. Filter geometry/visual problems (~500)
3. Run AI matching
4. Generate suggestions report

## Setup

### Prerequisite:
```bash
# Install dependencies
pip install google-generativeai

# Set API key (get from https://makersuite.google.com/app/apikey)
$env:GEMINI_API_KEY='your-gemini-api-key'  # PowerShell
```

### Test Single Match:
```bash
cd tools
python geogebra_matcher.py
```

### Batch Process:
```bash
python tools/batch_geogebra_matching.py
```

## Workflow

### Phase 1: Batch Matching (Current)
```
problems.json (1100) 
  → Filter geometry (500)
  → AI matching (Gemini)
  → geogebra_matches.json
```

### Phase 2: Manual Review
```
geogebra_matches.json
  → Review UI (web interface)
  → Teacher approval
  → Approved matches
```

### Phase 3: Auto-Update
```
Approved matches
  → Update problems.json
  → Rebuild site
  → Deploy
```

## AI Match Output Format

```json
{
  "problem_id": "sigma_01",
  "filename": "sigma_01.md",
  "match": {
    "material_id": "mp67pxtz",
    "confidence": 0.92,
    "reason": "Одличен match - интерактивни височини во триаголник, соодветно за 8 одделение",
    "alternatives": ["k3mp5x2n", "n5zj6ryk"]
  }
}
```

## Performance Targets

**Goal**: Map 500 geometry problems in 2 days

### Estimated Processing:
- **Rate**: ~30 problems/hour (2 min per problem with AI)
- **Cost**: Gemini 1.5 Pro - ~$0.01 per match = $5 total
- **Accuracy Target**: 70%+ high-confidence matches (≥0.7)

### Success Metrics:
- ✅ 500 problems processed
- ✅ 350+ high-confidence matches (70%)
- ✅ 150+ approved by teachers (30%)
- ✅ Manual GeoGebra creation for remaining 150

## Current Coverage

| Status | Count | Percentage |
|--------|-------|------------|
| Total Problems | 1100 | 100% |
| With GeoGebra ID | 0 | 0% |
| **Missing** | **1100** | **100%** |

### After Phase 1 (Target):
| Category | Count | Percentage |
|----------|-------|------------|
| High Confidence (≥0.7) | 350 | 32% |
| Medium Confidence (0.4-0.7) | 150 | 14% |
| No Match | 600 | 54% |

### After Manual Review (Target):
| Category | Count | Percentage |
|----------|-------|------------|
| Auto-Matched | 350 | 32% |
| Teacher-Approved | 150 | 14% |
| **Total Coverage** | **500** | **46%** |

## Next Steps

### Immediate (Today):
1. ✅ Create GeoGebra library (10 materials)
2. ✅ Build matcher engine with Gemini
3. ✅ Create batch processing script
4. ⏳ **Get valid Gemini API key**
5. ⏳ Test with 10 sample problems

### Short-term (Week 1):
1. Expand GeoGebra library to 50+ materials
2. Run batch matching on 500 geometry problems
3. Build review UI for teacher approval
4. Manual validation of high-confidence matches

### Medium-term (Week 2):
1. Teacher reviews and approves matches
2. Auto-update problems.json with approved IDs
3. Test GeoGebra embeds on live site
4. Create custom GeoGebra applets for gaps

## API Key Setup

### Get Gemini API Key:
1. Visit: https://makersuite.google.com/app/apikey
2. Create project (if needed)
3. Generate API key
4. Set environment variable:

**PowerShell (Windows):**
```powershell
$env:GEMINI_API_KEY='YOUR_API_KEY_HERE'
```

**Bash (Linux/Mac):**
```bash
export GEMINI_API_KEY='YOUR_API_KEY_HERE'
```

**Persistent (Add to profile):**
```powershell
# PowerShell Profile: $PROFILE
[Environment]::SetEnvironmentVariable("GEMINI_API_KEY", "YOUR_KEY", "User")
```

## Library Expansion

### Current Materials (10):
- Triangle altitudes
- Pythagorean theorem
- Circle tangents
- Linear functions
- Quadratic functions
- Similar triangles
- Angle bisector
- Inscribed angles
- Parallelogram
- Linear systems

### Planned Additions (40+):
- Trigonometry (right triangle, unit circle)
- Transformations (rotation, reflection, translation)
- 3D geometry (prisms, pyramids, spheres)
- Statistics (graphs, distributions)
- Probability (tree diagrams, Venn diagrams)
- Number theory (divisibility, primes)

## Troubleshooting

### Error: "API key not valid"
- Verify key at https://makersuite.google.com/app/apikey
- Check environment variable: `echo $env:GEMINI_API_KEY`
- Ensure billing is enabled on Google Cloud project

### Error: "Library not found"
- Check path: `tools/geogebra_library.json` exists
- Run from repo root directory

### Low confidence scores (<0.5)
- Expand GeoGebra library with more materials
- Improve problem metadata (add БРО standards)
- Refine AI prompts with better examples

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────┐
│                    problems.json (1100)                 │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│          Filter Geometry/Visual Problems                │
│                    (~500 problems)                      │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              GeoGebra Auto-Matcher                      │
│            (Gemini 1.5 Pro AI Engine)                   │
│                                                         │
│  Input:                                                 │
│    - Problem text                                       │
│    - Metadata (grade, topic, БРО)                       │
│    - Library (50+ GeoGebra materials)                   │
│                                                         │
│  Output:                                                │
│    - material_id                                        │
│    - confidence (0.0-1.0)                               │
│    - reason (explanation)                               │
│    - alternatives (backups)                             │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│            geogebra_matches.json                        │
│              (AI Suggestions)                           │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              Review UI (Teacher Portal)                 │
│                                                         │
│  - View problem + suggested GeoGebra                    │
│  - Preview interactive applet                           │
│  - Approve / Reject / Edit                              │
│  - Suggest custom applet requirements                   │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│         Auto-Update problems.json                       │
│         (Approved GeoGebra IDs)                         │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              Rebuild & Deploy Site                      │
│        (GeoGebra embeds now live)                       │
└─────────────────────────────────────────────────────────┘
```

## Impact

### Before:
- ❌ 0 problems with GeoGebra visualization
- ❌ Static images only
- ❌ No interactivity

### After (Target):
- ✅ 500 problems with interactive GeoGebra (46%)
- ✅ Students can manipulate diagrams
- ✅ Dynamic visualization of concepts
- ✅ Better understanding through exploration

### Teacher Benefits:
- Save 5 hours/week on diagram creation
- Professional interactive materials
- Curriculum-aligned visualizations
- One-click embedding in lessons

### Student Benefits:
- Learn by doing (interactive exploration)
- Visual understanding of abstract concepts
- Self-paced discovery learning
- Macedonian language interface

---

**Status**: ✅ Phase 1 Ready - Awaiting Gemini API key for testing
**Next**: Set GEMINI_API_KEY and run `python tools/geogebra_matcher.py`
