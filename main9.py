print()
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
.split('value') разделяет на указанное значение
" ".join(list)  объеденяет на указанный символ
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
break
continue

txt[0] индексация
txt[0:4] срезы

'Цикл'
while
for i in 'test' / for i in range(5)
"""

# print("1","2","3")
# input("1 2 3")
#
# n = ['a','b']
# n.remove('b')
# del n[0]

# log = "amadi"
# passw = 123456
#
# for _ in range(3):
#     login = input("введите логин")
#     password = int(input("введите пароль"))
#     if login == log and password == passw:
#         print("Добро пожаловать")
#         break
#     else:
#        print("неверно")
# else:
#       print("попытки исчерпаны")


url = 'https://www.avito.ru/groznyy/velosipedy/gornye-ASgBAgICAUS4AqgK?p=176'  # без split, через find
a = url.find("=")
b = len(url)
# a = 1
# b = 2
print(url[a:])
# split()
# .join()
