# вложенные циклы: таблица умножения и треугольник
for i in range(1, 6):
    for j in range(1, 6):
        print(f'{i * j:3}', end='')
    print()

for i in range(1, 5):
    print('*' * i)

# то же самое с end=' ': столбцы получаются кривые
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end=' ')
    print()
