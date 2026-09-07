"""Задача 2: «Угадай число» с ограничением попыток и повтором игры."""
from random import randint

LOW, HIGH = 1, 100
MAX_ATTEMPTS = 7


def play_round() -> bool:
    """Одна партия. True, если игрок угадал число."""
    secret = randint(LOW, HIGH)
    for attempt in range(1, MAX_ATTEMPTS + 1):
        guess = int(input(f'Попытка {attempt} из {MAX_ATTEMPTS}: '))
        if guess == secret:
            print(f'Угадали! Попыток: {attempt}')
            return True
        if guess < secret:
            print('Загадано больше')
        else:
            print('Загадано меньше')
    print(f'Попытки кончились, было загадано {secret}')
    return False


def main() -> None:
    while True:
        play_round()
        answer = input('Сыграем ещё? (да/нет): ')
        if answer.strip().lower() != 'да':
            print('Пока!')
            break


if __name__ == '__main__':
    main()
