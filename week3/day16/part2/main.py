from enum import Enum
import sys

class Direction(Enum):
    NORTH = (-1, 0)
    WEST = (0, -1)
    SOUTH = (1, 0)
    EAST = (0, 1)

    @staticmethod
    def direction_forward_slash(direction):
        if direction == Direction.EAST:
            return Direction.NORTH
        if direction == Direction.WEST:
            return Direction.SOUTH
        if direction == Direction.NORTH:
            return Direction.EAST
        if direction == Direction.SOUTH:
            return Direction.WEST
        
    @staticmethod
    def direction_backslash(direction):
        if direction == Direction.EAST:
            return Direction.SOUTH
        if direction == Direction.WEST:
            return Direction.NORTH
        if direction == Direction.NORTH:
            return Direction.WEST
        if direction == Direction.SOUTH:
            return Direction.EAST
    
    @staticmethod
    def directions_vertical_splitter(direction):
        if direction == Direction.NORTH or direction == Direction.SOUTH:
            return [direction]
        return [Direction.NORTH, Direction.SOUTH]

    @staticmethod
    def directions_horizontal_splitter(direction):
        if direction == Direction.WEST or direction == Direction.EAST:
            return [direction]
        return [Direction.WEST, Direction.EAST]

            

def move_beam(direction: Direction, x: int, y: int, layout, visited):
    while x >= 0 and x < len(layout) and y >= 0 and y < len(layout[0]):     
        if direction in visited[x][y]:
            return
        visited[x][y].add(direction)

        if layout[x][y] == "/":
            direction = Direction.direction_forward_slash(direction)
        elif layout[x][y] == "\\":
            direction = Direction.direction_backslash(direction)
        elif layout[x][y] == "-" or layout[x][y] == "|":
            if layout[x][y] == "-":
                directions = Direction.directions_horizontal_splitter(direction)
            else:
                directions = Direction.directions_vertical_splitter(direction)
            if len(directions) == 2:
                new_x = x + directions[1].value[0]
                new_y = y + directions[1].value[1]
                move_beam(directions[1], new_x, new_y, layout, visited) 
            direction = directions[0]

        x =  x + direction.value[0]
        y = y + direction.value[1]
    return

def get_total_energized(visited):
    sum = 0
    for i in visited:
        for j in i:
            if len(j) != 0:
                sum += 1
    return sum
        

def aoc(input):
    with open(input) as file:
        lines = [line.rstrip() for line in file]

    layout = [[c for c in line] for line in lines]

    n = len(layout)
    m = len(layout[0])

    start_placement =  [(0, i, Direction.SOUTH) for i in range(m)]
    start_placement +=  [(n - 1, i, Direction.NORTH) for i in range(m)] 
    start_placement += [(i, 0, Direction.EAST) for i in range(n)] 
    start_placement += [(i, m - 1, Direction.WEST) for i in range(n)]

    max_energized = 0
    for x, y, direction in start_placement:
            visited = [[set() for _ in i] for i in layout]
            move_beam(direction, x, y, layout, visited)
            max_energized = max(max_energized, get_total_energized(visited))
                
    print(max_energized)


aoc("../input.txt")