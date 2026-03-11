from abc import ABC, abstractmethod
from core.character import Character


class SpellStrategy(ABC):
    """
    Defines how a spell behaves.
    Different spell types will implement this.
    """

    @abstractmethod
    def calculate_spell_power(self, caster: Character) -> int:
        pass

class ShortRangeSpell(SpellStrategy):
    """
    Stronger but meant for close enemies.
    """

    def calculate_spell_power(self, caster: Character) -> int:
        return caster.spell_power + 5

class LongRangeSpell(SpellStrategy):
    """
    Weaker but safer distance spell.
    """

    def calculate_spell_power(self, caster: Character) -> int:
        return caster.spell_power