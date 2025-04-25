"""
Create a program that includes animals or vehicles with the same action
 (like move()).
   However, make each class define move()
     differently (for example, Car.move() prints "Driving" 🚗,
       while Plane.move() prints "Flying" ✈️).
"""

class Vehicle:
    def __init__(self):
        pass
    def move(self):
        return "Moving"
my_vehicle = Vehicle()
print(my_vehicle.move())

class Plane(Vehicle):
    def __init__(self):
        pass
    def move(self):
        return "Flying"
my_plane = Plane()
print(my_plane.move())

class Car:
    def __init__(self):
        pass
    def move(self):
        return "Driving"
my_car = Car() 
print(my_car.move())

