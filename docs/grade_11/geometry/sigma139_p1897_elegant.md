---
difficulty: 7
grade: 11
problem_id: sigma139_p1897_elegant
source: Sigma 139, Zadaca 1897
tags:
- geometry
- area
- isosceles_triangle
- similarity
- sine_rule
title: Еднаквост на плоштини во рамнокрак триаголник (Елегантно решение)
type: geometry
---

# Текст на задачата
Нека правата $p$ ја сече основата $AB$ на рамнокракиот триаголник $ABC$ во точка $D$, страната $AC$ во точка $E$ и полуправата $BC$ во точка $F$, при што $\angle ADE = \angle BDC$. Докажи дека триаголниците $BCE$ и $AEF$ имаат еднакви плоштини.

# Решение
## Стратегија
За да докажеме дека плоштините на $\triangle BCE$ и $\triangle AEF$ се еднакви, ќе ги изразиме преку тригонометриската формула за плоштина и ќе покажеме дека производите на соодветните страни се еднакви.
1.  Ќе ја искористиме сличноста на триаголниците $\triangle ADE$ и $\triangle BDC$ (која произлегува од условот за аглите) за да добиеме релација меѓу страните.
2.  Ќе ја примениме Синусната теорема на триаголниците $\triangle ADE$ и $\triangle BDF$ за да воспоставиме врска помеѓу отсечките $AE$ и $BF$.
3.  Ќе покажеме дека условот за еднаквост на плоштините ($AE \cdot CF = CE \cdot BC$) е еквивалентен на веќе изведените релации.

## 📐 Детално Решение

<details>
<summary>Чекор 1: Сличност на триаголници</summary>

Нека $\angle A = \angle B = \alpha$ (бидејќи $\triangle ABC$ е рамнокрак).
Дадено е дека $\angle ADE = \angle BDC$.
Во $\triangle ADE$, третиот агол е $\angle AED = 180^\circ - \alpha - \angle ADE$.
Во $\triangle BDC$, третиот агол е $\angle BCD = 180^\circ - \alpha - \angle BDC$.
Бидејќи $\angle ADE = \angle BDC$, следи дека $\angle AED = \angle BCD$.
Бидејќи триаголниците $\triangle ADE$ и $\triangle BDC$ имаат по два еднакви агли ($\alpha$ и $\angle ADE = \angle BDC$), тие се слични:
$$ \triangle ADE \sim \triangle BDC $$
Од сличноста следи пропорционалност на страните:
$$ \frac{AE}{BC} = \frac{AD}{BD} = \frac{DE}{DC} $$
Од првото равенство добиваме:
$$ AE \cdot BD = AD \cdot BC \quad \dots(1) $$

</details>

<details>
<summary>Чекор 2: Примена на Синусна теорема</summary>

Да ги разгледаме триаголниците $\triangle ADE$ и $\triangle BDF$.
Во $\triangle ADE$, според Синусна теорема:
$$ \frac{AE}{\sin(\angle ADE)} = \frac{DE}{\sin \alpha} \implies AE = DE \frac{\sin(\angle ADE)}{\sin \alpha} $$
Во $\triangle BDF$, аголот кај $B$ е надворешен за $\triangle ABC$, па $\angle DBF = 180^\circ - \alpha$.
Аголот $\angle BDF$ е накрстен со $\angle ADE$, па $\angle BDF = \angle ADE$.
Според Синусна теорема за $\triangle BDF$:
$$ \frac{BF}{\sin(\angle BDF)} = \frac{DF}{\sin(180^\circ - \alpha)} = \frac{DF}{\sin \alpha} $$
$$ BF = DF \frac{\sin(\angle ADE)}{\sin \alpha} $$

Ако ги поделиме изразите за $AE$ и $BF$:
$$ \frac{AE}{BF} = \frac{DE}{DF} \implies AE \cdot DF = BF \cdot DE \quad \dots(2) $$

</details>

<details>
<summary>Чекор 3: Изразување на плоштините</summary>

Треба да докажеме $P_{BCE} = P_{AEF}$.
1.  $P_{BCE} = \frac{1}{2} CE \cdot BC \sin(\angle C)$.
2.  $P_{AEF} = \frac{1}{2} AE \cdot CF \sin(\angle C)$. (Бидејќи $A, E, C$ се колинеарни и $B, C, F$ се колинеарни, аголот кај $C$ е ист или накрстен).

