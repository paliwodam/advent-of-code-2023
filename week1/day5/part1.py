def change_seed(seed, rules):
    for rule in rules:
        [change, start, length] = [int(x) for x in rule.split()]
        if start <= seed < start + length:
            return change + seed - start
    return seed


def aoc(input):
    with open(input) as file:
        data = file.read()
    seeds, *mappings = data.split("\n\n")
    seeds = seeds.split(":")[1].strip().split()
    seeds = list(map(int, seeds))

    for mapping in mappings:
        _, *rules = mapping.split("\n")
        seeds = list(map(lambda seed: change_seed(seed, rules), seeds))
    print(min(seeds))


aoc("../input.txt")