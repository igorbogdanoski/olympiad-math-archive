---
title: Cauchy-Schwarz Inequality (Коши-Шварц)
category: Algebra / Inequalities
difficulty: Advanced
primary_skill: inequalities_cs
related_skills:
  - vectors
  - optimization
  - am_gm_inequality

tags:
  - squares
  - proof
  - inequalities
  - equations
  - logic
  - functions
  - analysis
  - vectors
  - geometry
  - algebra
---


# 📜 Cauchy-Schwarz Inequality (Коши-Шварц)

## 💡 Дефиниција
За било кои две низи од реални броеви $a_1, \dots, a_n$ и $b_1, \dots, b_n$:
**Квадратот на скаларниот производ е помал или еднаков на производот на нормите.**

$$ (a_1^2 + a_2^2 + \dots + a_n^2)(b_1^2 + b_2^2 + \dots + b_n^2) \ge (a_1b_1 + a_2b_2 + \dots + a_nb_n)^2 $$

**Еднаквост важи** ако и само ако низите се пропорционални: $\frac{a_1}{b_1} = \frac{a_2}{b_2} = \dots = k$.

---

## 🧠 Интуиција (Векторска)
Во векторски облик, ова е:
$$ |\vec{a}|^2 \cdot |\vec{b}|^2 \ge (\vec{a} \cdot \vec{b})^2 $$
Или ако коренуваме: $|\vec{a}| |\vec{b}| \ge |\vec{a} \cdot \vec{b}|$.
Бидејќи $\vec{a} \cdot \vec{b} = |\vec{a}| |\vec{b}| \cos \theta$, неравенството е еквивалентно на $|\cos \theta| \le 1$, што е очигледно точно.
Максимумот се достигнува кога векторите се колинеарни ($\cos \theta = 1$).

---

## 📝 Доказ (Квадратна функција)
Да ја разгледаме функцијата $f(x) = \sum_{i=1}^n (a_i x - b_i)^2$.
Ова е збир на квадрати, па мора да е $f(x) \ge 0$ за секое $x$.
Ако го развиеме:
$$ f(x) = (\sum a_i^2)x^2 - 2(\sum a_i b_i)x + (\sum b_i^2) $$
Ова е квадратна равенка $Ax^2 + Bx + C \ge 0$.
За да биде секогаш ненегативна, нејзината дискриминанта мора да е $\le 0$.
$$ D = B^2 - 4AC \le 0 $$
$$ (2\sum a_i b_i)^2 - 4(\sum a_i^2)(\sum b_i^2) \le 0 $$
$$ 4(\sum a_i b_i)^2 \le 4(\sum a_i^2)(\sum b_i^2) $$
Ако поделиме со 4, го добиваме неравенството.

---

## 🛠 Каде се користи?
1.  **Титанова Лема (Titu's Lemma):** Специјална форма на CS, многу корисна за дропки.
    $$ \frac{x_1^2}{a_1} + \dots + \frac{x_n^2}{a_n} \ge \frac{(x_1+\dots+x_n)^2}{a_1+\dots+a_n} $$
2.  **Докажување неравенства:** Кога имате збир на квадрати или корени.
3.  **Максимизација/Минимизација:** Наоѓање екстреми без изводи.
