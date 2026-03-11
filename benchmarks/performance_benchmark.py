import time

from core.mage import Mage
from core.monster import Monster
from core.strategy import ShortRangeSpell
from concurrency.combat_executor import CombatExecutor


def run_benchmark(spell_count=100_000):

    executor = CombatExecutor(max_workers=8)

    mage = Mage("Wizard", 1000, 10, ShortRangeSpell())
    monster = Monster("Training Dummy", 10_000_000, 0)

    start_time = time.perf_counter()

    futures = []

    for _ in range(spell_count):
        futures.append(executor.submit_spell(mage, monster))

    for f in futures:
        f.result()

    executor.shutdown()

    end_time = time.perf_counter()

    duration = end_time - start_time
    throughput = spell_count / duration

    print(f"Total spells cast: {spell_count}")
    print(f"Execution time: {duration:.4f} seconds")
    print(f"Throughput: {throughput:.2f} spells/sec")


if __name__ == "__main__":
    run_benchmark()