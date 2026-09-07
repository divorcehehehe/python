"""Модуль с вспомогательными функциями для задачи 1."""


def is_palindrome(text: str) -> bool:
    """True, если строка читается одинаково в обе стороны."""
    clean = text.lower()
    return clean == clean[::-1]


def digits_sum(n: int) -> int:
    """Сумма цифр целого неотрицательного числа."""
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


if __name__ == '__main__':
    # самопроверка модуля: при импорте не выполняется
    print(is_palindrome('Anna'), is_palindrome('Python'))
    print(digits_sum(1234))
