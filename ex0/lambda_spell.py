artifacts = [{'name': 'Wind Cloak', 'power': 67, 'type': 'relic'}, {'name': 'Storm Crown', 'power': 116, 'type': 'weapon'}, {'name': 'Crystal Orb', 'power': 120, 'type': 'armor'}, {'name': 'Light Prism', 'power': 81, 'type': 'accessory'}]
mages = [{'name': 'Storm', 'power': 83, 'element': 'wind'}, {'name': 'Riley', 'power': 69, 'element': 'light'}, {'name': 'Riley', 'power': 100, 'element': 'water'}, {'name': 'Kai', 'power': 86, 'element': 'water'}, {'name': 'Phoenix', 'power': 72, 'element': 'ice'}]
spells = ['freeze', 'darkness', 'lightning', 'earthquake']


def artifact_sorter(artifacts: list[dict]):
    sort = sorted(artifacts, key=lambda p: p['power'], reverse=True)
    return sort

def power_filter(mages : list[dict], min_power: int):
    minpow = list(filter(lambda m: m['power'] >= min_power, mages))
    return minpow

def spell_transformer(spells: list[str]):
    spell = list(map(lambda x: '* ' + x + ' *', spells))
    return spell

def mage_stats(mages: list[dict]):
    max_mage = max(mages, key=lambda x: x['power'], )['power']
    min_mage = min(mages, key=lambda x: x['power'], )['power']
    av_mage = round(sum(m['power'] for m in mages) / len(mages), 2)
    return {
        'max_power': max_mage,
        'min_power': min_mage,
        'average_power': av_mage
            }

def test_sorter():
    print("\ntesting artifact sorter...")
    sorted_dict = artifact_sorter(artifacts)
    i = 0
    for dict in sorted_dict:
        while i < len(sorted_dict) - 1:
            for key, value in dict.items():
                if key == "name":
                    name = value
                if key == "power":
                    power = value
            print(f"{name} ({power}) comes befor, ", end= "")
            break
        i += 1
    last = sorted_dict[len(sorted_dict) -1]
    for key, value in last.items():
        if key == "name":
            name = value
        if key == "power":
            power = value
    print(f"{name} ({power})")


def test_filter():
    print("\ntesting power filter...")
    filtered_dict = power_filter(mages, 80)
    print("still in the list:", end= "")
    for element in filtered_dict:
        for key, value in element.items():
            if key == "name":
                name = value
            if key == "power":
                power = value
            if key == "element":
                element = value
        print(f" {name} power({power}) with element: ({element}) ", end="")
    print()


def test_transformer():
    print("\ntesting spell transformer...")
    transformed_str = spell_transformer(spells)
    for spell in transformed_str:
        print(spell, end=" ")
    print()


def test_stats():
    print("\ntesting mage stats... ")
    stats = mage_stats(mages)
    for key, value in stats.items():
        if key == "max_power":
            max_p = value
        if key == "min_power":
            min_p = value
        if key == "average_power":
            av_p = value
    print(f"max Power: {max_p}, Min Power: {min_p}, Average Power: {av_p}")


def main():
    test_sorter()
    test_filter()
    test_transformer()
    test_stats()
    print()

if __name__ == "__main__":
    main()