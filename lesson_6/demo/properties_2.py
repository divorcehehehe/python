class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        print('Вызван getter возраста')
        return self.__age

    @age.setter
    def age(self, value):
        print('Вызван setter возраста')
        if value < 0:
            raise ValueError('Возраст не может быть отрицательным')
        self.__age = value


person = Person('Анна', 30)
print(person.age)
person.age = 25
print(person.age)
# person.age = -5   # уберите комментарий: сразу ValueError
