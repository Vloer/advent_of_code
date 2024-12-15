from __future__ import annotations
from pathlib import Path
import time
from copy import deepcopy
from typing import Callable, Any
import functools


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
test = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732""".split(
    "\n"
)


def get_adj(grid, pos):
    row, col = pos
    adjacent = []
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        try:
            new_row = row + dx
            new_col = col + dy
            if new_row >= 0 and new_col >= 0:
                new_pos = row + dx, col + dy
                value = grid[row + dx][col + dy]
                adjacent.append((value, new_pos))
        except IndexError:
            pass
    return adjacent


TOTAL = 0


def p(d, pos):
    dd = deepcopy(d)
    dd[pos[0]][pos[1]] = "X"
    for x in dd:
        print(x)


def check_path(grid, pos, current_path, all_paths, seen):
    val = grid[pos[0]][pos[1]]
    seen.add(pos)
    if val == 9:
        all_paths.append(current_path)
        return

    for new_val, new_pos in get_adj(grid, pos):
        if new_val == val + 1 and new_pos not in seen:
            current_path.append(new_pos)
            check_path(grid, new_pos, current_path, all_paths, seen)
            current_path.pop()


def check_path2(grid, pos):
    global TOTAL
    val = grid[pos[0]][pos[1]]
    if val == 9:
        TOTAL += 1

    for new_val, new_pos in get_adj(grid, pos):
        if new_val == val + 1:
            check_path2(grid, new_pos)


@timer
def solve1(data: list[str], result: int = 0) -> int:
    d = [[int(y) for y in x] for x in data]
    all_paths = []
    starting_positions = [(row, col) for row in range(len(d)) for col in range(len(d[0])) if d[row][col] == 0]
    for row, col in starting_positions:
        check_path(d, (row, col), [row, col], all_paths, set())
    result = len(all_paths)
    return result


@timer
def solve2(data: list[str], result: int = 0) -> int:
    d = [[int(y) for y in x] for x in data]
    starting_positions = [(row, col) for row in range(len(d)) for col in range(len(d[0])) if d[row][col] == 0]
    for row, col in starting_positions:
        check_path2(d, (row, col))
    result = TOTAL
    return result


answer_1 = solve1(inp)
answer_2 = solve2(inp)
