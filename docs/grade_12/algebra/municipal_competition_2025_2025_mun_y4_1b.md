---
difficulty: 3
field: algebra
grade: 12
language_original: mk
prerequisites:
- basic_math
primary_skill: logic
problem_id: 2025_mun_y4_1b
problem_type: proof
related_skills:
- logic
related_theorems:
- vectors
- cauchy_schwarz_inequality
source: Municipal_Competition_2025
tags:
- geometric_progression
- algebraic_identities
- cauchy_schwarz
- olympiad
translated: false
---

[⬅️ Назад кон Индексот](../README.md) | [🧰 Skill: logic](../../skill_guides/logic.md)

# Геометриска прогресија и идентитет

## 📝 Текст на задачата
Нека $a, b, c, d$ се четири последователни членови на геометриска прогресија. Докажи дека:

$$ (a^2 + b^2 + c^2)(b^2 + c^2 + d^2) = (ab + bc + cd)^2 $$

## 🧠 Анализа (Клучна идеја)
Може да се реши со замена $b=aq, c=aq^2, d=aq^3$, но поелегантно е да се препознае **Неравенството на Коши-Шварц**. За векторите $\vec{u}=(a,b,c)$ и $\vec{v}=(b,c,d)$, равенството важи ако и само ако векторите се колинеарни, т.е. $b/a = c/b = d/c$.

## 💡 Решение

??? success "👀 Прикажи го решението"
    **Метод 1: Алгебарска замена**
    Нека $b=aq, c=aq^2, d=aq^3$.
    Лева страна:
    
    $$ L = (a^2 + a^2q^2 + a^2q^4)(a^2q^2 + a^2q^4 + a^2q^6) $$
    
    $$ L = a^2(1+q^2+q^4) \cdot a^2q^2(1+q^2+q^4) = a^4q^2(1+q^2+q^4)^2 $$
    
    Десна страна:
    
    $$ D = (a(aq) + aq(aq^2) + aq^2(aq^3))^2 $$
    
    $$ D = (a^2q + a^2q^3 + a^2q^5)^2 = [a^2q(1+q^2+q^4)]^2 = a^4q^2(1+q^2+q^4)^2 $$
    
    Важи $L=D$.
    
    **Метод 2: Лагранжов идентитет (Коши-Шварц)**
    Идентитетот гласи:
    
    $$ (a^2+b^2+c^2)(x^2+y^2+z^2) - (ax+by+cz)^2 = (ay-bx)^2 + (az-cx)^2 + (bz-cy)^2 $$
    
    Во нашиот случај $x=b, y=c, z=d$. Разликата е:
    
    $$ (ac-b^2)^2 + (ad-bc)^2 + (bd-c^2)^2 $$
    
    Бидејќи се во геометриска прогресија:
    
    *   $b^2 = ac \implies ac-b^2 = 0$
    *   $c^2 = bd \implies bd-c^2 = 0$
    *   $ad = a(aq^3) = a^2q^3$ и $bc = (aq)(aq^2) = a^2q^3 \implies ad-bc=0$
    
    Сите членови се 0, па равенството важи.

## 🏁 Заклучок
Видете го решението погоре.

## 👩‍🏫 За наставници
Вториот метод е многу побрз ако ученикот го знае условот за равенство кај Коши-Шварц (пропорционалност на компонентите).