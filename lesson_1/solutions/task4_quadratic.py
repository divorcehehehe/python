a = float(input())
b = float(input())
c = float(input())
discriminant = b ** 2 - 4 * a * c
eps = 1e-9   # float нельзя сравнивать с нулём через ==

if discriminant < -eps:
    print('нет корней')
elif abs(discriminant) <= eps:
    x = -b / (2 * a)
    print(f'x = {x:.2f}')
else:
    root = discriminant ** 0.5
    x1 = (-b + root) / (2 * a)   # сначала корень с плюсом
    x2 = (-b - root) / (2 * a)
    print(f'x1 = {x1:.2f}, x2 = {x2:.2f}')
