"""Задача 6: факториал и число Фибоначчи через рекурсию."""


def factorial(n: int) -> int:
    """n! = 1 * 2 * ... * n, простой случай: 0! и 1! равны 1."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fib(n: int) -> int:
    """n-е число Фибоначчи: 1, 1, 2, 3, 5, 8, ..."""
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def main() -> None:
    n = int(input())
    print(factorial(n), fib(n))


if __name__ == '__main__':
    main()