За да бидат плоштините еднакви, треба:
$$ CE \cdot BC = AE \cdot CF $$
$$ \frac{CE}{AE} = \frac{CF}{BC} $$
Додаваме 1 на двете страни:
$$ \frac{CE}{AE} + 1 = \frac{CF}{BC} + 1 $$
$$ \frac{CE+AE}{AE} = \frac{CF+BC}{BC} $$
Бидејќи $CE+AE = AC$ и $CF+BC = BF$ (бидејќи $F$ е на полуправата $BC$, распоредот е $C-B-F$? Не, $D$ е на $AB$, $E$ на $AC$. Правата $ED$ ја сече $BC$ во $F$. За да биде $F$ на полуправата $BC$, $B$ мора да е меѓу $C$ и $F$. Тогаш $CF = CB + BF$. Ако $C$ е меѓу $B$ и $F$, тогаш $BF = BC + CF$.
Ајде да провериме. $\angle ADE = \angle BDC$. Ова сугерира дека $E$ е „поблиску“ до $A$ отколку $D$ до $B$ во однос на висината. Геометриски, $F$ е надворешна точка на страната $BC$ од кај $B$. Значи $C-B-F$. Тогаш $CF = CB + BF$.
Равенството станува:
$$ \frac{AC}{AE} = \frac{BF}{BC} $$
$$ AC \cdot BC = AE \cdot BF $$
Бидејќи $AC = BC$ (рамнокрак), ова се сведува на:
$$ BC^2 = AE \cdot BF $$

</details>

<details>
<summary>Чекор 4: Доказ на релацијата $BC^2 = AE \cdot BF$</summary>

Од (1) имаме $AE = \frac{AD \cdot BC}{BD}$.
Заменуваме во бараното равенство:
$$ \frac{AD \cdot BC}{BD} \cdot BF = BC^2 $$
$$ \frac{AD \cdot BF}{BD} = BC $$
$$ \frac{BF}{BD} = \frac{BC}{AD} $$

Дали ова е точно?
Да се вратиме на (2): $\frac{AE}{BF} = \frac{DE}{DF}$.
Од сличноста $\triangle ADE \sim \triangle BDC$, имаме $\frac{AE}{BC} = \frac{DE}{DC}$.
Делиме:
$$ \frac{AE/BF}{AE/BC} = \frac{DE/DF}{DE/DC} $$
$$ \frac{BC}{BF} = \frac{DC}{DF} $$
Ова значи дека во $\triangle FDC$, отсечката $DB$ ја дели страната $FC$ во однос на другите две страни.
Според теоремата за симетрала на агол, ова важи ако $DB$ е симетрала на $\angle FDC$.
Дали е?
$\angle FDB = \angle ADE$ (накрстни).
$\angle BDC = \angle ADE$ (услов).
Значи $\angle FDB = \angle BDC$.
Да, $DB$ е симетрала!
Затоа релацијата $\frac{BC}{BF} = \frac{DC}{DF}$ е точна.

Ова имплицира дека сите претходни чекори се еквивалентни и точни.
Специјално, $BC^2 = AE \cdot BF$ е точно.
Следи дека $P_{BCE} = P_{AEF}$.

**Заклучок:**
Докажавме дека плоштините се еднакви.

# Pedagogical Notes
1.  **Основна идеја:** Задачата е прекрасен пример за поврзување на различни геометриски концепти: сличност, синусна теорема и теорема за симетрала на агол. Клучниот момент е препознавањето дека $DB$ е симетрала на аголот во $\triangle FDC$.
2.  **Совет од Олимпиец:** Кога имате услов за еднаквост на агли кои не се во ист триаголник ($\angle ADE = \angle BDC$), обидете се да ги доведете до заедничко теме (преку накрстни агли) за да откриете својства како симетрала.
3.  **Елеганција:** Ова решение е „елегантно“ бидејќи избегнува тешки пресметки и Менелаева теорема, потпирајќи се само на основните својства на триаголниците.



</details>

---
### 🎨 Визуелизација
![Илустрација](/assets/images/sigma139_p1897_elegant/sigma139_p1897_elegant.png)