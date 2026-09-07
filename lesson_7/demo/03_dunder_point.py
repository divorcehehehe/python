# Магические методы: учим класс работать с + - * abs() == < и print()
import math


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, k: float):
        return Point(self.x * k, self.y * k)

    def __abs__(self) -> float:
        # расстояние до нуля
        return math.hypot(self.x, self.y)

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __lt__(self, other) -> bool:
        return abs(self) < abs(other)

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __repr__(self) -> str:
        # так точка выглядит внутри списка: print зовёт __repr__, а не __str__
        return f'Point({self.x}, {self.y})'


a = Point(1, 2)
b = Point(3, 4)

print(a + b)
print(b - a)
print(a * 3)
print(abs(b))
print(a == Point(1, 2), a == b)
print(a < b)
print(sorted([b, a, Point(0, 0)]))
