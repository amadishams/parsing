# import model
# model.calc(1,2,"+")
#
# from model import vhod
# vhod("amadi",12345)

from package.model import test
from package.test_model import circle

# from package import test2, circle
#
# test2(1,2)
# circle()

class Calcu:
    def __init__(self):
        print("Калькулятор")

    def plus(self, a,b):
        print(a+b)

    def minus(self, a,b):
        print(a-b)

class Calc(Calcu):
    def __init__(self):
        super().__init__()

    def umn(self,a,b):
        print(a*b)

    def razd(self, a, b):
        print(a/b)

x = Calc()
x.minus(5,1)

"""
Типы данных
Функции
Циклы
Условные операторы
Классы (унаследование)
Пакеты и модули
"""

try:
    print(1+'5')
except:
    print(1+5)