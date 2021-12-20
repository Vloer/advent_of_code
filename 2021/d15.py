from __future__ import annotations
from pathlib import Path
import numpy as np
from time import perf_counter

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


class Node:
    def __init__(self, position: tuple(), parent: tuple()):
        self.position = position
        self.parent = parent
        self.dist_start = 0
        self.dist_goal = 0
        self.dist_tot = 0

    def __eq__(self, other: Node):
        return self.position == other.position

    def __lt__(self, other: Node):
        return self.dist_tot < other.dist_tot

    def __repr__(self):
        return (f'({self.position}, {self.dist_tot})')


def astar_search(mat: np.ndarray, start: tuple(int), end: tuple(int)) -> list(tuple) | int:
    open = []
    closed = []
    start_node = Node(start, None)
    end_node = Node(end, None)
    open.append(start_node)

    while len(open) > 0:
        open.sort()
        current_node: Node = open.pop(0)
        closed.append(current_node)
        if current_node == end_node:
            total_cost = current_node.dist_tot
            path = []
            while current_node != start_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1], total_cost

        adjacent = get_adj_indices(mat, current_node.position)

        for next in adjacent:
            value = mat[next]
            adj = Node(next, current_node)
            if adj in closed:
                continue

            adj.dist_start = current_node.dist_tot
            adj.dist_goal = value
            adj.dist_tot = adj.dist_start + adj.dist_goal

            # Check if neighbor is in open list and if it has a lower total value
            if add_to_open(open, adj):
                open.append(adj)

    # Return None, no path is found
    return None, None


def add_to_open(open: list[Node], neighbor: Node):
    for node in open:
        if (neighbor == node and neighbor.dist_tot >= node.dist_tot):
            return False
    return True


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
answer_1 = solve(test)
print(f"Answer 1 took {perf_counter()-timing_1}: {answer_1}")
timing_2 = perf_counter()
answer_2 = solve(test, part1=False)
print(f"Answer 2 took {perf_counter()-timing_2}: {answer_2}")
