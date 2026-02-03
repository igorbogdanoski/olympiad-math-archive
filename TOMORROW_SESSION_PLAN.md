# План за Утрешна Сесија - 02 Feb 2026 (Вечер)

## 🎯 Главна Цел: Phase 4A Day 2 - Worksheet Generator (40% Remaining)

---

## ✅ Што е ЗАВРШЕНО (Денес - Day 1)

### Database & Infrastructure ✅
- ✅ MongoDB running with 1100 problems
- ✅ Backend API (minimal version) deployed
- ✅ Homepage statistics working (1100 tasks, 62.7% coverage)
- ✅ All services stable and tested

### Worksheet Generator Foundation (60%) ✅
- ✅ Database schema (worksheets_schema.sql)
- ✅ 15 professional templates (test, quiz, homework, etc.)
- ✅ 3-step UI workflow (Template → Problems → Preview)
- ✅ Filter panel (subject, grade, difficulty, БРО)
- ✅ Statistics dashboard
- ✅ Teachers portal integration
- ✅ Responsive design

### Files Created ✅
- `backend/database/worksheets_schema.sql`
- `web/src/data/worksheet_templates.ts`
- `web/src/pages/teachers/worksheet-builder.astro`
- `backend/api_minimal.py` (production API)
- `DATABASE_DEPLOYMENT_SESSION_2026-02-02.md` (docs)

---

## 🚀 Што ТРЕБА да се НАПРАВИ (Утре - Day 2)

### Priority 1: Problem Rendering (2-3 hours) 🔴

**Што треба:**
1. JavaScript за прикажување на проблеми
   - Fetch problems from API: `GET /api/problems?ids=1,2,3`
   - Render problem content (HTML)
   - Display images/diagrams
   - Render mathematical formulas (KaTeX)

2. Problem Card Component
   - Problem number badge
   - Difficulty indicator
   - Points display
   - БРО standard tag
   - Drag handle icon

**Files:**
- Create: `web/src/scripts/worksheet-problem-renderer.js`
- Update: `web/src/pages/teachers/worksheet-builder.astro` (add script tag)

**API Endpoint Needed:**
```javascript
// GET /api/problems?ids=1,2,3
// Response: [{ id: 1, content: "...", difficulty: "medium", ... }]
```

**Action**: Провери дали `routers/problems.py` има овој endpoint, ако не - креирај го.

---

### Priority 2: Drag-and-Drop Reordering (1-2 hours) 🟡

**Што треба:**
1. Integrate Sortable.js library
   - Add CDN link или npm install
   - Initialize on problems grid
   - Handle drag events

2. Update problem order in state
   - Track problem positions
   - Renumber problems after reorder
   - Show visual feedback during drag

**Files:**
- Update: `web/src/pages/teachers/worksheet-builder.astro`
- CDN: `https://cdn.jsdelivr.net/npm/sortablejs@latest/Sortable.min.js`

**Implementation:**
```javascript
// Initialize Sortable
const problemsGrid = document.getElementById('selected-problems-grid');
Sortable.create(problemsGrid, {
  animation: 150,
  handle: '.drag-handle',
  onEnd: function(evt) {
    // Update problem order
    updateProblemOrder();
  }
});
```

---

### Priority 3: Backend API Endpoints (2-3 hours) 🟡

**Потребни Endpoints:**

#### 3.1 Get Problems by IDs
```python
# File: backend/routers/problems.py (or create it)
@router.get("/problems")
async def get_problems(ids: str):
    """Get problems by comma-separated IDs"""
    problem_ids = [int(id) for id in ids.split(",")]
    db = get_database()
    problems = list(db["problems"].find({"id": {"$in": problem_ids}}))
    return problems
```

#### 3.2 Generate PDF
```python
# File: backend/routers/worksheet.py (create if doesn't exist)
@router.post("/worksheet/generate-pdf")
async def generate_worksheet_pdf(request: WorksheetRequest):
    """Generate PDF from worksheet data"""
    # TODO: Implement PDF generation
    # Options:
    # 1. WeasyPrint (HTML → PDF)
    # 2. ReportLab (programmatic PDF)
    # 3. Playwright (browser rendering)
    pass
```

