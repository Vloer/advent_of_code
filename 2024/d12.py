from __future__ import annotations
from pathlib import Path
import time
from typing import Callable, Any
import functools
from collections import defaultdict
from copy import deepcopy
from dataclasses import dataclass


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


def parse_input(txt_file: str = input_file) -> list[str]:
    with open(txt_file, "r") as f:
        return f.read().strip().split("\n")


inp = parse_input()
test = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE""".strip().split(
    "\n"
)


def check_perimeter(grid, pos):
    diags = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    r, c = pos
    letter = grid[r][c]
    perim = 0
    SEEN.append((r, c))
    global PERIM
    for nr, nc in diags:
        rr, cc = r + nr, c + nc
        if rr in range(len(grid)) and cc in range(len(grid[0])):
            if grid[rr][cc] == letter:
                if (rr, cc) not in SEEN:
                    check_perimeter(grid, (rr, cc))
            else:
                perim += 1
        else:
            perim += 1
    AREA.append((r, c, perim))
    PERIM += perim


SEEN = []
AREA = []
PERIM = 0


def add_tuple(t1: tuple[int, int], t2: tuple[int, int]) -> tuple[int, int]:
    r = t1[0] + t2[0]
    c = t1[1] + t2[1]
    return r, c


@timer
def solve1(data: list[str], result: int = 0, p1: bool = True) -> int:
    d = [[y.strip() for y in x] for x in data]
    rows = len(d)
    cols = len(d[0])
    res = []
    global PERIM, AREA
    for r in range(rows):
        for c in range(cols):
            letter = d[r][c]
            if (r, c) not in SEEN:
                check_perimeter(d, (r, c))
                res.append((letter, AREA, PERIM))
                N, NE, E, SE, S, SW, W, NW = (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)
                if p1:
                    s = len(AREA) * PERIM
                    # print(f"A region of {letter} plants with price {len(AREA)} * {PERIM} = {s}.")
                    PERIM = 0
                    AREA = []
                else:
                    area = sorted([(pos[0], pos[1]) for pos in AREA])
                    corners = [
                        # (diagonal, vertical, horizontal) directions for each corner
                        (NW, N, W),  # top left
                        (NE, N, E),  # top right
                        (SW, S, W),  # bottom left
                        (SE, S, E),  # bottom right
                    ]

                    sides = 0
                    for pos in area:
                        for diagonal, vert, horiz in corners:
                            adj_diagonal = add_tuple(pos, diagonal)
                            adj_vert = add_tuple(pos, vert)
                            adj_horiz = add_tuple(pos, horiz)

                            if adj_diagonal not in area and adj_vert not in area and adj_horiz not in area:
                                # 3 free spaces
                                sides += 1
                            elif adj_diagonal in area and adj_vert not in area and adj_horiz not in area:
                                # only diagonal occupied
                                sides += 1
                            elif adj_diagonal not in area and adj_vert in area and adj_horiz in area:
                                # inner corner
                                sides += 1

                    s = sides * len(AREA)
                    # print(f"A region of {letter} plants with price {len(AREA)} * {sides} = {s}.")
                result += s
                PERIM = 0
                AREA = []

    return result


answer_1 = solve1(inp)
SEEN = []
PERIM = 0
AREA = []
answer_2 = solve1(inp, p1=False)
