# часть 1: атрибут класса против атрибута экземпляра


class Player:
    MAX_ATTEMPTS = 6      # атрибут класса, один на всех
    count = 0             # сколько игроков создали

    def __init__(self, name):
        self.name = name  # свой у каждого объекта
        Player.count += 1


anya = Player('Аня')
boris = Player('Борис')
print(Player.count, anya.MAX_ATTEMPTS, boris.MAX_ATTEMPTS)


# часть 2: _protected по соглашению и __private с искажением имени


class Account:
    def __init__(self, balance):
        self._owner = 'Аня'         # просто соглашение
        self.__balance = balance    # имя будет искажено


account = Account(100)
print(account._owner)
print(account._Account__balance)    # так всё равно можно

try:
    print(account.__balance)        # а так уже нет
except AttributeError as error:
    print('AttributeError:', error)
