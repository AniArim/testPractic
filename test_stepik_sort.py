"""
Дан файл с таблицей в формате TSV с информацией о росте школьников разных классов.
Напишите программу, которая прочитает этот файл и подсчитает для каждого класса средний рост учащегося.
Файл состоит из набора строк, каждая из которых представляет собой три поля:
Класс Фамилия Рост
Класс обозначается только числом. Буквенные модификаторы не используются. Номер класса может быть от 1 до 11
включительно. В фамилии нет пробелов, а в качестве роста используется натуральное число, но при подсчёте среднего
требуется вычислить значение в виде вещественного числа.
Выводить информацию о среднем росте следует в порядке возрастания номера класса (для классов с первого по одиннадцатый).
 Если про какой-то класс нет информации, необходимо вывести напротив него прочерк.
В качестве ответа прикрепите файл с полученными данными о среднем росте.

Sample Input:

6	Вяххи	159
11	Федотов	172
7	Бондарев	158
6	Чайкина	153

Sample Output:
1 -
2 -
3 -
4 -
5 -
6 156.0
7 158.0
8 -
9 -
10 -
11 172.0
"""

try:
    with open("test.txt", "r", encoding="utf-8") as file:
        text = file.read().strip()
except:
    pass
final_collect = {}
text = text.rsplit(sep="\n", maxsplit=-1)
i = 0
for item in text:
    text[i] = item.rsplit(sep=None, maxsplit=-1)
    i += 1

collect = {}
i = 0
for item in text:
    collect.setdefault(int(item[0]), []).append(int(item[2]))  # создает пары ключ-значение, добавляет по ключу значение в список

for i in range(1,12):
    if i not in collect.keys():
        collect.update({i: "-"})

list_keys = list(collect.keys())
list_keys.sort()
for i in list_keys:
    if isinstance(collect[i], list):
        final_collect.update({i: sum(collect[i])/len(collect[i])})
    else:
        final_collect.update({i: collect[i]})

try:
    with open("result.txt", "w", encoding="utf-8") as file:
        for items in final_collect:
            file.write(f"{items} {final_collect.get(items)}\n")

except:
    pass





