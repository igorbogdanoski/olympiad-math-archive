---
problem_id: <unique_id_here>
title: <Title in Macedonian>
grade: <integer>
difficulty: <1-10>
type: <logic/geometry/algebra/number_theory/combinatorics>
tags:
  - tag1
  - tag2
concepts:
  - concept1 (e.g., "Modular Arithmetic", "Angle Chasing")
  - concept2 (e.g., "Pigeonhole Principle")
theorems:
  - theorem1 (e.g., "Pythagorean Theorem")
  - theorem2 (e.g., "Ceva's Theorem")
source: <Source Name>
---

# Текст на задачата
(The problem statement in Macedonian using LaTeX)

# Решение
## Стратегија
(A high-level plan before calculating. Use keywords: "Working Backwards", "Invariants", "Extremal Principle", "Symmetry")

## Чекор по чекор
**Чекор 1: [Title of step]**
(Extremely detailed proof. Explain *every* logical jump. Do NOT skip steps.)

**Чекор 2: [Title of step]**
(Continue...)

**Заклучок:**
(State the final answer clearly and explicitly.)

# Pedagogical Notes
1. **Основна идеја:** (Deep dive into the core mathematical concept)
2. **Совет од Олимпиец:** (Practical exam strategy - how to recognize this pattern)
3. **Чести грешки:** (Common pitfalls students make)

# Manim Code
```python
from manim import *

class SolutionScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        # Complete Manim code here
        # Use BLACK for main objects, RED/BLUE for highlights
        # Position labels with next_to() and buff parameter
```
```

### 🎨 MANIM RULES (Visual Architect)
When generating Manim code:
- **Library:** Manim Community Edition
- **Background:** Always set `self.camera.background_color = WHITE`
- **Colors:** Use `BLACK` for lines/vertices. Use `RED` or `BLUE` only for highlights.
- **Labels:** Use `MathTex` (not `Tex`). Position carefully with `next_to()` and `buff` parameter.
- **Format:** Provide the **complete** Python script including all imports and class definition.
- **Completeness:** Code must be immediately runnable. No placeholders like "# add code here".
- **Avoid:** Do NOT use deprecated methods like `ShowCreation` (use `Create` instead).

### 🧠 CONTENT GUIDELINES (Macedonian Language)

#### Solution Strategy (Стратегија)
- Start with the **heuristic approach**
- Ask guiding questions: "What makes this hard?", "What constraint is hidden?"
- Mention the technique name (e.g., "Working Backwards", "Invariants", "Pigeonhole Principle")

#### Solution Content (Чекор по чекор)
- **Detail Level:** EXTREMELY DETAILED
- Explain *every* algebraic manipulation
- Justify *every* geometric construction
- **Geometry Rule:** **STRICTLY SYNTHETIC GEOMETRY** (congruence, similarity, cyclic quads)
  - **Allowed:** Euclidean theorems, angle chasing, power of a point
  - **Prohibited:** Coordinates, Complex numbers, Trigonometry (unless problem specifically requires them)
- **Theorem Protocol:** If using named theorems (Ceva, Menelaus, Ptolemy), **state them clearly** but do NOT prove them

#### Pedagogical Notes
1. **Основна идеја:** Explain the "big picture" mathematical concept
2. **Совет од Олимпиец:** Give practical competition advice
3. **Чести грешки:** List common errors students make

### 📂 CLASSIFICATION RULES
- **problem_id:** Use format `source_grade_number` (e.g., `jbmo_2020_p3`)
- **grade:** Integer 1-12
- **difficulty:** 1 (School) to 10 (IMO Gold)
- **tags:** Searchable keywords (e.g., `primes`, `cyclic_quadrilateral`)
- **concepts:** Mathematical skills used (e.g., `Modular Arithmetic`, `Difference of Squares`)
- **theorems:** Named theorems used (e.g., `Fermat's Little Theorem`, `Simson Line`)
- **type:** One of: `logic`, `geometry`, `algebra`, `number_theory`, `combinatorics`

### ✅ QUALITY CHECKLIST
Before finalizing your response, verify:
- [ ] YAML header contains `concepts` and `theorems` fields clearly separated
- [ ] Problem text is in Macedonian with proper LaTeX
- [ ] Solution has both "Стратегија" and "Чекор по чекор" sections
- [ ] Manim code is complete and runnable

### 📚 EXAMPLE OUTPUT (Follow this EXACTLY)

```markdown
---
problem_id: example_geo_001
title: Агли во рамностран триаголник
grade: 7
difficulty: 2
type: geometry
tags:
  - triangle
  - angles
  - equilateral
concepts:
  - Angle Chasing
  - Properties of Equilateral Triangles
theorems:
  - Sum of Angles in Triangle
source: Example Source
---

# Текст на задачата
Даден е рамностран триаголник $ABC$. Точката $D$ лежи на страната $BC$. Најдете го аголот $\angle ADB$ ако $\angle CAD = 20^\circ$.

# Решение
## Стратегија
Користиме својства на рамностран триаголник (сите агли се $60^\circ$) и збир на агли во триаголник.

## Чекор по чекор
**Чекор 1: Ги користиме својствата на $ABC$**
Бидејќи $\triangle ABC$ е рамностран, знаеме дека:
$$ \angle A = \angle B = \angle C = 60^\circ $$

**Чекор 2: Го наоѓаме $\angle BAD$**
Знаеме дека $\angle A = \angle BAD + \angle CAD$.
Заменуваме:
$$ 60^\circ = \angle BAD + 20^\circ $$
$$ \angle BAD = 40^\circ $$

**Чекор 3: Го наоѓаме $\angle ADB$**
Во $\triangle ABD$, збирот на аглите е $180^\circ$:
$$ \angle ADB = 180^\circ - (\angle B + \angle BAD) $$
$$ \angle ADB = 180^\circ - (60^\circ + 40^\circ) = 80^\circ $$

**Заклучок:**
Аголот е $80^\circ$.

# Pedagogical Notes
1. **Основна идеја:** Разложување на агли и користење на основни својства.
2. **Совет од Олимпиец:** Секогаш запишувајте ги познатите агли на скицата.
3. **Чести грешки:** Заборавање дека рамностран триаголник има агли од $60^\circ$.

# Manim Code
```python
from manim import *

class TriangleProblem(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # Define points
        A = UP * 2
        B = LEFT * 2 + DOWN * 1.5
        C = RIGHT * 2 + DOWN * 1.5

        # Define Triangle
        triangle = Polygon(A, B, C, color=BLACK, stroke_width=4)

        # Labels
        label_A = MathTex("A", color=BLACK).next_to(A, UP)
        label_B = MathTex("B", color=BLACK).next_to(B, DL)
        label_C = MathTex("C", color=BLACK).next_to(C, DR)

        # Animation
        self.play(Create(triangle))
        self.play(Write(label_A), Write(label_B), Write(label_C))
        self.wait(2)
```
```
