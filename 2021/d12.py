from __future__ import annotations
from pathlib import Path
from collections import defaultdict

input_file = Path(__file__).parent / "inputs" / "d12.txt"


def parse_input(txt_file: str = input_file) -> list[int]:
    with open(txt_file, 'r') as f:
        return(f.read().split("\n"))


inp = parse_input()
test1 = ["start-A",
         "start-b",
         "A-c",
         "A-b",
         "b-d",
         "A-end",
         "b-end"]


class System:
    def __init__(self) -> None:
        self.caves = []

    def add_cave(self, cave: Cave) -> None:
        self.caves.append(cave)


class Cave:
    def __init__(self, name: str, is_big: bool, connections: list[str]) -> None:
        self.visisted = False
    def


def create_system(inp: list[str]) -> defaultdict(list[str]):
    # system = defaultdict(list)
    # for line in inp:
    #     k, v = line.split('-')
    #     system[k].append(v)
    #     system[v].append(k)
    system = System
    for line in inp:
        k,v = line.split('-')
        cave = Cave(k, k.isupper(), v)
        system.add_cave(cave)
    return system


def solve1(data: list[str]) -> int:
    result = 0
    system = create_system(data)
    for cave, connections in system.items():
        cave = Cave(cave.isupper(), connections)
    return result


def solve2(data: list[int]) -> int:
    result = 0
    return result


print(f"Answer 1: {solve1(test1)}")
print(f"Answer 2: {solve2(inp)}")
