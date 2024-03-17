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
tuple (кортеж) - неизменяемый, упорячдоченгный тип данных
dict (библиотека) - это неупорядоченный, изменяемый пары ключ и значение

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

True
1==1
1

False
1 !=1
0
''
"""


# login = input('Введите логин')
# password = input('Введите пароль')
#
# while login != 'adam' or password != '12345':
#     login = input('Введите логин')
#     password = input('Введите пароль')
# print("Добро пожаловать")



# n = ()
# "***************"
# n2 = ('yunus',)
# "***************"
# n3 = 'yunus',
# n4 = 'musa','ibragim'
# print(type(n))

a = (1,2)
b = (3,4)
c = a + b
print(c)
print(a)
print(b)
#
# a = (1,2,3)
# # x = a + 4,5 error
# x = a + (4,5)
# print(x)