from models.display import Display
from models.game import Game
from models.hard_game import HardGame
from models.player import Player
from models.records import Records


def ask_player(display):
    # спрашиваем имя, пока Player не примет его без ошибки
    while True:
        try:
            return Player(display.ask_text('Как вас зовут? '))
        except ValueError as error:
            display.show(f'Ошибка: {error}')


def ask_level(display):
    # выбираем класс игры: любой ответ кроме 2 считаем обычным уровнем
    answer = display.ask_text('Уровень: 1 обычный, 2 сложный? ')
    if answer.strip() == '2':
        return HardGame
    return Game


def play(display, game):
    # одна партия: спрашиваем числа, пока игра не закончится
    display.show(f'Загадал число от {game.LOW} до {game.HIGH}, '
                 f'попыток {game.MAX_ATTEMPTS}.')
    while not game.is_over:
        number = display.ask_number('Ваше число: ', game.HIGH)
        hint = game.guess(number)
        if hint == 'угадал':
            display.show(f'Угадали! Это {game.secret}.')
        else:
            display.show(f'Число {hint}. Осталось: {game.attempts_left}.')
    if not game.is_won:
        display.show(f'Попытки кончились. Я загадал {game.secret}.')


def main():
    display = Display()
    records = Records()
    try:
        level = ask_level(display)
        player = ask_player(display)
        # одна и та же строка создаёт Game или HardGame: это полиморфизм
        game = level(player)
        play(display, game)
    except EOFError:
        # ввод закончился: например, программу запустили с файлом на входе
        display.show('\nВвод закончился, выходим.')
        return
    records.add(player.name, player.attempts, game.is_won, game.LEVEL)
    display.show(f'{player}\n{game}\n{records}')


if __name__ == '__main__':
    main()
