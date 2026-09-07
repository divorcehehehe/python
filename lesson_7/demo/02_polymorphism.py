# Полиморфизм: один вызов speak(), разное поведение
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return '...'

    def __str__(self) -> str:
        return f'{self.name}: {self.speak()}'


class Dog(Animal):
    def speak(self) -> str:
        return 'Гав'


class Cat(Animal):
    def speak(self) -> str:
        return 'Мяу'


class Robot:
    """Не наследник Animal, но метод speak() у него есть: этого достаточно."""

    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return 'Бип'

    def __str__(self) -> str:
        return f'{self.name}: {self.speak()}'


# в списке лежат объекты разных классов, цикл об этом не знает
for creature in [Dog('Шарик'), Cat('Мурка'), Robot('Робот'), Animal('Некто')]:
    print(creature)

print(isinstance(Dog('Рекс'), Animal))
print(isinstance(Robot('Жестянка'), Animal))
