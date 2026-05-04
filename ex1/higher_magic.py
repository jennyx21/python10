from collections.abc import Callable, Sequence
from typing import Any


def spell_combiner(spell1: Callable[[Any, Any], Any],
                   spell2:
                   Callable[[Any, Any], Any]) -> Callable[[Any, Any], Any]:
    return (
        lambda target, power: (spell1(target, power), spell2(target, power))
        )


def power_amplifier(base_spell: Callable[[Any, Any], Any],
                    multiplier: int) -> Callable[[Any, Any], Any]:
    return (lambda target, power: base_spell(target, power * multiplier))


def conditional_caster(condition: Callable[[Any], Any],
                       spell: Callable[[Any, Any],
                                       Any]) -> Callable[[Any, Any], Any]:
    return (
        lambda target, power: spell(target, power)
        if condition(target) else "spell fizzeled"
        )


def spell_sequence(
        spells:
        Sequence[Callable[[Any,
                           Any], Any]]) -> Callable[[Any, Any], list[Any]]:
    return lambda target, power: [spell(target, power) for spell in spells]


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} Damage"


def lighting(target: str, power: int) -> str:
    return f"Lightning hits {target} for {power} Damage"


def storm(target: str, power: int) -> str:
    return f"Storm hits {target} for {power} Damage"


def test_combiner() -> None:
    comb = spell_combiner(heal, fireball)
    combo = comb("Dragon", 9)
    finall = []
    for i in combo:
        msg = i.split(" for")
        finall.append(msg[0])
    print(f"Combined spell Result: {finall[0]}, {finall[1]}")


def test_amplifier() -> None:
    mega_fireball = power_amplifier(fireball, 3)
    mega = mega_fireball("Dragon", 9)
    print(mega)


def test_condition() -> None:
    condi = conditional_caster(lambda target: target == "Dragon", fireball)
    cond_pass = condi("Dragon", 45)
    cond_fail = condi("Spider", 45)
    print(cond_pass)
    print(cond_fail)


def test_sequence() -> None:
    liste = [
        heal,
        fireball,
        lighting,
        storm
    ]
    sequence = spell_sequence(liste)
    seq = sequence("Dragon", 45)
    for i in seq:
        print(i)


def main() -> None:
    print("\nTesting spell combiner...")
    test_combiner()
    print("\nTesting power amplifier...")
    test_amplifier()
    print("\nTesting conditional caster...")
    test_condition()
    print("\nTesting spell sequence...")
    test_sequence()
    print()


if __name__ == "__main__":
    main()
