from core.character import Character
from core.prototype import Prototype
import copy


class Monster(Character, Prototype):
    def __init__(self, name: str, health: int, attack_power: int):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def cast_spell(self, target: Character) -> None:
        target.take_damage(self.attack_power)

    def take_damage(self, amount: int) -> None:
        self.health -= amount

    def is_alive(self) -> bool:
        return self.health > 0

    def __repr__(self):
        return f"{self.name}(HP={self.health}, ATK={self.attack_power})"
    
    def clone(self):
        return copy.deepcopy(self)