class Player:
    """Игрок: имя и счётчик сделанных попыток."""

    def __init__(self, name):
        self.name = name        # проверку делает setter ниже
        self._attempts = 0      # защищённое поле: снаружи менять нечего

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # пустое имя не принимаем: объект без имени бесполезен
        if not value.strip():
            raise ValueError('имя не может быть пустым')
        self._name = value.strip()

    @property
    def attempts(self):
        # только для чтения: увеличить можно лишь через add_attempt()
        return self._attempts

    def add_attempt(self):
        # единственный счётчик попыток в программе, игра его только читает
        self._attempts += 1

    def __str__(self):
        return f'Игрок {self._name}, попыток сделано: {self._attempts}'
