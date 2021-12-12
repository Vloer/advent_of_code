from __future__ import annotations
from pathlib import Path
import numpy as np
from collections import Counter


input_file = Path(__file__).parent / "inputs" / "d11.txt"


def parse_input(txt_file: str = input_file) -> list[int]:
    with open(txt_file, 'r') as f:
        return([[int(y) for y in x] for x in f.read().split("\n")])


inp = parse_input()
test_set2 = [[1, 1, 1, 1, 1],
             [1, 9, 9, 9, 1],
             [1, 9, 1, 9, 1],
             [1, 9, 9, 9, 1],
             [1, 1, 1, 1, 1]]
test_set = [[5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
            [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
            [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
            [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
            [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
            [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
            [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
            [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
            [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
            [5, 2, 8, 3, 7, 5, 1, 5, 2, 6]]


def get_adj(data: list[list[int]],  y: int, x: int) -> list[int]:
    result = []
    if x > 0:
        min_x = x - 1
    else:
        min_x = 0
    if x + 1 >= len(data[0]):
        max_x = len(data[0])
    else:
        max_x = x + 2
    if y > 0:
        min_y = y - 1
    else:
        min_y = 0
    if y + 1 >= len(data):
        max_y = len(data)
    else:
        max_y = y + 2
    range_y = range(min_y, max_y)
    range_x = range(min_x, max_x)
    for row in range_y:
        for col in range_x:
            if not (row == y and col == x):
                result.append(data[row][col])
    return result


def solve(data: list[int], steps: int, part2=False) -> int:
    total_flashes = 0
    data = np.array(data)
    for i in range(steps):
        data += 1
        set_to_0 = np.ones_like(data)
        while any([any([num > 9 for num in r]) for r in data]):
            data_to_add = np.zeros_like(data)
            for row in range(len(data)):
                for col in range(len(data[0])):
                    adjacent = get_adj(data, row, col)
                    c = Counter(adjacent)
                    num_flashes = sum([v for k,v in c.items() if k >= 10])
                    data_to_add[row][col] += num_flashes
                    if data[row][col] > 9:
                        set_to_0[row][col] = 0
                        total_flashes += 1
            data += data_to_add
            data *= set_to_0
            if set_to_0.any() == np.zeros_like(data).any() and part2:
                return i+1
    return total_flashes


print(f"Answer 1: {solve(inp, 100)}")
print(f"Answer 2: {solve(inp, 100000, True)}")
