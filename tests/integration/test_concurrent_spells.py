from core.mage import Mage
from core.monster import Monster
from core.strategy import ShortRangeSpell
from concurrency.combat_executor import CombatExecutor


def test_multiple_spells_can_run_concurrently():

    executor = CombatExecutor(max_workers=4)

    mage = Mage("Wizard", 100, 10, ShortRangeSpell())
    monster = Monster("Skeleton", 200, 5)

    futures = []

    for _ in range(10):
        futures.append(executor.submit_spell(mage, monster))

    for f in futures:
        f.result()

    executor.shutdown()

    assert monster.health < 200