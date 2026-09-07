# цикл while: счётчик, цифры числа, выход по слову stop
i = 1
while i <= 3:
    print('виток', i)
    i += 1        # без этой строки цикл вечный

n = 123
while n > 0:
    print('цифра:', n % 10)
    n //= 10      # отбросили последнюю

total = 0
while True:
    line = input('Число или stop: ')
    if line == 'stop':
        break
    total += int(line)
print('Сумма:', total)
