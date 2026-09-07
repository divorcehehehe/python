# Наследование: Bike и Scooter берут всё от Transport
class Transport:
    def __init__(self, name: str, wheels: int):
        self.name = name
        self.wheels = wheels

    def info(self) -> str:
        return f'{self.name}, колёс: {self.wheels}'

    def drive(self):
        print(f'{self.name}: поехали')


class Bike(Transport):
    def __init__(self, color: str):
        super().__init__('велосипед', 2)   # сначала родитель
        self.color = color

    def info(self) -> str:
        # расширяем метод родителя, а не переписываем заново
        return super().info() + f', цвет: {self.color}'

    def drive(self):
        print('кручу педали')


class Scooter(Transport):
    def __init__(self):
        super().__init__('самокат', 2)


bike = Bike('красный')
print(bike.info())
bike.drive()

scooter = Scooter()
print(scooter.info())
scooter.drive()          # метод родителя: его никто не переопределял

print(isinstance(bike, Transport), isinstance(scooter, Bike))
print(issubclass(Bike, Transport))
