"""Чтение и запись файлов: тот же код, что на слайдах, плюс выбор слова для «Виселицы»."""
import random

# Запись с нуля: режим 'w' стирает старое содержимое
with open('notes.txt', 'w', encoding='utf-8') as f:
    f.write('первая строка\n')
    f.write('вторая строка\n')

# Дозапись в конец: режим 'a'
with open('notes.txt', 'a', encoding='utf-8') as f:
    print('третья строка', file=f)

# Чтение целиком
with open('notes.txt', 'r', encoding='utf-8') as f:
    print(f.read())

# Чтение по строке: так делают почти всегда
with open('notes.txt', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        print(i, line.strip())

# Слова для игры «Виселица»
with open('words.txt', 'r', encoding='utf-8') as f:
    words = [line.strip() for line in f if line.strip()]

secret = random.choice(words)
print(f'Слов в файле: {len(words)}, загадано букв: {len(secret)}')

with open('results.txt', 'a', encoding='utf-8') as f:
    f.write(f'{secret}: победа\n')

# Файла может не быть: программа не должна падать
try:
    with open('нет_такого_файла.txt', 'r', encoding='utf-8') as f:
        print(f.read())
except FileNotFoundError:
    print('Файл не найден, но программа жива')
