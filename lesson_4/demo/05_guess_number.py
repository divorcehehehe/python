# игра «Угадай число»: функция, константа, цикл и random
from random import randint

MAX_ATTEMPTS = 7


def play():
    secret = randint(1, 100)
    for attempt in range(1, MAX_ATTEMPTS + 1):
        guess = int(input(f'Попытка {attempt}: '))
        if guess == secret:
            print(f'Угадал за {attempt}!')
            return True
        if guess < secret:
            print('Загадано больше')
        else:
            print('Загадано меньше')
    print(f'Попытки кончились, было {secret}')
    return False


play()
