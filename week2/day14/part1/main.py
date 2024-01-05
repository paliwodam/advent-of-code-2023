def tilt_rock(x, y, platform):
    if x <= 0:
        return
    if platform[x-1][y] == ".":
        platform[x][y] = "."
        platform[x-1][y] = "O"
        tilt_rock(x-1, y, platform)

def tilt_all_rocks(platform):
    dx = len(platform)
    dy = len(platform[0])

    for x in range(1, dx):
        for y in range(dy):
            if platform[x][y] == "O":
                tilt_rock(x, y, platform)

def count_total_load(platform):
    dx = len(platform)
    dy = len(platform[0])

    sum = 0
    for x in range(dx):
        for y in range(dy):
            if platform[x][y] == "O":
                sum += dx - x

    return sum

def aoc(input):
    with open(input) as file:
        lines = [line.rstrip() for line in file]

    platform = [[c for c in line] for line in lines]

    tilt_all_rocks(platform)
    print(count_total_load(platform))
    # for line in platform:
    #     print("".join(line))

aoc("../input.txt")