from __future__ import annotations
from collections import deque
from pathlib import Path
import numpy as np
import collections
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

def astar_search(mat: np.ndarray, start: tuple(int), end: tuple(int)):
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
            path = []
            while current_node != start_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]
        
        adjacent = get_adj_indices(mat, current_node.position)

        for next in adjacent:
            value = mat[next]
            adj = Node(next, current_node)
            if adj in closed:
                continue

            # Generate heuristic
            adj.dist_start = abs(adj.position[0] - start_node.position[0]) + abs(adj.position[1] - start_node.position[1])
            adj.dist_goal = abs(adj.position[0] - adj.position[0]) + abs(adj.position[1] - adj.position[1])
            adj.dist_tot = adj.dist_start + adj.dist_goal

class Graph:
    # example of adjacency list (or rather map)
    # adjacency_list = {
    # 'A': [('B', 1), ('C', 3), ('D', 7)],
    # 'B': [('D', 5)],
    # 'C': [('D', 12)]
    # }

    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    # heuristic function with equal values for all nodes
    def h(self, n):
        H = {
            'A': 1,
            'B': 1,
            'C': 1,
            'D': 1
        }

        return H[n]

    def a_star_algorithm(self, start_node, stop_node):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = set([start_node])
        closed_list = set([])

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}

        g[start_node] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if n is None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v

            if n is None:
                print('Path does not exist!')
                return None

            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path

            # for all neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None


def solve1(data: np.ndarray, result: int = 0) -> int:
    start = (0, 0)
    end = (data.shape[0] - 1, data.shape[1] - 1)

    return result


def solve2(data: list[int], result: int = 0) -> int:
    return result


print(f"Answer 1: {solve1(test)}")
print(f"Answer 2: {solve2(inp)}")
