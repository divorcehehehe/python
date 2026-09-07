# кортежи и множества
point = (3, 4)
x, y = point
print(x, y, len(point))

a, b = 1, 2
a, b = b, a         # обмен значений через кортеж
print(a, b)

print(divmod(17, 5))

one = (1,)          # запятая обязательна
print(type(one), type((1)))

# кортеж изменить нельзя: снимите комментарий и получите TypeError
# point[0] = 9

# множества
numbers = [4, 5, 6, 5, 6, 6, 5]
unique = set(numbers)
print(sorted(unique), len(unique))

first = {1, 2, 3}
second = {3, 4}
print(sorted(first | second), sorted(first & second), sorted(first - second))
first.add(10)
first.discard(99)   # discard не ругается на отсутствующее значение
print(sorted(first))
print(type({}), type(set()))
