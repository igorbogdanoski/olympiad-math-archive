---
grade: 8
field: geometry
difficulty: 5
source: "<натпревар / списание / година>"
problem_id: geom_8_2015_square
language_original: <mk | en | sr | hr | ...>
translated: false

# 
tags:
  - vectors
  - angle_chasing
  - geometry
  - complex_numbers
  - algebra
  - triangle_geometry
  - similarity
related_skills:
  - vectors
  - angle_chasing
  - complex_numbers
  - triangle_geometry
  - similarity--- GEOMETRY SKILLS ---
geometry_style: synthetic # synthetic | analytic | mixed
primary_skill: <main_tool> # e.g., angle_chasing, similarity, cyclic_quads
related_skills:
  - similarity
  - diagonal_properties

allowed_tools:
  - classical_euclidean
  - similarity
  - symmetry
forbidden_tools:
  - coordinate_geometry
  - vectors
  - complex_numbers
tags:
  - geometry
  - olympiad
---

# Поделба на дијагонала во квадрат

## Текст на задачата
Даден е квадрат $ABCD$. Темето $A$ е поврзано со точките $M$ и $N$, кои се средини на страните $CD$ и $BC$, соодветно. Да се докаже дека дијагоналата $BD$ со отсечките $AM$ и $AN$ поделена е на три еднакви делови.

## 📐 Скица / Конструкција

![Square Diagonal Division](images/geom_8_2015_square.png)

## 💡 Решение

### Метод 1: Сличност на триаголници
Нека $P$ е пресечната точка на $AM$ и $BD$, а $Q$ е пресечната точка на $AN$ и $BD$.

1.  **Разгледуваме $\triangle ABP$ и $\triangle MDP$:**
    Бидејќи $AB \parallel CD$ (страни на квадрат), следува дека $\triangle ABP \sim \triangle MDP$.
    Коефициентот на сличност е $k = \frac{AB}{DM} = \frac{AB}{AB/2} = 2$.
    Оттука $\frac{BP}{DP} = 2 \implies BP = 2DP$.
    Бидејќи $BP + DP = BD$, следува $3DP = BD \implies DP = \frac{1}{3}BD$.

2.  **Разгледуваме $\triangle ADQ$ и $\triangle NBQ$:**
    Бидејќи $AD \parallel BC$, следува дека $\triangle ADQ \sim \triangle NBQ$.
    Коефициентот на сличност е $k = \frac{AD}{BN} = \frac{AD}{AD/2} = 2$.
    Оттука $\frac{DQ}{BQ} = 2 \implies DQ = 2BQ$.
    Бидејќи $DQ + BQ = BD$, следува $3BQ = BD \implies BQ = \frac{1}{3}BD$.

3.  **Заклучок:**
    $DP = \frac{1}{3}BD$ и $BQ = \frac{1}{3}BD$.
    $PQ = BD - DP - BQ = BD - \frac{1}{3}BD - \frac{1}{3}BD = \frac{1}{3}BD$.
    Значи, $DP = PQ = QB$.

### Метод 2: Тежиште на триаголник
1.  Нека $O$ е пресекот на дијагоналите $AC$ и $BD$. Тогаш $O$ е средина на $AC$.
2.  Во триаголникот $ABC$, отсечката $BO$ е тежишна линија (бидејќи $O$ е средина на $AC$).
3.  Отсечката $AN$ е исто така тежишна линија (бидејќи $N$ е средина на $BC$).
4.  Нивниот пресек $Q$ е тежиште на $\triangle ABC$.
5.  Тежиштето ја дели тежишната линија во однос $2:1$ од темето.
    Значи, $BQ = \frac{2}{3} BO$.
    Бидејќи $BO = \frac{1}{2} BD$, имаме $BQ = \frac{2}{3} \cdot \frac{1}{2} BD = \frac{1}{3} BD$.
6.  Аналогно, во триаголникот $ACD$, $P$ е тежиште (пресек на $DO$ и $AM$).
    $DP = \frac{2}{3} DO = \frac{2}{3} \cdot \frac{1}{2} BD = \frac{1}{3} BD$.
7.  Останува $PQ = \frac{1}{3} BD$.