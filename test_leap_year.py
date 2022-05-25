# Магия
import calendar

year = list(range(1904, 3000, 4)) 
year_last = list(range(1903, 3000, 4)) 
year_next = list(range(1905, 3000, 4))
year_stab = list(range(1906, 3000, 4))
full_list = []
full_list2 =[]

# Определяем високосный ли год
x = int(input("year "))
if x in year:
	print(x, "Високосный год " + "\n" + "Повторение календаря: ")
else:
	print(x, "Обычный год "  + "\n" + "Повторение календаря: ")
if x in year_last: # для предвисокосного года
	i = x
	while i >= 1903:
		i = i - 6
		full_list2.append(i)
		i = i - 11
		full_list2.append(i)
		i = i - 11
		full_list2.append(i)
		continue
	full_list2.sort()
	
	x1 = x
	while x1 <= 2200:
		x1 = x1 + 11
		full_list.append(x1)
		x1 = x1 + 11
		full_list.append(x1)
		x1 = x1 + 6
		full_list.append(x1)
		continue
	joined_list = [*full_list2, x, *full_list]
	print(*joined_list, sep=", ")
	#print("1 января - пятница; 31 декабря - пятница")

if x in year_next: # для послевискосного года +
	i = x
	while i >= 1903:
		i = i - 11
		full_list2.append(i)
		i = i - 11
		full_list2.append(i)
		i = i - 6
		full_list2.append(i)
		continue
	full_list2.sort()

	
	x1 = x
	while x1 <= 2200:
		x1 = x1 + 6
		full_list.append(x1)
		x1 = x1 + 11
		full_list.append(x1)
		x1 = x1 + 11
		full_list.append(x1)
		continue
	joined_list = [*full_list2, x, *full_list]
	print(*joined_list, sep=", ")
	#print("1 января - пятница; 31 декабря - пятница")

if x in year_stab: # для регулярного года
	i = x
	while i >= 1903:
		i = i - 11
		full_list2.append(i)
		i = i - 6
		full_list2.append(i)
		i = i - 11
		full_list2.append(i)
		continue
	full_list2.sort()

	x1 = x
	while x1 <= 2200:
		x1 = x1 + 11
		full_list.append(x1)
		x1 = x1 + 6
		full_list.append(x1)
		x1 = x1 + 11
		full_list.append(x1)
		continue
	joined_list = [*full_list2, x, *full_list]
	print(*joined_list, sep=", ")
	#print("1 января - понедельник; 31 декабря - понедельник")

if x in year: # для вискосного года +
	i = x
	while i >= 1903:
		i = i - 28
		full_list2.append(i)
		continue
	full_list2.sort()

	x1 = x
	while x1 <= 2200:
		x1 = x1 + 28
		full_list.append(x1)
		continue
	joined_list = [*full_list2, x, *full_list]
	print(*joined_list, sep=", ", step=7)
	#print("1 января - среда; 31 декабря - четверг; (29 февраля - суббота)")

# Определяем день недели для 1 января
if calendar.weekday(x,1,1) == 0:
	print("1 января - понедельник")
elif calendar.weekday(x,1,1) == 1:
	print("1 января - вторник")
elif calendar.weekday(x,1,1) == 2:
	print("1 января - среда")
elif calendar.weekday(x,1,1) == 3:
	print("1 января - четверг")
elif calendar.weekday(x,1,1) == 4:
	print("1 января - пятница")
elif calendar.weekday(x,1,1) == 5:
	print("1 января - суббота")
elif calendar.weekday(x,1,1) == 6:
	print("1 января - воскресенье")

# Определяем день недели для 31 декабря
if calendar.weekday(x,12,31) == 0:
	print("31 декабря - понедельник")
elif calendar.weekday(x,12,31) == 1:
	print("31 декабря - вторник")
elif calendar.weekday(x,12,31) == 2:
	print("31 декабря - среда")
elif calendar.weekday(x,12,31) == 3:
	print("31 декабря - четверг")
elif calendar.weekday(x,12,31) == 4:
	print("31 декабря - пятница")
elif calendar.weekday(x,12,31) == 5:
	print("31 декабря - суббота")
elif calendar.weekday(x,12,31) == 6:
	print("31 декабря - воскресенье")

q1 = input(" Показать календарь на этот год? ")
if q1 == "да" or "Да" or "Yes" or "yes" or "+":
	calendar.prcal(x)
else:
	pass