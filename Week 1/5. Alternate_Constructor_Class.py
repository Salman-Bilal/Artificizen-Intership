"""
Question: 5: Add a @classmethod to a Person class that works as an alternate constructor, e.g. Person.from_birth_year(name, year).

"""


class Person:

    # Standard Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Alternate Constructor
    @classmethod
    def from_birth_year(cls, name, birth_year):
        calculated_age = 2026 - birth_year
        return cls(name, calculated_age)




p1 = Person("Asif", 25)

p2 = Person.from_birth_year("Ali", 2000)

print("Person 1 Age:", p1.age)
print("Person 2 Age:", p2.age)