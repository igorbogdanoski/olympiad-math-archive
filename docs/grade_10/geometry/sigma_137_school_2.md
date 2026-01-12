---
difficulty: 5
grade: 10
primary_skill: vector_addition
problem_id: sigma_137_school_2
related_skills:
- similarity
- midsegment_theorem
related_theorems:
- vectors
- similarity
source: Сигма 137, Задачи од училницата (Втора година)
tags:
- vectors
- triangle_geometry
- centroid
title: Векторска геометрија во триаголник
type: geometry
---

# Векторска геометрија во триаголник

# Текст на задачата
Даден е $\triangle ABC$ и точки $T$ и $S$ за кои $\overrightarrow{AS} = 3 \cdot \overrightarrow{CS}$ и $\overrightarrow{BT} = 3 \cdot \overrightarrow{CT}$. Нека $\{Q\} = BS \cap AT$. Докажи дека $\overrightarrow{QC} = \overrightarrow{CA} + \overrightarrow{CB}$.

*(Забелешка: Во оригиналниот текст има мала грешка во ознаките на векторите во условот, но од контекстот и решението е јасно дека се работи за точки кои ги делат страните во одреден однос. Условот $\overrightarrow{AS} = 3\overrightarrow{CS}$ значи дека $S$ лежи на правата $AC$ и $A, S, C$ се колинеарни. Бидејќи векторите се исто насочени (позитивен коефициент), $C$ е меѓу $A$ и $S$ или $S$ е меѓу $A$ и $C$? Всушност, ако $\overrightarrow{AS} = 3\overrightarrow{CS}$, тогаш $S$ е надворешна точка или $C$ е меѓу нив?
Ајде да го провериме решението од сликата. Решението вели $AC = 2CS$. Ова значи $\overrightarrow{AC} + \overrightarrow{CS} = 3\overrightarrow{CS} \implies \overrightarrow{AC} = 2\overrightarrow{CS}$. Значи $C$ е средина на $AS$? Не, $AC:CS = 2:1$. Точките се подредени $A-C-S$. Слично за $B-C-T$.)*

# 💡 Помош (Hints)
<details>
<summary>Кликни за мала помош</summary>
1. Нацртај скица. Од условот $\overrightarrow{AS} = 3\overrightarrow{CS}$, заклучи каде се наоѓа точката $C$ во однос на $A$ и $S$. (Дали е внатрешна или надворешна поделба?)
   $$ \overrightarrow{AC} = \overrightarrow{AS} - \overrightarrow{CS} = 3\overrightarrow{CS} - \overrightarrow{CS} = 2\overrightarrow{CS} $$

2. Забележи ја сличноста помеѓу $\triangle ABC$ и $\triangle STC$. Кој е коефициентот на сличност?
   $$ \frac{AC}{CS} = \frac{BC}{CT} = 2 $$

3. Разгледај го четириаголникот $ABST$. Што претставува отсечката $AB$ во однос на $ST$? (Средна линија во некој поголем триаголник или паралелност?)
   $$ AB \parallel ST \text{ и } AB = 2ST $$

4. Точката $Q$ е пресек на дијагоналите на трапезот (или вкрстените линии). Искористи ја сличноста на $\triangle ABQ$ и $\triangle STQ$ за да го најдеш односот на $QC$ со некоја тежишна линија.
</details>

# Решение
## 🧠 Експертска Анализа (Интуиција)
Задачата бара да докажеме векторско равенство $\overrightarrow{QC} = \overrightarrow{CA} + \overrightarrow{CB}$.
Ако го препишеме ова како $\overrightarrow{QC} = -(\overrightarrow{AC} + \overrightarrow{BC})$, или уште подобро, да го преместиме почетокот во $C$:
$\overrightarrow{CQ} = -(\overrightarrow{CA} + \overrightarrow{CB}) = \overrightarrow{AC} + \overrightarrow{BC}$.
Ова значи дека $\overrightarrow{CQ}$ е дијагонала на паралелограмот конструиран над $\overrightarrow{AC}$ и $\overrightarrow{BC}$.
Или поедноставно: Ако $M$ е средина на $AB$, тогаш $\overrightarrow{CA} + \overrightarrow{CB} = 2\overrightarrow{CM}$.
Значи треба да докажеме дека $\overrightarrow{QC} = 2\overrightarrow{CM}$, односно $Q, C, M$ се колинеарни и $Q$ е "двојно подалеку" од $C$ отколку $M$, но во спротивна насока? Не, $\overrightarrow{QC}$ е насочен од $Q$ кон $C$.
Равенството $\overrightarrow{QC} = \overrightarrow{CA} + \overrightarrow{CB}$ значи дека $C$ е средина на $QM$? Не, тоа би било $\overrightarrow{CQ} + \overrightarrow{CM} = 0$.
Ајде да видиме геометриски.
Од условот $\overrightarrow{AS} = 3\overrightarrow{CS}$, следи $\overrightarrow{AC} + \overrightarrow{CS} = 3\overrightarrow{CS} \implies \overrightarrow{AC} = 2\overrightarrow{CS}$. Значи $C$ ја дели $AS$ во однос $2:1$.
Слично, $C$ ја дели $BT$ во однос $2:1$.
Ова значи дека $\triangle ABC \sim \triangle STC$ со коефициент $2$ и центар на сличност во $C$.
Бидејќи $AC/CS = BC/CT = 2$ и аглите се накрстни, триаголниците се слични и $AB \parallel ST$ со $AB = 2ST$.
Сега го гледаме "песочниот часовник" формиран од $AB$, $ST$ и пресекот $Q$.
$\triangle ABQ \sim \triangle STQ$ со коефициент $AB/ST = 2$.
Ова значи дека $Q$ лежи на тежишната линија од $C$ во $\triangle ABQ$? Не.
Ајде да одиме со вектори, тоа е најсигурно.

