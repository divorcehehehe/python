# ветвление: if, elif, else
temp = int(input('Температура: '))

if temp < 0:
    print('Мороз')
elif temp < 15:
    print('Прохладно')
elif temp < 25:
    print('Тепло')
else:
    print('Жара')
    if temp > 35:
        print('Очень')
