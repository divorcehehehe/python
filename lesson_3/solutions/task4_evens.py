numbers = [int(x) for x in input().split()]

best = []
current = []
for x in numbers:
    if x % 2 == 0:
        current.append(x)
        if len(current) > len(best):
            best = current.copy()
    else:
        current = []

if best:
    print(' '.join([str(x) for x in best]))
else:
    print('нет')
