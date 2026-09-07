# comprehension и вложенные структуры
squares = [x ** 2 for x in range(6)]
print(squares)

numbers = [0, 3, -2, 7, 0]
print([x for x in numbers if x != 0])

words = ['кот', 'домик', 'сыр']
print([w.upper() for w in words])
print({len(w) for w in words})          # множество
print({w: len(w) for w in words})       # словарь
print([int(x) for x in '4 8 15'.split()])

# то же самое обычным циклом: длиннее, но понятнее
result = []
for x in range(6):
    result.append(x ** 2)
print(result)

# список словарей
students = [{'name': 'Аня', 'age': 19},
            {'name': 'Пётр', 'age': 21}]
print(students[0]['name'], students[1]['age'])
for student in students:
    print(student['name'], student['age'])
print([s['name'] for s in students if s['age'] > 19])

# матрица как список списков
matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix[1][2])
for row in matrix:
    print(sum(row))
