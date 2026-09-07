# значения по умолчанию и именованные аргументы
def power(x, p=2):
    return x ** p


print(power(3))
print(power(3, 3))
print(power(p=4, x=3))
print(power(4, p=3))


# *args это кортеж лишних позиционных аргументов,
# **kwargs это словарь именованных
def show(*args, **kwargs):
    print(args)
    print(kwargs)


show(1, 2, 3)
show(1, 2, name='Аня', age=19)


def total(*numbers):
    return sum(numbers)


print(total(1, 2, 3, 4))


# несколько результатов возвращаются кортежем
def min_max(numbers):
    return min(numbers), max(numbers)


data = [4, 8, 15, 16, 23, 42]
result = min_max(data)
print(result)
print(type(result))

lo, hi = min_max(data)
print(lo, hi)
