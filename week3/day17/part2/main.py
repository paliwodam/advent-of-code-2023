from math import inf
from queue import PriorityQueue
from collections import defaultdict


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

    min_heat = [[defaultdict(lambda: inf) for _ in range(3) for _ in range(m)] for _ in range(n)]

    while queue:
        heat, x, y, dx, dy, blocks_in_dir = queue.get()
        if heat >= min_heat[x][y][(blocks_in_dir, dx, dy)]:
            continue

        min_heat[x][y][(blocks_in_dir, dx, dy)] = heat
    
        if x == n-1 and y == m-1 and blocks_in_dir >= 4:
            break

        if blocks_in_dir <= 10 and is_in_range(x+dx, y+dy, n, m):
            queue.put((heat + heat_map[x+dx][y+dy], x+dx, y+dy, dx, dy, blocks_in_dir + 1))
        if blocks_in_dir >= 4:
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

    min_val = inf
    for (block_in_dir, _, _), val in min_heat[n-1][m-1].items():
        if block_in_dir >= 4:
            min_val = min(min_val, val)
    print(min_val)

aoc("../input.txt")