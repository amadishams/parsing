"""x = 1 == 1
True
"text"
1"""

"""
False
1 != 1
""
0
None
"""


# while 1 == 1:
#     print("while")
#     continue
#
# for _ in 'python':
#     print("hello")

# for i in range(1, 10, 2):
#     print(i)

# x = len("python")
# x2 = print("python")
# print(x2)
# if x2:
#     print("*")
#
#
# def test():
#     print('test func')
#     len("python")
#
#
# x3 = test()
# print(x3)


"""Области видимости"""

def test(number, discount):  # параметр функции
    print("Цена без скидки", number)
    print("Вам скидка:", discount, "%")
    result = (number / 100) * discount
    print("Итог после скидки:", number - result)


def test2(price):
    x = 0
    if price > 1000 and price < 5000:
        x = 10
    elif price > 5000:
        x = 20
    else:
        x = 0
    return x


price = int(input("Введите цену покупок: "))
x = test2(price)
test(price, x)  # аргумент функции


