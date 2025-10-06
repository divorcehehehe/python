class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person('Иван', 25)
person.age = -100
