""" СОЗДАНИЕ ФУКНКЦИИ
def
name
()
:
a,b
return
"области видимости"

"""



def test(a, b):  # a - параметр функции
    print('Ответ', a+b)
test(10, 20)



'Глобальная обсласть видимости'
x = 1

def test2():
    'локальная область видимости'
    x = 2
    return x
print(x)

n = test2()
print(n, '<<')


def test(a, b, c):  # a - параметр функции
    if c == "+":
        return a + b
    elif c == "-":
        return a - b
    elif c == '/':
        return a / b
    else:
        print("Неправильный ввод!!!")

x = test(10, 2, "/")
print("Ответ:", x)
