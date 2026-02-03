# 📋 Worksheet Builder - План за Комплетирање до 100%

**Датум**: Февруари 3, 2026  
**Статус**: Task 1 е 80% готов, треба 2 дена за 100%  
**Цел**: Комплетен Worksheet Builder со сите функционалности  
**Експертска Препорака**: Комплетирај ова ПРВО пред Manim Templates  

---

## ✅ Што е Веќе Завршено (80%)

### Backend API ✅
- **Endpoint**: `/api/worksheet/generate-pdf`
- **Технологија**: WeasyPrint + Jinja2
- **Кирилица**: ✅ Целосна поддршка (Училиште:, Наставник:, Одделение:)
- **PDF Генерирање**: ✅ Работи (11-16KB PDFs)
- **Deployment**: ✅ Production ready (app.mismath.net)

### Frontend UI ✅
- **Локација**: `web/src/pages/teachers/worksheet-builder.astro`
- **Македонски Labels**: ✅ Имплементирано (Approach 3 - Hybrid)
- **API Интеграција**: ✅ Работи
- **Problem Selection**: ✅ Базична функционалност

### Git Commits ✅
```
6d64da31 docs: Add comprehensive Cyrillic encoding fix report
a612fc90 fix: Resolve Cyrillic encoding in worksheet PDFs
c1d3ad02 feat: Implement Approach 3 (Hybrid) for Worksheet Builder labels
```

**Pushed to GitHub**: ✅ `origin/production-clean-v2`

---

## ❌ Што Недостасува (20%)

### 1. Template Library (0/15 templates)
**Проблем**: Наставникот мора рачно да избира проблеми  
**Решение**: Pre-designed templates со автоматска селекција

**Потребни Templates:**
1. ✅ Стандарден Тест (20 проблеми, одговори)
2. ✅ Брза Проверка (5 проблеми, 15 мин)
3. ✅ Домашна (10 проблеми)
4. ✅ Вежбање (30 проблеми, групирани по тема)
5. ✅ Мешана Ревизија (различни теми)
6. ⏳ Загревање (3-5 брзи проблеми)
7. ⏳ Challenge Problems (5 тешки)
8. ⏳ Геометрија Focus (со дијаграми)
9. ⏳ Алгебра Focus (со простор за чекори)
10. ⏳ Текстуални Проблеми
11. ⏳ Multiple Choice
12. ⏳ Точно/Неточно + Краток Одговор
13. ⏳ "Прикажи го Решението"
14. ⏳ Групна Активност (4 ученици)
15. ⏳ Независна Студија

### 2. Advanced Problem Selection (0%)
**Проблем**: Нема филтри, нема preview  
**Потребно**:
- ❌ Филтри: Тема, Одделение, Тежина
- ❌ Preview пред export
- ❌ Drag & drop reordering
- ❌ Problem замена (Replace button)
- ❌ Problem бришење (Remove button)

### 3. Smart Features (0%)
**Проблем**: Наставникот мора рачно да балансира тежина  
**Потребно**:
- ❌ Auto-Balance (30% easy, 50% medium, 20% hard)
- ❌ БРО Coverage Check (warning за недостасувачки стандарди)
- ❌ Duplicate Prevention (last 30 days)
- ❌ Point Auto-Assignment (based on difficulty)

### 4. Export Options (0%)
**Проблем**: Само basic PDF export  
**Потребно**:
- ❌ Include/exclude answer key (checkbox)
- ❌ Include/exclude БРО standards (checkbox)
- ❌ QR code за online верзија (optional)
- ❌ Save as Template (за повторна употреба)

---

## 📅 ПЛАН ЗА ИМПЛЕМЕНТАЦИЈА (2 дена)

### **ДЕН 1 (Февруари 4, 2026) - 6 часа**

#### Утро (3 часа): Template System
**Цел**: 5 working templates + UI selector

