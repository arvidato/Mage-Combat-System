from core.decorator import SpellBoostDecorator
from core.mage import Mage
from core.monster import Monster
from core.strategy import BarrageSpell, LongRangeSpell, ShortRangeSpell

MONSTER_TEMPLATES = [
    Monster("Goblin", 35, 6),
    Monster("Skeleton", 45, 8),
    Monster("Orc", 60, 10),
]


def create_mage() -> Mage:
    name = input("Enter your mage name: ").strip() or "Arcana"
    return Mage(name=name, health=100, spell_power=10, strategy=ShortRangeSpell())


def choose_monster() -> Monster:
    print("\nChoose a monster to battle:")
    for index, template in enumerate(MONSTER_TEMPLATES, start=1):
        print(
            f"{index}. {template.name} (HP={template.health}, ATK={template.attack_power})"
        )

    while True:
        choice = input("Select monster: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(MONSTER_TEMPLATES):
            return MONSTER_TEMPLATES[int(choice) - 1].clone()
        print("Invalid choice. Try again.")


def choose_spell() -> str:
    print("\nChoose your action:")
    print("1. Short Range Spell")
    print("2. Long Range Spell")
    print("3. Boosted Short Range Spell")
    print("4. Arcane Barrage")

    while True:
        choice = input("Select spell: ").strip()
        if choice in {"1", "2", "3", "4"}:
            return choice
        print("Invalid choice. Try again.")


def resolve_player_turn(mage: Mage, monster: Monster) -> None:
    choice = choose_spell()

    if choice == "1":
        mage.strategy = ShortRangeSpell()
        damage = mage.cast_spell(monster)
        print(f"\n{mage.name} casts Short Range Spell and deals {damage} damage!")
    elif choice == "2":
        mage.strategy = LongRangeSpell()
        damage = mage.cast_spell(monster)
        print(f"\n{mage.name} casts Long Range Spell and deals {damage} damage!")
    elif choice == "3":
        mage.strategy = ShortRangeSpell()
        boosted_mage = SpellBoostDecorator(mage, bonus=5)
        damage = boosted_mage.cast_spell(monster)
        print(f"\n{mage.name} unleashes a boosted spell and deals {damage} damage!")
    else:
        mage.strategy = BarrageSpell(hit_count=4, hit_damage=3, max_workers=4)
        damage = mage.cast_spell(monster)
        print(f"\n{mage.name} casts Arcane Barrage!")
        print(
            f"4 bolts strike {monster.name} for 3 damage each. Total damage: {damage}!"
        )


def resolve_monster_turn(mage: Mage, monster: Monster) -> None:
    if not monster.is_alive():
        return
    damage = monster.cast_spell(mage)
    print(f"{monster.name} hits back for {damage} damage!")


def print_status(mage: Mage, monster: Monster) -> None:
    print("\n" + "=" * 40)
    print(f"{mage.name}: HP={mage.health}, Spell Power={mage.spell_power}")
    print(f"{monster.name}: HP={monster.health}, ATK={monster.attack_power}")
    print("=" * 40)


def battle_loop() -> None:
    print("=== Mage Combat Arena ===")
    mage = create_mage()
    monster = choose_monster()

    print(f"\nA wild {monster.name} appears!")

    while mage.is_alive() and monster.is_alive():
        print_status(mage, monster)
        resolve_player_turn(mage, monster)

        if monster.is_alive():
            resolve_monster_turn(mage, monster)

    print("\n=== Battle Result ===")
    if mage.is_alive() and not monster.is_alive():
        print(f"{mage.name} defeated the {monster.name}!")
    elif monster.is_alive() and not mage.is_alive():
        print(f"{mage.name} was defeated by the {monster.name}.")
    else:
        print("Both combatants have fallen.")

    print_status(mage, monster)


if __name__ == "__main__":
    battle_loop()
