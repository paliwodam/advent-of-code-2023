from collections import Counter

def parse_line(line):
    [card, bid] = line.split()
    return {"card": card, "bid": int(bid)}

def is_five_of_a_kind(counter_values):
    return 5 in counter_values

def is_four_of_a_kind(counter_values):
    return 4 in counter_values

def is_full_house(counter_values):
    return 3 in counter_values and 2 in counter_values

def is_three_of_a_kind(counter_values):
    return sorted(counter_values) == [1, 1, 3]

def is_two_pair(counter_values):
    return sorted(counter_values) == [1, 2, 2]

def is_one_pair(counter_values):
    return sorted(counter_values) == [1, 1, 1, 2]

def is_high_card(counter_values):
    return list(counter_values) == [1, 1, 1, 1, 1]

def get_strength(card):
    functions = [is_five_of_a_kind, is_four_of_a_kind, is_full_house, is_three_of_a_kind, is_two_pair, is_one_pair, is_high_card]
    counter_values = Counter(card).values()
    return max([idx for idx, function in enumerate(functions) if function(counter_values)])
    
def get_relative_strength(card):
    characters = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    value = 0
    for c in card:
        value *= 100
        value += characters.index(c)
    return value

def aoc(input):
    with open(input) as file:
        lines = [line.rstrip() for line in file]

    input = [parse_line(line) for line in lines]
    cards_sorted = sorted(input, key=lambda x: (get_strength(x["card"]), get_relative_strength(x["card"])), reverse=True)
    # for card in cards_sorted:
    #     print(card)
    print(sum([x["bid"] * (idx + 1) for idx, x in enumerate(cards_sorted)]))

aoc("../input.txt")