**Task 1.1: Template Definitions (1 час)**
```javascript
// backend/templates/worksheet_templates.js
export const templates = {
  standard_test: {
    name: "Стандарден Тест",
    problems: 20,
    difficulty: { easy: 0.3, medium: 0.5, hard: 0.2 },
    include_solutions: true,
    time_limit: 45,
    description: "Класичен тест со 20 задачи и одговори"
  },
  quick_quiz: {
    name: "Брза Проверка",
    problems: 5,
    difficulty: { easy: 0.6, medium: 0.4, hard: 0 },
    include_solutions: false,
    time_limit: 15,
    description: "5 задачи за брза проверка на знаењето"
  },
  homework: {
    name: "Домашна Задача",
    problems: 10,
    difficulty: { easy: 0.4, medium: 0.4, hard: 0.2 },
    include_solutions: true,
    time_limit: null,
    description: "10 задачи за вежбање дома"
  },
  practice_sheet: {
    name: "Вежба Лист",
    problems: 30,
    difficulty: { easy: 0.4, medium: 0.5, hard: 0.1 },
    include_solutions: true,
    time_limit: null,
    description: "30 задачи групирани по тема"
  },
  mixed_review: {
    name: "Мешана Ревизија",
    problems: 15,
    difficulty: { easy: 0.3, medium: 0.5, hard: 0.2 },
    include_solutions: true,
    time_limit: 30,
    description: "15 задачи од различни теми"
  }
};
```

**Task 1.2: Template Selector UI (1 час)**
```astro
<!-- web/src/pages/teachers/worksheet-builder.astro -->
<div class="template-selector">
  <h3>Избери Template</h3>
  <div class="template-grid">
    {Object.entries(templates).map(([key, template]) => (
      <button class="template-card" data-template={key}>
        <h4>{template.name}</h4>
        <p>{template.description}</p>
        <div class="template-meta">
          <span>📝 {template.problems} задачи</span>
          {template.time_limit && <span>⏱️ {template.time_limit} мин</span>}
        </div>
      </button>
    ))}
  </div>
</div>
```

**Task 1.3: Auto-Select Problems (1 час)**
```javascript
// Auto-select problems based on template
async function selectProblemsFromTemplate(template, filters) {
  const { problems: count, difficulty } = template;
  
  // Calculate counts per difficulty
  const easyCount = Math.floor(count * difficulty.easy);
  const mediumCount = Math.floor(count * difficulty.medium);
  const hardCount = count - easyCount - mediumCount;
  
  // Fetch problems
  const allProblems = await fetchProblems(filters);
  
  // Filter by difficulty
  const easy = shuffle(allProblems.filter(p => p.difficulty <= 2)).slice(0, easyCount);
  const medium = shuffle(allProblems.filter(p => p.difficulty === 3)).slice(0, mediumCount);
  const hard = shuffle(allProblems.filter(p => p.difficulty >= 4)).slice(0, hardCount);
  
  return [...easy, ...medium, ...hard];
}
```

#### Попладне (3 часа): Problem Selection UI

**Task 1.4: Filters Implementation (1.5 часа)**
```astro
<!-- Advanced filters -->
<div class="filters">
  <div class="filter-group">
    <label>Тема:</label>
    <select id="topic-filter">
      <option value="">Сите</option>
      <option value="geometry">Геометрија</option>
      <option value="algebra">Алгебра</option>
      <option value="combinatorics">Комбинаторика</option>
      <option value="number_theory">Теорија на броеви</option>
    </select>
  </div>
  
  <div class="filter-group">
    <label>Одделение:</label>
    <div class="grade-buttons">
      <button class="grade-btn" data-grade="6">6</button>
      <button class="grade-btn" data-grade="7">7</button>
      <button class="grade-btn" data-grade="8">8</button>
      <button class="grade-btn" data-grade="9">9</button>
    </div>
  </div>
  
  <div class="filter-group">
    <label>БРО Стандард (optional):</label>
    <input type="text" id="bro-filter" placeholder="МАТ.7.Г.3">
  </div>
</div>
```

**Task 1.5: Problem Preview & Reorder (1.5 часа)**
```javascript
// Drag & drop reordering
import Sortable from 'sortablejs';

const problemList = document.getElementById('problem-list');
Sortable.create(problemList, {
  animation: 150,
  handle: '.drag-handle',
  onEnd: function(evt) {
    reorderProblems(evt.oldIndex, evt.newIndex);
  }
});

// Problem card with actions
function renderProblemCard(problem, index) {
  return `
    <div class="problem-card" data-id="${problem.id}">
      <span class="drag-handle">⋮⋮</span>
      <div class="problem-content">
        <strong>Задача ${index + 1}:</strong>
        <p>${problem.content.substring(0, 100)}...</p>
        <div class="problem-meta">
          <span class="difficulty-badge">${getDifficultyLabel(problem.difficulty)}</span>
          <span class="points">${problem.points || 5} поени</span>
        </div>
      </div>
      <div class="problem-actions">
        <button onclick="replaceProblem(${problem.id})">🔄 Замени</button>
        <button onclick="removeProblem(${problem.id})">🗑️ Избриши</button>
      </div>
    </div>
  `;
}
```

