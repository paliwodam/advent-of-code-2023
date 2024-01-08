from collections import defaultdict

def hash(to_hash):
    hash = 0
    for ch in to_hash:
        hash += ord(ch)
        hash *= 17
        hash %= 256
    return hash

def action(x, hashmap):
    if "=" in x:
        splited = x.split("=")
        lens = splited[0]
        num = int(splited[1])
        hashmap[hash(lens)][lens] = num
    else:
        lens = x.rstrip("-")
        if lens in hashmap[hash(lens)]:
            del hashmap[hash(lens)][lens]




def aoc(input):
    with open(input) as file:
        lines = [line.rstrip() for line in file]
        input = "".join(lines).split(",")

    hashmap = defaultdict(dict)
    for x in input:
        action(x, hashmap)

    sum = 0
    for box, content in hashmap.items():
        for i, length in enumerate(content.values()):
            sum += (box + 1) * (i + 1) * length
    print(sum)


aoc("../input.txt")