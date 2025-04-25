"""
Assignment 1: Design Your Own Class! 🏗️
Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
Add attributes and methods to bring the class to life!
Use constructors to initialize each object with unique values.
Add an inheritance layer to explore polymorphism or encapsulation.
"""
class Superhero:
    def __init__(self, name, age, powers, city):
        self.__name = name
        self.age = age
        self._power = powers
        self.city = city

    def get_name(self):
        return self.__name

class Person(Superhero):
    def __init__(self, name, age, powers, city, cover_job):
        super().__init__( name, age, powers, city)
        self.cover_job = cover_job

p1 = Person("Superman", 35,"Everything","Star City", "journalist")

print(p1.get_name())    