---
allowed_tools:
- classical_euclidean
- similarity
- symmetry
difficulty: 7
field: geometry
forbidden_tools:
- coordinate_geometry
- vectors
- complex_numbers
geometry_style: synthetic
grade: 9
language_original: <mk | en | sr | hr | ...>
primary_skill: <main_tool>
problem_id: num_li2_12
related_skills:
- reflection_principle
related_theorems:
- symmetry
source: <натпревар / списание / година>
tags:
- geometry
- olympiad
translated: false
---

# Ортоцентри и кружници

## Текст на задачата
Ако $S$ и $T$ се ортоцентри на $\triangle ABD$ и $\triangle BCD$ во тетивен четириаголник со радиус $R$, докажи дека $BTDS$ е тетивен со радиус $R$.

## 📐 Скица / Конструкција


## 🧠 Анализа
Користи ја лемата: Кружницата опишана околу $\triangle ABH$ (каде $H$ е ортоцентар) е симетрична на кружницата околу $\triangle ABC$ во однос на страната $AB$.

## 📝 Решение (СИНТЕТИЧКО)
1. **Лема:** Радиусот на кружницата околу триаголникот формиран од две темиња и ортоцентарот е еднаков на радиусот на опишаната кружница ($R$).
2. **Примена:**
   - За $\triangle ABD$: Кружницата околу $\triangle SBD$ има радиус $R$.
   - За $\triangle BCD$: Кружницата околу $\triangle TBD$ има радиус $R$.
3. **Симетрија:**
   Двете кружници се добиваат со рефлексија на оригиналната кружница преку тетивата $BD$. Значи тие се поклопуваат.
   Точките $S, T, B, D$ лежат на иста кружница со радиус $R$.

**Резултат:** $BTDS$ е тетивен.

## ⚠️ Аналитички пристап (само ако е неизбежен)
<Ако мора да се користат координати, објасни зошто синтетичкиот пат е претежок.>

## 🏁 Заклучок
Видете го решението погоре.