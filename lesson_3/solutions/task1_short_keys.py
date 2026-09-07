n = int(input())
data = {}

for i in range(n):
    key, value = input().split()
    data[key] = int(value)

total = 0
for key, value in data.items():
    if len(key) == 1:
        total += value

print(total)
