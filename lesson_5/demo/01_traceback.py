"""Как читать traceback.

Traceback читается снизу вверх: тип и сообщение внизу, выше строка, где сломалось,
ещё выше та строка, которая её вызвала.
"""
import traceback


def average(numbers):
    """Среднее арифметическое списка чисел."""
    return sum(numbers) / len(numbers)


print(average([4, 5, 3]))

try:
    print(average([]))
except ZeroDivisionError:
    print('Ниже настоящий traceback этой ошибки:')
    traceback.print_exc()

# Уберите try и except и запустите файл снова: программа остановится на пустом списке.
