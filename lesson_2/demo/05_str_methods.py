# методы строк, split и join, коды символов
name = '  Ада Лавлейс  '
print(f'[{name.strip()}]')
print(name.strip().upper())

s = 'банан'
print(s.replace('а', 'о'))
print(s.find('нан'), s.find('кот'))
print(s.count('а'), 'нан' in s)
print(s.startswith('ба'), s.endswith('ан'))

# строку изменить нельзя, собираем новую
s = 'Python'
s = 'S' + s[1:]
print(s)

a, b = input().split()
print(int(a) + int(b))

text = 'раз два три'
print(text.split())
print('-'.join('abc'))

print(ord('a'), ord('b'), ord('z'))
print(chr(97), chr(1040))
print(chr(ord('a') + 1))
print('a' < 'b')

ch, shift = 'y', 3          # сдвиг с переходом через z
code = (ord(ch) - ord('a') + shift) % 26
print(chr(ord('a') + code))
