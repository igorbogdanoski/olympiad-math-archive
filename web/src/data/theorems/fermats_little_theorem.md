---
title: Fermat's Little Theorem (Мала Теорема на Ферма)
category: Number Theory
difficulty: Intermediate
primary_skill: modular_arithmetic
related_skills:
  - eulers_theorem
  - primality_testing

tags:
  - number_theory
  - gcd_lcm
  - proof
  - logic
  - integers
  - prime_numbers
  - modular_arithmetic
---


# 📜 Fermat's Little Theorem (Мала Теорема на Ферма)

## 💡 Дефиниција
Ако $p$ е **прост број**, тогаш за секој цел број $a$:

$$ a^p \equiv a \pmod p $$

Ако $a$ не е делив со $p$ (т.е. $\gcd(a, p) = 1$), тогаш можеме да поделиме со $a$:

$$ a^{p-1} \equiv 1 \pmod p $$

---

## 🧠 Интуиција
Ова е специјален случај на Ојлеровата теорема.
За прост број $p$, сите броеви од $1$ до $p-1$ се заемно прости со $p$.
Значи $\phi(p) = p-1$.
Заменуваме во Ојлер: $a^{\phi(p)} \equiv 1 \implies a^{p-1} \equiv 1$.

---

## 📝 Доказ (Со ѓердани - Комбинаторен)
Замислете дека правиме ѓердани со $p$ монистри, користејќи $a$ различни бои.
Вкупниот број на можни низи е $a^p$.
Има $a$ еднобојни ѓердани (сите монистри иста боја).
Останатите $a^p - a$ низи се разнобојни.
Бидејќи $p$ е прост број, ако ротираме разнобоен ѓердан, добиваме $p$ различни изгледи кои всушност се ист ѓердан.
Значи, бројот на разнобојни низи мора да се дели со $p$.
$$ a^p - a \equiv 0 \pmod p \implies a^p \equiv a \pmod p $$

---

## 🛠 Каде се користи?
1.  **Тестирање за простост:** Ако $2^{n-1} \not\equiv 1 \pmod n$, тогаш $n$ сигурно НЕ е прост (Fermat Primality Test).
2.  **Делење во модуларна аритметика:** За да поделиме со $a$ модуло $p$, множиме со $a^{p-2}$.
    $x \cdot a \equiv b \implies x \equiv b \cdot a^{p-2} \pmod p$.
3.  **Пресметка на остатоци:** $2^{100} \pmod{13}$.
    $p=13 \implies 2^{12} \equiv 1$.
    $100 = 8 \cdot 12 + 4$.
    $2^{100} = (2^{12})^8 \cdot 2^4 \equiv 1^8 \cdot 16 \equiv 3 \pmod{13}$.
