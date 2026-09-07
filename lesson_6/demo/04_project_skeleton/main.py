# Запускать из этой папки: python main.py
from models.player import Player

ROUNDS = 3


def main():
    player = Player('Аня')
    for number in range(1, ROUNDS + 1):
        player.add_score(number * 10)
        print(f'Раунд {number}: {player}')
    print('Итог:', player)


if __name__ == '__main__':
    main()
