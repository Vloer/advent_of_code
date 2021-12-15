from __future__ import annotations
from pathlib import Path
import numpy as np
from collections import deque
from sys import maxsize

input_file = Path(__file__).parent / "inputs" / "d15.txt"


def parse_input(txt_file: str = input_file) -> list[int]:
    with open(txt_file, 'r') as f:
        return([[int(y) for y in x] for x in f.read().split("\n")])


inp = np.array(parse_input())
test = np.array([
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
])


def get_adj_indices(mat: np.ndarray, node: tuple(int)) -> list(tuple(int)):
    adj = []
    row = node[0]
    col = node[1]
    if row > 0:
        adj.append((row-1, col))
    if row+1 < mat.shape[0]-1:
        adj.append((row+1, col))
    if col > 0:
        adj.append((row, col-1))
    if col+1 < mat.shape[1]-1:
        adj.append((row, col+1))
    return adj


def dijkstra(mat: np.ndarray, start: tuple(int) = (0, 0)):
    unvisited = list(np.ndindex(mat.shape))
    previous_nodes = {}
    max_value = maxsize
    shortest_path = {node: max_value for node in unvisited}
    shortest_path[start] = 0

    while unvisited:
        current_min_node = None

        # find lowest
        for node in unvisited:
            if not current_min_node:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        # get possible paths and update length
        adjacent = get_adj_indices(mat, current_min_node)
        for adj in adjacent:
            temp_value = shortest_path[current_min_node] + mat[adj]
            if temp_value < shortest_path[adj]:
                shortest_path[adj] = temp_value
                previous_nodes[adj] = current_min_node

        unvisited.remove(current_min_node)
        print(f"{len(unvisited)} nodes remaining ...")
    return previous_nodes, shortest_path


def print_result(mat, previous_nodes, shortest_path, start, target):
    path = []
    node = target

    while node != start:
        path.append(node)
        node = previous_nodes[node]

    # Add the start node manually
    path.append(start)
    grid = np.array(mat, dtype='object')
    for node in path:
        grid[node] = ''
    

    print("We found the following best path with a value of {}.".format(
        shortest_path[target]))
    print(" -> ".join([str(x) for x in reversed(path)]))
    print(grid)

def solve1(data: np.ndarray, result: int = 0) -> int:
    start = (0, 0)
    end = (data.shape[0] - 1, data.shape[1] - 1)
    # get_adj_indices(data, 1, 3)
    previous_nodes, shortest_path = dijkstra(data)
    print_result(data, previous_nodes, shortest_path, start, end)
    return result


def solve2(data: list[int], result: int=0) -> int:
    return result


print(f"Answer 1: {solve1(inp)}")
print(f"Answer 2: {solve2(inp)}")
