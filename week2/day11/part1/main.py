

def double_column(image):
    dx = len(image)
    dy = len(image[0])

    j = 0
    while j < dy:
        all_empty = True
        for i in range(dx):
            if image[i][j] != ".":
                all_empty = False
        if all_empty:
            for i in range(dx):
                image[i] = image[i][:j] + "." + image[i][j:] 
            j += 1
        j += 1


def double_row(image):
    dx = len(image)
    i = 0
    while i < dx:
        if all([True if x == "." else False for x in image[i]]):
            image.insert(i, image[i])
            i += 1
        i += 1


def get_galaxy_positions(image):
    dx = len(image)
    dy = len(image[0])

    return [(i, j) for i in range(dx) for j in range(dy) if image[i][j] == "#"]

def sum_distances(positions):
    n = len(positions)
    sum = 0
    
    for i in range(n):
        for j in range(i+1, n):
            dist = abs(positions[i][0] - positions[j][0]) + abs(positions[i][1] - positions[j][1])
            sum +=  dist

    return sum


def aoc(input):
    with open(input) as file:
        lines = [line.rstrip() for line in file]

    double_column(lines)
    double_row(lines)

    positions = get_galaxy_positions(lines)
    print(sum_distances(positions))

aoc("../input.txt")