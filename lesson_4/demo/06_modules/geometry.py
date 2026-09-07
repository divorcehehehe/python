# geometry.py: модуль с функциями, здесь только определения
from math import pi


def circle_area(r: float) -> float:
    """Площадь круга радиуса r."""
    return pi * r ** 2


def rect_area(width: float, height: float) -> float:
    """Площадь прямоугольника."""
    return width * height


def perimeter(width: float, height: float) -> float:
    """Периметр прямоугольника."""
    return 2 * (width + height)


if __name__ == '__main__':
    # быстрая самопроверка модуля: при импорте не выполняется
    print(circle_area(1))
    print(rect_area(2, 3), perimeter(2, 3))
