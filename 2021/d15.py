from __future__ import annotations
from pathlib import Path
import numpy as np
from time import perf_counter
import cProfile
from sys import maxsize

input_file = Path(__file__).parent / "inputs" / "d15.txt"


def parse_input(txt_file: str = input_file) -> list[int]:
    with open(txt_file, 'r') as f:
        return([[int(y) for y in x] for x in f.read().split("\n")])


inp = np.array(parse_input())
test = [
    [1, 1, 6, 3, 7, 5, 1, 7, 4, 2],
    [1, 3, 8, 1, 3, 7, 3, 6, 7, 2],
    [2, 1, 3, 6, 5, 1, 1, 3, 2, 8],
    [3, 6, 9, 4, 9, 3, 1, 5, 6, 9],
    [7, 4, 6, 3, 4, 1, 7, 1, 1, 1],
    [1, 3, 1, 9, 1, 2, 8, 1, 3, 7],
    [1, 3, 5, 9, 9, 1, 2, 4, 2, 1],
    [3, 1, 2, 5, 4, 2, 1, 6, 3, 9],
    [1, 2, 9, 3, 1, 3, 8, 5, 2, 1],
    [2, 3, 1, 1, 9, 4, 4, 5, 8, 1]
]
test2 = [
    [1, 1, 1],
    [1, 1, 1],
    [2, 2, 2]
]


def get_adj_indices(mat: np.ndarray, node: tuple(int)) -> list(tuple(int)):
    adj = []
    row = node[0]
    col = node[1]
    if row > 0:
        adj.append((row-1, col))
    if row+1 <= mat.shape[0]-1:
        adj.append((row+1, col))
    if col > 0:
        adj.append((row, col-1))
    if col+1 <= mat.shape[1]-1:
        adj.append((row, col+1))
    return adj


def create_adj_list(mat: np.ndarray) -> dict(str):
    adj_list = {}
    for node in np.ndindex(mat.shape):
        adj_list[node] = get_adj_indices(mat, node)
    return adj_list


def astar_search(mat: np.ndarray, start: tuple(int), end: tuple(int)) -> list(tuple) | int:
    start_node = start
    end_node = end
    parents = {}
    # open = set()
    # closed = set()
    # open.add(start_node)
    open = []
    closed = []
    open.append(start_node)
    value_mat = np.zeros_like(mat) + maxsize
    value_mat[start_node] = 0

    while len(open) > 0:
        # current_node = open.pop()
        # closed.add(current_node)
        current_node = open.pop(0)
        closed.append(current_node)
        value_cur = value_mat[current_node]
        print(value_cur)
        if current_node == end_node:
            total_cost = value_mat[current_node]
            path = []
            while current_node != start_node:
                path.append(current_node)
                current_node = parents[current_node]
            return path[::-1], total_cost

        adjacent = get_adj_indices(mat, current_node)

        for next_node in adjacent:
            if next_node in closed:
                continue
            value_next = mat[next_node]
            value_new = value_cur + value_next
            if value_new < value_mat[next_node]:
                value_mat[next_node] = value_cur + value_next
                parents[next_node] = current_node
                open.append(next_node)

    print("No path found!")
    return None, None


def wrap(x: int) -> int:
    return ((x-1) % 9) + 1


def solve(data: np.ndarray, part1=True, result: int = 0) -> int:
    if part1:
        data = np.array(data)
    else:
        big_grid = np.array([row * 5 for row in data] * 5)
        i = [*range(len(data), len(data)*2)]
        for l in i:
            count = 0
            count_col = 0
            for row in range(l, len(big_grid), len(data)):
                count += 1
                big_grid[row] += count
            for col in range(l, len(big_grid[0]), len(data)):
                count_col += 1
                big_grid[:, col] += count_col

        wrap_func = np.vectorize(wrap)
        data = wrap_func(big_grid)

    start = (0, 0)
    end = (data.shape[0] - 1, data.shape[1] - 1)
    path, cost = astar_search(data, start, end)
    return cost


timing_1 = perf_counter()
# cProfile.run('solve(inp)')
answer_1 = solve(inp)
print(f"Answer 1 took {perf_counter()-timing_1}: {answer_1}")
timing_2 = perf_counter()
# answer_2 = solve(inp, part1=False)
# print(f"Answer 2 took {perf_counter()-timing_2}: {answer_2}")
