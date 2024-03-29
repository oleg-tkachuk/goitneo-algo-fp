# goitneo-algo-fp

## Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком

```shell
Task 1 - Single Linked List | The original list:
0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> None

Task 1 - Single Linked List | Reversed list:
8 -> 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> 0 -> None

Task 1 - Single Linked List | An unsorted list:
4 -> 7 -> 2 -> 5 -> 8 -> 1 -> 9 -> 3 -> 6 -> 0 -> None

Task 1 - Single Linked List | Sorted list:
0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> None

Task 1 - Single Linked List | Merge sorted list:
0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> None
```

## Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії

![Дерево Піфагора](/images/task-2.png)

## Завдання 3. Дерева, алгоритм Дейкстри

```shell
+------------+-----------------------------------+------------+
| City       | Route                             |   Distance |
+============+===================================+============+
| Athens     | Kyiv -> Rome -> Athens            |       3612 |
+------------+-----------------------------------+------------+
| Berlin     | Kyiv -> Berlin                    |       1300 |
+------------+-----------------------------------+------------+
| Copenhagen | Kyiv -> Copenhagen                |       1776 |
+------------+-----------------------------------+------------+
| Lisbon     | Kyiv -> Rome -> Lisbon            |       4862 |
+------------+-----------------------------------+------------+
| Oslo       | Kyiv -> Warsaw -> Oslo            |       1828 |
+------------+-----------------------------------+------------+
| Rome       | Kyiv -> Rome                      |       2351 |
+------------+-----------------------------------+------------+
| Stockholm  | Kyiv -> Warsaw -> Stockholm       |       2359 |
+------------+-----------------------------------+------------+
| Tallinn    | Kyiv -> Warsaw -> Oslo -> Tallinn |       2600 |
+------------+-----------------------------------+------------+
| Warsaw     | Kyiv -> Warsaw                    |        800 |
+------------+-----------------------------------+------------+
```

![Найкоротші шляхи, знайдені алгоритмом Дейкстри](/images/task-3.png)

## Завдання 4. Візуалізація піраміди

```shell
Arbitrary list: [5, 79, 10, 51, 10, 49, 64, 84, 81, 25, 9, 44, 80, 56, 51]
Binary heap: [5, 9, 10, 51, 10, 44, 51, 84, 81, 25, 79, 49, 80, 56, 64]
```

![Бінарна купа](/images/task-4.png)

## Завдання 5. Візуалізація обходу бінарного дерева

```shell
Arbitrary list: [66, 80, 91, 22, 11, 51, 18, 49, 65, 69, 95, 51, 97, 41, 46]
Binary heap: [11, 22, 18, 49, 69, 51, 41, 66, 65, 80, 95, 51, 97, 91, 46]
```

![Обхід дерева у глибину](/images/task-5-1.png)

![Обхід дерева в ширину](/images/task-5-2.png)

## Завдання 6: Жадібні алгоритми та динамічне програмування

```shell
Жадібний алгоритм (Greedy Algorithm):

Item       Cost    Calories
-------  ------  ----------
Cola         15         220
Potato       25         350
Pepsi        10         100
Hot-dog      30         200

TOTAL:       80         870

Динамічне програмування (Dynamic Programming):

Item      Cost    Calories
------  ------  ----------
Cola        15         220
Cola        15         220
Cola        15         220
Cola        15         220
Cola        15         220
Potato      25         350

TOTAL:      100        1450
```

## Завдання 7: Використання методу Монте-Карло

**Метод Монте-Карло:**

```shell
+-------+---------------+
|   Sum |   Probability |
+=======+===============+
|     2 |      0.02801  |
+-------+---------------+
|     3 |      0.055748 |
+-------+---------------+
|     4 |      0.083595 |
+-------+---------------+
|     5 |      0.110166 |
+-------+---------------+
|     6 |      0.138937 |
+-------+---------------+
|     7 |      0.166527 |
+-------+---------------+
|     8 |      0.13939  |
+-------+---------------+
|     9 |      0.110905 |
+-------+---------------+
|    10 |      0.083185 |
+-------+---------------+
|    11 |      0.055721 |
+-------+---------------+
|    12 |      0.027816 |
+-------+---------------+
```

![Ймовірність суми при підкиданні двох гральних кісток (метод Монте-Карло)](/images/task-7.png)

**Аналітичні розрахунки:**

```shell
+-------+---------------+
|   Sum |   Probability |
+-------+---------------+
|     2 |  2.78% (1/36) |
+-------+---------------+
|     3 |  5.56% (2/36) |
+-------+---------------+
|     4 |  8.33% (3/36) |
+-------+---------------+
|     5 | 11.11% (4/36) |
+-------+---------------+
|     6 | 13.89% (5/36) |
+-------+---------------+
|     7 | 16.67% (6/36) |
+-------+---------------+
|     8 | 13.89% (5/36) |
+-------+---------------+
|     9 | 11.11% (4/36) |
+-------+---------------+
|    10 |  8.33% (3/36) |
+-------+---------------+
|    11 |  5.56% (2/36) |
+-------+---------------+
|    12 |  2.78% (1/36) |
+-------+---------------+
```

**Порівняємо результати:**

- Для суми 2, метод Монте-Карло дає 0.02801, а аналітичний розрахунок — 0.0278. Розбіжність невелика, що свідчить про високу точність методу Монте-Карло.
- Аналогічно, для інших сум можна побачити, що результати методу Монте-Карло досить близькі до аналітичних розрахунків. Найбільша розбіжність спостерігається для суми 7, де метод Монте-Карло дає 0.166527, а аналітичний розрахунок — 0.1667.

**Висновки:**  

- **Точність методу Монте-Карло:** Результати, отримані за допомогою методу Монте-Карло, досить точно відповідають аналітичним розрахункам. Це свідчить про те, що метод Монте-Карло може бути ефективним для вирішення задач, де аналітичне рішення важко знайти або воно недоступне.

- **Варіабельність результатів Монте-Карло:** Невеликі розбіжності між методом Монте-Карло та аналітичними розрахунками можуть бути пов'язані з випадковістю вибірки, що є характерною для методу Монте-Карло. Збільшення кількості ітерацій у методі Монте-Карло може зменшити цю розбіжність.

- **Результати методу Монте-Карло** в цьому випадку демонструють його ефективність і точність у моделюванні ймовірносних процесів, підтверджуючи його важливість як інструмента в математичному аналізі.