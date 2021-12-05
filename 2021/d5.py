from __future__ import annotations
from pathlib import Path
import re
import numpy as np

input_file = Path(__file__).parent / "inputs" / "d5.txt"


def parse_input(txt_file: str = input_file) -> list[int]:
    with open(txt_file, 'r') as f:
        return(f.read().split("\n"))


inp = parse_input()
inp_parsed = [tuple(map(int, re.findall("(\d+),(\d+) -> (\d+),(\d+)", a)[0])) for a in inp]


def draw_lines(inp: list[tuple[int]], diagonal = False) -> np.array:
    grid = np.zeros((10000,10000), dtype=int)
    for line in inp:
        x1, y1, x2, y2 = line
        xcoords = range(min(x1,x2), max(x1,x2)+1)
        ycoords = range(min(y1,y2), max(y1,y2)+1)
        if x1 == x2 or y1 == y2:
            grid[ycoords, xcoords] += 1
        elif diagonal:
            for x, y in xcoords, ycoords:
              
    return grid

def solve1(inp: list[tuple[int]]) -> None:
    grid = draw_lines(inp)
    result = np.count_nonzero(grid > 1)
    print(f"Answer 1: {result}")


def solve2() -> None:
    result = 0
    print(f"Answer 2: {result}")

solve1(inp_parsed)