# for и range, а также break и continue
for i in range(5):
    print(i, end=' ')
print()

for i in range(2, 10, 3):
    print(i, end=' ')
print()

for i in range(10, 0, -1):
    print(i, end=' ')
print()
print(range(5), len(range(10 ** 9)))

for i in range(1, 10):
    if i % 2 == 0:
        continue      # чётные пропускаем
    print(i, end=' ')
print()

n = 91                # выглядит простым, но нет
d = 2
while d * d <= n:
    if n % d == 0:
        print('делитель', d)
        break         # выходим из цикла
    d += 1
