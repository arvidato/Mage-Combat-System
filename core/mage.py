from core.character import Character
from core.strategy import SpellStrategy
from core.prototype import Prototype
import copy


class Mage(Character, Prototype):
    def __init__(self, name: str, health: int, spell_power: int, strategy: SpellStrategy):
        self.name = name
        self.health = health
        self.spell_power = spell_power
        self.strategy = strategy

    def cast_spell(self, target: Character) -> None:
        damage = self.strategy.calculate_spell_power(self)
        target.take_damage(damage)

    def take_damage(self, amount: int) -> None:
        self.health -= amount

    def is_alive(self) -> bool:
        return self.health > 0

    def __repr__(self):
        return f"{self.name}(HP={self.health}, SP={self.spell_power})"
    
    def clone(self):
        return copy.deepcopy(self)