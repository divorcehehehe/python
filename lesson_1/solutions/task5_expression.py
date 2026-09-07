a = float(input())
b = float(input())
c = float(input())
expected = float(input())

result = a + 8 * b ** 2 / (4 * c)
# сравнивать float через == нельзя: 0.1 + 0.2 != 0.3
print(f'{result:.3f} {abs(result - expected) < 0.001}')
