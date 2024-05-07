def format_seeds(seeds):
    seeds_split = seeds.split(":")[1].strip().split()
    seeds_int = list(map(int, seeds_split))
    return [[s, s+r-1] for s, r in zip(seeds_int[::2], seeds_int[1::2])]

def format_rules(rules):
    rules_int = [list(map(int, rule.split())) for rule in rules]
    return list(map(lambda x: [x[0] - x[1], x[1], x[1] + x[2] - 1], rules_int))

def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals:
        previous = merged[-1]
        if current[0] <= previous[1] + 1:  
            previous[1] = max(previous[1], current[1])
        else:
            merged.append(current)

    return merged
    
def change_seeds(seeds_pairs, rules):
    new_seeds_pairs = []
    for pair in seeds_pairs:
        [seed_start, seed_end] = pair
        changed = False
        for rule in rules:
            [difference, range_start, range_end] = rule
            change_start = max(seed_start, range_start)
            change_end = min(seed_end, range_end)
            if change_end >= change_start:
                new_seeds_pairs.append([change_start + difference, change_end + difference])
                if seed_start < change_start:
                    seeds_pairs.append([seed_start, change_start-1])
                if seed_end > change_end:
                    seeds_pairs.append([change_end+1, seed_end])
                changed = True
                break
        if not changed:
            new_seeds_pairs.append(pair)
    return merge_intervals(new_seeds_pairs)
    
            

def aoc(input):
    with open(input) as file:
        data = file.read()
    seeds, *mappings = data.split("\n\n")
    seeds = format_seeds(seeds)

    for mapping in mappings:
        _, *rules = mapping.split("\n")
        rules = format_rules(rules)
        seeds = change_seeds(seeds, rules)
    print(seeds[0][0])


aoc("../input.txt")