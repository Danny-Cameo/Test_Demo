from __future__ import annotations
from datetime import date

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name: str, birthYear: int) -> Person:
        return cls(name, date.today().year - birthYear)

    def __repr__(self) -> str:
        return f"{self.name}'s age is: {str(self.age)}"

person = Person('Adam', 19)
print(person)

person1 = Person.fromBirthYear('John',  1985)
print(person1)
