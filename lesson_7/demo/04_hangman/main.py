"""Точка входа: собирает объекты и запускает игру."""
from models.display import Display
from models.game import Game
from models.player import Player
from models.word_manager import WordManager

LIVES = 6
WORDS_FILE = 'words.txt'


def main():
    name = input('Как тебя зовут? ')
    player = Player(name, LIVES)
    words = WordManager(WORDS_FILE)
    game = Game(player, words, Display())
    game.run()


if __name__ == '__main__':
    main()
