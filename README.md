# <center>🔥  PracticeLinear_Lab2  🔥</center>

## <center>♦️  *Задание 3*  ♦️</center>


> #### 💠 Начальный треугольник
Состоит из 3-х пиков A, B, C следующим образом:
- `A(5, -5)`
- `B(4, 3)`
- `C(10, 5)`

![Original Triangle](Images/part_0.png)

> #### 💠 Отображение 1: Отражение (симметрию) плоскости относительно прямой y = 2x.
🔸Cобственные векторы
-  $v_1$ = (1, 2) 
-  $v_2$ = (-4, 2)

🔸Преобразование

| Начальный треугольник | Треугольник после отображения |
|:-----------:|:------:|
| A(5, -5) | A'(-7, 1) |
| B(4, 3)  | B'(0, 5)  |
| C(10, 5) | C'(-2, 11)|

![](Images/part_1.png)

> #### 💠  Отображение 2: Отображение всей плоскости в прямую y = -2x.
🔸Преобразование

| Начальный треугольник | Треугольник после отображения |
|:-----------:|:------:|
| A(5, -5) | A'(-5/2, 5) |
| B(4, 3)  | B'(5, -10)  |
| C(10, 5) | C'(10, -20) |

![](Images/part_2.png)

> #### 💠 Отображение 3: Поворот плоскости на 90 градусов против часовой стрелки.
🔸Преобразование

| Начальный треугольник | Треугольник после отображения |
|:-----------:|:------:|
| A(5, -5) | A'(5, 5)   |
| B(4, 3)  | B'(-3, 4)  |
| C(10, 5) | C'(-5, 10) |

![](Images/part_3.png)

> #### 💠 Отображение 4: Центральную симметрию плоскости относительно начала координат.
🔸Преобразование

| Начальный треугольник | Треугольник после отображения |
|:-----------:|:------:|
| A(5, -5) | A'(-5, 5)   |
| B(4, 3)  | B'(-4, -3)  |
| C(10, 5) | C'(-5, -10) |

![](Images/part_4.png)

> #### 💠 Отображение 5: Отображение, которое можно описать так: сначала отражение относительно прямой y = 2x, потом поворот на 60 градусов по часовой стрелке.
🔸`y = 2x - Зеленый`

🔸Преобразование

| Начальный треугольник | Черный треугольник после первого отображения | Зеленый треугольник после второго отображения|
|:-----------:|:------:|:------:|
| A(5, -5) | A'(-7, 1)  | A*($\frac{{5\sqrt{3} - 35\sqrt{2}}}{2}$, $\frac{{35 \sqrt{3} + 5}}{2}$) |
| B(4, 3)  | B'(0, 5)   | B*($\frac{{25\sqrt{3}}}{2}$, $\frac{25}{2}$) |
| C(10, 5) | C'(-2, 11) | C*($\frac{{55\sqrt{3} - 10\sqrt{2}}}{2}$, $\frac{{10\sqrt{3} + 55}}{2}$) |


![](Images/part_5.png)

> #### 💠 Отображение 6: Отображение, которое переводит прямую y = 0 в y = 2x и прямую x = 0 в y = -2x.
🔸`y = 2x - Зеленый` 

🔸`y = -2x - Синий` 

🔸Преобразование

| Начальный треугольник | Треугольник после отображения |
|:-----------:|:------:|
| A(5, -5) | A'(5, 5)   |
| B(4, 3)  | B'(-3, 4)  |
| C(10, 5) | C'(-5, 10) |

![](Images/part_6.png)

> #### 💠 Отображение 7: Отображение, которое переводит прямую y = 2x в y = 0 и прямую y = -2x в x = 0.
🔸`y = 2x - Зеленый` 

🔸`y = -2x - Синий` 

🔸Преобразование

| Начальный треугольник | Треугольник после отображения |
|:-----------:|:------:|
| A(5, -5) | A'(-5, -5) |
| B(4, 3)  | B'(3, -4)  |
| C(10, 5) | C'(5, -10) |

![](Images/part_7.png)

> #### 💠 Отображение 8: Отображение, которое меняет местами прямые y = 2x и y = -2x.
🔸`y = 2x -  Красный`

🔸`y = -2x - Синий` 

🔸Преобразование

| Начальный треугольник | Треугольник после отображения |
|:-----------:|:------:|
| A(5, -5) | A'(7, 1)  |
| B(4, 3)  | B'(0, 5)  |
| C(10, 5) | C'(2, 11) |

![](Images/part_8.png)

> #### 💠 Отображение 9: Отображение, которое переводит круг единичной площади с центром в начале координат в круг площади 9.
🔸Круг единичной площади - Красный 

🔸Круг площади 9 - Зеленый

🔸Преобразование