---

### **ДЕН 2 (Февруари 5, 2026) - 6 часа**

#### Утро (3 часа): Smart Features

**Task 2.1: Auto-Balance Algorithm (1 час)**
```javascript
// backend/routers/worksheets.py
def auto_balance_problems(problems, target_count=15, distribution=None):
    """
    Auto-balance problem difficulty
    Default: 30% easy, 50% medium, 20% hard
    """
    if distribution is None:
        distribution = {"easy": 0.3, "medium": 0.5, "hard": 0.2}
    
    easy_count = int(target_count * distribution["easy"])
    medium_count = int(target_count * distribution["medium"])
    hard_count = target_count - easy_count - medium_count
    
    easy = [p for p in problems if p["difficulty"] <= 2]
    medium = [p for p in problems if p["difficulty"] == 3]
    hard = [p for p in problems if p["difficulty"] >= 4]
    
    import random
    selected = (
        random.sample(easy, min(easy_count, len(easy))) +
        random.sample(medium, min(medium_count, len(medium))) +
        random.sample(hard, min(hard_count, len(hard)))
    )
    
    return selected
```

**Task 2.2: БРО Coverage Check (1 час)**
```javascript
// frontend: BRO coverage indicator
function checkBROCoverage(problems, requiredStandards) {
  const covered = new Set(problems.map(p => p.bro_standard).filter(Boolean));
  const missing = requiredStandards.filter(s => !covered.has(s));
  
  if (missing.length > 0) {
    return {
      status: 'warning',
      message: `⚠️ Недостасуваат: ${missing.join(', ')}`,
      coverage: ((requiredStandards.length - missing.length) / requiredStandards.length * 100).toFixed(0)
    };
  }
  
  return {
    status: 'success',
    message: '✓ Сите БРО стандарди покриени',
    coverage: 100
  };
}

// Display coverage
function displayBROCoverage(coverage) {
  const indicator = document.getElementById('bro-coverage');
  indicator.innerHTML = `
    <div class="coverage-bar" style="width: ${coverage.coverage}%"></div>
    <span>${coverage.message}</span>
  `;
  indicator.className = `coverage-indicator ${coverage.status}`;
}
```

**Task 2.3: Duplicate Prevention (1 час)**
```javascript
// Track recently used problems (localStorage)
function filterRecentlyUsed(problems, daysAgo = 30) {
  const recentWorksheets = JSON.parse(localStorage.getItem('recent_worksheets') || '[]');
  const cutoffDate = new Date(Date.now() - daysAgo * 24 * 60 * 60 * 1000);
  
  // Get recently used problem IDs
  const usedIds = new Set();
  recentWorksheets
    .filter(ws => new Date(ws.created_at) > cutoffDate)
    .forEach(ws => ws.problem_ids.forEach(id => usedIds.add(id)));
  
  // Filter out recently used
  const fresh = problems.filter(p => !usedIds.has(p.id));
  
  // If too few fresh problems, include some recent ones
  if (fresh.length < 10) {
    return problems; // Use all problems
  }
  
  return fresh;
}

// Save worksheet to recent history
function saveToRecentHistory(worksheet) {
  const recent = JSON.parse(localStorage.getItem('recent_worksheets') || '[]');
  recent.unshift({
    id: worksheet.id,
    title: worksheet.title,
    problem_ids: worksheet.problems.map(p => p.id),
    created_at: new Date().toISOString()
  });
  
  // Keep only last 50 worksheets
  localStorage.setItem('recent_worksheets', JSON.stringify(recent.slice(0, 50)));
}
```

#### Попладне (3 часа): Export Options + Polish

