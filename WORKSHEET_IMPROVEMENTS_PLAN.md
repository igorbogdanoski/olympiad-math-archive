# Одговори на Прашања за Worksheet Builder

## Датум: 02 Feb 2026, 23:15

---

## 1️⃣ Како да се избират повеќе задачи?

### ✅ ИМПЛЕМЕНТИРАНО (Веќе работи!)

**Опции за bulk selection:**

1. **✅ Избери сите** - селектира сите видливи проблеми (до 50)
2. **❌ Откажи сите** - десელектира сите проблеми
3. **🎲 10 random** - избира 10 random проблеми од филтрираните

**Како работи:**
- Кликни на копчето "✅ Избери сите" → сите 50 проблеми одеднаш
- Користи филтри (grade, difficulty, topic) → "Избери сите" → само филтрираните
- "🎲 10 random" → лесен начин за брз worksheet

**Примери:**
```
1. Филтер: Grade 7, Geometry → "Избери сите" → сите 7 одд. геометрија проблеми
2. Филтер: Difficulty 1-5 → "🎲 10 random" → 10 лесни random проблеми
3. Филтер: Topic Algebra → "Избери сите" → site алгебра проблеми
```

---

## 2️⃣ Како да се корегира "Untitled Problem"?

### ✅ ИМПЛЕМЕНТИРАНО (Веќе работи!)

**Проблемот:** MongoDB има encoding issues со cyrillic text.

**Решението (автоматско):**
```javascript
// 1. Проба 1: Користи title
displayTitle = problem.title

// 2. Ако title има "????" или encoding issues:
displayTitle = problem.problem_id  // пример: "sigma_138_1874"

// 3. Ако problem_id не постои:
displayTitle = "Задача " + problem.id  // пример: "Задача 42"

// 4. Ако ништо не работи:
displayTitle = content.substring(0, 60)  // првите 60 знаци од содржина
```

**Резултат:**
- ❌ Пред: "Untitled Problem" или "????????????"
- ✅ Сега: "sigma_138_1874" или "Задача 42" или кратки preview од содржина

**Подолгорочно решение** (за наредна сесија):
1. Fix encoding во MongoDB - re-import проблемите со правилен UTF-8
2. Додај `title_mk` поле со гарантирана cyrillic подршка
3. Валидација на import - reject проблеми без валиден наслов

---

## 3️⃣ Мој Став за Подобрување на Worksheet Builder

### 🎯 Приоритети (по важност)

#### **A. КРИТИЧНИ** (Мора да се направи пред production)
1. **PDF Generation** 🔴
   - WeasyPrint или ReportLab
   - Generate worksheet со math формули (KaTeX)
   - Answer key на крајот
   - **Време**: 3-4 часа

2. **Fix MongoDB Encoding** 🟠
   - Re-import сите проблеми со UTF-8
   - Валидација на cyrillic text
   - **Време**: 1-2 часа

3. **Save Worksheet** 🟡
   - POST /api/worksheet/save
   - Зачувај во PostgreSQL
   - Link кон created_by teacher
   - **Време**: 2 часа

#### **B. ВАЖНИ** (Подобрува UX significantly)
4. **Drag-and-Drop Reordering** 🟢
   - Sortable.js интеграција
   - Reorder проблеми со drag
   - **Време**: 1-2 часа

5. **БРО Coverage Checker** 🟢
   - Анализа на избрани проблеми
   - Прикажи покриени стандарди
   - Highlight празнини
   - **Време**: 1 час

6. **Preview Improvements** 🟢
   - Math rendering (KaTeX)
   - Images/diagrams
   - Better formatting
   - **Време**: 1 час

#### **C. NICE TO HAVE** (За понатаму)
7. **Search во Problems** 🔵
   - Search by keyword
   - Filter by БРО standard
   - Advanced filters

8. **Worksheet Templates** 🔵
   - Pre-made worksheets
   - Community sharing
   - Import/export

9. **Analytics** 🔵
   - Most used problems
   - Difficulty distribution
   - БРО coverage statistics

### 📊 Completion Status

