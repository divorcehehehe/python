class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError('размер должен быть больше нуля')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError('размер должен быть больше нуля')
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f'Прямоугольник {self.width} на {self.height}'


try:
    rect = Rectangle(float(input()), float(input()))
    print(rect)
    print(f'Площадь: {rect.area()}')
    print(f'Периметр: {rect.perimeter()}')
except ValueError:
    print('Ошибка: размер должен быть больше нуля')
