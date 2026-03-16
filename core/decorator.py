from core.character import Character
from core.mage import Mage


class CharacterDecorator(Character):
    def __init__(self, wrapped: Character):
        self._wrapped = wrapped

    def cast_spell(self, target: Character) -> int:
        return self._wrapped.cast_spell(target)

    def take_damage(self, amount: int) -> None:
        self._wrapped.take_damage(amount)

    def is_alive(self) -> bool:
        return self._wrapped.is_alive()


class SpellBoostDecorator(CharacterDecorator):
    def __init__(self, wrapped: Mage, bonus: int):
        super().__init__(wrapped)
        self._wrapped: Mage = wrapped
        self.bonus = bonus

    def cast_spell(self, target: Character) -> int:
        original_power = self._wrapped.spell_power
        self._wrapped.spell_power += self.bonus
        try:
            return self._wrapped.cast_spell(target)
        finally:
            self._wrapped.spell_power = original_power

