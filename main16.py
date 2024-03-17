
names1 = [1, 2, 3, 4, 'python']

names2 = names1
names1.remove('python')

print(names2)

n = 1


def test(a):
    print(a)
    n = 2
    return n


x3 = test(10)
print(x3, "<<")

x = print(n)
x2 = len("musa")
print(x2)

def get_name(name, age=False):
    print('Имя:', name)
    if age:
        print("Возраст:", age)


get_name('Yunus')

"""
True
1
1 == 1

False
0
''
1 != 1
"""


def names(*args):  # *args копит в себе занчения
    print(*args)

names('yunus', 'musa', 'hasan')


def names(a):
    print(a)
# если функция принимает только один аргумент, то можно
# туда передать нельколько занчение ввиде кортежа или списка
names(('yunus', 'musa', 'hasan'))

# целый список считается как один элемент
x = [1, 2, 3, 4, 5, ['yunus', 'hasan', 'isa']]
print(x[5])

print(*x)

a = [1, 2]
b = [*a, 3, 4]  # распаковка
print(b)

# def names(**kwargs):


"""
1) Создать меню ввиде отдельной функции
        Меню содержить:
            1) Зарегистрироваться
            2) Войти
2) Если выбрал 1, то отдельная функция для запроса:  
            1. Логин, 2. Пароль, 3. Возраст
3) Если выбрал 2, то отдельная функция для запроса:
            1. Логин, 2. Пароль
"""

def get_menu():
    number = input("1) Зарегистрироватья\n2) Войти\nВаш выбор: ")
    return number


def register():
    print("Регистрация")
    login = input("Введите логин: ")
    password = input("Введтие пароль: ")
    age = input("Введите возраст: ")
    return login, password, age


def log_in():
    print("Вход")
    login = input("Введите логин: ")
    password = input("Введтие пароль: ")
    return login, password


def boolean(n):
    if n == '1':
        register()
    elif n == '2':
        log_in()
    else:
        print("Неправильный ввод!")


# x = get_menu()
# boolean(x)


def xxx():
    n = 10
    print("1111111111")
    return n
    print("hello")  # после return программа дальше не идет

xxx()
