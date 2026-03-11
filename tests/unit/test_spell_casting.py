from core.mage import Mage
from core.monster import Monster
from core.strategy import ShortRangeSpell


def test_spell_casting_reduces_monster_health():
    mage = Mage("Wizard", 100, 10, ShortRangeSpell())
    monster = Monster("Skeleton", 50, 5)

    mage.cast_spell(monster)

    assert monster.health == 35