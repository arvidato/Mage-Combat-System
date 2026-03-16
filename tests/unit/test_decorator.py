from core.decorator import SpellBoostDecorator
from core.mage import Mage
from core.monster import Monster
from core.strategy import ShortRangeSpell



def test_spell_boost_decorator_increases_damage():
    mage = Mage("Wizard", 100, 10, ShortRangeSpell())
    monster = Monster("Skeleton", 50, 5)

    boosted_mage = SpellBoostDecorator(mage, bonus=5)
    damage = boosted_mage.cast_spell(monster)

    assert damage == 20
    assert monster.health == 30
    assert mage.spell_power == 10
