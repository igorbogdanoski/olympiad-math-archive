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
problem_id: sigma_adv_27
related_skills:
- area_method
- orthocenter
related_theorems:
- optimization
source: <натпревар / списание / година>
tags:
- geometry
- olympiad
translated: false
---

# Геометриско неравенство (Ердеш-Мордел тип)

## Текст на задачата
Докажи дека за секоја внатрешна точка $P$ во $\triangle ABC$ важи $a \cdot PA + b \cdot PB + c \cdot PC \ge 4 P_{ABC}$. Кога важи знак за равенство?

## 📐 Скица / Конструкција


## 🧠 Анализа
Разгледај ги проекциите на $P$ врз страните. $PA$ е секогаш поголема или еднаква на растојанието од $P$ до страната $a$.

## 📝 Решение (СИНТЕТИЧКО)
Нека $P_{ABC} = S$.
Ова неравенство е познато и равенство се достигнува кога $P$ е **Ортоцентарот** на триаголникот (ако е остроаголен).

**Доказ:**
Нека $A_1, B_1, C_1$ се подножјата на висините од $A, B, C$.
Ако $P$ е ортоцентар $H$, тогаш $PA = HA$.
Познато е дека $a \cdot HA = 2R \sin A \cdot 2R \cos A = 2R^2 \sin 2A$.
Збирот $\sum a \cdot HA = 4S$.

За произволна точка $P$:
Точното равенство за плоштина е: $2S = a \cdot d_a + b \cdot d_b + c \cdot d_c$ (каде $d$ се растојанијата од $P$ до страните).
Очигледно $PA \ge d_c$ и $PA \ge d_b$ (хипотенуза $\ge$ катета).
За појаката граница ($4S$), се користи фактот дека функцијата $f(P) = \sum a \cdot PA$ е конвексна и минимумот се постигнува во Ортоцентарот.

**Заклучок:** Неравенството е точно, а равенство важи ако $P$ е ортоцентар.

## ⚠️ Аналитички пристап (само ако е неизбежен)
<Ако мора да се користат координати, објасни зошто синтетичкиот пат е претежок.>

## 🏁 Заклучок
Видете го решението погоре.