from __future__ import annotations
from pathlib import Path
import math

input_file = Path(__file__).parent / "inputs" / "d9.txt"


def parse_input(txt_file: str = input_file) -> list[int]:
    with open(txt_file, 'r') as f:
        return ([list(map(int, x)) for x in f.read().split("\n")])


inp = parse_input()
test_set = ['2199943210',
            '3987894921',
            '9856789892',
            '8767896789',
            '9899965678']
test_set = [list(map(int, x)) for x in test_set]


def get_neighbours(mat: list[list[int]], curpos: tuple(int)) -> list[int]:
    adjacent = []
    row = curpos[0]
    pos = curpos[1]
    if pos > 0:
        adjacent.append(mat[row][pos - 1])
    if pos + 1 < len(mat[0]):
        adjacent.append(mat[row][pos + 1])
    if row > 0:
        adjacent.append(mat[row - 1][pos])
    if row + 1 < len(mat):
        adjacent.append(mat[row + 1][pos])
    return adjacent


def solve1(heightmap: list[list[int]]) -> int:
    result = 0
    for row in range(len(heightmap)):
        for pos in range(len(heightmap[0])):
            cur = heightmap[row][pos]
            adjacent = get_neighbours(heightmap, (row, pos))
            if all(i > cur for i in adjacent):
                result += cur + 1
    return result


def solve2(heightmap: list[list[int]]) -> int:
    '''
    als je een laagste vind ga vanuit daar recursive kijken of je nog omhoog kan <9
    dit voor elk getal tot je een 9 tegen komt of niet omhoog kan
    '''

    result = 0
    return result


print(f"Answer 1: {solve1(inp)}")
print(f"Answer 2: {solve2(inp)}")
