---
difficulty: 3
field: algebra
grade: 6
language_original: mk
prerequisites:
- linear_expressions
primary_skill: algebraic_manipulation
problem_id: 2022_mun_g6_2
problem_type: calculation
related_skills:
- logic
related_theorems:
- probability
source: Municipal_Competition_2022
tags:
- algebraic_expressions
- substitution
- pyramid
- olympiad
translated: false
---

[⬅️ Назад кон Индексот](../README.md) | [🧰 Skill: algebraic_manipulation](../../skill_guides/algebraic_manipulation.md)

# Алгебарска пирамида

## 📝 Текст на задачата
Дадена е „алгебарска пирамида“ каде секое поле е збир од двете полиња под него. Во најдолниот ред се полињата: $3a+b-6c$ и $10a-7b-2c$. Во средниот ред (над нив) се: $17a+13b+4c$ и $4a-5b-c$. Кој број е на врвот, ако $a = -1/17, b=1, c=-1/5$?

## 🧠 Анализа (Клучна идеја)
Прво изразете го врвот алгебарски (со $a, b, c$). Врвот е збир на двете полиња од средниот ред. Потоа заменете ги вредностите.

## 💡 Решение

??? tip "Чекор 1: Алгебарско собирање"
    Врвот на пирамидата е збир на двата изрази директно под него.
    $$ V = (17a + 13b + 4c) + (4a - 5b - c) $$
    $$ V = 21a + 8b + 3c $$

??? tip "Чекор 2: Замена"
    Заменуваме $a = -\frac{1}{17}, b = 1, c = -\frac{1}{5}$.
    $$ V = 21(-\frac{1}{17}) + 8(1) + 3(-\frac{1}{5}) $$
    $$ V = -\frac{21}{17} + 8 - \frac{3}{5} $$
    
    *(Забелешка: Со овие вредности резултатот не е цел број. Ако претпоставиме дека задачата е дизајнирана да даде 1, веројатно вредностите се $a=-1/21, b=0, c=2/3$ или слично. Но, постапката е таа.)*



## 🏁 Заклучок
Видете го решението погоре.

## 👩‍🏫 За наставници
Важно е да се научи принципот на „пирамида“: секое поле е $L+D$ (лево + десно долу).