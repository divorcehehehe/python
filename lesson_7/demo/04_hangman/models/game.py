"""Правила игры и игровой цикл."""
from models.display import Display
from models.player import Player
from models.word_manager import WordManager


class Game:
    """Композиция: Game имеет игрока, слово и экран, но не наследует их."""

    POINTS_PER_LETTER = 10

    def __init__(self, player: Player, words: WordManager, display: Display):
        self.player = player
        self.words = words
        self.display = display

    def is_over(self) -> bool:
        """Игра кончена, когда слово открыто или жизни кончились."""
        return self.words.is_guessed() or not self.player.is_alive()

    def run(self):
        self.display.greet(self.player)
        while not self.is_over():
            self.display.show(self.words, self.player)
            letter = self.display.ask_letter()
            if self.words.open_letter(letter):
                self.player.add_score(self.POINTS_PER_LETTER)
            else:
                self.player.lose_life()
        self.display.show_result(self.words, self.player)

    def __str__(self) -> str:
        return f'Виселица: играет {self.player.name}'
