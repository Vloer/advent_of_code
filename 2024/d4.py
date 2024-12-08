from __future__ import annotations
from pathlib import Path
from time import perf_counter

input_file = Path(__file__).parent / "inputs" / f'{Path(__file__).stem}.txt'


def parse_input(txt_file: str = input_file) -> list[str]:
    with open(txt_file, 'r') as f:
        return f.read().split("\n")


inp = parse_input()
test = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".split('\n')


def solve(data: list[str], result: int = 0, part1=True) -> int:
    data = [[letter for letter in row] for row in data]
    matches = ['XMAS', 'SAMX']
    for i in range(len(data)):
        row = data[i]
        for j in range(len(row)):
            to_add = 0
            try:
                horizontal = data[i][j] + data[i][j + 1] + data[i][j + 2] + data[i][j + 3]
                if horizontal in matches:
                    to_add += 1
            except IndexError:
                ...

            try:
                vertical = data[i][j] + data[i + 1][j] + data[i + 2][j] + data[i + 3][j]
                if vertical in matches:
                    to_add += 1
            except IndexError:
                ...
            try:
                diagonal_front = data[i][j] + data[i + 1][j + 1] + data[i + 2][j + 2] + data[i + 3][j + 3]
                if diagonal_front in matches:
                    to_add += 1
            except IndexError:
                ...
            try:
                if j > 2:
                    diagonal_back = data[i][j] + data[i + 1][j - 1] + data[i + 2][j - 2] + data[i + 3][j - 3]
                    if diagonal_back in matches:
                        to_add += 1
            except IndexError:
                ...
            if not to_add:
                data[i][j] = '.'
            result += to_add
    return result


def solve2(data: list[str], result: int = 0) -> int:
    data = [[letter for letter in row] for row in data]
    for y in range(1, len(data) - 1):
        row = data[y]
        for x in range(1, len(row) - 1):
            if data[y][x] != 'A':
                continue
            top_left = data[y - 1][x - 1]
            top_right = data[y - 1][x + 1]
            bottom_left = data[y + 1][x - 1]
            bottom_right = data[y + 1][x + 1]
            if all([letter in ['M', 'S'] for letter in [top_left, top_right, bottom_right, bottom_left]]):
                if top_left == top_right and bottom_left == bottom_right and top_left != bottom_left:
                    result += 1
                elif top_left == bottom_left and top_right == bottom_right and top_left != top_right:
                    result += 1

    return result


timing_1 = perf_counter()
answer_1 = solve(inp)
print(f"Answer 1 took {perf_counter() - timing_1}: {answer_1}")
timing_2 = perf_counter()
answer_2 = solve2(inp)
print(f"Answer 2 took {perf_counter() - timing_2}: {answer_2}")
