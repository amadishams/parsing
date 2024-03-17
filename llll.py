# n = 0
# for i in 'yunus':
#     print(n, i)
#     n += 1

# for i in range(2, 10, 2):
#     print(i)
# for _ in range(5):
#     print('hello')
# for i in ['ahmad', 'islam', 'isa']:
#     print(i)
# url = 'https://www.avito.ru/groznyy/velosipedy/gornye-ASgBAgICAUS4AqgK?p=2'
#
# for i in range(1, 10):
#     print('https://www.avito.ru/groznyy/velosipedy/gornye-ASgBAgICAUS4AqgK?p=' + str(i))

# n2 = ['1', '2']
# n3 = "".join(n2)
# print(n3)



# txt2 = 'Я изучаю язык Python. Python это язык программирования'
# #  взять слово Python через срезы
# print(txt2[14:20])
#
# txt3 = 'Я изучаю dfgfdgdfgdfgdязык Python. Python это язык программирования'
# #  взять слово Python через срезы внезависимо от того меняется ли текст или нет
# a = txt3.find("Python")
# b = len("Python")
# print(txt3[a:a+b])
#
#
# url = 'https://www.avito.ru/groznyy/velosipedy/gornye-ASgBAgICAUS4AqgK?p=176'# через split
# a = url.split("=")
# b = a.remove("176")
# print(a[0]+"=")

url = 'https://www.avito.ru/groznyy/velosipedy/gornye=ASgBAgICAUS4AqgK?p=176'# = = если в url 2 равно
a = url.split("=")
ab = a.remove("176")
b = "=".join(a)+'='
print(b,)


# url = 'https://www.avito.ru/groznyy/velosipedy/gornye-ASgBAgICAUS4AqgK?p=176'  # без split, через find
# a = url.find("=")
# print(url[0:a]+"=")

# log = "amadi"
# passw = 123456
#
# for _ in range(3):
#     login = input("введите логин")
#     password = int(input("введите пароль"))
#     if login == log and password == passw:
#         print("Добро пожаловать")
#        *
#     else:
#         print("неверно")
# else:
#     print("попытки исчерпаны")

# books = {
#     'русский язык': [3,1],
#     'математика': [2,5],
#     'гарри поттер': [4,6]
# }
#
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

"""
1) создать базу данных изпользую dict, где есть имя, пароль, возраст
2) создать меню где есть выбор 1 Войти, 2 Зарегистрироваться
3) При нажатии 1 нас пропускает и выводим его имя, пароль и возраст если мы есть в нашей базе данных, иначе выводим вы не зарегистрированы
4) При нажатии 2 мы запрашиваем ввод логина, пароля и возраста и вносим эти данные в нашу базу данных
"""

# db = {
#     'yunus': ['12345',27],
#     'ahmad': ['123456',32]
# }
# while True:
#     vhod = input("1 - Войти\n2 - Зарегистрироваться")
#
#     if vhod == "1":
#         name = input("Введите имя")
#         passw = input("Введите пароль")
#         if name in db:
#             passwdb = db[name][0]
#             if passw == passwdb:
#                 print("Добро пожаловать")
#             else:
#                 print("Вы не зарегистрированы")
#         else:
#             print("Вы не зарегистрированы")
#
#     if vhod == "2":
#         login = input("Введите логин")
#         password1 = input("Введите пароль")
#         age1 = input("Введите возраст")
#         db[login] = [password1,age1]
#         print(db)

# text = ['1', '2', '3', ['4', '5'], {'6':'7', '8': ['9','python']}]
# a = (text[-1])
# b = (a['8'])
# print(b[-1])

# n = "amadi"
# p = 1234
#
# for i in range(1,4):
#     print("Попытка номер:", i)
#     name = input("Введите логин")
#     password = int(input("Введите пароль"))
#     if name == n and password == p:
#         print("Добро пожаловать")
#         break
#     else:
#         print("ошибка")


# def test(a, b, c):  # a - параметр функции
#     if c == "+":
#         return a + b
#     elif c == "-":
#         return a - b
#     elif c == '/':
#         return a / b
#     else:
#         print("Неправильный ввод!!!")
#
# x = test(10, 2, "/")
# print("Ответ:", x)
#
#
# x = 1
# def test2():
#     'локальная область видимости'
#     x = 2
#     return x
# print(x)
#
# n = test2()
# print(n, '<<')
#
# def test(a, b):  # a - параметр функции
#     print('Ответ', a+b)
# test(5,6)

# def test(a, b, c):  # a - параметр функции
#     if c == "+":
#         return a + b
#     elif c == "-":
#         return a - b
#     elif c == '/':
#         return a / b
#     else:
#         print("Неправильный ввод!!!")

# n = 1
#
#
# def test(a):
#     print(a)
#     n = 2
#     return n
#
#
# x3 = test(10)
# print(x3, "<<")
#
# x = print(n)
# x2 = len("musa")
# print(x2)

# x = len("python")
# x2 = print("python")
# print(x2)
# if x2:
#     print("*")

# def test():
#     print('test func')
#     len("python")
#
#
# x3 = test()
# print(x3)

# def test(number, discount):  # параметр функции
#     print("Цена без скидки", number)
#     print("Вам скидка:", discount, "%")
#     result = (number / 100) * discount
#     print("Итог после скидки:", number - result)


# def test2(price):
#     x = 0
#     if price > 1000 and price < 5000:
#         x = 10
#     elif price > 5000:
#         x = 20
#     else:
#         x = 0
#     return x
#
#
# price = int(input("Введите цену покупок: "))
# x = test2(price)
# print("Ваша скидка:", x)

# test2(price, x)  # аргумент функции


# def name(x): # параметр функции
#     x = 0
#     if x > 0:
#         name = 10
#     elif x < 0:
#         name = 1
#     return name
#
# a = int(input("Введите число"))
# b = name(a) #аргумент функции
# print(b)

# def calcu(a,b,x):
#     calc = 0
#     if x == "+":
#         calc = a + b
#     if x == "-":
#         calc = a - b
#     if x == "*":
#         calc = a * b
#     if x == "/":
#         calc = a / b
#     else:
#         print("Неправильный знак")
#     print(calc)
#
# a = int(input("Введите число"))
# b = int(input("Введите число"))
# x = input("Введите знак")
# calcu(a,b,x)