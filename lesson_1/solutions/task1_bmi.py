height = float(input())
weight = float(input())
bmi = weight / height ** 2

if bmi < 18.5:
    category = 'недостаток'
elif bmi < 25:
    category = 'норма'
elif bmi < 30:
    category = 'избыток'
else:
    category = 'ожирение'

print(f'ИМТ: {bmi:.1f}, {category}')
