text = input()
shift = int(input())
result = ''

for ch in text:
    code = (ord(ch) - ord('a') + shift) % 26   # переход через z
    result += chr(ord('a') + code)

print(result)
