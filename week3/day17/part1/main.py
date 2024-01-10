from math import inf
from queue import PriorityQueue


# def move(x, y, dx, dy, blocks_in_dir, heat, heat_map, visited):
    # if x == len(heat_map) - 1 and y == len(heat_map[0]) - 1:
    #     return heat + heat_map[x][y]
    # if x < 0 or x >= len(heat_map):
    #     return inf
    # if y < 0 or y >= len(heat_map[0]):
    #     return inf

    # heat += heat_map[x][y]

    # if visited[x][y] <= heat:
    #     return inf

    # visited[x][y] = heat    

    # first_move = [move(x + dx, y + dy, dx, dy, blocks_in_dir + 1, heat, heat_map, visited)] if blocks_in_dir < 3 else [] 

    # if dx == 0:
    #     return min(first_move + [move(x + 1, y, 1, 0, 1, heat, heat_map, visited), move(x - 1, y, -1, 0, 1, heat, heat_map, visited)])
    # else:
    #     return min(first_move + [move(x, y + 1, 0, 1, 1, heat, heat_map, visited), move(x, y - 1, 0, -1, 1, heat, heat_map, visited)])


def is_in_range(x, y, n, m):
    return x >= 0 and y >= 0 and x < n and y < m

def aoc(input):
    with open(input) as file:
        lines = [line.rstrip() for line in file]


    heat_map = [[int(c) for c in line] for line in lines]
    n = len(heat_map)
    m = len(heat_map[0])

    queue = PriorityQueue()
    queue.put((heat_map[1][0], 1, 0, 1, 0, 1))
    queue.put((heat_map[0][1], 0, 1, 0, 1, 1))

    min_heat = [[[{(-1, 0): inf, (1, 0): inf, (0, -1): inf, (0, 1): inf} for _ in range(3)] for _ in range(m)] for _ in range(n)]

    while queue:
        heat, x, y, dx, dy, blocks_in_dir = queue.get()
        if heat >= min_heat[x][y][blocks_in_dir-1][(dx, dy)]:
            continue

        min_heat[x][y][blocks_in_dir-1][(dx, dy)] = heat
    
        if x == n-1 and y == m-1:
            break
        if blocks_in_dir < 3:
            if is_in_range(x+dx, y+dy, n, m):
                queue.put((heat + heat_map[x+dx][y+dy], x+dx, y+dy, dx, dy, blocks_in_dir + 1))
        if dx == 0:
            if x+1 < n:
                queue.put((heat + heat_map[x+1][y], x+1, y, 1, 0, 1))
            if x-1 >= 0:
                queue.put((heat + heat_map[x-1][y], x-1, y, -1, 0, 1))
        else:
            if y+1 < m:
                queue.put((heat + heat_map[x][y+1], x, y+1, 0, 1, 1))
            if y-1 >= 0:
                queue.put((heat + heat_map[x][y-1], x, y-1, 0, -1, 1))

    vals = []
    for i in min_heat[n-1][m-1]:
        vals += i.values()
    print(min(vals))
    # print(reduce(lambda a,b: a+b, min_heat[n-1][m-1]))
    # print(min(min_heat[n-1][m-1]))


aoc("../input.txt")