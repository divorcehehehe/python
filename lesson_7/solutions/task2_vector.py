import math


class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, k: float):
        return Vector2D(self.x * k, self.y * k)

    def __abs__(self) -> float:
        return math.hypot(self.x, self.y)

    def __eq__(self, other) -> bool:
        # координаты бывают дробными, поэтому сравниваем с допуском, а не через ==
        return abs(self.x - other.x) < 1e-9 and abs(self.y - other.y) < 1e-9

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'


def read_vector() -> Vector2D:
    # координаты вводятся по одной в строке
    x = int(input())
    y = int(input())
    return Vector2D(x, y)


a = read_vector()
b = read_vector()

print(a + b)
print(a - b)
print(a * 2)
print(f'{abs(a):.2f}')
print(a == b)
