n = int(input())

matrix = []
for i in range(n):
    matrix.append([int(x) for x in input().split()])

for column in range(n):
    row = [matrix[line][column] for line in range(n)]
    print(' '.join([str(x) for x in row]))

total = 0
for i in range(n):
    total += matrix[i][i]
print(total)
