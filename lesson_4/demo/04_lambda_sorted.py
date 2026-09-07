# функцию можно передать в другую функцию
words = ['python', 'if', 'модуль']
print(sorted(words, key=len))

students = [{'name': 'Аня', 'age': 19},
            {'name': 'Ян', 'age': 21}]
oldest = max(students, key=lambda s: s['age'])
print(oldest['name'])

# имя без скобок это сама функция, со скобками это вызов
action = print
action('функция лежит в переменной')
print(len, type(len))


# docstring и аннотации типов: подсказка для человека и для PyCharm
def average(numbers: list[float]) -> float:
    """Среднее арифметическое списка чисел.

    Пустой список не принимается.
    """
    return sum(numbers) / len(numbers)


print(average([4, 8, 15]))
print(average.__doc__.splitlines()[0])
