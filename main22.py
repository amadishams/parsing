class Car():
    def __init__(self, model, color, speed, oil):
        self.model = model
        self.color = color
        self.speed = speed
        self.oil = oil

    def zapr(self):
        x = int(input("На сколько вы хотите заправиться?: "))
        self.oil += x

    def rashod(self):
        self.oil -= 1

    def main(self):
        print("Модель",self.model,"\n""Цвет",self.color,"\n""Скорость",self.speed,"\n""бензин",self.oil,"\n")

car = Car("Мерседес","черный",100,10)
while True:
    a = input("1-заправить\n2-общая информация")
    if a == "1":
        car.zapr()
    if a == "2":
        car.main()
    car.rashod()


