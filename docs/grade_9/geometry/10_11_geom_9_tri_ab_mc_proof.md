---
grade: 9
field: geometry
difficulty: 8
source: "<натпревар / списание / година>"
problem_id: geom_9_tri_ab_mc_proof
language_original: <mk | en | sr | hr | ...>
translated: false

# 
tags:
  - vectors
  - angle_chasing
  - geometry
  - complex_numbers
  - algebra
  - triangle_geometry
  - similarity
related_skills:
  - vectors
  - angle_chasing
  - complex_numbers
  - triangle_geometry
  - similarity--- GEOMETRY SKILLS ---
geometry_style: synthetic # synthetic | analytic | mixed
primary_skill: <main_tool> # e.g., angle_chasing, similarity, cyclic_quads
related_skills:
  - isosceles_triangles
  - angle_chasing

allowed_tools:
  - classical_euclidean
  - similarity
  - symmetry
forbidden_tools:
  - coordinate_geometry
  - vectors
  - complex_numbers
tags:
  - geometry
  - olympiad
---

# Еднаквост на отсечки преку центар на кружница

## Текст на задачата
Во внатрешноста на $\triangle ABC$ со агли $\angle BAC=70^\circ$ и $\angle ABC=80^\circ$ земена е точка $M$. Ако $\angle ACM=10^\circ$ и $\angle CBM=20^\circ$, докажи дека $AB=MC$.

## 📐 Скица / Конструкција

![Визуелизација](../../assets/images/geom_9_tri_ab_mc_proof.png)


![Визуелизација](../../assets/images/geom_9_tri_ab_mc_proof.png){ width=500 }
## 🧠 Анализа
Пресметај го аголот $\angle MCB$ и воочи дека $\triangle MBC$ е рамнокрак. Потоа конструирај го центарот на опишаната кружница $O$ и покажи дека $O \equiv M$.

## 📝 Решение (СИНТЕТИЧКО)
1. **Агли:** $\angle ACB = 180 - (70+80) = 30^\circ$. $\angle MCB = 30 - 10 = 20^\circ$. Бидејќи $\angle MBC = \angle MCB = 20^\circ$, триаголникот $\triangle MBC$ е рамнокрак и $MB=MC$.
2. **Конструкција:** Нека $O$ е центар на опишаната кружница околу $\triangle ABC$. Централниот агол $\angle AOB = 2\angle ACB = 60^\circ$. Бидејќи $OA=OB$ и $\angle AOB=60^\circ$, $\triangle AOB$ е рамностран, па $AB=OB$.
3. **Позиција на O:** Централниот агол $\angle BOC = 2\angle BAC = 140^\circ$. Аглите при основата на рамнокракиот $\triangle BOC$ се по $(180-140)/2 = 20^\circ$.
4. **Идентификација:** Бидејќи полуправите од $B$ и $C$ под агол од $20^\circ$ се сечат во единствена точка, $M \equiv O$. 
5. **Заклучок:** $AB = OB$ и $MC = MB = OB$, па $AB = MC$.

## ⚠️ Аналитички пристап (само ако е неизбежен)
<Ако мора да се користат координати, објасни зошто синтетичкиот пат е претежок.>

## 🏁 Заклучок
Видете го решението погоре.