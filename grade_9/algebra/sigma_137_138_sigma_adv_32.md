---
grade: 9
field: algebra
difficulty: 6
source: "Sigma 137/138"
problem_id: sigma_adv_32
language_original: mk
translated: false

# 
tags:
  - geometry
  - trigonometry
related_skills:
  - trigonometry--- SKILL MAPPING (New Standard) ---
primary_skill: trigonometry # e.g., symmetry, invariants, telescoping
related_skills:
  - algebraic_substitution

# --- TOPICS ---
tags:
  - <topic_1> # e.g., percentages
  - <topic_2> # e.g., linear_equations
  - olympiad
---

# Тригонометриски идентитет

## Текст на задачата
Докажи дека ако $\frac{\cos \alpha}{\cos \beta} + \frac{\sin \alpha}{\sin \beta} = -1$, тогаш $\frac{\cos^3 \beta}{\cos \alpha} + \frac{\sin^3 \beta}{\sin \alpha} = 1$.

## 🧠 Анализа (Клучна идеја)
Сведи го условот на заеднички именител: $\sin(\alpha+\beta) = -\sin\beta \cos\beta$.

## 📝 Решение
Даден услов:
$$ \frac{\cos \alpha \sin \beta + \sin \alpha \cos \beta}{\cos \beta \sin \beta} = -1 $$
$$ \frac{\sin(\alpha+\beta)}{\sin \beta \cos \beta} = -1 $$
$$ \sin(\alpha+\beta) = -\sin \beta \cos \beta $$

Треба да пресметаме:
$$ S = \frac{\cos^3 \beta}{\cos \alpha} + \frac{\sin^3 \beta}{\sin \alpha} $$

Користиме алгебарска супституција. Нека $u = \frac{\cos \alpha}{\cos \beta}$ и $v = \frac{\sin \alpha}{\sin \beta}$.
Условот е $u + v = -1$.
Бараме вредност на $\frac{\cos^2 \beta}{u} + \frac{\sin^2 \beta}{v}$.

Од дефинициите:
$u \cos \beta = \cos \alpha \implies u^2 \cos^2 \beta = \cos^2 \alpha$
$v \sin \beta = \sin \alpha \implies v^2 \sin^2 \beta = \sin^2 \alpha$

Собираме:
$u^2 \cos^2 \beta + v^2 \sin^2 \beta = \cos^2 \alpha + \sin^2 \alpha = 1$.

Знаеме $v = -1-u$. Заменуваме:
$u^2 \cos^2 \beta + (-1-u)^2 \sin^2 \beta = 1$
$u^2 \cos^2 \beta + (1+2u+u^2) \sin^2 \beta = 1$
$u^2(\cos^2 \beta + \sin^2 \beta) + 2u \sin^2 \beta + \sin^2 \beta = 1$
$u^2 + 2u \sin^2 \beta = 1 - \sin^2 \beta = \cos^2 \beta$

Значи $\cos^2 \beta = u^2 + 2u \sin^2 \beta$.
Аналогно $\sin^2 \beta = v^2 + 2v \cos^2 \beta$.

Бараниот израз е:
$$ S = \frac{\cos^2 \beta}{u} + \frac{\sin^2 \beta}{v} $$
$$ S = \frac{u^2 + 2u \sin^2 \beta}{u} + \frac{v^2 + 2v \cos^2 \beta}{v} $$
$$ S = u + 2\sin^2 \beta + v + 2\cos^2 \beta $$
$$ S = (u+v) + 2(\sin^2 \beta + \cos^2 \beta) $$
$$ S = -1 + 2(1) = 1 $$

**Заклучок:** Докажано.
<Користи LaTeX за формули: $x^2$ или $$ x^2 $$>

## 💡 Алтернативен пристап (опционално)
<Ако постои решение со друг Skill (на пр. геометриски наместо алгебарски).>

## 🏁 Заклучок
<Краен резултат, јасно истакнат во \boxed{}.>

## 👩‍🏫 За наставници
Супституцијата $u, v$ го претвора тригонометрискиот проблем во чиста алгебра.