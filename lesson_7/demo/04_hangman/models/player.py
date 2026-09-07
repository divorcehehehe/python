"""Игрок: имя, жизни и очки."""


class Player:
    """Состояние игрока. Жизни меняются только методами."""

    def __init__(self, name: str, lives: int):
        self.name = name
        self._lives = lives
        self._score = 0

    @property
    def lives(self) -> int:
        return self._lives

    @property
    def score(self) -> int:
        return self._score

    def lose_life(self):
        if self._lives > 0:
            self._lives -= 1

    def add_score(self, points: int):
        self._score += points

    def is_alive(self) -> bool:
        return self._lives > 0

    def __str__(self) -> str:
        return f'{self.name}: жизней {self._lives}, очков {self._score}'
