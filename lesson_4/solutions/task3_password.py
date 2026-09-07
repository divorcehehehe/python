"""Задача 3: генератор паролей с параметрами по умолчанию."""
from random import choice

LETTERS = 'abcdefghijklmnopqrstuvwxyz'
DIGITS = '0123456789'
SPECIALS = '!@#$%*'


def make_password(length: int = 8, use_digits: bool = True, use_specials: bool = False) -> str:
    """Случайный пароль заданной длины из выбранных наборов символов."""
    alphabet = LETTERS + LETTERS.upper()
    if use_digits:
        alphabet += DIGITS
    if use_specials:
        alphabet += SPECIALS
    password = ''
    for _ in range(length):
        password += choice(alphabet)
    return password


def main() -> None:
    length = int(input())
    print(make_password())
    print(make_password(length))
    print(make_password(length, use_specials=True))


if __name__ == '__main__':
    main()
