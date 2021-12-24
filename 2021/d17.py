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
    if np.any(grid>1):
        return steps
    return False


def calculate_range_vx(target_area: list(range)) -> range:
    xmin_target = target_area[0][0]
    xmax_target = target_area[0][-1]
    xmin = round(sqrt(xmin_target*2))
    xmax = round(sqrt(xmax_target*2)) + 2
    return range(xmin, xmax)


def calculate_steps(range_vx: range, init_vy: int, init_grid: np.array, offset: int, area: list(range)) -> tuple(int) | int:
    total_steps = 10000
    final_vx = final_vy = 0
    max_y_final = -10
    correct_input_count = 0
    correct_inputs = []
    for vx in range_vx:
        init_vx = vx
        vy = -init_vy
        grid = init_grid.copy()
        x = 0
        y = offset
        max_y = 0
        steps = 0
        while True:
            grid[y, x] += 1
            if -y+offset > max_y:
                max_y = -y+offset
            ypos = y-offset
            if (x in area[0]) and (ypos in area[1]):
                correct_inputs.append((init_vx, init_vy))
                if steps < total_steps:
                    total_steps = steps
                if max_y > max_y_final:
                    max_y_final = max_y
                    final_vx = init_vx
                    final_vy = init_vy
                # print(f'Total steps for input {init_vx, init_vy}: {steps}. Final pos: {x, -(y-offset)}. Max y: {max_y}')
                correct_input_count += 1
                break
            if x > max(area[0]) or y > (max(area[1]) + offset):
                # print(f'Missed target area for input {init_vx, init_vy}. Final pos: {x, -(y-offset)}. Max y: {max_y}')
                break
            x, y, vx, vy = move(x, y, vx, vy)
            steps += 1
    return final_vx, final_vy, total_steps, max_y_final, correct_input_count, correct_inputs

def solve(data: str, result: int = 0, part1=True) -> int:
    area = get_target_area(data)
    grid, offset = create_grid(area)
    max_y = 0
    final_input_count = 0
    final_inputs = []
    for vy in range(-10, 100):
        vx = calculate_range_vx(area)
        # vx = range(0, 35)
        final_vx, final_vy, total_steps, final_y, correct_input_count, correct_inputs = calculate_steps(vx, vy, grid, offset, area)
        final_input_count += correct_input_count
        if final_y > max_y:
            max_y = final_y
        final_inputs.append(correct_inputs)
        print(f'{vy} done')
    print(final_inputs)
    return max_y, final_input_count


timing_1 = perf_counter()
answer = solve(inp)
answer_1 = answer[0]
print(f"Answer 1 took {perf_counter()-timing_1}: {answer_1}")
timing_2 = perf_counter()
answer_2 = answer[1]
print(f"Answer 2 took {perf_counter()-timing_2}: {answer_2}")
