
def transformLines(lines):
    dx = len(lines)
    dy = len(lines[0])

    return [[[lines[i][j], (i, j)] for j in range(dy)] for i in range(dx)]


def double_column(image):
    dx = len(image)
    dy = len(image[0])

    j = 0
    while j < dy:
        all_empty = True
        for i in range(dx):
            if image[i][j][0] != ".":
                all_empty = False
        if all_empty:
            for k in range(j+1, dy):
                for i in range(dx):
                    x, y = image[i][k][1]
                    image[i][k][1] = (x, y+999999)
        j += 1


def double_row(image):
    dx = len(image)
    dy = len(image[0])

    i = 0
    while i < dx:
        all_empty = True
        for j in range(dy):
            if image[i][j][0] != ".":
                all_empty = False
        if all_empty:
            for k in range(i+1, dx):
                for j in range(dy):
                    x, y = image[k][j][1]
                    image[k][j][1] = (x+999999, y)
        i += 1        


def get_galaxy_positions(image):
    dx = len(image)
    dy = len(image[0])

    return [image[i][j][1] for i in range(dx) for j in range(dy) if image[i][j][0] == "#"]

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

    image = transformLines(lines)
    double_column(image)
    double_row(image)

    positions = get_galaxy_positions(image)
    print(sum_distances(positions))

aoc("../input.txt")