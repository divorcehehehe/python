"""Задача 5: калькулятор на словаре функций."""

OPERATIONS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}


def main() -> None:
    first = float(input())
    operation = input().strip()
    second = float(input())
    if operation not in OPERATIONS:
        print('неизвестная операция')
    elif operation == '/' and second == 0:
        print('на ноль делить нельзя')
    else:
        print(OPERATIONS[operation](first, second))


if __name__ == '__main__':
    main()