## 📐 Детално Решение

<details>
<summary>Чекор 1: Анализа на положбата на точките</summary>

Дадено е $\overrightarrow{AS} = 3\overrightarrow{CS}$.
Можеме да запишеме:
$$ \overrightarrow{AC} + \overrightarrow{CS} = 3\overrightarrow{CS} $$
$$ \overrightarrow{AC} = 2\overrightarrow{CS} \implies \overrightarrow{CS} = \frac{1}{2}\overrightarrow{AC} $$
Ова значи дека $C$ лежи на отсечката $AS$, и $S$ е "продолжение" на $AC$ преку $C$.

Аналогно за $T$:
$$ \overrightarrow{BT} = 3\overrightarrow{CT} \implies \overrightarrow{BC} = 2\overrightarrow{CT} \implies \overrightarrow{CT} = \frac{1}{2}\overrightarrow{BC} $$
</details>

<details>
<summary>Чекор 2: Сличност на триаголници</summary>

Ги разгледуваме $\triangle ABC$ и $\triangle STC$.
Имаме:
$$ \frac{AC}{CS} = 2 \quad \text{и} \quad \frac{BC}{CT} = 2 $$
Аголот $\angle ACB$ и $\angle SCT$ се накрстни агли (бидејќи $A,C,S$ и $B,C,T$ се колинеарни).
Според признакот САС (Страна-Агол-Страна), $\triangle ABC \sim \triangle STC$.
Од сличноста следи:
1.  $AB \parallel ST$ (бидејќи аглите се наизменични).
2.  $AB = 2 \cdot ST$, односно $\overrightarrow{AB} = -2\overrightarrow{ST}$ (заради спротивната ориентација низ $C$).
</details>

<details>
<summary>Чекор 3: Анализа на пресекот Q</summary>

Точката $Q$ е пресек на $BS$ и $AT$.
Да го разгледаме триаголникот $ABQ$.
Правата $ST$ е паралелна со $AB$ и ги сече краците $QA$ и $QB$.
Според Талесова теорема (или сличност на $\triangle ABQ \sim \triangle STQ$):
$$ \frac{AQ}{TQ} = \frac{BQ}{SQ} = \frac{AB}{ST} = 2 $$
Ова значи дека $Q$ ја дели отсечката $AT$ во однос $2:1$, и $BS$ во однос $2:1$.
Чекај, ова е позната конфигурација!
Во $\triangle ABQ$, точките $S$ и $T$ лежат на продолженијата? Не, $S$ е на $AC$, $T$ е на $BC$.
$Q$ е пресек на $AT$ и $BS$.
Во $\triangle ABQ$, отсечката $ST$ поврзува точки на страните $QA$ и $QB$.
Бидејќи $ST \parallel AB$, триаголниците се хомотетични.
</details>

<details>
<summary>Чекор 4: Векторски доказ</summary>

Сакаме да го изразиме $\overrightarrow{QC}$.
Нека $R$ е средина на $AB$. Тогаш $\overrightarrow{CA} + \overrightarrow{CB} = 2\overrightarrow{CR}$.
Треба да докажеме $\overrightarrow{QC} = 2\overrightarrow{CR}$.
Ова е еквивалентно на тоа $C$ да е средина на $QR$.

