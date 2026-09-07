# def и return: функция считает и отдаёт результат
def greet(name):
    print(f'Привет, {name}!')


def area(width, height):
    return width * height


greet('Аня')
result = area(3, 4)
print(result)
print(greet('Ян'))      # greet ничего не возвращает, поэтому None


# функция прячет детали: снаружи видно только имя и ответ
def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


for number in range(10, 21):
    if is_prime(number):
        print(number, end=' ')
print()
print(is_prime(97), is_prime(1))
