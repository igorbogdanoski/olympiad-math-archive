---
difficulty: 6
grade: 10
primary_skill: sine_theorem
problem_id: sigma_137_school_4
related_skills:
- angle_sum
- trigonometric_identities
related_theorems:
- geometry_construction
- trigonometric_identities
- functions
source: Сигма 137, Задачи од училницата (Втора година)
tags:
- trigonometry
- sine_theorem
- special_angles
- synthetic_geometry
title: Пресметка на агли во триаголник со продолжена страна
type: geometry
---

# Пресметка на агли во триаголник со продолжена страна

# Текст на задачата
Во $\triangle ABC$, $\angle ABC = 45^\circ$ и $\angle CAB = 15^\circ$. Нека $M$ е точка на полуправата $BC$, таква што $\overline{BM} = 3 \cdot \overline{BC}$. Одреди ги аглите на $\triangle ABM$.

*(Забелешка: Точката $M$ е на полуправата $BC$. Бидејќи $BM = 3BC$, редоследот на точките е $B - C - M$.)*

# 💡 Помош (Hints)
<details>
<summary>Кликни за мала помош</summary>

1. Прво, пресметај го третиот агол во $\triangle ABC$.
   $$ \angle ACB = 180^\circ - (45^\circ + 15^\circ) = 120^\circ $$

2. Искористи ја Синусната теорема за $\triangle ABC$ за да најдеш врска помеѓу страната $BC$ и страната $AB$ (или $AC$).
   $$ \frac{BC}{\sin 15^\circ} = \frac{AC}{\sin 45^\circ} = \frac{AB}{\sin 120^\circ} $$

3. Во $\triangle ABM$, знаеш две страни ($AB$ и $BM=3BC$) и аголот меѓу нив ($\angle ABM = 45^\circ$). Ова е класичен случај за Синусна теорема или Косинусна теорема. Обиди се да го најдеш $\tan(\angle BAM)$ или директно $\sin(\angle BAM)$.

</details>

# Решение
## 🧠 Експертска Анализа (Интуиција)
Имаме триаголник со специфични агли ($45^\circ, 15^\circ, 120^\circ$). Ова веднаш сугерира дека страните имаат "убави" односи кои вклучуваат $\sqrt{3}, \sqrt{2}$ итн.
Точката $M$ е на продолжението на $BC$ така што $BM$ е три пати поголема од $BC$.
Знаеме:
1.  Аголот кај $B$ е заеднички за $\triangle ABC$ и $\triangle ABM$ ($45^\circ$).
2.  Страната $BM$ е експлицитно дадена преку $BC$.
3.  Страната $AB$ е заедничка.

Стратегијата е јасна:
1.  Преку Синусна теорема во $\triangle ABC$ ќе го изразиме односот $AB/BC$.
2.  Во $\triangle ABM$ ќе ги знаеме односот $AB/BM$ и аголот $B$.
3.  Ќе ја искористиме Синусната теорема во $\triangle ABM$ за да го најдеме аголот $\angle AMB$ (или $\angle BAM$).

## 📐 Детално Решение

<details>
<summary>Чекор 1: Анализа на $\triangle ABC$</summary>

Аглите во $\triangle ABC$ се:
$$ \angle A = 15^\circ, \quad \angle B = 45^\circ $$
$$ \angle C = 180^\circ - (15^\circ + 45^\circ) = 120^\circ $$

Применуваме Синусна теорема за да го најдеме односот на страните $c = AB$ и $a = BC$:
$$ \frac{AB}{\sin 120^\circ} = \frac{BC}{\sin 15^\circ} $$
$$ AB = BC \cdot \frac{\sin 120^\circ}{\sin 15^\circ} $$

Знаеме дека:
$$ \sin 120^\circ = \sin(180^\circ - 60^\circ) = \sin 60^\circ = \frac{\sqrt{3}}{2} $$
$$ \sin 15^\circ = \sin(45^\circ - 30^\circ) = \sin 45^\circ \cos 30^\circ - \cos 45^\circ \sin 30^\circ $$
$$ \sin 15^\circ = \frac{\sqrt{2}}{2} \cdot \frac{\sqrt{3}}{2} - \frac{\sqrt{2}}{2} \cdot \frac{1}{2} = \frac{\sqrt{6} - \sqrt{2}}{4} $$

