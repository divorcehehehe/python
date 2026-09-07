n = int(input())
divisor = 0
d = 2

while d * d <= n:      # делители ищем только до корня
    if n % d == 0:
        divisor = d
        break
    d += 1

if n < 2:              # 0 и 1 не простые
    print(f'{n} не простое')
elif divisor == 0:
    print(f'{n} простое')
else:
    print(f'{n} не простое, делитель {divisor}')
