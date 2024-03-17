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
dict (словарь) - это неупорядоченный, изменяемый пары ключ и значение

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

# 'dict это неупорядоченный, изменяемые пары ключ и значение'
# d = {}
# d2 = dict()
# print(type(d))
#
# test = {"yunus": "GELDABAEV", "musa": "js"}
# print(test['yunus'])
# test['python'] = "django" # добавить значения
# del test['yunus']
# print(test)
#
# n = ['a','b','c']
# n2 = {'a': 1,'b':2,'c':3}
# del n[0]
# del n2['a']

# books = {
#     'русский язык': [3,1],
#     'математика': [2,5],
#     'гарри поттер': [4,6]
# }
# while True:
#     ans = input("Что хотите?").lower()
#     if ans in books:
#         info = books[ans]
#         print("Ряд", info[0])
#         print("Полка", info[1])
#     else:
#         print("Такой книги нет, хотите заказать?")
#         var = input("")
#         if var == "да":
#             polka = int(input("Введите полку"))
#             ryad = int(input("Введите ряд"))
#             books[ans] = [polka,ryad]
#         print(books)


# vhod = input("1 - Войти\n2- Зарегистрироваться")


# if vhod == 1:
#     print("Добро пожаловать")

"""
1) создать базу данных изпользую dict, где есть имя, пароль, возраст
2) создать меню где есть выбор 1 Войти, 2 Зарегистрироваться
3) При нажатии 1 нас пропускает и выводим его имя, пароль и возраст если мы есть в нашей базе данных, иначе выводим вы не зарегистрированы
4) При нажатии 2 мы запрашиваем ввод логина, пароля и возраста и вносим эти данные в нашу базу данных
"""

db = {
    'yunus': ['12345',27],
    'ahmad': ['123456',32]
}
vhod = input("1 - Войти\n2 - Зарегистрироваться")
if vhod == "1":
    name = input("Введите имя")

    if name in db:
        print("Добро пожаловать")
    else:
        print("Вы не зарегистрированы")

if vhod == "2":
    login = input("Введите логин")
    password1 = input("Введите пароль")
    age1 = input("Введите возраст")
    db[login] = [password1,age1]
    print(db)

# while True:
#     if i in db:
#         print("")
