from __future__ import annotations

from abc import ABC, abstractmethod

from concurrency.combat_executor import CombatExecutor


class SpellStrategy(ABC):
    """Defines how a spell behaves."""

    name: str = "Unnamed Spell"

    @abstractmethod
    def cast(self, caster, target) -> int:
        """Execute the spell and return total damage dealt."""
        raise NotImplementedError


class ShortRangeSpell(SpellStrategy):
    name = "Short Range Spell"

    def cast(self, caster, target) -> int:
        damage = caster.spell_power + 5
        target.take_damage(damage)
        return damage


class LongRangeSpell(SpellStrategy):
    name = "Long Range Spell"

    def cast(self, caster, target) -> int:
        damage = caster.spell_power
        target.take_damage(damage)
        return damage


# Original (unoptimized)


# class BarrageSpell(SpellStrategy):
#     name = "Arcane Barrage"
#
#     def __init__(self, hit_count: int = 4, hit_damage: int = 3, max_workers: int = 4):
#         self.hit_count = hit_count
#         self.hit_damage = hit_damage
#         self.max_workers = max_workers
#
#     def _single_hit(self, target) -> int:
#         target.take_damage(self.hit_damage)
#         return self.hit_damage
#
#     def cast(self, caster, target) -> int:
#         executor = CombatExecutor(max_workers=min(self.max_workers, self.hit_count))
#         futures = [
#             executor.submit_callable(self._single_hit, target)
#             for _ in range(self.hit_count)
#         ]
#         total_damage = sum(f.result() for f in futures)
#         executor.shutdown()
#         return total_damage


class BarrageSpell(SpellStrategy):
    name = "Arcane Barrage"

    def __init__(self, hit_count: int = 4, hit_damage: int = 3, max_workers: int = 4):
        self.hit_count = hit_count
        self.hit_damage = hit_damage
        self.max_workers = max_workers
        self.executor = CombatExecutor(
            max_workers=min(self.max_workers, self.hit_count)
        )

    def _single_hit(self, target) -> int:
        target.take_damage(self.hit_damage)
        return self.hit_damage

    def cast(self, caster, target) -> int:
        futures = [
            self.executor.submit_callable(self._single_hit, target)
            for _ in range(self.hit_count)
        ]
        total_damage = sum(f.result() for f in futures)
        return total_damage

    def shutdown(self) -> None:
        self.executor.shutdown()

