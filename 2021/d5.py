from __future__ import annotations
from pathlib import Path
import re
import numpy as np

input_file = Path(__file__).parent / "inputs" / "d5.txt"


def parse_input(txt_file: str = input_file) -> list[int]:
    with open(txt_file, 'r') as f:
        return(f.read().split("\n"))


inp = parse_input()
inp_parsed = [
    tuple(map(int, re.findall("(\d+),(\d+) -> (\d+),(\d+)", a)[0])) for a in inp]


def draw_lines(grid: np.array, inp: list[tuple[int]], diagonal=False) -> np.array:
    for line in inp:
        x1, y1, x2, y2 = line
        xcoords = range(min(x1, x2), max(x1, x2)+1)
        ycoords = range(min(y1, y2), max(y1, y2)+1)
        if x1 == x2 or y1 == y2:
            grid[ycoords, xcoords] += 1
        elif diagonal:
            if x1 > x2:
                xcoords = range(x1, x2-1, -1)
            if y1 > y2:
                ycoords = range(y1, y2-1, -1)
            for i in range(len(xcoords)):
                grid[ycoords[i], xcoords[i]] += 1
    return grid


def solve1(template: np.array, inp: list[tuple[int]]) -> None:
    grid = draw_lines(template, inp)
    result = np.count_nonzero(grid > 1)
    print(f"Answer 1: {result}")


def solve2(template: np.array, inp: list[tuple[int]]) -> None:
    grid = draw_lines(template, inp, True)
    result = np.count_nonzero(grid > 1)
    print(f"Answer 2: {result}")


solve1(np.zeros((1000, 1000), dtype=int), inp_parsed)
solve2(np.zeros((1000, 1000), dtype=int), inp_parsed)
