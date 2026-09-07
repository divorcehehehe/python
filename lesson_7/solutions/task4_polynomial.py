class Polynomial:
    """Многочлен. Коэффициенты по убыванию степени: [3, 2, 1] это 3x^2 + 2x + 1."""

    def __init__(self, coefficients: list[int]):
        self.coefficients = list(coefficients)

    def degree(self) -> int:
        return len(self.coefficients) - 1

    def value(self, x: float) -> float:
        """Схема Горнера: ((3 * x) + 2) * x + 1."""
        result = 0
        for c in self.coefficients:
            result = result * x + c
        return result

    def derivative(self):
        n = self.degree()
        new_coefficients = [c * (n - i) for i, c in enumerate(self.coefficients[:-1])]
        return Polynomial(new_coefficients or [0])

    def term(self, c: int, power: int) -> str:
        """Одно слагаемое без знака: 3x^2, x, 5."""
        if power == 0:
            return f'{c}'
        letter = 'x' if power == 1 else f'x^{power}'
        return letter if c == 1 else f'{c}{letter}'

    def __add__(self, other):
        length = max(len(self.coefficients), len(other.coefficients))
        left = [0] * (length - len(self.coefficients)) + self.coefficients
        right = [0] * (length - len(other.coefficients)) + other.coefficients
        return Polynomial([left[i] + right[i] for i in range(length)])

    def __str__(self) -> str:
        n = self.degree()
        text = ''
        for i, c in enumerate(self.coefficients):
            if c == 0:
                continue
            piece = self.term(abs(c), n - i)
            if not text:
                text = f'-{piece}' if c < 0 else piece
            else:
                text += (' - ' if c < 0 else ' + ') + piece
        return text or '0'


first = Polynomial([int(c) for c in input().split()])
second = Polynomial([int(c) for c in input().split()])
x = int(input())

lines = [str(first), str(second), str(first + second), str(first.value(x)), str(first.derivative())]
for line in lines:
    print(line)

with open('polynomials.txt', 'w', encoding='utf-8') as f:
    for line in lines:
        f.write(line + '\n')
