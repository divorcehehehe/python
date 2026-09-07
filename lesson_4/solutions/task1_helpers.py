"""Задача 1: main.py, который пользуется модулем helpers.py."""
from helpers import digits_sum, is_palindrome


def main() -> None:
    word = input()
    number = int(input())
    if is_palindrome(word):
        print(f'{word}: палиндром')
    else:
        print(f'{word}: не палиндром')
    print(f'{number}: сумма цифр {digits_sum(number)}')


if __name__ == '__main__':
    main()
