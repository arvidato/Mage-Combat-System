from concurrency.unsafe_metrics_registry import UnsafeMetricsRegistry
from concurrency.combat_executor import CombatExecutor
from core.mage import Mage
from core.monster import Monster
from core.strategy import ShortRangeSpell


def test_race_condition_without_lock():

    registry = UnsafeMetricsRegistry()
    executor = CombatExecutor(max_workers=8)

    mage = Mage("Wizard", 100, 10, ShortRangeSpell())
    monster = Monster("Skeleton", 1000, 5)

    futures = []

    attack_count = 1000

    for _ in range(attack_count):
        futures.append(executor.submit_spell(mage, monster))
        registry.record_spell(10)

    for f in futures:
        f.result()

    executor.shutdown()

    assert registry.total_spells_cast <= attack_count