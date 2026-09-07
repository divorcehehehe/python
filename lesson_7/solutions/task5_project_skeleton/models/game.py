"""Правила викторины. Пока каркас: цикл допишем в проекте."""
from models.display import Display
from models.player import Player
from models.question_bank import QuestionBank


class Game:
    """Game имеет игрока, вопросы и экран: это композиция."""

    def __init__(self, player: Player, questions: QuestionBank, display: Display):
        self.player = player
        self.questions = questions
        self.display = display

    def run(self):
        # TODO: цикл по вопросам, проверка ответа, начисление очков
        self.display.show('Здесь будет игровой цикл')
        self.display.show(str(self.player))

    def __str__(self) -> str:
        return f'Викторина: {self.player}, {self.questions}'
