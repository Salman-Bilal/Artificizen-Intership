"""
Question: 1: Create a base class Animal with a speak() method, and Dog/Cat subclasses that override it.

"""

class Animal:
    def speak(self):
        return "The animal makes a generic sound."

class Dog(Animal):
    def speak(self):
        return "Bark, Bark!"

class Cat(Animal):
    def speak(self):
        return "Meow, Meow!"


my_animal = Animal()
my_dog = Dog()

print(my_animal.speak())
print(my_dog.speak())
