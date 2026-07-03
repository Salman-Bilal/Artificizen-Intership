"""
Question: 1: Create a Car class with attributes (brand, model, year) and a method that displays the car’s info.

"""

class Car:
    def __init__(self, brand, model, year):
        self.brand  = brand
        self.model = model
        self.year = year

    def INFO_Printer(self):
        print(f"The Brnad of Car is: {self.brand}")
        print(f"The Model of the Car is: {self.model}")
        print(f"This Car Launch in: {self.year}")


my_car = Car("BMW", "I8", "2025")

my_car.INFO_Printer()
