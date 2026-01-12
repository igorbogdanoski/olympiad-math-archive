---
difficulty: 5
grade: 11
problem_id: sigma139_y3_p1
related_theorems:
- functions
source: Sigma 139, Treta godina, Zadaca 1
tags:
- trigonometry
- telescoping_sum
- identities
title: Телескопска сума со тригонометрија
type: algebra
---

# Текст на задачата
Пресметај го збирот:
$$ S = \frac{\sin 1^\circ}{\cos 0^\circ \cdot \cos 1^\circ} + \frac{\sin 1^\circ}{\cos 1^\circ \cdot \cos 2^\circ} + \frac{\sin 1^\circ}{\cos 2^\circ \cdot \cos 3^\circ} + \dots + \frac{\sin 1^\circ}{\cos 2024^\circ \cdot \cos 2025^\circ} $$

# Решение
## Стратегија
Ова е класична задача за **телескопска сума** во тригонометрија.
Клучната идеја е да се трансформира општиот член на сумата во разлика на два члена.
Забележуваме дека во броителот имаме $\sin 1^\circ$, а во именителот производ на косинуси од агли чија разлика е токму $1^\circ$ (на пример, $1^\circ - 0^\circ = 1^\circ$, $2^\circ - 1^\circ = 1^\circ$).
Ќе го искористиме идентитетот за синус од разлика: $\sin(x-y) = \sin x \cos y - \cos x \sin y$.

## 📐 Детално Решение

<details>
<summary>Чекор 1: Трансформација на општиот член</summary>

Да го разгледаме $k$-тиот член на сумата:
$ a_k = \frac{\sin 1^\circ}{\cos k^\circ \cdot \cos (k+1)^\circ} $

Бидејќи $1^\circ = (k+1)^\circ - k^\circ$, можеме да запишеме:
$ a_k = \frac{\sin((k+1)^\circ - k^\circ)}{\cos k^\circ \cdot \cos (k+1)^\circ} $

</details>

<details>
<summary>Чекор 2: Примена на адициона формула</summary>

Го развиваме броителот:
$ \sin((k+1)^\circ - k^\circ) = \sin(k+1)^\circ \cos k^\circ - \cos(k+1)^\circ \sin k^\circ $

Заменуваме во изразот за $a_k$:
$ a_k = \frac{\sin(k+1)^\circ \cos k^\circ - \cos(k+1)^\circ \sin k^\circ}{\cos k^\circ \cdot \cos (k+1)^\circ} $

</details>

<details>
<summary>Чекор 3: Разделување на дропката</summary>

Ја делиме дропката на два дела:
$ a_k = \frac{\sin(k+1)^\circ \cos k^\circ}{\cos k^\circ \cdot \cos (k+1)^\circ} - \frac{\cos(k+1)^\circ \sin k^\circ}{\cos k^\circ \cdot \cos (k+1)^\circ} $

Кратиме:
$ a_k = \frac{\sin(k+1)^\circ}{\cos(k+1)^\circ} - \frac{\sin k^\circ}{\cos k^\circ} $
$ a_k = \tan(k+1)^\circ - \tan k^\circ $

</details>

<details>
<summary>Чекор 4: Пресметка на сумата</summary>

Сега ја запишуваме целата сума $S$ користејќи го новиот облик:
$ S = (\tan 1^\circ - \tan 0^\circ) + (\tan 2^\circ - \tan 1^\circ) + (\tan 3^\circ - \tan 2^\circ) + \dots + (\tan 2025^\circ - \tan 2024^\circ) $

Забележуваме дека ова е телескопска сума каде што средните членови се поништуваат:
*   $+\tan 1^\circ$ се поништува со $-\tan 1^\circ$
*   $+\tan 2^\circ$ се поништува со $-\tan 2^\circ$
*   ...
*   $+\tan 2024^\circ$ се поништува со $-\tan 2024^\circ$

Остануваат само последниот позитивен и првиот негативен член:
$ S = \tan 2025^\circ - \tan 0^\circ $

</details>

<details>
<summary>Чекор 5: Финална пресметка</summary>

Знаеме дека $\tan 0^\circ = 0$.

За $\tan 2025^\circ$, ќе го искористиме периодот на тангенсот ($180^\circ$):
$ 2025 = 11 \cdot 180 + 45 $

Значи:
$ \tan 2025^\circ = \tan(11 \cdot 180^\circ + 45^\circ) = \tan 45^\circ = 1 $

Конечно:
$ S = 1 - 0 = 1 $

</details>

**Заклучок:**
Вредноста на збирот е **1**.

# Pedagogical Notes
1.  **Основна идеја:** Кога гледате сума од дропки со тригонометриски функции во именител, секогаш обидете се да го изразите броителот како синус од разликата на аглите во именителот. Ова е универзален „клуч“ за вакви задачи.
2.  **Совет од Олимпиец:** Оваа техника работи и за $\frac{\sin(x-y)}{\sin x \sin y} = \cot y - \cot x$. Запомнете ги овие два идентитети, тие се појавуваат многу често.
3.  **Чести грешки:** Внимавајте на редоследот при одземањето. Дали е $\tan(k+1) - \tan k$ или обратно? Проверете со првиот член: $\frac{\sin(1-0)}{\cos 0 \cos 1} = \frac{\sin 1 \cos 0 - \cos 1 \sin 0}{\cos 0 \cos 1} = \tan 1 - \tan 0$. Значи редоследот е (поголем) - (помал).

---
### 🎨 Визуелизација
![Илустрација](/assets/images/sigma139_y3_p1/sigma139_y3_p1.png)