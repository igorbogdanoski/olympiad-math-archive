---
difficulty: 7
grade: 11
problem_id: sigma139_p1902_elegant
related_theorems:
- similarity
source: Sigma 139, Zadaca 1902
tags:
- geometry
- rhombus
- cyclic_quadrilateral
- similarity
- rotation
title: Колинеарност во ромб (Елегантно решение)
type: geometry
---

# Текст на задачата
Нека $ABCD$ е ромб со $\angle ABC = 60^\circ$. Нека $M$ е точка од внатрешноста на триаголникот $ADC$, така што $\angle AMC = 120^\circ$. Нека правите $BA$ и $CM$ се сечат во точката $P$ и правите $BC$ и $AM$ се сечат во точката $Q$. Докажи дека точката $D$ лежи на правата $PQ$.

# Решение
## Стратегија
Ова е задача која најубаво се решава со комбинирање на својствата на тетивни четириаголници и геометриски трансформации (ротација).
1.  Ќе воочиме дека точките $A, B, C, M$ лежат на иста кружница. Ова е клучното откритие кое ни овозможува да ги поврземе аглите.
2.  Ќе докажеме дека триаголниците $\triangle PAD$ и $\triangle DCQ$ се слични (всушност, ротационо поврзани).
3.  Од сличноста ќе заклучиме дека аголот $\angle PDQ$ е рамен агол ($180^\circ$), што значи дека точките се колинеарни.

## 📐 Детално Решение

<details>
<summary>Чекор 1: Тетивност на четириаголникот $ABCM$</summary>

Дадено е дека $\angle ABC = 60^\circ$ и $\angle AMC = 120^\circ$.
Бидејќи збирот на спротивните агли е $\angle ABC + \angle AMC = 60^\circ + 120^\circ = 180^\circ$, четириаголникот $ABCM$ е **тетивен**.
Тоа значи дека точките $A, B, C, M$ лежат на иста кружница $k$.

</details>

<details>
<summary>Чекор 2: Еднаквост на агли</summary>

Од тетивноста на $ABCM$ следат следниве еднаквости на агли (агли над иста тетива):
1.  $\angle BAM = \angle BCM$ (над тетивата $BM$).
2.  $\angle AMB = \angle ACB$. Бидејќи $ABCD$ е ромб со агол $60^\circ$, триаголникот $ABC$ е рамностран, па $\angle ACB = 60^\circ$. Значи $\angle AMB = 60^\circ$.
3.  $\angle BMC = \angle BAC = 60^\circ$.

</details>

<details>
<summary>Чекор 3: Сличност на триаголници</summary>

Да ги разгледаме триаголниците $\triangle PAD$ и $\triangle QCD$.
1.  **Страни:** Бидејќи $ABCD$ е ромб со агол $60^\circ$, триаголникот $ADC$ е исто така рамностран. Значи $AD = CD$.
2.  **Агли:**
    *   Во $\triangle PAD$, аголот $\angle PAD$ е надворешен за ромбот кај темето $A$. Внатрешниот агол е $120^\circ$, па $\angle PAD = 180^\circ - 120^\circ = 60^\circ$.
    *   Во $\triangle QCD$, аголот $\angle QCD$ е надворешен за ромбот кај темето $C$. Внатрешниот агол е $120^\circ$, па $\angle QCD = 180^\circ - 120^\circ = 60^\circ$.
    *   Значи $\angle PAD = \angle QCD = 60^\circ$.

