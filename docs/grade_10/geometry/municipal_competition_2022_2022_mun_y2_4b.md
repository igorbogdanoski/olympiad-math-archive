---
grade: 10
field: geometry
difficulty: 3
problem_type: calculation
source: "Municipal_Competition_2022"
problem_id: 2022_mun_y2_4b
language_original: <mk | en | sr | hr | ...>
translated: false

# --- GEOMETRY SKILLS ---
geometry_style: synthetic
primary_skill: angle_chasing
related_skills:
  - logic
prerequisites:
  - incenter_properties

# --- VISUALIZATION ---
visual_prompt: "Draw triangle PQR with angle Q = 120 degrees (obtuse). Draw angle bisectors from P and R intersecting at S inside the triangle. Mark angle PSR with a question mark."

tags:
  - geometry
  - olympiad
  - triangle
  - angle_bisector
---

[⬅️ Назад кон Индексот](../../README.md) | [🧰 Skill: angle_chasing](../../../tools/skill_guides/angle_chasing.md)

# Агли со симетрали

## 📝 Текст на задачата
Даден е $\triangle PRQ$ за кој важи $\angle PQR = 120^\circ$. Точката $S$ е пресек на симетралите на аглите $\angle P$ и $\angle R$. Колку изнесува аголот $\angle PSR$?

## 📐 Скица

<div align="center">
  <img src="../../assets/images/2022_mun_y2_4b.png" alt="Визуелизација" width="500"/>
</div>
## 🧠 Анализа
**Зошто е оваа задача тешка?**
Точката $S$ е центар на впишаната кружница (пресек на симетрали). Аголот кај центарот е $\angle PSR = 90^\circ + \frac{\angle Q}{2}$.

**Конструктивен потег:**
Точката $S$ е центар на впишаната кружница (пресек на симетрали). Аголот кај центарот е $\angle PSR = 90^\circ + \frac{\angle Q}{2}$.

## 💡 Решение

??? success "👀 Прикажи го решението"
    Во $\triangle PQR$, $PS$ и $RS$ се симетрали на аглите.
    Во $\triangle PSR$, аглите се $\frac{\angle P}{2}$, $\frac{\angle R}{2}$ и $\angle S$.
    
    Збирот на агли во $\triangle PSR$:
    $$ \angle S + \frac{\angle P}{2} + \frac{\angle R}{2} = 180^\circ $$
    $$ \angle S = 180^\circ - \frac{\angle P + \angle R}{2} $$
    
    Од големиот триаголник: $\angle P + \angle R = 180^\circ - \angle Q = 180^\circ - 120^\circ = 60^\circ$.
    
    Заменуваме:
    $$ \angle S = 180^\circ - \frac{60^\circ}{2} = 180^\circ - 30^\circ = 150^\circ $$
    
    **Одговор:** $150^\circ$.

## 🏁 Заклучок
Видете го решението погоре.

## 👩‍🏫 За наставници
Формулата $90 + \alpha/2$ е многу корисна за брзина.