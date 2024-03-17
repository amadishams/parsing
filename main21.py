# def calc(a,b,c):
#     if c == "+":
#         calc = a + b
#     elif c == "-":
#         calc = a - b
#     elif c == "/":
#         calc = a / b
#     elif c == "*":
#         calc = a * b
#     else:
#         calc = "Ошибка"
#     print(calc)
# calc(1,2,"+")
#
#
# class Calcu:
#     def __init__(self, a, b, x):
#         self.a = a
#         self.b = b
#         self.x = x
#         self.main()
#
#     def plus(self):
#         print("Ответ: ", self.a + self.b)
#
#     def minus(self):
#         print("Ответ: ", self.a - self.b)
#
#     def umn(self):
#         print("Ответ: ", self.a * self.b)
#
#     def razd(self):
#         print("Ответ: ", self.a // self.b)
#
#     def main(self):
#         if self.x == "+":
#             self.plus()
#         elif self.x == "-":
#             self.minus()
#         elif self.x == "*":
#             self.umn()
#         elif self.x == "/":
#             self.razd()
#
# # a = int(input("Введите первое число: "))
# # b = int(input("Введите второе число: "))
# # x = int(input("Введите знак: "))
# # t = Calcu(a, b, x)
#
# class CalcProf:
#     def __init__(self, a, b, x):
#         self.a = a
#         self.b = b
#         self.x = x
#         self.main()
#
#     def plus(self):
#         print("Ответ: ", self.a + self.b)
#
#     def minus(self):
#         print("Ответ: ", self.a - self.b)
#
#     def umn(self):
#         print("Ответ: ", self.a * self.b)
#
#     def razd(self):
#         print("Ответ: ", self.a // self.b)
#
#     def step(self):
#         print("Ответ: ", self.a ** self.b)
#
#     def main(self):
#         if self.x == "+":
#             self.plus()
#         elif self.x == "-":
#             self.minus()
#         elif self.x == "*":
#             self.umn()
#         elif self.x == "/":
#             self.razd()
#         elif self.x == "**":
#             self.step()
#
# class CalcProf(Calcu):
#     def __init__(self,a,b,x):
#         super().__init__(a,b,x)
#
# c = CalcProf(2,2,"*")
#
#
# class Test2:
#     def get_name(self, x):
#         print(x)
#
# Test2().get_name(1)

"""
создать класс Animal
1 - цвет
2 - голос
3 - имя
4 - жизнь

class Animal:
    def __init__(self, color, golos, name, hp):
        pass

cat = Animal(color: "Черный")
dog = Animal()
xx = Animal
"""

class Animal:
    def __init__(self, name, color, golos, hp):
        self.name = name
        self.color = color
        self.golos = golos
        self.hp = hp

    def eat(self, n):
        if n:
            self.hp += n
            print("ням-ням")
        else:
            if not self.hp-5 < 0:
                self.hp -= 5
                print(self.golos)
            else:
                self.hp = 0

    def status_hp(self):
        if self.hp <=20:
            print(self.golos * 3)
        if self.hp <= 0:
            print("Ваш питомец погиб")

            return 1


    def info(self):
        print("Имя:", self.name)
        print("Жизнь:", self.hp)

# cat = Animal("Симба","Черный","Мяу", 9)
#
# while True:
#     cat.info()
#     answer = input("Хотите покормить питомца?").lower()
#     if answer == "да":
#         cat.eat(5)
#     else:
#         cat.eat(0)
#     x = cat.status_hp()
#     if x:
#         break
# print("Конец игры!!!")




class Banc():
    def __init__(self, name, balance):
        self.balance = balance
        print("Вас приветсвует банк", name)

    def plus(self):
        x = int(input("Введите сумму: "))
        self.balance += x
        print("Ваш баланс пополнен на: ", x )

    def minus(self):
        x = int(input("Введите сумму для вывода: "))
        if self.balance >= x:
            self.balance -= x
            print("Вы взяли: ", x)
        else:
            print("Недостаточно средств")

    def status(self):
        print("Ваш счет: ", self.balance)

    def info(self):
        print("Ваш баланс:", self.balance)

banc = Banc("Сбербанк", 10000)

while True:
    a = input("1-посмотреть баланс\n2-вывести деньги\n3-пополнить счет\nВаш выбор: ")
    if a == "1":
        banc.info()
    elif a == "2":
        banc.minus()
    elif a == "3":
        banc.plus()
    x = banc.status()
    if x:
        break