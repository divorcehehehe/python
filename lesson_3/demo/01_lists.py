# списки: создание, изменение, полезные функции, перебор
numbers = [4, 5, 6, 10]
mixed = ['odin', 2, [3, 4]]
print(len(numbers), numbers[0], numbers[-1])
print(numbers[1:3], numbers[::-1])
print(mixed[2], mixed[2][1])

items = [4, 5, 6]
items[0] = 100
items.append(7)
items.insert(1, 'новый')
items.extend([8, 9])
print(items)
last = items.pop()
items.remove('новый')
del items[0]
print(items, last)
print(6 in items, 42 in items)

scores = [7, 3, 10, 5]
print(sum(scores), min(scores), max(scores))
print(sorted(scores), scores)
print(scores.sort())      # None: sort меняет список на месте
print(scores)
print(list(reversed(scores)))
print(list(range(1, 6)))

words = ['кот', 'дом', 'сыр']
for word in words:
    print(word, len(word))

for i, word in enumerate(words):
    print(i, word)

# изменение на месте: тут индекс действительно нужен
tens = [1, 2, 3]
for i in range(len(tens)):
    tens[i] = tens[i] * 10
print(tens)

# числа из одной строки
print('Введите числа через пробел:')
line_numbers = [int(x) for x in input().split()]
print(line_numbers, sum(line_numbers))
