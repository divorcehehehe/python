first = input()
second = input()
half_first = len(first) // 2
half_second = len(second) // 2
print(first[:half_first] + second[half_second:])
