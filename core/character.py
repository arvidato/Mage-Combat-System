from abc import ABC, abstractmethod


class Character(ABC):
    """
    Base interface for any entity that can participate in combat.
    """

    @abstractmethod
    def cast_spell(self, target: "Character") -> None:
        pass

    @abstractmethod
    def take_damage(self, amount: int) -> None:
        pass

    @abstractmethod
    def is_alive(self) -> bool:
        pass