#### 3.3 Save Worksheet
```python
@router.post("/worksheet/save")
async def save_worksheet(worksheet: WorksheetData):
    """Save worksheet to database"""
    db = get_database()
    result = db["worksheets"].insert_one(worksheet.dict())
    return {"id": str(result.inserted_id)}
```

**Action**: 
- Провери дали `backend/routers/problems.py` постои
- Креирај `backend/routers/worksheet.py` ако не постои
- Додади routeri во `api_minimal.py`

---

### Priority 4: PDF Generation Engine (3-4 hours) 🔴

**Опции:**

#### Опција 1: WeasyPrint (Препорачано) ⭐
```bash
# Install
pip install weasyprint

# Usage
from weasyprint import HTML
HTML(string=html_content).write_pdf('worksheet.pdf')
```
**Pros**: Одличен HTML/CSS support, лесен за употреба
**Cons**: Зависности за system fonts

#### Опција 2: ReportLab
```python
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
```
**Pros**: Lightweight, no external deps
**Cons**: Programmatic (тешко за сложени layouts)

#### Опција 3: Playwright (веќе го имаме)
```python
page.pdf(path='worksheet.pdf', format='A4')
```
**Pros**: Perfect rendering (browser-based)
**Cons**: Тешко за deployment (ги имавме проблемите)

**Препорака**: Почни со WeasyPrint, fallback на ReportLab

**HTML Template:**
```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    @page { size: A4; margin: 2cm; }
    body { font-family: Arial; }
    .problem { page-break-inside: avoid; margin: 1em 0; }
    .answer-key { page-break-before: always; }
  </style>
</head>
<body>
  <h1>{{ worksheet.title }}</h1>
  <p>Име: __________ Одделение: ____ Датум: _______</p>
  
  {% for problem in problems %}
  <div class="problem">
    <strong>{{ loop.index }}. ({{ problem.points }} поени)</strong>
    <div>{{ problem.content }}</div>
  </div>
  {% endfor %}
  
  <div class="answer-key">
    <h2>Одговори</h2>
    {% for problem in problems %}
    <div>{{ loop.index }}. {{ problem.answer }}</div>
    {% endfor %}
  </div>
</body>
</html>
```

---

### Priority 5: БРО Coverage Checker (1 hour) 🟢

**Што треба:**
1. Анализирај избрани проблеми
2. Извлечи БРО стандарди од секој проблем
3. Прикажи покриени области
4. Highlight празнини

**Implementation:**
```javascript
function analyzeBROCoverage(selectedProblems) {
  const standards = new Set();
  selectedProblems.forEach(p => {
    if (p.primary_skill) standards.add(p.primary_skill);
    if (p.secondary_skills) {
      p.secondary_skills.forEach(s => standards.add(s));
    }
  });
  
  return {
    covered: Array.from(standards),
    count: standards.size,
    percentage: (standards.size / 391) * 100  // 391 total БРО standards
  };
}
```

---

### Priority 6: Testing & Deployment (1-2 hours) 🟢

**Local Testing:**
```bash
# 1. Test API endpoints
curl http://localhost:8000/api/problems?ids=1,2,3

# 2. Test worksheet creation flow
# - Select template
# - Add problems
# - Generate preview
# - Download PDF

# 3. Test edge cases
# - 0 problems selected
# - 100+ problems selected
# - Special characters in title
# - Missing БРО standards
```

**Production Deployment:**
```bash
# 1. Build frontend
cd web
npm run build

# 2. Deploy to server
scp -r dist/* root@76.13.129.9:/var/www/html/

# 3. Update API (if needed)
ssh root@76.13.129.9
cd /opt/olympiad-math-archive/backend
# Add new routers to api_minimal.py
docker build -t app-api:latest -f Dockerfile .
docker restart math_api

# 4. Test production
curl https://app.mismath.net/api/problems?ids=1,2,3
```

---

## 📋 Checklist за Утре

