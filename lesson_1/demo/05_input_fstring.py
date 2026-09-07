# input() всегда возвращает строку, f-строки собирают текст
name = input('Как тебя зовут? ')
age = int(input('Сколько лет? '))
height = float(input('Рост в метрах? '))
print(type(name), type(age), type(height))

print(f'{name}, тебе {age} лет, через год будет {age + 1}')
print(f'Рост {height:.2f} м, это {height * 100:.0f} см')
print(f'{7:02d}:{5:02d}')