Заменуваме во изразот за $AB$:
$$ AB = BC \cdot \frac{\frac{\sqrt{3}}{2}}{\frac{\sqrt{6} - \sqrt{2}}{4}} = BC \cdot \frac{2\sqrt{3}}{\sqrt{6} - \sqrt{2}} $$
Рационализираме:
$$ AB = BC \cdot \frac{2\sqrt{3}(\sqrt{6} + \sqrt{2})}{6 - 2} = BC \cdot \frac{2(\sqrt{18} + \sqrt{6})}{4} = BC \cdot \frac{3\sqrt{2} + \sqrt{6}}{2} $$
Ова изгледа комплицирано. Да пробаме поелегантно.
Забележуваме дека $\sin 120^\circ = \sin(2 \cdot 60^\circ)$? Не.
Ајде да го оставиме односот како што е:
$$ \frac{AB}{BC} = \frac{\sin 120^\circ}{\sin 15^\circ} $$
</details>

<details>
<summary>Чекор 2: Анализа на $\triangle ABM$</summary>

Во $\triangle ABM$ имаме:
*   Страна $c' = AB$
*   Страна $a' = BM = 3 \cdot BC$
*   Агол $\beta = 45^\circ$

Сакаме да го најдеме аголот $\angle M = \angle AMB$. Нека го означиме со $\delta$.
Според Синусна теорема за $\triangle ABM$:
$$ \frac{AB}{\sin \delta} = \frac{BM}{\sin \angle BAM} $$
Ова воведува две непознати. Подобро е да го искористиме односот $AB/BM$:
$$ \frac{AB}{\sin \delta} = \frac{BM}{\sin \angle BAM} $$
Но, знаеме дека $\angle BAM = 180^\circ - (45^\circ + \delta)$.
Уште подобро, да ја искористиме врската со $BC$:
$$ \frac{AB}{\sin \delta} = \frac{3BC}{\sin(135^\circ - \delta)} $$
Од Чекор 1 знаеме $AB = BC \frac{\sin 120^\circ}{\sin 15^\circ}$. Заменуваме:
$$ \frac{BC \frac{\sin 120^\circ}{\sin 15^\circ}}{\sin \delta} = \frac{3BC}{\sin(135^\circ - \delta)} $$
Кратиме со $BC$:
$$ \frac{\sin 120^\circ}{\sin 15^\circ \sin \delta} = \frac{3}{\sin(135^\circ - \delta)} $$
$$ \sin(135^\circ - \delta) \cdot \sin 120^\circ = 3 \sin 15^\circ \sin \delta $$

Ова е тригонометриска равенка. Да ја решиме.
Знаеме $\sin 120^\circ = \frac{\sqrt{3}}{2}$.
Знаеме $3 \sin 15^\circ = 3 \frac{\sqrt{6}-\sqrt{2}}{4}$.
$$ \sin(135^\circ - \delta) \frac{\sqrt{3}}{2} = 3 \sin 15^\circ \sin \delta $$
Развиваме $\sin(135^\circ - \delta) = \sin 135^\circ \cos \delta - \cos 135^\circ \sin \delta$.
$\sin 135^\circ = \frac{\sqrt{2}}{2}, \cos 135^\circ = -\frac{\sqrt{2}}{2}$.
$$ (\frac{\sqrt{2}}{2} \cos \delta + \frac{\sqrt{2}}{2} \sin \delta) \frac{\sqrt{3}}{2} = 3 \sin 15^\circ \sin \delta $$
Делиме со $\cos \delta$ (претпоставувајќи $\delta \neq 90^\circ$) за да добиеме $\tan \delta$:
$$ \frac{\sqrt{6}}{4} (1 + \tan \delta) = 3 \sin 15^\circ \tan \delta $$
$$ \frac{\sqrt{6}}{4} + \frac{\sqrt{6}}{4} \tan \delta = 3 \frac{\sqrt{6}-\sqrt{2}}{4} \tan \delta $$
Множиме со 4:
$$ \sqrt{6} + \sqrt{6} \tan \delta = (3\sqrt{6} - 3\sqrt{2}) \tan \delta $$
$$ \sqrt{6} = \tan \delta (3\sqrt{6} - 3\sqrt{2} - \sqrt{6}) $$
$$ \sqrt{6} = \tan \delta (2\sqrt{6} - 3\sqrt{2}) $$
$$ \tan \delta = \frac{\sqrt{6}}{2\sqrt{6} - 3\sqrt{2}} $$
Делиме со $\sqrt{2}$ горе и долу:
$$ \tan \delta = \frac{\sqrt{3}}{2\sqrt{3} - 3} $$
Рационализираме:
$$ \tan \delta = \frac{\sqrt{3}(2\sqrt{3} + 3)}{(2\sqrt{3}-3)(2\sqrt{3}+3)} = \frac{2(3) + 3\sqrt{3}}{12 - 9} = \frac{6 + 3\sqrt{3}}{3} = 2 + \sqrt{3} $$

