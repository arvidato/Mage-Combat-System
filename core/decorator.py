from core.character import Character


class CharacterDecorator(Character):
    """
    Base decorator that wraps a Character.
    """

    def __init__(self, wrapped: Character):
        self._wrapped = wrapped

    def cast_spell(self, target: Character) -> None:
        self._wrapped.cast_spell(target)

    def take_damage(self, amount: int) -> None:
        self._wrapped.take_damage(amount)

    def is_alive(self) -> bool:
        return self._wrapped.is_alive()

class SpellBoostDecorator(CharacterDecorator):
    """
    Increases spell damage by a fixed bonus.
    """

    def __init__(self, wrapped: Character, bonus: int):
        super().__init__(wrapped)
        self.bonus = bonus

    def cast_spell(self, target: Character) -> None:
        original_power = self._wrapped.spell_power
        self._wrapped.spell_power += self.bonus

        self._wrapped.cast_spell(target)

        self._wrapped.spell_power = original_power