def hash(to_hash):
    hash = 0
    for ch in to_hash:
        hash += ord(ch)
        hash *= 17
        hash %= 256
    return hash

def aoc(input):
    with open(input) as file:
        lines = [line.rstrip() for line in file]
        input = "".join(lines).split(",")

    hashes = [hash(x) for x in input]
    print(sum(hashes))


aoc("../input.txt")