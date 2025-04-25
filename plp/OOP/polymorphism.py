class Animal:
    def speaks(self):
        return "This animal produced a sound"

class Cat(Animal):
    def speaks(self):
        return "Cat says meow!! "
class Dog(Animal):
    def speaks(self):
        return "Dog says Bark!! "

for animal in [Animal(),Cat(),Dog()]:
    print(animal.speaks())