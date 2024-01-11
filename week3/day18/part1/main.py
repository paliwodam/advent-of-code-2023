from queue import Queue

def parse_line(line):
    splited = line.split()
    direction = splited[0]
    meters = int(splited[1])
    rgb = splited[2].strip("()")

    return (direction, meters, rgb)


def get_sizes_and_start_idxs(input):
    max_heigh, max_width = 1,1
    min_heigh, min_width = 0, 0
    curr_heigh, curr_width = 1, 1

    for direction, meters, _ in input:
        if direction == "D":
            curr_heigh += meters
            max_heigh = max(curr_heigh, max_heigh)
        elif direction == "U":
            curr_heigh -= meters
            min_heigh = min(curr_heigh, min_heigh)
        elif direction == "R":
            curr_width += meters
            max_width = max(curr_width, max_width)
        elif direction == "L":
            curr_width -= meters
            min_width = min(curr_width, min_width)

    return max_heigh - min_heigh, max_width - min_width, -min_heigh, -min_width

def dig(i, j, dig_plan, input):
    for direction, meters, _ in input:
        if direction == "D":
            for k in range(i, i+meters+1):
                dig_plan[k][j] = "#"
            i += meters
        elif direction == "U":
            for k in range(i-meters, i+1):
                dig_plan[k][j] = "#"
            i -= meters
        elif direction == "R":
            for k in range(j, j+meters+1):
                dig_plan[i][k] = "#"
            j += meters
        elif direction == "L":
            for k in range(j-meters, j+1):
                dig_plan[i][k] = "#"
            j -= meters

def top_left_idxs(dig_plan):
    for i in range(len(dig_plan)):
        for j in range(len(dig_plan[0])):
            if dig_plan[i][j] == "#":
                return i, j
            
def is_in_range(i, j, dig_plan):
    if i < 0 or i >= len(dig_plan):
        return False
    if j < 0 or j >= len(dig_plan[0]):
        return False
    return True

def dig_interior(i, j, dig_plan):
    dig_directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    dig_queue = Queue()
    dig_queue.put((i, j))

    while not dig_queue.empty():
        i, j = dig_queue.get()
        if dig_plan[i][j] == "#":
            continue
        dig_plan[i][j] = "#"
        for d in dig_directions:
            x, y = i + d[0], j + d[1]
            if is_in_range(x, y, dig_plan) and dig_plan[x][y] == ".":
                dig_queue.put((x, y))


def count_diged(dig_plan):
    diged = 0
    for i in range(len(dig_plan)):
        for j in range(len(dig_plan[0])):
            if dig_plan[i][j] == "#":
                diged += 1
    return diged

def aoc(input):
    with open(input) as file:
        lines = [line.rstrip() for line in file]

    input = [parse_line(line) for line in lines]
    heigh, width, i, j, = get_sizes_and_start_idxs(input)

    dig_plan = [["." for _ in range(width)] for _ in range(heigh)]  

    dig(i, j, dig_plan, input)

    i, j = top_left_idxs(dig_plan)
    dig_interior(i+1, j+1, dig_plan)

    for i in dig_plan:
        print("".join(i))

    print(count_diged(dig_plan))
    


aoc("../input.txt")