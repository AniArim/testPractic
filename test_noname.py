"""
Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит
на стандартный вывод сводную таблицу результатов всех матчей.
За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
Формат ввода следующий:
В первой строке указано целое число n — количество завершенных игр.
После этого идет n строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков
Конкретный пример ввода-вывода приведён ниже.
Порядок вывода команд произвольный.

Sample Input:

3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15
Sample Output:

Спартак:2 0 0 2 0
Зенит:2 1 0 1 3
Локомотив:2 2 0 0 6
"""

n = int(input())
game_line = []
game_dict = {}

while len(game_line) != n:
    try:
        game_line.append(input().split(sep=";"))
    except:
        break

i = 0
for elements in game_line:
    if game_line[i][0] not in game_dict:
        game_dict.update({game_line[i][0]: [0, 0, 0, 0, 0]})
    if game_line[i][2] not in game_dict:
        game_dict.update({game_line[i][2]: [0, 0, 0, 0, 0]})
    i += 1

for i in range(n):
    if int(game_line[i][1]) < int(game_line[i][3]):
        a = game_dict.get(game_line[i][0])
        a[0] += 1
        a[3] += 1
        game_dict.update({game_line[i][0]: a})

        a = game_dict.get(game_line[i][2])
        a[0] += 1
        a[1] += 1
        a[4] += 3
        game_dict.update({game_line[i][2]: a})

    elif int(game_line[i][1]) > int(game_line[i][3]):
        a = game_dict.get(game_line[i][0])
        a[0] += 1
        a[1] += 1
        a[4] += 3
        game_dict.update({game_line[i][0]: a})

        a = game_dict.get(game_line[i][2])
        a[0] += 1
        a[3] += 1
        game_dict.update({game_line[i][2]: a})

    else:
        a = game_dict.get(game_line[i][0])
        a[0] += 1; a[2] += 1; a[4] += 1
        game_dict.update({game_line[i][0]: a})

        a = game_dict.get(game_line[i][2])
        a[0] += 1; a[2] += 1; a[4] += 1
        game_dict.update({game_line[i][2]: a})



for keys, values in game_dict.items():
    print(f"{keys}: ",end=" ")
    for i in values:
        print(i, end=" ")
    print()
