"""
Question: 4:

"""
# Task 4: Private Attributes using @property


class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    
    @property
    def price(self):
        return self._price

    
    @price.setter
    def price(self, new_value):
        if new_value < 0:
            print("Error: Price cannot be negative!")
        else:
            self._price = new_value





item = Product("Keyboard", 100)

print("Current Price of Keyboard:", item.price)


item.price = -50


item.price = 150
print("Updated Price of Keyboard:", item.price)