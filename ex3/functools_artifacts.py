from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Any
from collections.abc import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    ops = {
        "add": add,
        "multiply": mul,
        "max": lambda a, b: a if a > b else b,
        "min": lambda a, b: a if a < b else b
    }
    if operation not in ops:
        print(" Invalid Opperation ", end="")
        return 0
    outcome: int = reduce(ops[operation], spells)
    return outcome


def partial_enchanter(base_enchantment:
                      Callable[..., Any]) -> dict[str, Callable[[str], Any]]:
    return {
        "fire": partial(base_enchantment, 50, "fire"),
        "ice": partial(base_enchantment, 70, "ice"),
        "storm": partial(base_enchantment, 90, "storm")
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return (n)
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def cast_spell(spell: Any) -> str:
        return "Unknown spell type"

    @cast_spell.register
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @cast_spell.register
    def _(spell: str) -> str:
        return f"Entchantment: {spell}"

    @cast_spell.register(list)
    def _(spell: list[Any]) -> str:
        return f"Mulit-cast: {len(spell)} spells"
    return cast_spell


def test_reducer() -> None:
    print("\nTesting Reducer...")
    spells = [1, 2, 3]
    print(f"add: {spell_reducer(spells, 'add')}")
    print(f"multiply: {spell_reducer(spells, 'multiply')}")
    print(f"min: {spell_reducer(spells, 'min')}")
    print(f"max: {spell_reducer(spells, 'max')}")
    print(f"divide (invalid) {spell_reducer(spells, 'divide')}")


def test_enchanter() -> None:
    print("\nTesting Partial Enchanter...")

    def base_entchant(power: int, element: str, target: str) -> str:
        return f"{target} got hit form {element} with {power} damage"
    enchant = partial_enchanter(base_entchant)
    print(f"fire entchant: {enchant['fire']('Dragon')}")
    print(f"ice entchant: {enchant['ice']('Dragon')}")
    print(f"storm entchant: {enchant['storm']('Dragon')}")


def test_memorized() -> None:
    print("\nTesting memorized fibonacci")
    print(f"fib 4: {memoized_fibonacci(4)}")
    print(f"fib 9: {memoized_fibonacci(9)}")
    print(f"fib 6: {memoized_fibonacci(6)}")
    print(f"fib 10: {memoized_fibonacci(10)}")


def test_dispatcher() -> None:
    print("\nTesting Spell dispatcher")
    spells = ["ice", "fire", "lightning"]
    spellcast = spell_dispatcher()
    print(spellcast(30))
    print(spellcast("fireball"))
    print(spellcast(spells))
    print(spellcast(8.08))


def main() -> None:
    test_reducer()
    test_enchanter()
    test_memorized()
    test_dispatcher()


if __name__ == "__main__":
    main()
