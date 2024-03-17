try:
    n = int(input("Введите первое число"))
    n2 = int(input("Введите второе число"))
except:
    n = 0
    n2 = 0
    print("введи число")
else:
    print("вы ввели число!!!")
finally:
    print(n + n2)