**Сега (23:15, 02 Feb 2026):**
```
Template Selection:    ✅ 100%
Problem Filtering:     ✅ 100%
Problem Selection:     ✅ 100%
Bulk Selection:        ✅ 100%
Preview:               ✅ 80% (без math rendering)
PDF Generation:        ❌ 0%
Save Worksheet:        ❌ 0%
Drag-and-Drop:         ❌ 0%
БРО Coverage:          ❌ 0%

TOTAL: 65% Complete
```

**Target за крај на вечер:**
```
PDF Generation:        ✅ 100%
Save Worksheet:        ✅ 100%

TOTAL: 85% Complete
```

---

## 4️⃣ Curriculum Activities (Предлог Активности) - Каде ќе се користат?

### 📚 Што се "Предлог Активности"?

**Од Официјални Наставни Програми:**
- Министерство за Образование ги објавува програми за 1-9 одделение
- Секоја програма содржи:
  - БРО стандарди (391 total)
  - **Предлог активности** за секој стандард
  - Препораки за часови, оценување, материјали

**Пример:**
```
БРО Стандард: M.6.1.2.1
"Ученикот ги применува основните својства на триаголниците"

Предлог Активности:
1. Конструирање триаголници со различни страни
2. Мерење агли и проверка на сума 180°
3. Групна работа: класификација по агли и страни
4. Решавање проблеми со примена на Питагорина теорема
```

### 🎯 Каде ќе ги искористиме?

#### **Локација 1: Lesson Planner** ⭐ (Primary Use)
**Pathname:** `/teachers/lesson-planner`

**Функционалност:**
```javascript
// User selects БРО standard
selectedStandard = "M.6.1.2.1"

// System shows:
1. Standard description
2. **Suggested Activities** (од официјална програма)
3. Existing problems that cover this standard
4. Recommended worksheets
5. Time allocation (45 min, 90 min, etc.)

// Teacher can:
- Add activities to lesson plan
- Customize activities
- Generate lesson plan PDF
- Link problems to specific activities
```

**Имплементација:**
```typescript
// web/src/data/curriculum_activities.ts
export const CURRICULUM_ACTIVITIES = {
  "M.6.1.2.1": {
    standard: "M.6.1.2.1",
    title: "Применување својства на триаголници",
    grade: 6,
    topic: "geometry",
    suggestedActivities: [
      {
        id: "act_6_1_2_1_a",
        title: "Конструирање триаголници",
        duration: 20,
        materials: ["лењир", "шестар", "транспортир"],
        steps: [
          "Демонстрација на конструкција",
          "Индивидуална работа",
          "Групна дискусија"
        ],
        learningObjectives: [
          "Ученикот конструира триаголник по дадени елементи",
          "Ученикот класификува триаголници"
        ]
      },
      // ... more activities
    ],
    relatedProblems: [123, 456, 789], // problem IDs
    timeAllocation: "3 часа", // од програмата
    assessmentSuggestions: [
      "Практична проверка на конструкција",
      "Тест со 5 задачи"
    ]
  }
}
```

#### **Локација 2: Worksheet Builder** (Secondary Use)
**Pathname:** `/teachers/worksheet-builder`

**Функционалност:**
```javascript
// When selecting problems:
// Show "Suggested Activity" badge if problem has related activity

<div class="problem-card">
  <span class="badge">Geometry</span>
  <span class="badge">Grade 6</span>
  {problem.hasActivity && (
    <span class="badge badge-activity" title="Има предлог активност">
      📚 Activity
    </span>
  )}
  <p>{problem.title}</p>
</div>

// Click on activity badge → opens modal with activity details
```

#### **Локација 3: Problem Detail Page**
**Pathname:** `/tasks/[id]`

**Функционалност:**
```html
<!-- After problem solution -->
<section class="related-activities">
  <h3>📚 Предлог Активности (од наставна програма)</h3>
  
  <div class="activity-card">
    <h4>Конструирање триаголници</h4>
    <p><strong>Траење:</strong> 20 минути</p>
    <p><strong>Материјали:</strong> лењир, шестар, транспортир</p>
    
    <details>
      <summary>Види чекори</summary>
      <ol>
        <li>Демонстрација...</li>
        <li>Индивидуална работа...</li>
      </ol>
    </details>
    
    <button>Додади во lesson plan</button>
  </div>
</section>
```

