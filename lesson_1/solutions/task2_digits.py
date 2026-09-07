n = int(input())
hundreds = n // 100
tens = n // 10 % 10
units = n % 10
print(hundreds + tens + units)
