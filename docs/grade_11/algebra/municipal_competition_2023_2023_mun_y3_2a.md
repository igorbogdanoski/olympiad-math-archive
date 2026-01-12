---
difficulty: 4
field: algebra
grade: 11
language_original: mk
prerequisites:
- logarithm_properties
primary_skill: algebraic_manipulation
problem_id: 2023_mun_y3_2a
problem_type: calculation
related_skills:
- logic
related_theorems:
- vieta_formulas
source: Municipal_Competition_2023
tags:
- logarithms
- exponential_equations
- substitution
- olympiad
translated: false
---

[⬅️ Назад кон Индексот](../README.md) | [🧰 Skill: algebraic_manipulation](../../skill_guides/algebraic_manipulation.md)

# Логаритамска равенка

## 📝 Текст на задачата
Одреди го производот од решенијата на равенката $\sqrt{2023} \cdot x^{\log_{2023} x} = x^2$.

## 🧠 Анализа (Клучна идеја)
Имаме непозната во експонентот. Логаритмирајте ја целата равенка со основа 2023. Внимавајте на коренот: $\log(\sqrt{A}) = \frac{1}{2}\log A$. Ова ќе ве доведе до квадратна равенка по $t = \log_{2023} x$.

## 💡 Решение

??? tip "Чекор 1: Логаритмирање"
    Логаритмираме со основа 2023:
    $$ \log_{2023}(\sqrt{2023} \cdot x^{\log_{2023} x}) = \log_{2023}(x^2) $$

??? tip "Чекор 2: Својства на логаритми"
    Лева страна:
    $$ \log_{2023}(2023^{1/2}) + \log_{2023}(x^{\log_{2023} x}) = \frac{1}{2} + (\log_{2023} x)(\log_{2023} x) $$
    Десна страна:
    $$ 2 \log_{2023} x $$
    
    Равенката е:
    $$ \frac{1}{2} + (\log_{2023} x)^2 = 2 \log_{2023} x $$

??? tip "Чекор 3: Смена"
    Нека $t = \log_{2023} x$.
    $$ \frac{1}{2} + t^2 = 2t $$
    Множиме со 2:
    $$ 1 + 2t^2 = 4t \implies 2t^2 - 4t + 1 = 0 $$

??? tip "Чекор 4: Производ на решенија"
    Бараме $P = x_1 \cdot x_2$. Знаеме дека $x = 2023^t$.
    $$ P = 2023^{t_1} \cdot 2023^{t_2} = 2023^{t_1 + t_2} $$
    Од Виетови формули за квадратната равенка: $t_1 + t_2 = -\frac{-4}{2} = 2$.
    $$ P = 2023^2 $$
    
    Одговор: Производот е $2023^2$.



## 🏁 Заклучок
Видете го решението погоре.

## 👩‍🏫 За наставници
Не мора да ги наоѓаме поединечните решенија за $t$ (кои се ирационални). Врската меѓу збирот на логаритмите и производот на броевите е клучна.