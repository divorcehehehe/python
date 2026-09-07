# строка как последовательность: перебор, индексы, срезы, enumerate
s = 'Python'
for ch in s:
    print(ch, end=' ')
print()
print(len(s))
print(s[0], s[1], s[5])
print(s[-1], s[-2])
# print(s[6])   # раскомментируйте: будет IndexError

s = 'Программа'
print(s[0:5])
print(s[:5], s[5:])
print(s[::2])
print(s[::-1])
print(s[2:4], len(s[2:4]))
print(s[5:100])

name = 'Ада'
for i, ch in enumerate(name):
    print(i, ch)

for i, ch in enumerate(name, start=1):
    print(i, ch)