#### **Локација 4: БРО Coverage Page** (NEW!)
**Pathname:** `/teachers/curriculum` (веќе постои)

**Подобрување:**
```javascript
// Current: Само листа на БРО стандарди
// NEW: + Предлог активности за секој стандард

<div class="standard-detail">
  <h3>M.6.1.2.1</h3>
  <p>Применување својства на триаголници</p>
  
  <!-- NEW SECTION -->
  <div class="suggested-activities">
    <h4>Предлог активности (3)</h4>
    <ul>
      <li>
        <span>Конструирање триаголници</span>
        <span>20 мин</span>
        <button>Додади</button>
      </li>
      <li>...</li>
    </ul>
  </div>
  
  <div class="related-problems">
    <h4>Задачи што го покриваат овој стандард (12)</h4>
    <!-- problem cards -->
  </div>
</div>
```

### 🔧 Имплементација План

#### **Phase 1: Data Structure** (1 час)
```bash
# Create curriculum activities data file
web/src/data/curriculum_activities.ts

# Structure:
- 391 БРО standards
- Each has 2-5 suggested activities
- Link to problems (many-to-many)
```

#### **Phase 2: Lesson Planner Integration** (2 часа)
```bash
# Update lesson planner page
web/src/pages/teachers/lesson-planner.astro

# Features:
- БРО standard selector
- Show related activities
- Drag-and-drop to lesson plan
- Generate PDF with activities + problems
```

#### **Phase 3: Worksheet Builder Badge** (30 мин)
```bash
# Add activity badge to problem cards
# Click → modal with activity details
```

#### **Phase 4: БРО Coverage Enhancement** (1 час)
```bash
# Update curriculum page
# Show activities for each standard
```

### 📊 Data Source

**Каде ги земаме активностите?**

1. **Официјални Програми** (Primary source)
   - PDF-ови од Министерство
   - Извлечени во structured format
   - Manual entry (time-consuming)

2. **AI Enhancement** (Secondary)
   - AI да предложи дополнителни активности
   - Based on standard description
   - Teacher review required

3. **Community Contributions**
   - Teachers додаваат свои активности
   - Voting system (upvote/downvote)
   - Quality control

### 💡 Пример Use Case

**Scenario:** Teacher планира час за триаголници (6 одд.)

**Workflow:**
```
1. Teachers Portal → Lesson Planner
2. Select: Grade 6, Geometry, Триаголници
3. System shows:
   - БРО Standards (3 standards)
   - Suggested Activities (9 activities)
   - Available Problems (24 problems)
4. Teacher:
   - Selects 2 activities (40 мин)
   - Adds 5 problems (worksheet)
   - Generates lesson plan PDF
5. PDF contains:
   - Learning objectives
   - Activities with steps
   - Worksheet (student version)
   - Answer key (teacher version)
   - Assessment suggestions
```

---

## 🎯 Заклучок

### Priority Order (за следните 2 сесии)

**Сесија 1 (Денес, вечер - 3 часа):**
1. ✅ Problem rendering and preview - ЗАВРШЕНО
2. 🔴 PDF generation - КРИТИЧНО
3. 🟡 Save worksheet - ВАЖНО

**Сесија 2 (Утре - 3 часа):**
4. 🟢 БРО Coverage checker
5. 🟢 Drag-and-drop reordering
6. 🔵 Curriculum activities integration

**Сесија 3 (Понатаму - 4 часа):**
7. 🔵 Lesson planner enhancement
8. 🔵 Advanced search
9. 🔵 Analytics dashboard

### Quick Wins (Денес!)
- ✅ Bulk selection - ЗАВРШЕНО
- ✅ Fix Untitled Problem - ЗАВРШЕНО
- ✅ Preview rendering - ЗАВРШЕНО
- 🔴 PDF generation - NEXT!

---

**Статус:** Prepared for PDF Generation
**Следно:** Implement WeasyPrint PDF engine
**Очекувано време:** 3-4 часа
**Deployment:** Backend + Frontend update required
