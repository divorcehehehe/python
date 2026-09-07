import math


class Shape:
    """Общий предок: знает, как себя напечатать."""

    name = 'Фигура'

    def area(self) -> float:
        return 0.0

    def perimeter(self) -> float:
        return 0.0

    def __str__(self) -> str:
        return f'{self.name}: площадь {self.area():.2f}, периметр {self.perimeter():.2f}'


class Circle(Shape):
    name = 'Круг'

    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    name = 'Прямоугольник'

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Triangle(Shape):
    name = 'Треугольник'

    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimeter(self) -> float:
        return self.a + self.b + self.c


def make_shape(line: str) -> Shape:
    parts = line.split()
    numbers = [float(x) for x in parts[1:]]
    if parts[0] == 'circle':
        return Circle(numbers[0])
    if parts[0] == 'rect':
        return Rectangle(numbers[0], numbers[1])
    return Triangle(numbers[0], numbers[1], numbers[2])


n = int(input())
shapes = [make_shape(input()) for _ in range(n)]

# полиморфизм: sorted и sum зовут area() каждой фигуры, не зная её класса
for shape in sorted(shapes, key=lambda s: s.area()):
    print(shape)
print(f'Общая площадь: {sum(s.area() for s in shapes):.2f}')
