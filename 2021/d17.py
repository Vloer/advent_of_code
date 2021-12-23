from __future__ import annotations
from pathlib import Path
from time import perf_counter
import numpy as np
from sys import maxsize
np.set_printoptions(threshold=maxsize)

input_file = Path(__file__).parent / "inputs" / "d2.txt"


def parse_input(txt_file: str = input_file) -> list[int]:
    with open(txt_file, 'r') as f:
        return(f.read())


inp = parse_input()
test = 'target area: x=20..30, y=-10..-5'


def get_target_area(s: str) -> list[tuple(int)]:
    c = s.split(' ')
    x1, x2 = list(map(int, c[2].split(',')[0].split('x=')[1].split('..')))
    y1, y2 = list(map(int, c[3].split(',')[0].split('y=')[1].split('..')))
    return [range(x1, x2+1), range(-y2, -y1)]

def create_grid(target_area: tuple(range)) -> np.array | int:
    size_grid = 50
    offset = int(size_grid / 2)
    g = np.zeros((size_grid, size_grid), dtype=int)
    g[offset, 0] = 1
    for x in target_area[0]:
        for y in target_area[1]:
            g[y+offset, x] = 1
    return g, offset


def move(x, y, vx, vy) -> tuple(int) | tuple(int):
    if vx > 0:
        end_v_x = vx - 1
    elif vx < 0:
        end_v_x = vx + 1
    else:
        end_v_x = 0
    return x + vx, y + vy, end_v_x, vy + 1


def check(grid: np.array, steps: int) -> bool | int:
    if np.any(grid>1):
        return steps
    return False


def solve(data: str, result: int = 0, part1=True) -> int:
    area = get_target_area(data)
    grid, offset = create_grid(area)
    x = 0
    y = offset
    vx = 17
    vy = 4
    init_v = (vx, vy)
    steps = 0
    while True:
        steps += 1
        x, y, vx, vy = move(x, y, vx, vy)
        grid[y, x] += 1
        if x > max(area[0]) or y > (max(area[1]) + offset):
            return check(grid, steps)
        print(f'new pos: {x, -(y-offset)}')


timing_1 = perf_counter()
answer_1 = solve(test)
print(f"Answer 1 took {perf_counter()-timing_1}: {answer_1}")
timing_2 = perf_counter()
answer_2 = solve(test, part1=False)
print(f"Answer 2 took {perf_counter()-timing_2}: {answer_2}")
