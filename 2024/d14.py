from __future__ import annotations
from pathlib import Path
import time
from typing import Callable, Any
from collections import defaultdict
import functools
import re
from math import prod


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
        return f.read().split("\n")


inp = parse_input()
test = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3""".split(
    "\n"
)


def get_pos(start, speed, grid_size, seconds) -> tuple[int, int]:
    new_x, new_y = start
    vx, vy = speed
    max_x = grid_size[0] - 1
    max_y = grid_size[1] - 1
    for _ in range(seconds):
        # p(11, 7, (new_x, new_y))
        new_x, new_y = new_x + vx, new_y + vy
        if new_x > max_x:
            new_x = new_x - max_x - 1
        elif new_x < 0:
            new_x = max_x + new_x + 1
        if new_y > max_y:
            new_y = new_y - max_y - 1
        elif new_y < 0:
            new_y = max_y + new_y + 1
    return new_x, new_y


def p(x, y, pos):
    grid = [["."] * x for i in range(y)]
    grid[pos[1]][pos[0]] = 'X'
    for i in grid:
        print(i)
    print()

def print_grid(x, y, positions):
    grid = [["."] * y for i in range(x)]
    for a, b in positions:
        grid[a][b] = "X"
    for i in grid:
        print(i)
    print()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if row == x // 2:
                grid[row][col] = "="
            if col == y // 2:
                grid[row][col] = "||"
    for i in grid:
        print(i)


@timer
def solve1(data: list[str], result: int = 0) -> int:
    pat = r"p=(\d+\,\d+) v=(-?\d+,-?\d+)"
    range_x = 101
    range_y = 103
    robot_final_positions = []
    for line in data:
        p, v = re.findall(pat, line)[0]
        px, py = map(int, p.split(","))
        vx, vy = map(int, v.split(","))
        robot_final_positions.append(get_pos((px, py), (vx, vy), (range_x, range_y), 100))

    # Check quadrants
    middle_x = range_x // 2
    middle_y = range_y // 2
    quadrants = defaultdict(int)
    for x, y in robot_final_positions:
        if x == middle_x or y == middle_y:
            continue
        if x < middle_x and y < middle_y:
            quadrants["NW"] += 1
        elif x < middle_x and y > middle_y:
            quadrants["SW"] += 1
        elif x > middle_x and y < middle_y:
            quadrants["NE"] += 1
        elif x > middle_x and y > middle_y:
            quadrants["SE"] += 1
    print_grid(range_x, range_y, robot_final_positions)
    print(quadrants)
    result = prod(quadrants.values())
    return result


@timer
def solve2(data: list[str], result: int = 0) -> int:
    pat = r"p=(\d+\,\d+) v=(-?\d+,-?\d+)"
    range_x = 101
    range_y = 103
    seconds = 100
    robot_final_positions = []
    for i in range(seconds):
        for line in data:
            p, v = re.findall(pat, line)[0]
            px, py = map(int, p.split(","))
            vx, vy = map(int, v.split(","))
            robot_final_positions.append(get_pos((px, py), (vx, vy), (range_x, range_y), 100))
    return result


answer_1 = solve1(inp)
answer_2 = solve2(inp)