### Backend Tasks
- [ ] Провери дали `routers/problems.py` постои
- [ ] Креирај `GET /api/problems?ids=...` endpoint
- [ ] Креирај `routers/worksheet.py`
- [ ] Имплементирај `POST /api/worksheet/generate-pdf`
- [ ] Додади routeri во `api_minimal.py`
- [ ] Одлучи за PDF engine (WeasyPrint vs ReportLab)
- [ ] Тестирај PDF генерирање локално

### Frontend Tasks
- [ ] Креирај `worksheet-problem-renderer.js`
- [ ] Интегрирај Sortable.js
- [ ] Имплементирај drag-and-drop
- [ ] Додади БРО coverage checker
- [ ] Тестирај целиот workflow
- [ ] Build и deploy

### Testing
- [ ] Test template selection
- [ ] Test problem filtering
- [ ] Test problem selection/deselection
- [ ] Test drag-and-drop reordering
- [ ] Test PDF generation
- [ ] Test БРО coverage display
- [ ] Test на production (app.mismath.net)

---

## 🔧 Потребни Команди

### Стартување на Development Environment
```bash
# Terminal 1: MongoDB (already running on server)
# Terminal 2: Backend API
cd backend
python api_minimal.py  # or uvicorn api_minimal:app --reload

# Terminal 3: Frontend
cd web
npm run dev
```

### Deployment Commands
```bash
# Frontend build
cd web
npm run build

# Deploy frontend
scp -r dist/* root@76.13.129.9:/var/www/html/

# Deploy backend (if API changes)
ssh root@76.13.129.9
cd /opt/olympiad-math-archive/backend
docker build -t app-api:latest -f Dockerfile .
docker restart math_api
```

---

## ⚠️ Потенцијални Проблеми

### Problem 1: API Endpoint Missing
**Симптом**: Problems не се прикажуваат
**Решение**: Провери дали `/api/problems` endpoint е имплементиран

### Problem 2: KaTeX Not Rendering
**Симптом**: Math формули не се прикажуваат
**Решение**: Додади KaTeX CDN во HTML head

### Problem 3: PDF Generation Fails
**Симптом**: Error при генерирање PDF
**Решение**: 
- Провери дали WeasyPrint е инсталиран
- Fallback на ReportLab
- Провери HTML template syntax

### Problem 4: Drag-and-Drop Not Working
**Симптом**: Problems не се движат
**Решение**: 
- Провери дали Sortable.js е loaded
- Провери selector (`getElementById`)
- Провери CSS класи

---

## 📊 Очекуван Прогрес

**Почеток на Сесија**: 60% Complete
**Крај на Сесија**: 100% Complete ✅

**Време Проценка**:
- Problem Rendering: 2-3h
- Drag-and-Drop: 1-2h
- Backend Endpoints: 2-3h
- PDF Generation: 3-4h
- БРО Coverage: 1h
- Testing: 1-2h
**Вкупно**: 10-15 часа работа

**Реалистичен План**: 2 работни сесии (вечерва + утре)

---

## 🎓 Референци

### PDF Libraries
- WeasyPrint: https://weasyprint.org/
- ReportLab: https://www.reportlab.com/
- Playwright PDF: https://playwright.dev/python/docs/api/class-page#page-pdf

### JavaScript Libraries
- Sortable.js: https://sortablejs.github.io/Sortable/
- KaTeX: https://katex.org/

### API Documentation
- FastAPI: https://fastapi.tiangolo.com/
- MongoDB PyMongo: https://pymongo.readthedocs.io/

---

## 📝 Забелешки

- **MongoDB**: Има 1100 проблеми, не треба повторно да се пополнува
- **API**: Минимална верзија работи, може да се прошири
- **Frontend**: Build time ~30s, deployment time ~2min
- **Testing**: Користи локален environment пред deployment

---

**Последна Ажурација**: 02 Feb 2026, 03:50 AM
**Следна Сесија**: 02 Feb 2026, Вечер (Phase 4A Day 2)
**Статус**: Prepared and Ready ✅
