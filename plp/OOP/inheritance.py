class Vehicle:
    def __init__(self, doors, color, model, wheels):
        self.doors = doors
        self.color=color
        self.model = model
        self.wheels = wheels

class Car(Vehicle):
    def __init__(self,doors, color, model, wheels, origin_country):
        super().__init__( doors, color, model, wheels)
        self.origin_country = origin_country

my_car = Car(2,"red","Toyota", 4,"Japan")
print(my_car.model)


class Person:
    def __init__(self, gender, name, age):
        self.gender = gender
        self.name = name
        self.age = age

class Baby(Person):
    def __init__(self, gender, name, age,speaks):
        super().__init__(gender, name, age)
        self.speaks = speaks

my_baby = Baby("Male", "Johnpaul", 2,"not yet")
print(my_baby.speaks)