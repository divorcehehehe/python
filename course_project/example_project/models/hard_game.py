from models.game import Game


class HardGame(Game):
    """Сложный уровень: шире диапазон и больше попыток, правила те же."""

    # меняем только константы, LOW и весь код правил достаются от Game
    LEVEL = 'сложный'
    MAX_ATTEMPTS = 10
    HIGH = 1000

    def __str__(self):
        # super() даёт строку родителя, а мы её дополняем
        return f'{super().__str__()}, уровень сложный'
