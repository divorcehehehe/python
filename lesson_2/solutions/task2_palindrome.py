s = input()
low = s.lower()

if low == low[::-1]:
    print(f'{s} является палиндромом')
else:
    print(f'{s} не является палиндромом')
