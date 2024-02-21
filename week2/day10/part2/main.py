from enum import Enum

def is_in_range(i, j, arr):
    if i < 0 or i >= len(arr):
        return False
    if j < 0 or j >= len(arr[i]):
        return False
    return True

def loop_starting_point(data):
    i, j = [(i, j) for i, row in enumerate(data) for j, char in enumerate(row) if char == 'S'][0]
    directions = set()
    if i - 1 >= 0 and data[i-1][j] in ["|", "7", "F"]:
        directions.add("south")
    if i + 1 < len(data) and data[i+1][j] in ["|", "L", "J"]:
        directions.add("north")
    if j - 1 >= 0 and data[i][j-1] in ["-", "L", "F"]:
        directions.add("west")
    if j + 1 < len(data[i]) and data[i][j+1] in ["-", "7", "J"]:
        directions.add("east")
    
    print(directions)

    if "west" in directions and "east" in directions:
        data[i][j] = "-"
    elif "south" in directions and "north" in directions:
        data[i][j] = "|"
    elif "north" in directions and "east" in directions:
        data[i][j] = "F"
    elif "north" in directions and "west" in directions:
        data[i][j] = "7"
    elif "south" in directions and "east" in directions:
        data[i][j] = "L"
    elif "south" in directions and "west" in directions:
        data[i][j] = "J"
    else:
        print(directions)
        data[i][j] = "!"

    return i, j
        

def mark_loop(x, y, visited, data):
    queue = [(x, y)]
    while len(queue) != 0:
        i, j = queue.pop()
        if not is_in_range(i, j, data):
            continue
        if visited[i][j]:
            continue
        
        visited[i][j] = True

        neigh = {
            "|": [(1, 0), (-1, 0)], 
            "-": [(0, 1), (0, -1)], 
            "L": [(-1, 0), (0, 1)], 
            "J": [(-1, 0), (0, -1)],
            "7": [(1, 0), (0, -1)],
            "F": [(1, 0), (0, 1)],
            "S": []
            }
        
        for di, dj in neigh[data[i][j]]:
            if is_in_range(i+di, j+dj, visited) and not visited[i+di][j+dj]:
                queue.append((i+di, j+dj))
    
def mark_outside(data):
    for i in range(len(data)):
    # for i in range(1, 2):
        left_pipe, prev_pipe = None, None
        for j in range(len(data[0])):
            if data[i][j] in ["|", "L", "F", "J", "7"]:
                if not left_pipe:
                    if data[i][j] == "J" and prev_pipe == "F":
                        left_pipe = None
                    elif data[i][j] == "7" and prev_pipe == "L":
                        left_pipe = None
                    else:
                        left_pipe = data[i][j]
                elif data[i][j] == "J" and left_pipe == "F":
                    left_pipe = "J"
                elif data[i][j] == "7" and left_pipe == "L":
                    left_pipe = "7"
                else:
                    left_pipe = None
                    
                prev_pipe = data[i][j]

            elif left_pipe and data[i][j] == ".":
                data[i][j] = "*"
            # print(j, left_pipe, prev_pipe)
                

def count_star(data):
    count = 0
    for row in data:
        for elem in row:
            if elem == "*":
                count += 1
    return count

def aoc(input):     
    with open(input) as file:
        data = [list(line.rstrip()) for line in file]
    i, j = loop_starting_point(data)

    visited = [[False for _ in row] for row in data]
    mark_loop(i, j, visited, data)

    for x in range(len(visited)):
        for y in range(len(visited[0])):
            if not visited[x][y]:
                data[x][y] = "."

    mark_outside(data)
    print(count_star(data))



aoc("../test.txt")