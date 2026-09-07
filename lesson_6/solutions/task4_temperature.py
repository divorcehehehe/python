ABSOLUTE_ZERO = -273.15


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        if value < ABSOLUTE_ZERO:
            raise ValueError('ниже абсолютного нуля')
        self.__celsius = value

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5 / 9

    def __str__(self):
        return f'{self.celsius} по Цельсию'


temperature = Temperature(0)
from_celsius = float(input())
from_fahrenheit = float(input())

try:
    temperature.celsius = from_celsius
    print(f'{temperature.celsius} по Цельсию это {temperature.fahrenheit} по Фаренгейту')
except ValueError:
    print('Ошибка: ниже абсолютного нуля')

temperature.fahrenheit = from_fahrenheit
print(f'{temperature.fahrenheit} по Фаренгейту это {temperature.celsius} по Цельсию')
