from __future__ import annotations
from pathlib import Path
import time
from typing import Callable, Any
import functools
from collections import Counter, defaultdict


def timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' took {execution_time:.4f} seconds to execute and returned {result}")
        return result

    return wrapper


input_file = Path(__file__).parent / "inputs" / f"{Path(__file__).stem}.txt"


def parse_input(txt_file: str = input_file) -> str:
    with open(txt_file, "r") as f:
        return f.read()


inp = parse_input()
test = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""


@timer
def solve1(data: str, result: int = 0) -> int:
    data = [[x for x in r] for r in data.split("\n")]
    nodes = defaultdict(list)

    # Find nodes
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            if col in [".", "#"]:
                continue
            nodes[col].append((i, j))

    # Check if positions are in line and calculate position of antinode
    m = len(data)
    antinodes = []
    for node, positions in nodes.items():
        for pos in positions:
            # check distance to other positions
            for other in positions:
                if other == pos:
                    continue
                p1r, p1c = pos
                p2r, p2c = other
                dr = abs(p1r - p2r)
                dc = abs(p1c - p2c)
                if p1r > p2r:
                    a1r = p1r + dr
                    a2r = p2r - dr
                else:
                    a1r = p1r - dr
                    a2r = p2r + dr
                if p1c > p2c:
                    a1c = p1c + dc
                    a2c = p2c - dc
                else:
                    a1c = p1c - dc
                    a2c = p2c + dc
                if 0 <= a1r < m and 0 <= a1c < m:
                    antinodes.append((a1r, a1c))
                if 0 <= a2r < m and 0 <= a2c < m:
                    antinodes.append((a2r, a2c))

    result = len(set(antinodes))
    return result


@timer
def solve2(data: str) -> int:
    data = [[x for x in r] for r in data.split("\n")]
    nodes = defaultdict(list)
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            if col in [".", "#"]:
                continue
            nodes[col].append((i, j))

    m = len(data)
    n = []
    for node, positions in nodes.items():
        for pos in positions:
            for other in positions:
                if other == pos:
                    continue
                p1r, p1c = pos
                p2r, p2c = other
                dr = abs(p1r - p2r)
                dc = abs(p1c - p2c)
                next_r, next_c = other
                while 0 <= next_r < m and 0 <= next_c < m:
                    n.append((next_r, next_c))
                    next_r += dr * (-1 if p1r > p2r else 1)
                    next_c += dc * (-1 if p1c > p2c else 1)

    result = len(set(n))
    print_grid(data, n)
    return result


def print_grid(grid, antinodes):
    for n in antinodes:
        r, c = n
        if grid[r][c] == ".":
            grid[r][c] = "#"
    for i, row in enumerate(grid):
        print(f"{str(i):<3}: {' '.join(row)}")


answer_1 = solve1(inp)
answer_2 = solve2(inp)
