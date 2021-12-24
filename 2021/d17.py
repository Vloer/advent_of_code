from __future__ import annotations
from pathlib import Path
from time import perf_counter
import numpy as np
from math import sqrt

input_file = Path(__file__).parent / "inputs" / "d17.txt"


def parse_input(txt_file: str = input_file) -> list[int]:
    with open(txt_file, 'r') as f:
        return(f.read())


inp = parse_input()
test = 'target area: x=20..30, y=-10..-5'


def get_target_area(s: str) -> list[tuple(int)]:
    c = s.split(' ')
    x1, x2 = list(map(int, c[2].split(',')[0].split('x=')[1].split('..')))
    y1, y2 = list(map(int, c[3].split(',')[0].split('y=')[1].split('..')))
    return [range(x1, x2+1), range(-y2, -y1+1)]


def create_grid(target_area: list(range)) -> np.array | int:
    size_grid = 5000
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
    if np.any(grid > 1):
        return steps
    return False


def calculate_range_vx(target_area: list(range)) -> range:
    xmin_target = target_area[0][0]
    x = 0
    vx = 0
    while x < xmin_target:
        vx += 1
        x += vx
    return range(vx, target_area[0][-1] + 1)


def calculate_steps(range_vx: range, init_vy: int, init_grid: np.array, offset: int, area: list(range)) -> tuple(int) | int:
    final_vx = final_vy = 0
    max_y_final = -10
    correct_input_count = 0
    for vx in range_vx:
        init_vx = vx
        vy = -init_vy
        x = 0
        y = offset
        max_y = 0
        while True:
            if -y+offset > max_y:
                max_y = -y+offset
            ypos = y-offset
            if (x in area[0]) and (ypos in area[1]):
                if max_y > max_y_final:
                    max_y_final = max_y
                    final_vx = init_vx
                    final_vy = init_vy
                correct_input_count += 1
                break
            if x > max(area[0]) or y > (max(area[1]) + offset):
                break
            x, y, vx, vy = move(x, y, vx, vy)
    return max_y_final, correct_input_count


def solve(data: str, result: int = 0, part1=True) -> int:
    area = get_target_area(data)
    grid, offset = create_grid(area)
    max_y = 0
    final_input_count = 0
    vx = calculate_range_vx(area)
    for vy in range(-10000, 10000):
        final_y, correct_input_count = calculate_steps(
            vx, vy, grid, offset, area)
        final_input_count += correct_input_count
        if final_y > max_y:
            max_y = final_y
        print(f'{vy} done')
    return max_y, final_input_count


timing_1 = perf_counter()
answer = solve(inp)
answer_1 = answer[0]
print(f"Answer 1 took {perf_counter()-timing_1}: {answer_1}")
timing_2 = perf_counter()
answer_2 = answer[1]
print(f"Answer 2 took {perf_counter()-timing_2}: {answer_2}")
