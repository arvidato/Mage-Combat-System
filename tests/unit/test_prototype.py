from core.mage import Mage
from core.strategy import ShortRangeSpell


def test_mage_clone():
    mage_template = Mage("Wizard", 100, 10, ShortRangeSpell())

    cloned_mage = mage_template.clone()

    assert cloned_mage is not mage_template
    assert cloned_mage.name == mage_template.name
    assert cloned_mage.health == mage_template.health