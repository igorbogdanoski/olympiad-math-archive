---
difficulty: 5
field: number_theory
grade: 12
language_original: mk
prerequisites:
- square_roots
primary_skill: number_properties
problem_id: 2022_mun_y4_8b
problem_type: calculation
related_skills:
- logic
related_theorems:
- parity
source: Municipal_Competition_2022
tags:
- radicals
- integers
- olympiad
translated: false
---

[⬅️ Назад кон Индексот](../README.md) | [🧰 Skill: number_properties](../../skill_guides/number_properties.md)

# Вгнездени корени

## 📝 Текст на задачата
Познато е дека постои само еден четирицифрен број $n$ за кој $\sqrt{3\sqrt{2\sqrt{n}}}$ е природен број. Колку изнесува збирот на цифрите на $n$?

## 🧠 Анализа (Клучна идеја)
Квадрирај го изразот последователно за да се ослободиш од корените. Ќе добиеш услов за $n$ да биде од облик $2^a 3^b$.

## 💡 Решение

??? success "👀 Прикажи го решението"
    Нека $K = \sqrt{3\sqrt{2\sqrt{n}}} = k \in \mathbb{N}$.
    
    1. **Квадрирање 1:**
       $k^2 = 3\sqrt{2\sqrt{n}}$.
       За десната страна да е цел број, $k^2$ мора да е делив со 3. Нека $k^2 = 3A$.
       $3A = 3\sqrt{2\sqrt{n}} \implies A = \sqrt{2\sqrt{n}}$.
    
    2. **Квадрирање 2:**
       $A^2 = 2\sqrt{n}$.
       $A^2$ мора да е парен. Нека $A^2 = 2B$.
       $2B = 2\sqrt{n} \implies B = \sqrt{n}$.
    
    3. **Квадрирање 3:**
       $B^2 = n$.
    
    Да ги поврземе:
    $n = B^2$.
    $A^2 = 2B \implies B = A^2/2$. За $B$ да е цел, $A$ мора да е парен ($A=2m$).
    $B = (2m)^2/2 = 2m^2$.
    $n = (2m^2)^2 = 4m^4$.
    
    Враќаме назад во $K$:
    $K^2 = 3A = 3(2m) = 6m$.
    За $K^2$ да биде квадрат, $6m$ мора да биде квадрат.
    Значи $m$ мора да биде од облик $6 \cdot u^2$.
    
    Заменуваме во $n$:
    $n = 4m^4 = 4(6u^2)^4 = 4 \cdot 6^4 \cdot u^8 = 4 \cdot 1296 \cdot u^8 = 5184 \cdot u^8$.
    
    Бараме четирицифрен број $n$ ($1000 \le n \le 9999$).
    - За $u=1$: $n = 5184 \cdot 1 = 5184$. (Четирицифрен!)
    - За $u=2$: $n = 5184 \cdot 2^8 = 5184 \cdot 256$ (Преголем).
    
    Единствен број е $n = 5184$.
    Збир на цифри: $5+1+8+4 = 18$.
    
    **Одговор:** 18.

## 🏁 Заклучок
Видете го решението погоре.

## 👩‍🏫 За наставници
Систематското ослободување од корени и анализата на 'квадратна форма' е клучот.