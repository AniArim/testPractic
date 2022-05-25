"""
Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. Программа принимает на вход две строки
одинаковой длины, на первой строке записаны символы исходного алфавита, на второй строке — символы конечного алфавита,
после чего идёт строка, которую нужно зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.

Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%

Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. Получаем следующие строки,
 которые и передаём на вывод программы:
*d*%*d*#*d*
dacabac

"""
# data = list(iter(input, ''))  будет считывать строки пока не введется пустая строка

date = []
while len(date) != 4:
    try:
        date.append(*input().split(sep="\n"))
    except:
        break

date_start, date_final, date_pack, date_unpack = date[0], date[1], date[2], date[3]
date = dict(zip(date_start, date_final))  # создается словарь, где из 1го списка берутся ключи, а со второго значения

for item in date_pack:
    print(date.get(item), end="")
print()

date = dict(zip(date_final, date_start))
for item in date_unpack:
    print(date.get(item), end="")
print()