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


def continue_upwards(mat: list[list[int]], starting_pos: tuple(int), size=1, positions_already_checked=[]) -> int:
    row = starting_pos[0]
    pos = starting_pos[1]
    height = mat[row][pos]
    # go right
    if pos + 1 < len(mat[0]):
        new_row = row
        new_pos = pos + 1
        new_height = mat[new_row][new_pos]
        if new_height > height and new_height < 9 and (new_row, new_pos) not in positions_already_checked:
            size += 1
            size = continue_upwards(
                mat, (new_row, new_pos), size, positions_already_checked)
            positions_already_checked.append((new_row, new_pos))

    # go left
    if pos > 0:
        new_row = row
        new_pos = pos - 1
        new_height = mat[new_row][new_pos]
        if new_height > height and new_height < 9 and (new_row, new_pos) not in positions_already_checked:
            size += 1
            size = continue_upwards(
                mat, (new_row, new_pos), size, positions_already_checked)
            positions_already_checked.append((new_row, new_pos))

    # go down
    if row + 1 < len(mat):
        new_row = row + 1
        new_pos = pos
        new_height = mat[new_row][new_pos]
        if new_height > height and new_height < 9 and (new_row, new_pos) not in positions_already_checked:
            size += 1
            size = continue_upwards(
                mat, (new_row, new_pos), size, positions_already_checked)
            positions_already_checked.append((new_row, new_pos))

    # go up
    if row > 0:
        new_row = row - 1
        new_pos = pos
        new_height = mat[new_row][new_pos]
        if new_height > height and new_height < 9 and (new_row, new_pos) not in positions_already_checked:
            size += 1
            size = continue_upwards(
                mat, (new_row, new_pos), size, positions_already_checked)
            positions_already_checked.append((new_row, new_pos))
    return size


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
    result = []
    for row in range(len(heightmap)):
        for pos in range(len(heightmap[0])):
            cur = heightmap[row][pos]
            adj = get_neighbours(heightmap, (row, pos))
            if all(i > cur for i in adj):
                result.append(continue_upwards(heightmap, (row, pos)))
    result.sort(reverse=True)
    final_result = math.prod(result[:3])
    return final_result


print(f"Answer 1: {solve1(inp)}")
print(f"Answer 2: {solve2(inp)}")