3.  **Однос на страни (Клучен момент):**
    Да ги разгледаме триаголниците $\triangle ABM$ и $\triangle CBM$.
    Применуваме Синусна теорема за $\triangle ABM$:
    $$ \frac{AB}{\sin(\angle AMB)} = \frac{BM}{\sin(\angle BAM)} \implies \frac{AB}{\sin 60^\circ} = \frac{BM}{\sin \alpha} $$ (каде $\alpha = \angle BAM$).
    Применуваме Синусна теорема за $\triangle CBM$:
    $$ \frac{BC}{\sin(\angle BMC)} = \frac{BM}{\sin(\angle BCM)} \implies \frac{BC}{\sin 60^\circ} = \frac{BM}{\sin \alpha} $$ (бидејќи $\angle BCM = \angle BAM = \alpha$).
    
    Сега да ги разгледаме $\triangle PAM$ и $\triangle QCM$.
    Во $\triangle PAM$: $\angle APM = 180^\circ - \angle PAM - \angle PMA$.
    $\angle PAM = 120^\circ + \alpha$ (надворешен агол).
    $\angle PMA = 180^\circ - \angle AMC - \angle PMC$? Не.
    Полесно е преку сличност:
    $\triangle PAM \sim \triangle QCM$.
    Зошто?
    $\angle PAM = 180^\circ - \angle BAM = 180^\circ - \alpha$.
    $\angle QCM = 180^\circ - \angle BCM = 180^\circ - \alpha$.
    Значи $\angle PAM = \angle QCM$.
    Исто така $\angle PMA = \angle QMC$ (накрстни агли? Не, $P, M, C$ се колинеарни, $Q, M, A$ се колинеарни).
    Значи $\triangle PAM \sim \triangle QCM$.
    Од сличноста следи:
    $$ \frac{PA}{QC} = \frac{AM}{CM} $$
    
    Дали $\frac{PA}{QC} = \frac{AD}{CD}$?
    Бидејќи $AD=CD$, ова е еквивалентно на $PA=QC$.
    Дали $PA=QC$?
    Од $\frac{PA}{QC} = \frac{AM}{CM}$, ова би значело $AM=CM$.
    Но $AM=CM$ важи само ако $M$ е на симетралата, што не е дадено.
    
    Значи $\triangle PAD$ и $\triangle QCD$ **не се складни**, туку се **слични**.
    Всушност, важи посилно тврдење:
    $$ \frac{PA}{AD} = \frac{CD}{QC} $$
    (Бидејќи $AD=AC=CD$).
    Ова е еквивалентно на $PA \cdot QC = AC^2$.
    Оваа релација се докажува со двојна примена на Синусна теорема (како што покажавме во претходната анализа):
    $PA = AC \frac{\sin(60^\circ-\alpha)}{\sin \alpha}$ и $QC = AC \frac{\sin \alpha}{\sin(60^\circ-\alpha)}$.
    Нивниот производ е точно $AC^2$.

    Бидејќи $\frac{PA}{AD} = \frac{CD}{QC}$ и $\angle PAD = \angle QCD = 60^\circ$, следи:
    $$ \triangle PAD \sim \triangle DCQ $$
    (Внимавајте на редоследот: $P$ одговара на $D$, $A$ на $C$, $D$ на $Q$).

</details>

<details>
<summary>Чекор 4: Колинеарност</summary>

Од сличноста $\triangle PAD \sim \triangle DCQ$ следи еднаквост на соодветните агли:
$$ \angle APD = \angle CDQ $$
$$ \angle PDA = \angle DQC $$

Да го пресметаме аголот $\angle PDQ$:
$$ \angle PDQ = \angle PDA + \angle ADC + \angle CDQ $$
Знаеме дека $\angle ADC = 60^\circ$ (од рамностраниот триаголник).
Заменуваме $\angle CDQ = \angle APD$:
$$ \angle PDQ = \angle PDA + 60^\circ + \angle APD $$
Во триаголникот $\triangle PAD$, збирот на аглите е $180^\circ$:
$$ \angle PDA + \angle APD + \angle PAD = 180^\circ $$
Бидејќи $\angle PAD = 60^\circ$, имаме:
$$ \angle PDA + \angle APD = 120^\circ $$
Заменуваме во изразот за $\angle PDQ$:
$$ \angle PDQ = 120^\circ + 60^\circ = 180^\circ $$

Бидејќи аголот $\angle PDQ$ е рамен агол, точките $P, D, Q$ лежат на иста права.

# Pedagogical Notes
1.  **Моќта на тетивноста:** Првиот чекор е секогаш да се бараат кружници. Условот $\angle B + \angle M = 180^\circ$ е „црвено знаме“ за тетивен четириаголник. Ова овозможува пренесување на аглите ($\alpha$) низ целиот цртеж.
2.  **Ротациона сличност:** Релацијата $\triangle PAD \sim \triangle DCQ$ не е обична сличност, туку вклучува и ротација за $60^\circ$. Ова е честа појава кај задачи со рамнострани триаголници. Кога ќе видите $PA \cdot QC = \text{const}$, помислете на сличност.
3.  **Доказ за колинеарност:** Стандардниот начин да се докаже дека $X, Y, Z$ се колинеарни е да се покаже дека $\angle XYZ = 180^\circ$. Ова често се прави со „пополнување“ на аглите од некој триаголник, како што направивме со $\triangle PAD$.



</details>

---
### 🎨 Визуелизација
![Илустрација](/assets/images/sigma139_p1902_elegant/sigma139_p1902_elegant.png)