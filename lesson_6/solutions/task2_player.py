class Player:
    MAX_ATTEMPTS = 6

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.__attempts_left = Player.MAX_ATTEMPTS

    @property
    def attempts_left(self):
        return self.__attempts_left

    def lose_attempt(self):
        if self.__attempts_left > 0:
            self.__attempts_left -= 1

    def add_score(self, points):
        self.score += points

    def __str__(self):
        return f'{self.name}: {self.score} очков, попыток {self.attempts_left}'


player = Player(input())
player.add_score(int(input()))
for _ in range(int(input())):
    player.lose_attempt()
print(player)
