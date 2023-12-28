def check_line(pattern, line_low_idx):
    n = len(pattern)
    i, j = line_low_idx, line_low_idx + 1

    while i >= 0 and j < n:
        if pattern[i] != pattern[j]:
            return False
        i -= 1
        j += 1
    
    return True


def pattern_notes(pattern):
    horizontal = [[pattern[i][j] for j in range(len(pattern[0]))] for i in range(len(pattern))] 
    vertical = [[pattern[i][j] for i in range(len(pattern))] for j in range(len(pattern[0]))] 

    horizontal_line = 0
    for i in range(len(horizontal) - 1):
        if check_line(horizontal, i):
            horizontal_line = i + 1
    
    vertical_line = 0
    for i in range(len(vertical) - 1):
        if check_line(vertical, i):
            vertical_line = i + 1
        
    return vertical_line + horizontal_line * 100
    


def aoc(input):
    with open(input) as file:
        data = file.read()

    patterns = [pattern.split() for pattern in data.split("\n\n")]

    print(sum([pattern_notes(pattern) for pattern in patterns]))

aoc("../test.txt")