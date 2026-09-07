"""Игрок викторины: имя и очки."""


class Player:
    def __init__(self, name: str):
        self.name = name
        self._score = 0

    @property
    def score(self) -> int:
        """Очки только для чтения: их начисляет add_score."""
        return self._score

    def add_score(self, points: int):
        self._score += points

    def __str__(self) -> str:
        return f'{self.name}: {self._score} очков'
