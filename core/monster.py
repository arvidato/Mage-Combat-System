import copy
import threading

from core.character import Character
from core.prototype import Prototype


class Monster(Character, Prototype):
    def __init__(self, name: str, health: int, attack_power: int):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self._lock = threading.Lock()

    def cast_spell(self, target: Character) -> int:
        damage = self.attack_power
        target.take_damage(damage)
        return damage

    def take_damage(self, amount: int) -> None:
        with self._lock:
            self.health -= amount

    def is_alive(self) -> bool:
        return self.health > 0

    def __repr__(self):
        return f"{self.name}(HP={self.health}, ATK={self.attack_power})"

    def clone(self):
        return Monster(self.name, self.health, self.attack_power)

