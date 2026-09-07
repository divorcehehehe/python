# словари: доступ по ключу, перебор, счётчик
week = {1: 'Пн', 2: 'Вт', 3: 'Ср'}
print(week[1], len(week))
week[4] = 'Чт'
week[1] = 'понедельник'
print(week)
print(week.get(9, 'нет такого дня'))
print(9 in week, 3 in week)
del week[1]
print(sorted(week))

ages = {'Аня': 19, 'Пётр': 21, 'Лиза': 20}
for name in ages:               # по ключам
    print(name, end=' ')
print()
print(list(ages.keys()))        # ключи
print(list(ages.values()))      # значения
for name, age in ages.items():  # пары
    print(f'{name}: {age}')
print(sum(ages.values()) / len(ages))

# словарь как счётчик
text = 'кот дом кот сыр дом кот'
counts = {}
for word in text.split():
    counts[word] = counts.get(word, 0) + 1
print(counts)

best, best_count = '', 0
for word, number in counts.items():
    if number > best_count:
        best, best_count = word, number
print('чаще всего:', best, best_count)
