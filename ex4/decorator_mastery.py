from functools import wraps
import time
from typing import Any
from collections.abc import Callable


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(target: str, power: int) -> Any:
        print(f"Casing {func.__name__}...")

        start = time.time()
        result = func(target, power)
        end = time.time()
        duration = start - end
        print(f"Spell completed in {duration:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power:
                    int) -> Callable[[Callable[...,
                                               Any]], Callable[..., str]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., str]:
        @wraps(func)
        def wrapper(target: str, power: int) -> str:
            if (power >= min_power):
                result = func(target, power)
                return f"{func.__name__}: {result}"
            else:
                return "power is to low"
        return wrapper
    return decorator


def retry_spell(max_attempts:
                int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(target: str, power: int) -> Any:
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(target, power)
                except Exception:
                    attempts += 1
                    print(f"spell failed retrying... (attempt{attempts}/"
                          f"{max_attempts})")
            return "Spell Casting failed after 3 attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        i = 0
        if len(name) < 3:
            return False
        while i < len(name):
            if not name[i].isalpha() and not name[i].isspace():
                return False
            i += 1
        return True

    def cast_spell(self, spell_name: str, power: int) -> str:

        @power_validator(30)
        def cast(target: str, power: int) -> str:
            return (f"{spell_name} successfully casted: "
                    f"hit {target} with {power}")
        return cast(spell_name, power)


def test_timer() -> None:
    print("\nTesting spell Time...\n")

    def fireball(target: str, power: int) -> str:
        time.sleep(5.157)
        return f"{target} got hit with {power} damage"

    def lightning(target: str, power: int) -> str:
        time.sleep(1.90)
        return f"{target} got hit with {power} damage"
    timer = spell_timer(fireball)
    timer2 = spell_timer(lightning)
    print(timer("Dragon", 70))
    print(timer2("Human", 150))


def test_validator() -> None:
    print("\nTesting Power Validator...")

    @power_validator(60)
    def fireball(target: str, power: int) -> str:
        return f"{target} got hit with {power} damage"

    @power_validator(60)
    def lightning(target: str, power: int) -> str:
        return f"{target} got hit with {power} damage"
    # validator = power_validator(60)
    # func = validator(fireball)
    # func2 = validator(lightning)
    # print(func("Dragon", 55))
    # print(func2("human", 70))
    print(fireball("Dragon", 55))
    print(lightning("Human", 70))


def test_retry() -> None:
    print("\nTesting retrying spell...")
    initial_power = 90

    @retry_spell(7)
    def success(target: str, power: int) -> str:
        return f"spell hit {target} with {power}"

    @retry_spell(7)
    def fail(target: str, power: int) -> str:
        nonlocal initial_power
        if initial_power > power:
            initial_power -= 10
            raise Exception
        else:
            return f"spell hit {target} whith {power}"

    print(success("Dragon", 800))
    print()
    print(fail("Human", 60))


def test_mageguild() -> None:
    print("\nTesting MageGuild...")
    names = ["Aron", "vlad", "H", "1234a", 'ralf schumacher']
    for i in names:
        print(MageGuild.validate_mage_name(i))
    spell = MageGuild()
    print(spell.cast_spell("fireball", 50))
    print(spell.cast_spell("lightning", 15))


def main() -> None:
    test_timer()
    test_validator()
    test_retry()
    test_mageguild()
    print()


if __name__ == "__main__":
    main()
