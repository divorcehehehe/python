class Character:
    """Общий предок бойцов: здоровье, урон, вывод."""

    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def attack(self) -> int:
        return 0

    def take_damage(self, damage: int):
        self.health = max(0, self.health - damage)

    def is_alive(self) -> bool:
        return self.health > 0

    def __str__(self) -> str:
        return f'{self.name}: {self.health} здоровья'


class Warrior(Character):
    def __init__(self, name: str):
        super().__init__(name, 100)

    def attack(self) -> int:
        return 35


class Mage(Character):
    def __init__(self, name: str):
        super().__init__(name, 100)
        self.mana = 20

    def attack(self) -> int:
        # заклинание, пока хватает маны, дальше посох
        if self.mana >= 10:
            self.mana -= 10
            return 40
        return 10


def hit(attacker: Character, target: Character):
    """Один удар. Кто бьёт, тот и решает, каким будет урон."""
    damage = attacker.attack()
    target.take_damage(damage)
    print(f'{attacker.name} наносит {damage} урона. {target}')


warrior = Warrior(input())
mage = Mage(input())

while warrior.is_alive() and mage.is_alive():
    hit(warrior, mage)
    if mage.is_alive():
        hit(mage, warrior)

print(f'Победил {warrior.name if warrior.is_alive() else mage.name}')
