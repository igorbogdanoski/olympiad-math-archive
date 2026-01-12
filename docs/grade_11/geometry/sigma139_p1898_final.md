---
difficulty: 6
grade: 11
problem_id: sigma139_p1898_final
related_theorems:
- geometry_construction
- trigonometric_identities
source: Sigma 139, Zadaca 1898
tags:
- geometry
- trapezoid
- synthetic_geometry
- parallelogram_construction
- cosine_rule
title: Трапез со нормална дијагонала (Синтетичко решение)
type: geometry
---

# Текст на задачата
Во трапезот $ABCD$ бочната страна $BC$ е нормална на дијагоналата $BD$, $\angle DCB = \frac{1}{2} \angle ADC$ и $\overline{AB} = \frac{1}{2} \overline{AD}$. Докажи дека $\overline{AC} = \overline{CD}$.

# Решение
## Стратегија
За да го решиме овој проблем чисто синтетички, ќе користиме помошна конструкција која е стандардна за трапези: повлекување на права низ едно теме паралелна со спротивниот крак.
1.  Ќе конструираме паралелограм за да ги пренесеме должините и аглите во еден триаголник.
2.  Ќе ги искористиме дадените услови за да ги изразиме сите страни преку еден параметар $x$.
3.  Ќе докажеме дека триаголникот $ACD$ е рамнокрак со пресметка на неговите страни.

## 📐 Детално Решение

<details>
<summary>Чекор 1: Ознаки и конструкција</summary>

Нека $\angle DCB = \alpha$. Според условот, $\angle ADC = 2\alpha$.
Нека $AB = x$. Според условот, $AD = 2x$.
Низ темето $B$ повлекуваме права паралелна со кракот $AD$, која ја сече основата $CD$ во точка $K$.
Четириаголникот $ABKD$ е паралелограм (бидејќи $AB \parallel DK$ и $AD \parallel BK$).
Од својствата на паралелограм следи:
*   $DK = AB = x$
*   $BK = AD = 2x$
*   $\angle BKC = \angle ADC = 2\alpha$ (согласни агли).

</details>

<details>
<summary>Чекор 2: Анализа на триаголникот $BKC$</summary>

Во $\triangle BKC$:
*   $\angle BCK = \alpha$ (дадено).
*   $\angle BKC = 2\alpha$ (од конструкцијата).
*   $\angle KBC = 180^\circ - (2\alpha + \alpha) = 180^\circ - 3\alpha$.

Применуваме Синусна теорема за $\triangle BKC$:
$$ \frac{BK}{\sin \alpha} = \frac{BC}{\sin 2\alpha} $$
Заменуваме $BK = 2x$:
$$ \frac{2x}{\sin \alpha} = \frac{BC}{2\sin \alpha \cos \alpha} $$
Кратиме $\sin \alpha$ (бидејќи $\alpha \neq 0$):
$$ 2x = \frac{BC}{2\cos \alpha} \implies BC = 4x \cos \alpha $$

</details>

<details>
<summary>Чекор 3: Анализа на правоаголниот триаголник $BCD$</summary>

Дадено е дека $BC \perp BD$, што значи $\triangle BCD$ е правоаголен со прав агол кај $B$ (во однос на дијагоналата, т.е. $\angle DBC = 90^\circ$).
Во овој триаголник:
$$ \cos(\angle DCB) = \frac{BC}{CD} $$
$$ \cos \alpha = \frac{4x \cos \alpha}{CD} $$
Кратиме $\cos \alpha$ (бидејќи $\alpha < 90^\circ$):
$$ 1 = \frac{4x}{CD} \implies CD = 4x $$

</details>

<details>
<summary>Чекор 4: Наоѓање на вредноста на $\cos \alpha$</summary>

Сега да го разгледаме триаголникот $ABD$.
$\angle ADB = \angle ADC - \angle BDC$.
Во правоаголниот $\triangle BCD$, $\angle BDC = 90^\circ - \alpha$.
Значи $\angle ADB = 2\alpha - (90^\circ - \alpha) = 3\alpha - 90^\circ$.
Применуваме Синусна теорема за $\triangle ABD$:
$$ \frac{AB}{\sin(3\alpha - 90^\circ)} = \frac{AD}{\sin(\angle ABD)} $$
Знаеме дека $\angle ABD = \angle BDC = 90^\circ - \alpha$ (наизменични агли).
$$ \frac{x}{-\cos 3\alpha} = \frac{2x}{\cos \alpha} $$
$$ \frac{1}{-\cos 3\alpha} = \frac{2}{\cos \alpha} \implies \cos \alpha = -2\cos 3\alpha $$
Користиме формула за троен агол $\cos 3\alpha = 4\cos^3 \alpha - 3\cos \alpha$:
$$ \cos \alpha = -2(4\cos^3 \alpha - 3\cos \alpha) $$
$$ \cos \alpha = -8\cos^3 \alpha + 6\cos \alpha $$
$$ 8\cos^3 \alpha = 5\cos \alpha $$
Делиме со $\cos \alpha$:
$$ 8\cos^2 \alpha = 5 \implies \cos^2 \alpha = \frac{5}{8} $$

</details>

<details>
<summary>Чекор 5: Доказ дека $AC = CD$</summary>

Во $\triangle ACD$, ги знаеме страните $AD = 2x$, $CD = 4x$ и аголот меѓу нив $\angle ADC = 2\alpha$.
Применуваме Косинусна теорема за да ја најдеме страната $AC$:
$$ AC^2 = AD^2 + CD^2 - 2 \cdot AD \cdot CD \cdot \cos 2\alpha $$
$$ AC^2 = (2x)^2 + (4x)^2 - 2(2x)(4x)(2\cos^2 \alpha - 1) $$
$$ AC^2 = 4x^2 + 16x^2 - 16x^2 \left( 2 \cdot \frac{5}{8} - 1 \right) $$
$$ AC^2 = 20x^2 - 16x^2 \left( \frac{5}{4} - 1 \right) $$
$$ AC^2 = 20x^2 - 16x^2 \left( \frac{1}{4} \right) $$
$$ AC^2 = 20x^2 - 4x^2 = 16x^2 $$
$$ AC = \sqrt{16x^2} = 4x $$

Бидејќи $CD = 4x$ (од Чекор 3) и $AC = 4x$, заклучуваме дека:
$$ AC = CD $$

**Заклучок:**
Докажавме дека страните $AC$ и $CD$ се еднакви.

# Pedagogical Notes
1.  **Основна идеја:** Конструкцијата на паралелограм ($ABKD$) е клучниот чекор што овозможува пренесување на должината $AD$ и аголот $D$ на исто место со $BC$, формирајќи триаголник ($BKC$) кој може лесно да се реши.
2.  **Совет од Олимпиец:** Воведувањето на параметар $x$ за најмалата страна ($AB$) е многу корисно. Наместо да работите со имиња на отсечки ($AB, CD$), работите со алгебарски изрази ($x, 2x, 4x$), што е многу попрегледно.
3.  **Синтеза:** Ова решение е убав спој на геометриска конструкција и тригонометриски идентитети. Иако користиме косинуси, суштината е геометриска (односи во триаголник).



</details>

---
### 🎨 Визуелизација
![Илустрација](/assets/images/sigma139_p1898_final/sigma139_p1898_final.png)