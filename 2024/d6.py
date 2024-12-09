from __future__ import annotations
from pathlib import Path
import time
from typing import Callable, Any
from copy import deepcopy
from collections import defaultdict
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


input_file = Path(__file__).parent / "inputs" / f'{Path(__file__).stem}.txt'


def parse_input(txt_file: str = input_file) -> str:
    with open(txt_file, 'r') as f:
        return f.read()


inp = parse_input()
test = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""


def find_start(grid: list[list[str]]) -> tuple[int, int]:
    for y, row in enumerate(grid):
        for x, pos in enumerate(row):
            if pos == '^':
                return y, x


def get_new_pos(grid: list[list[str]], direction: str, row: int, pos: int) -> tuple[str, int, int]:
    match direction:
        case 'up':
            return grid[row - 1][pos], row - 1, pos
        case 'down':
            return grid[row + 1][pos], row + 1, pos
        case 'left':
            return grid[row][pos - 1], row, pos - 1
        case 'right':
            return grid[row][pos + 1], row, pos + 1


def get_new_direction(direction: str) -> str:
    match direction:
        case 'up':
            return 'right'
        case 'right':
            return 'down'
        case 'down':
            return 'left'
        case 'left':
            return 'up'


@timer
def solve1(data: str, result: int = 0) -> int:
    visited = []
    data = [[x for x in r] for r in data.split('\n')]
    row, pos = find_start(data)
    direction = 'up'
    while True:
        try:
            visited.append((row, pos))
            symbol, new_row, new_pos = get_new_pos(data, direction, row, pos)
            if symbol == '#':
                direction = get_new_direction(direction)
            else:
                row = new_row
                pos = new_pos

        except IndexError:
            break
    result = len(set(visited))
    return result


def print_grid(grid):
    for i, row in enumerate(grid):
        print(f"{str(i):<3}: {' '.join(row)}")


@timer
def solve2(base_data: str, result: int = 0) -> int:
    base_data = [[x for x in r] for r in base_data.split('\n')]
    counter = 0
    for i, y in enumerate(base_data):
        for j, x in enumerate(y):
            counter += 1
            if counter % 250 == 0:
                print(f'Checked pos {counter} of {len(y) * len(base_data) - 1}')
            row, pos = find_start(base_data)
            if (i, j) == (row, pos) or base_data[i][j] == '#':
                continue
            data = deepcopy(base_data)
            data[i][j] = '#'
            visited: dict[tuple[int, int], list[str]] = defaultdict(list)
            direction = 'up'
            steps = 0
            while -1 < pos < (len(y) - 1) and -1 < row < (len(data) - 1):
                steps += 1
                if steps == 100000:
                    raise ValueError(f'Did something wrong on counter {counter}')
                visits = visited.get((row, pos))
                if visits and direction in visits:
                    result += 1
                    break
                visited[(row, pos)].append(direction)
                data[row][pos] = 'X'
                try:
                    symbol, new_row, new_pos = get_new_pos(data, direction, row, pos)
                except IndexError:
                    break
                if symbol == '#':
                    direction = get_new_direction(direction)
                else:
                    row = new_row
                    pos = new_pos
    return result


answer_1 = solve1(inp)
answer_2 = solve2(inp)
