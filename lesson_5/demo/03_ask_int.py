"""Безопасный ввод: программа не падает, а спрашивает заново."""


def ask_int(prompt):
    """Спрашивает целое число, пока не получит его."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Нужно целое число, попробуйте ещё раз')


def ask_float(prompt):
    """То же самое для дробного числа."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('Нужно число, например 1.75')


age = ask_int('Возраст: ')
height = ask_float('Рост в метрах: ')
print(f'Через год будет {age + 1}, рост {height * 100:.0f} см')
