"""Скелет курсового проекта «Викторина»: классы есть, логики пока нет."""
from models.display import Display
from models.game import Game
from models.player import Player
from models.question_bank import QuestionBank

QUESTIONS_FILE = 'questions.txt'


def main():
    name = input('Как тебя зовут? ')
    game = Game(Player(name), QuestionBank(QUESTIONS_FILE), Display())
    game.run()


if __name__ == '__main__':
    main()
