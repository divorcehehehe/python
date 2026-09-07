"""Задача 1. Безопасный калькулятор: не падает на буквах и на делении на ноль."""


def ask_int():
    """Читает целое число, пока не получит его."""
    while True:
        try:
            return int(input())
        except ValueError:
            print('Нужно целое число')


def main():
    a = ask_int()
    b = ask_int()
    sign = input().strip()
    if sign == '+':
        print(f'{a} + {b} = {a + b}')
    elif sign == '-':
        print(f'{a} - {b} = {a - b}')
    elif sign == '*':
        print(f'{a} * {b} = {a * b}')
    elif sign == '/':
        try:
            print(f'{a} / {b} = {a / b}')
        except ZeroDivisionError:
            print('На ноль делить нельзя')
    else:
        print('Неизвестная операция')


if __name__ == '__main__':
    main()