**Task 2.4: Export Options UI (1 час)**
```astro
<!-- Export modal -->
<div class="export-modal">
  <h3>Експортирај Работен Лист</h3>
  
  <div class="export-options">
    <label>
      <input type="checkbox" id="include-solutions" checked>
      Вклучи одговори (посебна страница)
    </label>
    
    <label>
      <input type="checkbox" id="include-work-space" checked>
      Вклучи празно место за решение
    </label>
    
    <label>
      <input type="checkbox" id="include-bro" checked>
      Додади БРО стандарди на дно
    </label>
    
    <label>
      <input type="checkbox" id="include-qr">
      Вклучи QR код за онлајн верзија
    </label>
  </div>
  
  <div class="export-actions">
    <button id="export-pdf" class="btn-primary">📄 Експортирај PDF</button>
    <button id="save-template" class="btn-secondary">💾 Зачувај како Template</button>
  </div>
</div>
```

**Task 2.5: Backend Export Logic (1 час)**
```python
# backend/routers/worksheets.py - update generate_worksheet_pdf()
def generate_worksheet_pdf(data: WorksheetRequest) -> BytesIO:
    # ... existing code ...
    
    # Export options
    export_options = data.export_options or {}
    include_solutions = export_options.get('include_solutions', True)
    include_work_space = export_options.get('include_work_space', True)
    include_bro = export_options.get('include_bro', False)
    include_qr = export_options.get('include_qr', False)
    
    # Generate QR code if requested
    qr_code_data = None
    if include_qr:
        worksheet_url = f"https://app.mismath.net/worksheet/{data.id}"
        qr_code_data = generate_qr_code(worksheet_url)
    
    # Add БРО standards footer if requested
    bro_standards = []
    if include_bro:
        bro_standards = list(set(p.bro_standard for p in data.problems if p.bro_standard))
    
    # Render template with options
    html_content = template.render(
        title=data.title,
        labels=labels,
        metadata=metadata,
        problems=problems,
        include_solutions=include_solutions,
        include_work_space=include_work_space,
        bro_standards=bro_standards,
        qr_code=qr_code_data,
        footer_text=footer_text
    )
    
    # ... rest of code ...
```

**Task 2.6: Save as Template (1 час)**
```javascript
// Save custom template
async function saveAsTemplate(worksheet) {
  const templateName = prompt('Име на template:');
  if (!templateName) return;
  
  const customTemplate = {
    id: `custom_${Date.now()}`,
    name: templateName,
    problems: worksheet.problems.length,
    difficulty: calculateDifficultyDistribution(worksheet.problems),
    topic_filters: worksheet.filters,
    grade: worksheet.grade,
    created_at: new Date().toISOString(),
    problem_ids: worksheet.problems.map(p => p.id)
  };
  
  // Save to localStorage
  const templates = JSON.parse(localStorage.getItem('custom_templates') || '[]');
  templates.push(customTemplate);
  localStorage.setItem('custom_templates', JSON.stringify(templates));
  
  alert(`✅ Template "${templateName}" зачуван!`);
}
```

---

## 🎯 УСПЕШНИ МЕТРИКИ

### Обавезни (Must-Have)
- ✅ Worksheet creation time: **< 5 минути**
- ✅ PDF export success rate: **> 95%**
- ✅ Cyrillic support: **100%**
- ⏳ Template library: **15+ templates**
- ⏳ БРО coverage check: **Working**
- ⏳ Auto-balance: **Working**

### Желни (Nice-to-Have)
- ⏳ Drag & drop reordering: **Intuitive**
- ⏳ Problem preview: **Fast (< 1s)**
- ⏳ Duplicate prevention: **Last 30 days**
- ⏳ Custom templates: **Save & reuse**

---

## 📊 ТЕСТИРАЊЕ (Efter Имплементација)

### Test Cases
1. **Template Selection**
   - ✅ Select "Стандарден Тест" → 20 problems auto-selected
   - ✅ Difficulty distribution: 30% easy, 50% medium, 20% hard
   - ✅ All filters applied correctly

2. **Problem Management**
   - ✅ Drag & drop reordering works
   - ✅ Replace problem works (similar difficulty)
   - ✅ Remove problem works (recalculate points)

3. **БРО Coverage**
   - ✅ Warning shows if standards missing
   - ✅ Coverage percentage accurate
   - ✅ Suggests problems to fill gaps

4. **Export Options**
   - ✅ Answer key on separate page
   - ✅ Work space included (2cm between problems)
   - ✅ БРО standards in footer
   - ✅ QR code generates correctly