Да видиме каде е $C$ во однос на $\triangle ABQ$.
$S$ е точка на $BQ$ таква што $QS : SB = 1:2$ (од сличноста).
$T$ е точка на $AQ$ таква што $QT : TA = 1:2$.
Всушност, $S$ и $T$ се точки кои ги делат страните во однос $1:2$ од врвот $Q$.
Правата $CS$ е тежишна линија? Не.
Дадено е дека $A, C, S$ се колинеарни. $C$ лежи на $AS$.
Во $\triangle ABQ$, $AS$ и $BT$ се тежишни линии!
Зошто?
Видовме дека $Q$ ја дели $AT$ во однос $2:1$. Тоа е својство на тежиштето.
Но, $AT$ е целата отсечка. $C$ лежи на неа.
Ајде да провериме:
$Q$ е врв. $A, B$ се другите врвови.
$T$ лежи на $AQ$. $S$ лежи на $BQ$.
$C$ е пресек на $AS$ и $BT$.
Бидејќи $AB \parallel ST$ и $AB = 2ST$, $C$ е центар на хомотетија што го preslikuva $\triangle ABQ$ во некој помал триаголник? Не.
$C$ е пресек на дијагоналите на трапезот $ABST$.
Но, $C$ е пресек на $AS$ и $BT$.
Во $\triangle ABQ$, $AS$ и $BT$ се линии од темињата кон спротивните страни.
Дали се тежишни линии?
Знаеме $QT/QA = 1/3$? Не, $QT/TA = 1/2 \implies QT = (1/3)QA$.
Значи $T$ не е средина.
Но, чекај. Решението во списанието вели: "$T$ и $S$ се средишни точки на соодветните страни во $\triangle ABQ$".
Ајде да го провериме тоа.
Ако $T$ е средина на $AQ$, тогаш $AT = 2QT$.
Ние имаме $AB = 2ST$.
Од сличноста $\triangle ABQ \sim \triangle STQ$, имаме $AB/ST = AQ/TQ = BQ/SQ = 2$.
Значи $AQ = 2TQ$. Ова значи $T$ е средина на $AQ$!
Слично, $S$ е средина на $BQ$.
Заклучок: $AS$ и $BT$ се **тежишни линии** во $\triangle ABQ$.
Нивниот пресек $C$ е **тежиште** на $\triangle ABQ$.
</details>

<details>
<summary>Чекор 5: Финален доказ преку својства на тежиште</summary>

Бидејќи $C$ е тежиште на $\triangle ABQ$, тоа лежи на третата тежишна линија $QR$, каде $R$ е средина на $AB$.
Својството на тежиштето е:
$$ \overrightarrow{QC} = \frac{2}{3} \overrightarrow{QR} $$
Чекај, ова не води до бараното равенство.
Бараме $\overrightarrow{QC} = \overrightarrow{CA} + \overrightarrow{CB}$.
Да го изразиме $\overrightarrow{CA} + \overrightarrow{CB}$ преку $R$.
$\overrightarrow{CA} + \overrightarrow{CB} = 2\overrightarrow{CR}$ (правило на паралелограм/средина).
Значи треба да докажеме $\overrightarrow{QC} = 2\overrightarrow{CR}$.
Ова значи дека $C$ ја дели отсечката $QR$ така што $QC = 2CR$.
Дали ова е точно за тежиште?
Да! Тежиштето ја дели тежишната линија во однос $2:1$ сметано од темето.
Значи $QC : CR = 2 : 1 \implies QC = 2CR$.
Векторски, бидејќи $Q, C, R$ се колинеарни и по тој редослед:
$$ \overrightarrow{QC} = 2\overrightarrow{CR} $$
Бидејќи $2\overrightarrow{CR} = \overrightarrow{CA} + \overrightarrow{CB}$ (за секоја точка $C$ и средина $R$ на $AB$), доказот е завршен.
</details>

**Краен одговор:** Равенството е докажано користејќи го фактот дека $C$ е тежиште на $\triangle ABQ$.



---
### 🎨 Визуелизација
![Илустрација](/assets/images/sigma_137_school_2/sigma_137_school_2.png)

## 👨‍🏫 Менторски Белешки
1.  **Златен Совет:** Кога имате односи на отсечки како $2:1$ или $1:1$, секогаш помислете на **тежиште**. Тежиштето е единствената точка што ги дели сите тежишни линии во однос $2:1$. Препознавањето на оваа конфигурација ја претвора тешката векторска задача во едноставна геометриска констатација.
2.  **Векторски "Трик":** Равенството $\overrightarrow{CA} + \overrightarrow{CB} = 2\overrightarrow{CM}$ е најкорисната алатка во векторска геометрија. Запаметете го како "Правило на средина".
3.  **Визуелизација:** Клучно беше да се сфати дека $Q$ е "врвот" на планината, а $AB$ е основата, додека $C$ лебди во средината како центар на рамнотежа (тежиште).

### 🔗 Поврзани вештини
*   **Примарна вештина:** Векторско собирање (Vector Addition).
*   **Потребни предзнаења:** Сличност на триаголници, Својства на тежиште.