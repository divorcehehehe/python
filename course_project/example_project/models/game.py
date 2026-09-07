import os
import random


class Game:
    """Правила игры: загадывает число и решает, когда партия окончена."""

    LEVEL = 'обычный'   # название уровня, попадает в таблицу рекордов
    MAX_ATTEMPTS = 7    # сколько попыток даётся игроку
    LOW = 1             # нижняя граница загаданного числа
    HIGH = 100          # верхняя граница загаданного числа

    def __init__(self, player):
        self._player = player       # игра не считает попытки, а спрашивает
        self._secret = random.randint(self.LOW, self.HIGH)
        from_env = os.environ.get('GUESS_SECRET')
        if from_env is not None:    # переменная фиксирует число для тестов
            self._secret = int(from_env)
        self._won = False

    @property
    def player(self):
        return self._player

    @property
    def secret(self):
        return self._secret

    @property
    def attempts_left(self):
        return self.MAX_ATTEMPTS - self.player.attempts

    @property
    def is_won(self):
        return self._won

    @property
    def is_over(self):
        # партия кончается победой или когда попытки исчерпаны
        return self._won or self.player.attempts >= self.MAX_ATTEMPTS

    def guess(self, number):
        # засчитываем попытку игроку и возвращаем подсказку
        self.player.add_attempt()
        if number < self._secret:
            return 'больше'
        if number > self._secret:
            return 'меньше'
        self._won = True
        return 'угадал'

    def __str__(self):
        return (f'Игра: число от {self.LOW} до {self.HIGH}, '
                f'ходов {self.player.attempts}')