5. **Duplicate Prevention**
   - ✅ Recent problems filtered (last 30 days)
   - ✅ Falls back to all if < 10 fresh problems

---

## 🚀 DEPLOYMENT PLAN

### Efter Тестирање (День 3)
1. **Frontend Build**
   ```bash
   cd web && npm run build
   ```

2. **Backend Deploy**
   ```bash
   scp backend/routers/worksheets.py root@76.13.129.9:/tmp/
   ssh root@76.13.129.9 "docker cp /tmp/worksheets.py math_api:/app/routers/ && docker restart math_api"
   ```

3. **Frontend Deploy**
   ```bash
   scp -r web/dist/teachers/worksheet-builder/* root@76.13.129.9:/var/www/html/teachers/worksheet-builder/
   ssh root@76.13.129.9 "chown -R www-data:www-data /var/www/html/"
   ```

4. **Verification**
   - ✅ Test production URL: https://app.mismath.net/teachers/worksheet-builder/
   - ✅ Create 3 test worksheets (different templates)
   - ✅ Verify PDF generation works
   - ✅ Check Cyrillic rendering

---

## 📝 ДОКУМЕНТАЦИЈА

### User Guide (Create після deployment)
1. **Брз Старт**: 5-minute tutorial video
2. **Template Gallery**: Screenshots + descriptions
3. **Best Practices**: Tips for teachers
4. **FAQ**: Common questions
5. **Troubleshooting**: Known issues

### Technical Docs
1. **API Documentation**: Updated OpenAPI spec
2. **Template System**: How to add new templates
3. **Custom Templates**: User guide for saving templates

---

## 🎓 СЛЕДНИ ЧЕКОРИ (Efter Worksheet Builder е 100%)

### Веднаш после (День 4-5):
✅ **Manim Templates** (10 most used)
- Geometry: Pythagorean, Triangles, Circles, Area, Transformations (5)
- Algebra: Linear Equations, Quadratic, Systems (3)
- Number Theory: Prime Factorization, Pascal's Triangle (2)

### Во рок од 1 недела:
✅ **Teacher Pilot Program**
- 5-10 pilot teachers
- Collect feedback
- Iterate based on usage patterns

### Долгорочно (Месец 2):
- Lesson Plan Builder
- Assessment Builder (auto-grading)
- Analytics Dashboard
- Mobile app prototype

---

## 💡 КЛУЧНИ ТОЧКИ ЗА УСПЕХ

### Педагошки Приоритети
1. **Брзина**: < 5 минути за создавање worksheet
2. **Квалитет**: Professional PDF излез (print-ready)
3. **Флексибилност**: Templates + custom options
4. **БРО Alignment**: Automatic curriculum coverage check
5. **Користење**: Zero learning curve (интуитивен UI)

### Технички Приоритети
1. **Performance**: Fast problem selection (< 1s)
2. **Reliability**: 99%+ PDF generation success
3. **Scalability**: Handle 100+ concurrent users
4. **Maintainability**: Clean code, good documentation
5. **Monitoring**: Track usage metrics

---

## 📞 КОНТАКТ / HELP

**Ако има проблеми:**
1. Check Docker logs: `docker logs math_api`
2. Verify frontend build: `npm run build` успешен
3. Test API directly: `curl POST /api/worksheet/generate-pdf`
4. Check browser console for JavaScript errors

**Git Repository**: 
```
https://github.com/igorbogdanoski/olympiad-math-archive
Branch: production-clean-v2
```

**Production Server**: 
```
SSH: root@76.13.129.9
Web: https://app.mismath.net
API: http://76.13.129.9:8000
```

---

## ✅ СТАТУС TRACKING

**Тековен Статус**: 80% Complete  
**Цел**: 100% Complete за 2 дена  
**ETA**: Февруари 5, 2026 (EOD)  

**Прогрес Dashboard**:
```
День 1: [░░░░░░░░░░] 0% → 50% (Template System + Problem Selection)
День 2: [░░░░░░░░░░] 50% → 100% (Smart Features + Export Options)
```

**Следна Сесија**: 
- **Датум**: Февруари 4, 2026
- **Старт**: День 1, Task 1.1 (Template Definitions)
- **Очекувано Траење**: 6 часа (со паузи)

---

**🎯 ДА ЗАПОЧНЕМЕ! Worksheet Builder → 100% → Production Ready! 🚀**
