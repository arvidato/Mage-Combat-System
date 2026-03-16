import time

from core.mage import Mage
from core.monster import Monster
from core.strategy import BarrageSpell


def run_barrage_benchmark(spell_count=10_000):
    spell = BarrageSpell(hit_count=4, hit_damage=3, max_workers=4)
    mage = Mage("Wizard", 1000, 10, spell)
    monster = Monster("Training Dummy", 10_000_000, 0)

    start_time = time.perf_counter()

    for _ in range(spell_count):
        mage.cast_spell(monster)

    end_time = time.perf_counter()

    shutdown = getattr(spell, "shutdown", None)
    if callable(shutdown):
        shutdown()

    duration = end_time - start_time
    throughput = spell_count / duration

    print(f"Total barrage spells cast: {spell_count}")
    print(f"Execution time: {duration:.4f} seconds")
    print(f"Throughput: {throughput:.2f} barrage casts/sec")


if __name__ == "__main__":
    run_barrage_benchmark()
