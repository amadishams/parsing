"""
ФУНКЦИИ:
print()
input()
type()
int()
str()
float()
.title()
.capitalize()
.lower()
.upper()
.count() 0  количество вхождений
.find() -1
len


ТИПЫ ДАННЫХ:
str
int
float
bool # логический тип данных


ОПЕРАТОРЫ:
if, elif, else - операторы сравнения

"""

#str
a = 'Amadi'

#int
a = 1

#float
a = 1.5

#bool
a = 1==1

# 'Составное сравнение'
# print(1 == 1 and 1 > 0)
# print(1 != 1 and 1 > 0)
# print(1 != 1 or 1 > 0)
#
# if 1 == 1 and 1 > 0:
#     print("Done!")

#password = input("Введите пароль: ")

#if password == "12345":
#    print("Доступ открыт!")

# name1 = 'ahmad'
# name2 = 'hasan'
# name3 = 'ibragim'
#
# name = input("Введите имя: ")
#
# if name == name1 or name == name2 or name == name3:
#     print("Входите")
# else:
#     print("Вас нет в списке")

# if 1==1:
#     print("if")
# elif 2 == 2:
#     print("elif")
# else:
#     print("else")
#
# if 1 == 1:
#     print("if")
# if 2 == 2:
#     print("elif")
# else:
#     print("else")
#
# login = input("Введите логин: ").lower()
# password = input("Введите пароль: ")
# if login == "magomed" and password == "12345":
#     print("Добро пожаловать",login.title())
# elif login == "ibragim" and password == "0000":
#     print("Добро пожаловать", login.title())
# else:
#     print("Неправильный логин и пароль")

# True
"""
1 == 1
1
'txt'
"""

#False
"""
False
1 != 1
0
' '
"""

# txt = 'я изучаю язык программирования Python. Python универсальный язык'
# print(txt.count("Python"))
# print(txt.find("Python"))
# print(len(txt))

print("Сочифорния")
print("************")
n = input("Как вы оцениваете ваш отдых?")
result = n.find("хорошо")
x = result != -1
print('Отзыв хороший:', x)





