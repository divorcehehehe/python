"""Задача 6. Калькулятор из задачи 1 с цветным выводом через rich.

Файл работает и без библиотеки: тогда вывод получится обычным, чёрно-белым.
"""
try:
    from rich import print
    HAS_RICH = True
except ImportError:
    HAS_RICH = False
    print('Библиотека rich не установлена. Поставьте её: pip install rich')


def paint(text, style):
    """Добавляет разметку rich, если библиотека есть."""
    return f'[{style}]{text}[/{style}]' if HAS_RICH else text


def ask_int():
    """Читает целое число, пока не получит его."""
    while True:
        try:
            return int(input())
        except ValueError:
            print(paint('Нужно целое число', 'bold red'))


def main():
    a = ask_int()
    b = ask_int()
    sign = input().strip()
    if sign == '/' and b == 0:
        print(paint('На ноль делить нельзя', 'bold red'))
    elif sign == '+':
        print(paint(f'{a} + {b} = {a + b}', 'bold green'))
    elif sign == '-':
        print(paint(f'{a} - {b} = {a - b}', 'bold green'))
    elif sign == '*':
        print(paint(f'{a} * {b} = {a * b}', 'bold green'))
    elif sign == '/':
        print(paint(f'{a} / {b} = {a / b}', 'bold green'))
    else:
        print(paint('Неизвестная операция', 'bold red'))


if __name__ == '__main__':
    main()
