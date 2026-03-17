from abc import ABC, abstractmethod


class Character(ABC):
    @abstractmethod
    def cast_spell(self, target: "Character") -> int:
        pass

    @abstractmethod
    def take_damage(self, amount: int) -> None:
        pass

    @abstractmethod
    def is_alive(self) -> bool:
        pass

