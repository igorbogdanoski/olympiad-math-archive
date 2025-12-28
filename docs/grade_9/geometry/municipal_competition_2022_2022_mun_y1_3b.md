---
grade: 9
field: geometry
difficulty: 3
problem_type: calculation
source: "Municipal_Competition_2022"
problem_id: 2022_mun_y1_3b
language_original: <mk | en | sr | hr | ...>
translated: false

# --- GEOMETRY SKILLS ---
geometry_style: synthetic
primary_skill: angle_chasing
related_skills:
  - logic
prerequisites:
  - parallelogram_properties
  - parallel_lines

# --- VISUALIZATION ---
visual_prompt: "Draw a parallelogram labeled BADC (vertices in counter-clockwise order: B bottom-left, A top-left, D top-right, C bottom-right). Draw diagonal AC. Label angle at B as 40 degrees. Label angle CAD as 57 degrees. Mark angle ACD with a question mark."

tags:
  - geometry
  - olympiad
  - parallelogram
  - angles
---

[⬅️ Назад кон Индексот](../README.md) | [🧰 Skill: angle_chasing](../../skill_guides/angle_chasing.md)

# Агол во паралелограм

## 📝 Текст на задачата
Колку степени изнесува аголот означен со прашалник на сликата, ако четириаголникот $BADC$ е паралелограм? (Дадено: $\angle B = 40^\circ$, $\angle CAD = 57^\circ$, се бара $\angle ACD$).

## 📐 Скица

![Визуелизација](../../assets/images/2022_mun_y1_3b.png){ width=500 }



## 🧠 Анализа
**Зошто е оваа задача тешка?**
Внимавај на редоследот на темињата: $BADC$ е паралелограм. Тоа значи $BA \parallel CD$ и $BC \parallel AD$. Искористи го својството на соседни агли во паралелограм (збир $180^\circ$) и наизменични агли.

**Конструктивен потег:**
Внимавај на редоследот на темињата: $BADC$ е паралелограм. Тоа значи $BA \parallel CD$ и $BC \parallel AD$. Искористи го својството на соседни агли во паралелограм (збир $180^\circ$) и наизменични агли.

## 💡 Решение

??? tip "Чекор 1: Својства на паралелограм $BADC$"
    Бидејќи $BADC$ е паралелограм, соседните агли имаат збир $180^\circ$.
    Дадено е $\angle B = 40^\circ$.
    Тогаш $\angle BAD = 180^\circ - 40^\circ = 140^\circ$.

??? tip "Чекор 2: Пресметка на $\angle BAC$"
    Аголот $\angle BAD$ е составен од $\angle BAC$ и $\angle CAD$.
    $$ \angle BAD = \angle BAC + \angle CAD $$
    $$ 140^\circ = \angle BAC + 57^\circ $$
    $$ \angle BAC = 140^\circ - 57^\circ = 83^\circ $$

??? tip "Чекор 3: Наизменични агли"
    Бидејќи $AB \parallel CD$ (страни на паралелограм) и $AC$ е трансверзала, аглите $\angle BAC$ и $\angle ACD$ се наизменични и еднакви.
    $$ \angle ACD = \angle BAC $$
    $$ \angle ACD = 83^\circ $$
    
    **Одговор:** 83.



## 🏁 Заклучок
Видете го решението погоре.

## 👩‍🏫 За наставници
Најчеста грешка е погрешно читање на името на паралелограмот. $BADC$ значи дека страните се $BA, AD, DC, CB$.