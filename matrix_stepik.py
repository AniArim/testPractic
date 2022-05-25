"""
Выведите таблицу размером n n×n, заполненную числами от 1 до n^2n
по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):

Sample Input:
5

Sample Output:
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
"""
import math

n = int(input())  # 5
count = n ** 2  # 25
step = 1

list = [[0 for item in range(0, n)] for i in range(0, n)]  # заполнение матрицы нолями

dlin, visot, napravlenie = 0, 0, 1
round = 0

while step <= count and round != math.ceil(n / 2):
    if napravlenie == 1:
        for item in list[visot]:
            if list[visot][dlin] == 0:
                list[visot][dlin] = step
                dlin += 1
                step += 1
        visot += 1
        napravlenie += 1

    if napravlenie == 2:
        dlin -= 1
        for k in range(visot, n - round):
            list[visot][dlin] = step
            step += 1
            visot += 1
        napravlenie += 1

    if napravlenie == 3:
        visot -= 1
        while dlin > round:
            dlin -= 1
            list[visot][dlin] = step
            step += 1
        napravlenie += 1

    if napravlenie == 4:
        while visot > round+1:
            visot -= 1
            list[visot][dlin] = step
            step += 1
        dlin = round + 1
        round += 1
        napravlenie = 1

for i in list:
    print(*i)
"""
for visot in range(n):
    for dlin in range(n):
        list[visot][dlin] = step
        step += 1
list[j] = [i for i in range(n)]
"""
