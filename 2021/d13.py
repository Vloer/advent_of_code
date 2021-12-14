from __future__ import annotations
from pathlib import Path
import numpy as np

input_file = Path(__file__).parent / "inputs" / "d13.txt"


def parse_input(txt_file: str = input_file) -> list[int]:
    with open(txt_file, 'r') as f:
        return([x.split('\n') for x in f.read().split("\n\n")])


inp = parse_input()
test1 = [
    ["6, 10",
     "0, 14",
     "9, 10",
     "0, 3",
     "10, 4",
     "4, 11",
     "6, 0",
     "6, 12",
     "4, 1",
     "0, 13",
     "10, 12",
     "3, 4",
     "3, 0",
     "8, 4",
     "1, 10",
     "2, 14",
     "8, 10",
     "9, 0"],
    ["fold along y=7",
     "fold along x=5"]
]


def make_grid(coords: list[tuple(int)]) -> np.ndarray:
    max_x = 0
    max_y = 0
    for c in coords:
        x, y = list(map(int, c.split(',')))
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    grid = np.zeros((max_y+1, max_x + 1), dtype=int)
    for c in coords:
        x, y = list(map(int, c.split(',')))
        grid[y][x] = 1
    return np.array(grid)


def solve(data: list[list[tuple | str]], result: int = 0, max_folds: int = 0) -> int:
    coords, instructions = data
    grid = make_grid(coords)
    for i, instruction in enumerate(instructions):
        new_grid = grid.copy()
        print(type(grid))
        print(type(new_grid))
        if i >= max_folds:
            break
        ax, line = instruction.split("fold along ")[1].split("=")
        # if ax == 'x':
        #     g1 = grid[:, :int(line)]
        #     g2 = grid[:, int(line)+1:]
        #     g2 = np.flip(g2, axis=1)
        # else:
        #     g1 = grid[:int(line), :]
        #     g2 = grid[int(line)+1:, :]
        #     g2 = np.flip(g2, axis=0)
        if ax == 'x':
            new_grid[:, :line] += np.fliplr(grid[:, line + 1:])
            new_grid = new_grid[:, :line]
        else:
            new_grid[:line, :] += np.flipud(grid[line + 1:, :])
            new_grid = new_grid[:line, :]
        grid = new_grid
    grid[grid > 0] = 1
    return np.sum(grid)


def test_func():
    count = -1
    grid = np.array([[1, 2, 3, 4, 5], [0, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                     [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [100, 100, 100, 100, 100], [10, 10, 10, 10, 10]])
    line = 4
    for i in range(line, len(grid)-1):
        count += 2
        for col in range(len(grid[0])):
            grid[i-count][col] += grid[i+1][col]
    print(grid)


# test_func()
# print(f"Answer 1: {solve(inp, max_folds=1)}")
print(f"Answer 2: {solve(inp, max_folds=1000)}")
