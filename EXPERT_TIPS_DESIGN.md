# Expert Tips Knowledge Base - Design Document

## 🎯 Vision

Централизирана база на знаење со **900+ expert tips** за решавање математички проблеми, организирани по:
- **БРО стандарди** (395 стандарди)
- **Тема** (Геометрија, Алгебра, Комбинаторика, Теорија на броеви)
- **Тежина** (Easy, Medium, Hard, Olympic)
- **Техника** (Proof strategies, Problem-solving patterns)

## 📊 Structure

### Categories (6 main)

1. **Geometry Tips** (200 tips)
   - Triangle properties (Pythagorean, similar triangles, altitudes)
   - Circle theorems (tangents, chords, inscribed angles)
   - Construction techniques (angle bisectors, perpendiculars)
   - Proof strategies (synthetic vs analytic)

2. **Algebra Tips** (180 tips)
   - Equation solving (linear, quadratic, systems)
   - Inequalities (AM-GM, Cauchy-Schwarz, rearrangement)
   - Functions (linear, quadratic, exponential)
   - Polynomial tricks (Vieta's formulas, factoring)

3. **Number Theory Tips** (120 tips)
   - Divisibility rules
   - Modular arithmetic
   - Diophantine equations
   - Prime number properties

4. **Combinatorics Tips** (100 tips)
   - Counting techniques (permutations, combinations)
   - Pigeonhole principle
   - Graph theory basics
   - Recursion patterns

5. **Problem-Solving Meta-Strategies** (200 tips)
   - Work backwards
   - Draw diagrams
   - Check extreme cases
   - Look for patterns
   - Simplify the problem

6. **БРО-Specific Tips** (100 tips)
   - Grade-level appropriate language
   - Macedonian mathematical terminology
   - Common student mistakes per topic
   - Assessment rubric insights

## 🗂️ Data Schema

```json
{
  "tip_id": "geo_triangle_001",
  "category": "geometry",
  "subcategory": "triangles",
  "title": "Питагорова теорема - Препознавање",
  "title_en": "Pythagorean Theorem - Recognition",
  "content_mk": "Кога видиш правоаголен триаголник, СЕКОГАШ проверете дали а² + б² = ц²...",
  "content_en": "When you see a right triangle, ALWAYS check if a² + b² = c²...",
  "grade_range": [7, 9],
  "difficulty": "easy",
  "bro_standards": ["МАТ.7.Г.3", "МАТ.8.Г.2"],
  "related_theorems": ["pythagorean_theorem", "right_triangle_properties"],
  "tags": ["pythagorean", "right-triangle", "geometry-basics"],
  "example_problems": ["2022_mun_g7_4", "sigma_137_y2_p1"],
  "visual_aid": "images/tips/pythagorean_visual.png",
  "common_mistakes": [
    "Заборавање дека теоремата важи САМО за правоаголни триаголници",
    "Мешање на катети и хипотенуза"
  ],
  "pro_tip": "Ако а, б, ц се природни броеви кои задоволуваат а² + б² = ц², тогаш (а, б, ц) е Питагорова тројка.",
  "created_at": "2026-01-20",
  "author": "expert_001"
}
```

## 🎨 UI Components

### 1. Tips Display Card (Problem Page)

```
┌─────────────────────────────────────────┐
│ 💡 Expert Tip: Питагорова теорема       │
│                                         │
│ Кога видиш правоаголен триаголник,      │
│ СЕКОГАШ провери а² + б² = ц²            │
│                                         │
│ 🎯 Применливо на овој проблем затоа што:│
│    - Има правоаголен триаголник         │
│    - Дадени се две страни               │
│                                         │
│ [📚 Повеќе информации] [❌ Затвори]      │
└─────────────────────────────────────────┘
```

### 2. Tips Browser (Dedicated Page)

```
/teachers/expert-tips

Filters:
- Category: [Geometry ▼]
- Grade: [7-9 ▼]
- Difficulty: [All ▼]
- Search: [__________________🔍]

Results (45 tips):

[Card 1]
💡 Питагорова теорема
Кога видиш правоаголен триаголник...
📊 7-9 одд. | 🎯 Easy | 📚 МАТ.7.Г.3

[Card 2]
💡 Сумата агли во триаголник
Секогаш α + β + γ = 180°...
📊 6-8 одд. | 🎯 Easy | 📚 МАТ.6.Г.1
```

### 3. Smart Suggestions (AI-Powered)

When student opens a problem, AI analyzes:
- Problem text → Extract topics
- БРО standard → Match tips
- Student history → Personalize

Display 2-3 most relevant tips automatically.

## 🔧 Implementation Plan

### Phase 1: Database Creation (Day 1-2)

1. **Create JSON structure**
   ```
   tools/expert_tips/
   ├── geometry.json (200 tips)
   ├── algebra.json (180 tips)
   ├── number_theory.json (120 tips)
   ├── combinatorics.json (100 tips)
   ├── meta_strategies.json (200 tips)
   └── bro_specific.json (100 tips)
   ```

2. **Seed initial tips** (100 tips per category)
   - Focus on most common БРО standards
   - Cover grades 6-9 first (80% of users)
   - Bilingual (Macedonian primary, English secondary)

### Phase 2: UI Components (Day 2-3)

1. **ExpertTipCard.svelte**
   - Props: tip (object), relevance (score)
   - Display: title, content, visual aid, related problems
   - Actions: "Helpful" / "Not helpful" feedback

2. **ExpertTipsBrowser.astro**
   - Page: `/teachers/expert-tips`
   - Filters: category, grade, difficulty, БРО standard
   - Search: Full-text search across titles and content

3. **Smart Suggestions Component**
   - Analyze problem text (keywords, БРО standard)
   - Match top 3 tips from database
   - Display on problem page sidebar

### Phase 3: AI Integration (Day 3)

1. **Keyword Extraction**
   ```python
   def extract_topics(problem_text):
       keywords = {
           'триаголник': ['geometry', 'triangles'],
           'кружница': ['geometry', 'circles'],
           'функција': ['algebra', 'functions'],
           # ... 100+ keywords
       }
       return matched_topics
   ```

2. **Tip Ranking Algorithm**
   ```python
   def rank_tips(problem, tips):
       scores = []
       for tip in tips:
           score = 0
           score += bro_match(problem.bro_standard, tip.bro_standards) * 3
           score += topic_overlap(problem.topics, tip.tags) * 2
           score += grade_proximity(problem.grade, tip.grade_range)
           scores.append((tip, score))
       return sorted(scores, reverse=True)[:3]
   ```

3. **Feedback Loop**
   - Track which tips students mark as "Helpful"
   - Use for future ranking improvements

## 📈 Success Metrics

1. **Coverage**: 900 tips covering all БРО standards
2. **Relevance**: 80%+ of suggested tips marked "Helpful"
3. **Engagement**: 60%+ of students interact with tips
4. **Impact**: Students who use tips have 15%+ higher success rate

## 🚀 Rollout Plan

1. **Week 1**: Create 100 high-priority tips (most common topics)
2. **Week 2**: Build UI components and integrate into problem pages
3. **Week 3**: Teacher feedback → refine tip content
4. **Week 4**: Expand to 500 tips
5. **Month 2**: Reach 900 tips, full БРO coverage

## 🎓 Sample Tips (Preview)

### Geometry Tip #1
**Title**: Питагорова теорема - Препознавање  
**Grade**: 7-9  
**Content**: Кога видиш правоаголен триаголник, СЕКОГАШ проверете дали а² + б² = ц². Ова е најчестиот начин да се најде непозната страна.

**Visual Aid**: [Right triangle diagram with a, b, c labeled]

**Common Mistake**: Заборавање дека теоремата важи САМО за правоаголни триаголници.

**Pro Tip**: Ако а, б, ц се природни броеви кои задоволуваат а² + б² = ц², тогаш (а, б, ц) е Питагорова тројка (пр. 3, 4, 5).

---

### Algebra Tip #42
**Title**: Решавање квадратни равенки - Стратегија  
**Grade**: 8-9  
**Content**: За ax² + bx + c = 0:
1. Пробај факторизација прво (побрзо)
2. Ако не, користи дискриминанта Δ = b² - 4ac
3. Корени: x = (-b ± √Δ) / 2a

**Common Mistake**: Заборавање на ± знак во формулата.

**Pro Tip**: Ако Δ < 0, нема реални решенија!

---

### Meta-Strategy Tip #150
**Title**: Цртање дијаграм - Моќна алатка  
**Grade**: 6-12  
**Content**: За 80% од проблемите, точен дијаграм те води до решението. Издвои 2 минути да нацрташ:
- Сите дадени информации
- Непознатите со посебна боја
- Релации помеѓу објектите

**Pro Tip**: Користи GeoGebra за динамични дијаграми!

## 🔒 Quality Control

1. **Expert Review**: Секој tip е прегледан од 2 професори
2. **Student Testing**: Pilot со 20 ученици пред објавување
3. **Continuous Update**: Додавај нови tips базирани на feedback
4. **Translation QA**: Македонски → Англиски → обратно (проверка)

## 💾 Storage Options

### Option 1: JSON Files (Simple, Fast)
- Pros: Easy to edit, no DB overhead, Git trackable
- Cons: No advanced querying, manual indexing
- **Recommended for MVP**

### Option 2: SQLite (Structured)
- Pros: SQL queries, relationships, ACID
- Cons: More complex, migration overhead

### Option 3: Vector DB (AI-powered)
- Pros: Semantic search, AI recommendations
- Cons: Expensive, complex setup
- **Recommended for Phase 2**

## 🎯 MVP Scope (3 Days)

**Day 1**: 
- Create JSON schema
- Seed 50 tips (geometry + algebra)
- Create ExpertTipCard component

**Day 2**:
- Create ExpertTipsBrowser page
- Implement keyword matching
- Integrate tips into 10 sample problems

**Day 3**:
- Test with teachers
- Refine content based on feedback
- Document usage guide
- Commit and deploy

## 📝 Next Steps

1. Start with Geometry tips (most visual, easiest to explain)
2. Focus on grades 7-8 (largest user base)
3. Create bilingual content from day 1
4. Build feedback loop into UI
5. Iterate based on real usage data

---

**Status**: Ready for implementation ✅  
**Estimated Effort**: 3 days full-time  
**Impact**: High - Direct student learning improvement
