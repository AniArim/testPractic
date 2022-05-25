"""
Напишите программу, которая считывает из файла строку, соответствующую тексту,
сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.
Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

Sample Input:
a13b4c2e10b1
Sample Output:
aaabbbbcceeeeeeeeeeb
"""
line = input()
line_final = []
i = 0  # индекс item
j = i + 1  # индекс count_

for item in line:
    if item.isalpha():
        if j < len(line) - 1:
            if line[j].isdigit() and line[j+1].isalpha():
                line_final.append(line[i] * int(line[j]))
                i += 2
                j = i + 1
            elif line[j].isdigit() and line[j+1].isdigit():
                line_final.append(line[i] * int(line[j] + line[j+1]))
                i += 3
                j = i + 1
        if j == len(line) - 1:
            line_final.append(line[i] * int(line[j]))
    if item.isdigit():
        pass

line2 = "".join(line_final)
try:
    with open("lesson.txt", "w") as file:
        file.write(f"{''.join(line_final)}\n")
except:
    pass