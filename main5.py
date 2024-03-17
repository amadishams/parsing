
"""
'Функции'
print()
input()
int()
float()
str()
.title()
.capitalize()
.lower()
.upper()
type()
.count()
.find()
len()
.append("Значение")  добавить значение в список
.extend(list)  добавть значения списка в новый список
.remove("Значение")  удалить занчение из списка по имени





name = 'Ahmad'

'Типы данных'
str
int
float
bool (True, False)
list

'Опреторы'
if, elif, else  операторы сравнения
del list[0]  удить заначение из списка по индексу  (del оператор)

'Цикл'
while

"""

n = 'yunus musa'
print(n.capitalize())

'Простое сравнение'
print(1 == 1)
print(1 != 1)
print(1 > 0)
print(1 < 0)
print(1 >= 1)
print(1 <= 1)

'Составное сравнение'
print(1 == 1 and 1 > 0)
print(1 != 1 and 1 > 0)
print(1 != 1 or 1 > 0)
x = 1 == 1
print(x)

if 1 == 1 and 1 > 0:
    print("Done!")

# password = input("Введите пароль: ")
#
# if password == "12345":
#     print("Доступ открыт!")
#
# name1 = 'ahmad'
# name2 = 'hasan'
# name3 = 'ibragim'
#
# name = input("Введите имя: ")
# if name == name1 or name == name2 or name == name3:
#     print("Входите!")
# else:
#     print("Вас нет в списке")


if 1 == 1:
    print("if")
elif 2 == 2:
    print("elif")
else:
    print("else")

if 1 == 1:
    print("if")
if 2 == 2:
    print("elif")
else:
    print("else")

"""
1) Запрашиваем логин и пароль
2) Если логин это magomed и пароль 12345, то выводим Добро пожадовать Магомед
3) А если это ibragim и пароль 0000, то выводим Добро пожаловать Ибрагим
4) Иначе выводим "Неправильный логин или пароль!"

"""
# n = 'a'
# n = int(n)

txt = 'Я изучаю язык программирования Python. Python иниверсальный язык'
print(txt.count("Python"))
print(txt.find("bdxfbdf"))
print(len(txt))

print("Сочифорния")\



print("****************")
# n = input("Как вы оцениваете ваш отдых? ")
# result = n.find("хорошо")
# x = result != -1
# print("Отзыв хороший:", x)


# True
"""
True
1 == 1
1
'txt'
"""

# False
"""
False
1 != 1
0
''
"""

txt = 'я изучаю Python js'
print(txt[-2])  # индексация
a = txt.find("Python")
b = len("Python")
print(a)
print(b)
print(txt[a:a+b])  # срез

# document =  """Запрашиваем логин и пароль
# 2) Если логин это magomed и пароль 12345, то выводим Добро пожадовать Магомед
# 3) А если это ibragim и пароль 0000, то выводим Добро пожаловать Ибрагим
# 4) Иначе выводим Неправильvdsfv jvsdfhnvjный логин или пароль!
# Запрашиваем логин и vdsf vvsdv пароль
# 2) Если логин это magomed и пароль 12345, то выводим Добро пожадовать Магомед
# 3) А если это ibragim и пароль 0000, то выводим Добро пожаловать Ибрагим
# 4) Иначе выводим Неправильный password логин или пароль!
# Запрашиваем логин и пароль
# 2) Если логин это magomed и пароль 12345, то выводим Добро пожадовать Магомед
# 3) А если это ibragim и пароль 0000, то выводим Добро пожаловать Ибрагим
# 4) Иначе выводим Неправильный логин или пароль!
# """
#
# x = document.find("password")
# print(x[1:33])

x = ['Юнус', 12345, [123, "Ахьмад"]]
print(type(x))
print(x[2][0])

names = ['magomed', 'hasan', 'isa', 'hamad']
names.append('hava')

names.remove('hasan')
del names[0]
print(names)
"""list - это упорядоченный, изменяемый тип данных"""

a = [1, 2, 3]
b = [4, 5, 6]
# a.append(b)
# a.extend(b)
print(a)

n = '012345'
n2 = [0, 1, 2, 3, 4, 5]
print(n[0:3])
print(n2[0:3])
n = len("yunus")
print(n)

n = 0
while n < 5:
    print("hello")
    n = n + 1

# while 3 == 3:
#     print("welcome")

password = 3324534

#УЗНАТЬ ПАРОЛЬ
test_password = 0
# while
if password == test_password:
    print("Добро пожаловать!")
else:
    print("Неправильно")
