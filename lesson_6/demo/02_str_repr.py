# __str__ для человека, __repr__ для отладки


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Пёс {self.name}, возраст {self.age}'

    def __repr__(self):
        return f"Dog('{self.name}', {self.age})"


bobik = Dog('Бобик', 3)
rex = Dog('Рекс', 5)

print(bobik)                # берёт __str__
print(f'В гостях: {bobik}')  # f-строка тоже берёт __str__
print([bobik, rex])         # список берёт __repr__
