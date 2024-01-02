from typing import List
from copy import deepcopy


def is_valid_line(records: List[str], sizes: List[int]):
    n, m = len(records), len(sizes)
    prev_size = 0
    
    i, j = 0, 0
    while i < n and j < m:
        if records[i] == "?":
            return True
        if records[i] == "#":
            prev_size += 1
        if records[i] == "." and prev_size != 0:
            if sizes[j] != prev_size:
                return False
            j += 1
            prev_size = 0  
        i += 1

    if j < m:
        if prev_size != sizes[j]:
            return False
        if j + 1 < m:
            return False
    
    if i < n and not all([False for x in records[i:] if x == "#"]):
        return False

    return True

def arregements_number(idx: int, records: List[str], sizes: List[str]):
    if not is_valid_line(records, sizes):
        return 0
             
    if idx == len(records):
        return 1
        
    if records[idx] == "?":
        records_copy1 = deepcopy(records)
        records_copy1[idx] = "."
        
        records_copy2 = deepcopy(records)
        records_copy2[idx] = "#"

        return arregements_number(idx+1, records_copy1, sizes) + arregements_number(idx+1, records_copy2, sizes)

    return arregements_number(idx+1, records, sizes)

def sum_arregements_number(lines):
    return sum([arregements_number(0, line[0], line[1]) for line in lines])

def str_records_to_list(records: str):
    return [x for x in records]

def str_sizes_to_list(sizes: str):
    return [int(x) for x in sizes.split(",")]

def transform_lines(lines: List[List[str]]):
    return [[str_records_to_list(line[0]), str_sizes_to_list(line[1])] for line in lines]


def aoc(input):
    with open(input) as file:
        lines = [line.rstrip().split() for line in file]

    lines = transform_lines(lines)

    print(sum_arregements_number(lines))


aoc("../input.txt")