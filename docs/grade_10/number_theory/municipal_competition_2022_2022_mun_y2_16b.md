---
difficulty: 5
field: number_theory
grade: 10
language_original: mk
prerequisites:
- quadratic_equation
- factorization
primary_skill: vieta_formulas
problem_id: 2022_mun_y2_16b
problem_type: calculation
related_skills:
- logic
related_theorems:
- vieta_formulas
source: Municipal_Competition_2022
tags:
- quadratic_equation
- primes
- integers
- olympiad
translated: false
---

[⬅️ Назад кон Индексот](../README.md) | [🧰 Skill: vieta_formulas](../../skill_guides/vieta_formulas.md)

# Параметар во квадратна равенка

## 📝 Текст на задачата
Квадратната равенка $x^2 - (10+m)x + 10m + 1 = 0$, каде што $m$ е цел број, има целобројни решенија $p$ и $q$, и притоа $p$ е прост број. Пресметај ја вредноста на параметарот $m$.

## 🧠 Анализа (Клучна идеја)
Користи Виетови формули. Изрази го $m$ преку $p$ и $q$ од првата равенка и замени го во втората. Ќе добиеш равенка од типот $(p-10)(q-10)=1$.

## 💡 Решение

??? success "👀 Прикажи го решението"
    Нека $p, q$ се целобројните решенија.
    Според Виетовите формули:
    1. $p + q = 10 + m$
    2. $p \cdot q = 10m + 1$
    
    Од (1) имаме $m = p + q - 10$. Заменуваме во (2):
    $$ pq = 10(p + q - 10) + 1 $$
    $$ pq = 10p + 10q - 100 + 1 $$
    $$ pq - 10p - 10q + 99 = 0 $$
    
    Додаваме 1 на двете страни за да факторизираме (Simon's Favorite Factoring Trick):
    $$ pq - 10p - 10q + 100 = 1 $$
    $$ p(q - 10) - 10(q - 10) = 1 $$
    $$ (p - 10)(q - 10) = 1 $$
    
    Бидејќи $p, q$ се цели броеви, множителите можат да бидат само $(1, 1)$ или $(-1, -1)$.
    
    **Случај 1:**
    $p - 10 = 1 \implies p = 11$
    $q - 10 = 1 \implies q = 11$
    Бројот $p=11$ е прост број. Ова решение е валидно.
    Тогаш $m = p + q - 10 = 11 + 11 - 10 = 12$.
    
    **Случај 2:**
    $p - 10 = -1 \implies p = 9$
    $q - 10 = -1 \implies q = 9$
    Бројот $p=9$ не е прост број. Ова решение отпаѓа.
    
    **Одговор:** $m = 12$.

## 🏁 Заклучок
Видете го решението погоре.

## 👩‍🏫 За наставници
Техниката на факторизација $(x-a)(y-b)=k$ е стандардна за вакви задачи.