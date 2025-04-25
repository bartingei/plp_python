class Car:
    def __init__(self, color, speed, model):
        self.color = color
        self.speed = speed
        self.model = model

    def drive(self):
        print("Car starts! ")

    def showInfo():
        print(f'Car ')

car1 = Car("red", 320, "GTR")
car2 = Car("black", 230, "Audi")

print("color",car1.color)
print("speed", car2.speed)
my_car = Car("blue", 190, "subaru")
print("model", my_car.model,"color",my_car.color)
my_car.drive()