Знаеме дека $\tan 75^\circ = \tan(45^\circ+30^\circ) = \frac{1 + 1/\sqrt{3}}{1 - 1/\sqrt{3}} = \frac{\sqrt{3}+1}{\sqrt{3}-1} = 2+\sqrt{3}$.
Значи $\delta = 75^\circ$.
</details>

<details>
<summary>Чекор 3: Пресметка на останатите агли</summary>

Најдовме дека $\angle AMB = 75^\circ$.
Аголот $\angle ABM = 45^\circ$ (даден).
Третиот агол е $\angle BAM$:
$$ \angle BAM = 180^\circ - (45^\circ + 75^\circ) = 180^\circ - 120^\circ = 60^\circ $$
</details>

**Краен одговор:** Аглите на $\triangle ABM$ се $\boxed{45^\circ, 75^\circ, 60^\circ}$.



---
### 🎨 Визуелизација
![Илустрација](/assets/images/sigma_137_school_4/sigma_137_school_4.png)

## 👨‍🏫 Менторски Белешки
1.  **Златен Совет:** Препознавањето на вредностите на тангенс е моќна алатка.
    *   $\tan 15^\circ = 2 - \sqrt{3}$
    *   $\tan 75^\circ = 2 + \sqrt{3}$
    Ако во текот на решавањето добиете ваков израз, веднаш знаете за кој агол се работи.
2.  **Алтернативен пристап (Синтетички):**
    Можеме да конструираме рамностран триаголник над $AB$ или да повлечеме висина.
    На пример, нека $h$ е висината од $A$ кон $BC$.
    Во $\triangle ABC$, $\angle C = 120^\circ$, што значи $C$ е тап агол. Висината паѓа на продолжението на $CB$.
    Оваа геометриска конструкција може да биде потешка за визуелизација од тригонометрискиот пристап, но е многу елегантна ако се погоди.
3.  **Проверка:**
    Ако $\angle BAM = 60^\circ$, тогаш $\angle CAM = 60^\circ - 15^\circ = 45^\circ$.
    Во $\triangle AMC$, аглите се $120^\circ$ (надворешен на $C$ е $60^\circ$, значи внатрешен е $120^\circ$? Не, $\angle ACB=120^\circ$, значи $\angle ACM = 60^\circ$).
    Агли во $\triangle AMC$: $\angle CAM = 45^\circ$, $\angle ACM = 60^\circ$ (бидејќи $C$ е помеѓу $B$ и $M$, $\angle ACM = 180-120=60^\circ$).
    Третиот агол е $\angle AMC = 180 - (45+60) = 75^\circ$.
    Ова се совпаѓа со нашето решение!

### 🔗 Поврзани вештини
*   **Примарна вештина:** Синусна теорема (Sine Theorem).
*   **Потребни предзнаења:** Тригонометриски идентитети, Вредности на тригонометриски функции за $15^\circ, 75^\circ$.