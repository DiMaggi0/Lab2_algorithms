Для набора тестовых данных использовались прямоугольники, построенные по формуле 
[(1+i) * 2, (1+i) * 2, (count-i) * 3, (count-i) * 3], где
count - количество прямоугольников
i изменяется от 0 до count с шагом 1.


Точки из запросов получались, исходя из следующей формулы 
((p1 + i) ** 3) % (count*2), ((p2 + i) ** 3) % (count*2), где
count - количество прямоугольников
i изменяется от 0 до count/2 с шагом 1
p1, p2 - различные большие простые числа, p1 = 99523, p2 = 98621

Код для тестирования времени алгоритмов можно найти по пути tests/algorithms_test.py

Графики сравнения алгоритмов и соответствующие выводы находятся по пути tests/графики+выводы.xlsx

Логин в контесте - dapetrov_4@edu.hse.ru

Петров Дмитрий 21ПИ-1 
