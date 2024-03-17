"""
ФУНКЦИИ:
print()
input()
type()
title()
capitalize()
lower()
upper()

ТИПЫ ДАННЫХ:
str
int
float
bool # логический тип данных
"""

n = 1.5
print(1+4.5)
print(type(n))

x = 1
x = float(x)
n = 1.7
print(x)


n = int(n)
print(n)

x = 1
x1 = 1.5
x3 = '1'
x4 = '1.5'

x = float(x)
print(x)

x = str(x)
print(type(x))

x1 = int(x1)
print(x1)

x1 = str(x1)
print(type(x1))

x3 = int(x3)
print(type(x3))

x3 = float(x3)
print(x3)

x4 = float(x4)
print(type(x4))

x4 = int(x4)
print(x4)

"просто сравнение"
b = 1 ==1 #True Истина
print(b)
b2 = 1 != 1 # False Ложь
print(b2)
b3 = 1 > 0
print(b3)
b4 = 1 < 0
print(b4)
b5 = 1 >= 0
print(b5)
b6 = 1 <= 0
print(b6)
b7 = 'Yunus' == 'Magomed'
b8 = 'Yunus' != 'Magomed'
print(b8)
#b9 = 'Yunus' > 'Musa'
login = input("Введите логин")
password = input("Введите пароль")
print(login == 'Magomed')
print(password == '12345')

name = 'ahmad'
print(name.title())
name2 = 'Ahmad'
print(name2.lower())
print(name.capitalize())

txt = 'у меня есть друг Магомед'
print(txt.title())
print(txt.capitalize())
print(txt) #значение не сохраняются

txt2 = 'Я изучаю язык Python'
txt2 = txt2.title()
print(txt2)

name3 = 'ADAM'
name4 = 'adam'
print(name3.lower())
print(name4.upper())

n = input("Если согласны нажмите да:")
n = n.lower()
print(n == 'да')

n = input("Если согласны нажмите да: ").lower()
print(n == 'да')