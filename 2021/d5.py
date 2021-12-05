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

def draw_empty_diagram(inp: list[tuple[int]]) -> np.array:
    max_x = 0
    max_y = 0
    for line in inp:
        x1, y1, x2, y2 = line
        if max(x1, x2) > max_x:
            max_x = max(x1, x2)
        if max(y1, y2) > max_y:
            max_y = max(y1, y2)
    return np.zeros((max_y, max_x), dtype=int)
        
def draw_lines(inp: list[tuple[int]]) -> np.array:
    grid = np.zeros((10000,10000), dtype=int)
    for line in inp:
        x1, y1, x2, y2 = line
        if x1 == x2:
            grid[min(y1,y2):max(y1,y2)+1, x1] += 1
        if y1 == y2:
            grid[y1, min(x1,x2):max(x1,x2)+1] += 1
    print(np.count_nonzero(grid > 1))
    return grid

def solve1() -> None:
    result = 0
    print(f"Answer 1: {result}")


def solve2() -> None:
    result = 0
    print(f"Answer 2: {result}")


draw_lines(inp_parsed)