from Levenshtein import distance 

def check_line(pattern, line_low_idx):
    n = len(pattern)
    i, j = line_low_idx, line_low_idx + 1

    while i >= 0 and j < n:
        if pattern[i] != pattern[j]:
            return False
        i -= 1
        j += 1
    
    return True


def repaired_smudge(pattern, line_low_idx):
    n = len(pattern)
    i, j = line_low_idx, line_low_idx + 1

    idx, to_change = None, None
    while i >= 0 and j < n:
        if distance(pattern[i], pattern[j]) > 1:
            return False
        if distance(pattern[i], pattern[j]) == 1:
            if idx is not None:
                return False
            idx, to_change = i, pattern[j]
        i -= 1
        j += 1
    
    if idx is not None:
        pattern[idx] = to_change
        return True
    return False


def single_pattern_note(pattern):
    for i in range(len(pattern) - 1):
        if repaired_smudge(pattern, i):
            return True, i+1
    return False, 0


def pattern_notes(pattern):
    horizontal = [[pattern[i][j] for j in range(len(pattern[0]))] for i in range(len(pattern))] 
    vertical = [[pattern[i][j] for i in range(len(pattern))] for j in range(len(pattern[0]))] 

    reapired_horizontal, horizontal_line = single_pattern_note(horizontal)

    if reapired_horizontal:
        return horizontal_line * 100

    _, vertical_line = single_pattern_note(vertical)
    return vertical_line 
    


def aoc(input):
    with open(input) as file:
        data = file.read()

    patterns = [pattern.split() for pattern in data.split("\n\n")]

    print(sum([pattern_notes(pattern) for pattern in patterns]))

aoc("../input.txt")