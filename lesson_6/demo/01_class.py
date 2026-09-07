# класс, объект, __init__, методы


class Dog:          # имя класса с большой буквы
    def __init__(self, name, age):
        self.name = name    # атрибут объекта
        self.age = age

    def bark(self):
        return f'{self.name}: гав!'

    def birthday(self):
        self.age += 1       # метод меняет состояние


bobik = Dog('Бобик', 3)
rex = Dog('Рекс', 5)

print(type(bobik))
print(bobik == rex)         # без __eq__ это разные объекты
print(bobik.bark())
bobik.birthday()
print(bobik.age, rex.age)
