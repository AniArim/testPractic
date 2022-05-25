"""
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла. Первое слово в тексте
последнего файла: "We". Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.
Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/
Загрузите содержимое последнего файла из набора, как ответ на это задание.
"""

import requests


try:
    with open("lesson.txt", "r", encoding="utf-8") as file:
        url_start = file.read().strip()
except:
    pass

r = requests.get(url_start)
url_base = "https://stepic.org/media/attachments/course67/3.6.3/"
i = 0 # Счетчик итераций из любопытства
while "We" not in r.text:
    url_next = url_base + r.text
    r = requests.get(url_next)
    i += 1
print(r.text)
print("Итераций", i)

