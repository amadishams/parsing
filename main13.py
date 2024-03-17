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
.items()
.values()
.keys


name = 'Ahmad'

'Типы данных'
str
int
float
bool (True, False)
list список
tuple (кортеж) - неизменяемый, упорячдоченгный тип данных
dict (словарь) - это неупорядоченный, изменяемый пары ключ и значение
set (множество) - это неупорядоченный, изменяемы тип данных

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

"set (множество) - это неупорядоченный, изменяемы тип данных"
# s = {'python','python'}
# print(type(s))
# s.add('django')
# s.remove('python')
# print(s)
#
# x1 = {1,2}
# x2 = {2,3}
# q = x1.union(x2)
# q2 = x1.intersection(x2)
# q3 = x1.difference(x2)
# q4 = x1.symmetric_difference(x2)
# print(q4)
#
#
# mat = {'мат1','мат3','мат3'}
# msg = {'мат1'}
# x = mat.intersection(msg)
# if x:
#     print("сообщение удалено")

# block = {'мат1','мат2','мат3'}
# messages = set()
# while True:
#     msg = input("Введите сообщение: ")
#     messages.add(msg)
#     if msg in block:
#         messages.remove(msg)
#         print('Сообщение удалено')
#     print(messages)

x1 = [1, 2]
x2 = list([1, 2])

x3 = ()
x4 = tuple([1, 2])
print(type(x4))

x5 = {}
x6 = dict()

x7 = {1}
x8 = set(x7)
'******************************'

x = [1,[2,3]]
print(x[1][0])
x.append(4)
x[1].remove(3)
print(x)
del x[1][0]
print(x)

'******************************'

x = ('1','2')
x2 = ('3','4')
x3 = x + x2
print(x3)

x = [1,2,(3,4)]
x2 = (1,2,[3,4])

x = {'a': 'b'}
print(x['a'])
x['d']='g'
print(x)
del x['a']
print(x)