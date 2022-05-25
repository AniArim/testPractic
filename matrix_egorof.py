"""
Заполнение змейкой

Даны числа n и m. Создайте массив A[n][m] и заполните его змейкой (см. пример).

Входные данные
Программа получает на вход два числа n и m.

Выходные данные
Программа должна вывести  полученный массив, при этом между числами может быть любое количество пробелов.

Sample Input:
4 10

Sample Output:
0  1  2  3  4  5  6  7  8  9
19 18 17 16 15 14 13 12 11 10
20 21 22 23 24 25 26 27 28 29
39 38 37 36 35 34 33 32 31 30
"""
visota, dlinna = [int(i) for i in input().split()]

list = [[0 for item in range(0, dlinna)] for i in range(0, visota)]

digit = 0
i, j = 0, 0
for elem in range(0, visota):
    for j in range(0, dlinna):
        list[i][j] = digit
        digit += 1
    i += 1

for i in range(visota):
    if i % 2 != 0:
        a = list[i]
        list[i] = list[i][::-1]
        print(*list[i])
    else:
        print(list[i])


