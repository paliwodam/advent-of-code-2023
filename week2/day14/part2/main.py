from copy import deepcopy

def print_platform(platform):
    for line in platform:
        print("".join(line))

def tilt_rock(x, y, dx, dy, platform):
    if x < 0 or x + dx < 0 or x >= len(platform) or x + dx >= len(platform):
        return
    if y < 0 or y + dy < 0 or y >= len(platform[0]) or y + dy >= len(platform[0]):
        return
    if platform[x + dx][y + dy] == ".":
        platform[x][y] = "."
        platform[x + dx][y + dy] = "O"
        tilt_rock(x + dx, y + dy, dx, dy, platform)

def tilt_all_rocks(platform, times):
    dx = len(platform)
    dy = len(platform[0])

    pattern = []
    queue = []

    for k in range(times):
        for x in range(dx):
            for y in range(dy):
                if platform[x][y] == "O":
                    tilt_rock(x, y, -1, 0, platform)
                    
        for y in range(dy):
            for x in range(dx):
                if platform[x][y] == "O":
                    tilt_rock(x, y, 0, -1, platform)

        for x in range(dx-1, -1, -1):
            for y in range(dy):
                if platform[x][y] == "O":
                    tilt_rock(x, y, 1, 0, platform)
                
        for y in range(dy-1, -1, -1):
            for x in range(dx):
                if platform[x][y] == "O":
                    tilt_rock(x, y, 0, 1, platform)
        
       
        if k > 100:
            if platform not in pattern:
                pattern.append(deepcopy(platform))
                queue = deepcopy(pattern)
            elif platform == queue[0]:
                queue.pop(0)
            if len(queue) == 0:
                break

    return pattern[(times - k - 2) % len(pattern)]
        
                

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
    platform = tilt_all_rocks(platform, 1000000000)

    print(count_total_load(platform))


aoc("../input.txt")