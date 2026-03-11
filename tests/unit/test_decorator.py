from core.mage import Mage
from core.monster import Monster
from core.strategy import ShortRangeSpell
from core.decorator import SpellBoostDecorator


def test_spell_boost_decorator_increases_damage():
    mage = Mage("Wizard", 100, 10, ShortRangeSpell())
    monster = Monster("Skeleton", 50, 5)

    boosted_mage = SpellBoostDecorator(mage, bonus=5)

    boosted_mage.cast_spell(monster)

    # 10 spell power + 5 decorator bonus + 5 short range bonus
    assert monster.health == 30