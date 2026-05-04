from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:

    def accumulation(add: int) -> int:
        nonlocal initial_power
        initial_power += add
        return initial_power
    return accumulation


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def item(item: str) -> str:
        return f"{enchantment_type} {item}"
    return item


def memory_vault() -> dict[str, Callable[..., Any]]:
    stored: dict[str, Any] = {}

    def store(key: str, value: Any) -> str:
        stored[key] = value
        return f"'{key}' = {value}"

    def recall(key: str) -> str:
        return f"'{key}': {stored.get(key, 'Memory not found')}"
    return {"stored": store, "recall": recall}


def counter_test() -> None:
    print("\nTesting mage counter...")
    count = mage_counter()
    print(f"counter1: {count()}")
    print(f"counter1: {count()}")
    count1 = mage_counter()
    print("\nsecond counter incomming...")
    print(f"counter2: {count1()}")
    print(f"counter2: {count1()}")
    print(f"counter1: {count()}")
    print(f"counter1: {count()}")


def test_accumulator() -> None:
    print("\nTesting spell accumulator...")
    accumulate = spell_accumulator(45)
    print(f"start: {accumulate(0)}")
    print(f"add 10: {accumulate(10)}")
    print(f"add another 12: {accumulate(12)}")


def test_enchantment() -> None:
    print("\nTesting enchantmant factory...")
    enchant1 = enchantment_factory("Glorious")
    enchant2 = enchantment_factory("Frozwn")
    enchant3 = enchantment_factory("Flaming")
    print(enchant1("sword"))
    print(enchant2("shield"))
    print(enchant3("knife"))


def test_memory() -> None:
    print("\nTesting memory")
    memory = memory_vault()
    print(f"Store {memory['stored']('secret', 42)}")
    print(f"Recall {memory['recall']('secret')}")
    print(f"Recall {memory['recall']('Unknown')}")


def main() -> None:
    counter_test()
    test_accumulator()
    test_enchantment()
    test_memory()


if __name__ == "__main__":
    main()
