"ООП - Обьектно-орриентированное программирование"
"class"

"""
Наследование
Полиморфизм
Инкапсуляция
"""
#
# class TestName:
#
#     def __init__(self): # магический метод, (конструктор)
#         name = 'yunus' # свойства класса
#         age = 20
#         self.name = name
#         self.age = age
#         print("Я функция __init__")
#     def test(self): # метод (дейстие)
#         print("Я функция test")
#
#     def test2(self): # метод (дейстие)
#         print("Я функция test2")
#
# n = TestName() # экземпляр класса
# n.test()
# n.test2()


class Banc:
    def __init__(self, name_banc, name_user, summa):
        print("Добрый день", name_user.title())
        self.name_banc = name_banc
        self.name_user = name_user
        self.summa = summa

    def plus(self, n):
        self.summa += n
        print("Ваш счет пополнен на", str(n) + 'р.')

    def minus(self, a):
        self.summa -= a
        print("Возьмите пожалуйста деньги", str(a) + 'р.')

    def info(self):
        print(self.name_banc.upper())

        print("Ваш счет:", self.summa)

sber = Banc("Сбербанк","Магомед", 0)
# tinkoff = Banc("Тинькофф","Ибрагим",
#                0)
# tinkoff.info()
while True:
    # sber.info()
    x = int(input('Введите сумму:'))
    #
    sber.plus(x)
    sber.info()

    z = int(input("Введите сумму: "))
    sber.minus(z)
    sber.info()

