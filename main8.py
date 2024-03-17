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

"""
txt = 'Я изучаю язык Python'
print(txt[-1])
print(txt[0:4])
print(txt[:4])
print(txt[3:])
a = 1
b = 3
print(txt[a:b])

n = 0
for i in 'yunus':
    print(n, i)
    n += 1

# for i in range(5):
# for i in range(2, 10):
for i in range(2, 10, 2):
    print(i)

for _ in range(5):
    print('hello')

for i in ['ahmad', 'islam', 'isa']:
    print(i)

# 1
url = 'https://www.avito.ru/groznyy/velosipedy/gornye-ASgBAgICAUS4AqgK?p=2'

for i in range(1, 10):
    print('https://www.avito.ru/groznyy/velosipedy/gornye-ASgBAgICAUS4AqgK?p=' + str(i))
# 2
url = 'https://www.avito.ru/groznyy/velosipedy/gornye-ASgBAgICAUS4AqgK?p=176'  # без split, через find
# find()
# len()
# a = 1
# b = 2
# print(url[a:b])
# split()
# .join()

# 3
url = 'https://www.avito.ru/groznyy/velosipedy/gornye-ASgBAgICAUS4AqgK?p=176'  # через split

# 4
url = 'https://www.avito.ru/groznyy/velosipedy/gornye=ASgBAgICAUS4AqgK?p=176'  # = = если в url 2 равно

txt2 = 'Я изучаю язык Python. Python это язык программирования'
#  взять слово Python через срезы
print(txt2[14:20])

txt3 = 'Я изучаю язык Python. Python это язык программирования'
#  взять слово Python через срезы внезависимо от того меняется ли текст или нет
a = txt3.find("Python")
b = len("Python")
print(txt3[a:a+b])


n = 'yunus'
print(n.split("n"))
n2 = ['1', '2']
n3 = "|".join(n2)
print(n3)

