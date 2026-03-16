import copy
import threading

from core.character import Character
from core.prototype import Prototype
from core.strategy import SpellStrategy


class Mage(Character, Prototype):
    def __init__(
        self, name: str, health: int, spell_power: int, strategy: SpellStrategy
    ):
        self.name = name
        self.health = health
        self.spell_power = spell_power
        self.strategy = strategy
        self._lock = threading.Lock()

    def cast_spell(self, target: Character) -> int:
        return self.strategy.cast(self, target)

    def take_damage(self, amount: int) -> None:
        with self._lock:
            self.health -= amount

    def is_alive(self) -> bool:
        return self.health > 0

    def __repr__(self):
        return f"{self.name}(HP={self.health}, SP={self.spell_power})"

    def clone(self):
        return Mage(self.name, self.health, self.spell_power, self.strategy)