![](Images/part_9.png)

> #### 💠 Отображение 10: Отображение, которое переводит круг единичной площади с центром в начале координат в некруг площади 6.
🔸Круг единичной площади - Красный 

  🔻Я выбираю любые 3 точки `A`, `B`, `C` на окружности.
  
- Затем выполните отображение и получите равносторонний треугольник.
    
🔸Треугольник площади 6 - Зеленый: `A'`, `B'`, `C'`

🔸Преобразование

![](Images/part_10.png)

> #### 💠 Отображение 11: Отображение, у которого собственные вектора перпендикулярны, и ни один из них не лежит на прямой y = 0 или y = x.
🔸Cобственный вектор
-  $v_1$ = (2, 4) 
-  $v_2$ = (-8, 4)

🔸Преобразование

| Начальный треугольник | Треугольник после отображения |
|:-----------:|:------:|
| A(5, -5) | A'(0, $\frac{15}{2}$)  |
| B(4, 3)  | B'(7,  $\frac{5}{2}$)  |
| C(10, 5) | C'(15, $\frac{15}{5}$) |

![](Images/part_11.png)

> #### 💠 Отображение 12: Отображение, у которого нет двух неколлинеарных собственных векторов.
🔸Cобственные векторы
-  $v_1$ = (-4, 2) 
-  $v_2$ = (2, 2)

🔸Преобразование

| Начальный треугольник | Треугольник после отображения |
|:-----------:|:------:|
| A(5, -5) | A'(-15, 5)|
| B(4, 3)  | B'(2, 4)  |
| C(10, 5) | C'(0, 10) |

![](Images/part_12.png)

> #### 💠 Отображение 13: Отображение, у которого нет ни одного вещественного собственного вектора.
🔸Cобственные векторы
-  $v_1$ = (5, 5) 
-  $v_2$ = (-5, 5)

🔸Преобразование

| Начальный треугольник | Треугольник после отображения |
|:-----------:|:------: |
| A(5, -5) | A'(0, -10) |
| B(4, 3)  | B'(7, -1)  |
| C(10, 5) | C'(15, -5) |

![](Images/part_13.png)

> #### 💠 Отображение 14: Отображение, для которого любой ненулевой вектор является собственным.
🔸Cобственные векторы
-  $v_1$ = (-10, -5) 
-  $v_2$ = (-10, 5)
-  $v_3$ = (5, 10)
-  $v_4$ = (5, -10)

🔸Преобразование

| Начальный треугольник | Треугольник после отображения |
|:-----------:|:------:|
| A(5, -5) | A'(10, -10)|
| B(4, 3)  | B'(8, 6)   |
| C(10, 5) | C'(20, 10) |

![](Images/part_14.png)

> #### 💠 Отображение 15: Пару отображений, последовательное применение которых даёт различные результаты в зависимости от порядка: AB ̸= BA.
🔸Cобственные векторы
-  $v_1$ = (12, 9) 
-  $v_2$ = (-9, 12)

🔸Преобразование

| Начальный треугольник | Треугольник после отображения A | Треугольник после отображения B|Треугольник после отображения AB |Треугольник после  отображения BA|
|:-----------:|:------:|:------:|:------:|:------:|
| a(5, -5) | $a_2$(-7, 1)  | $a_3$(7, 1) | $a_23$(-5, -5) | $a_32$($\frac{-17}{5}$, $\frac{31}{5}$) |
| b(4, 3)  | $b_2$(0, 5)   | $b_3$(0, 5) | $b_23$(-4, 3)  | $b_32$(4, 3)        |
| c(10, 5) | $c_2$(-2, 11) | $c_3$(2, 11)| $c_23$(-10, 5) | $c_32$(10, 5)       |

![](Images/part_15.png)

> #### 💠 Отображение 16: Пару отображений, последовательное применение которых даёт одинаковый результат независимо от порядка: AB = BA.
🔸Cобственные векторы
-  $v_1$ = (0, 9) 
-  $v_2$ = (9, 0)

🔸Преобразование

| Начальный треугольник | Треугольник после отображения A | Треугольник после отображения B|Треугольник после отображения AB |Треугольник после  отображения BA|
|:-----------:|:------:|:------:|:------:|:------:|
| a(5, -5) | $a_2$(-5, 5)  | $a_3$(5, 5)  | $a_23$(-5, -5) | $a_32$(-5, -5) |
| b(4, 3)  | $b_2$(-4, -3) | $b_3$(4, -3) | $b_23$(4, 3)   | $b_32$(4, 3)   |
| c(10, 5) | $c_2$(-10, -5)| $c_3$(10, -5)| $c_23$(-10, 5) | $c_32$(-10, 5) |

![](Images/part_16.png)
