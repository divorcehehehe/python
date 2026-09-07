"""try, except, else, finally и несколько типов исключений."""

# 1. Один except на конкретный тип
try:
    number = int('пять')
except ValueError:
    print('ValueError: строка не превращается в число')

# 2. Несколько except: сработает первый подходящий
data = {'Аня': 5}
for key in ('Аня', 'Игорь'):
    try:
        print(key, data[key])
    except KeyError:
        print(f'KeyError: ключа {key} в словаре нет')

# 3. else и finally
for text in ('7', 'семь'):
    try:
        value = int(text)
    except ValueError as e:
        print('Не получилось:', e)
    else:
        print('Получилось:', value ** 2)
    finally:
        print('finally выполняется в любом случае')

# 4. Так делать не надо: ошибка проглочена молча
try:
    print(10 / 0)
except ZeroDivisionError:
    pass
print('Программа дошла до конца')
