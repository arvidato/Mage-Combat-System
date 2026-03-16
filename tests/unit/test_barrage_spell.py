from core.mage import Mage
from core.monster import Monster
from core.strategy import BarrageSpell



def test_barrage_spell_hits_multiple_times():
    mage = Mage("Wizard", 100, 10, BarrageSpell(hit_count=4, hit_damage=3, max_workers=4))
    monster = Monster("Skeleton", 50, 5)

    damage = mage.cast_spell(monster)

    assert damage == 12
    assert monster.health == 38
