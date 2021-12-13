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
        self.caves: list[str] = []
        self.paths: list[str] = []
        self.connections: dict(str) = defaultdict(list)

    def add_cave(self, cave: str) -> None:
        if cave not in self.caves:
            self.caves.append(cave)
    
    def add_path(self, path: list[str]) -> None:
        self.paths.append(path)

    def add_connection(self, cave: str, connection: str) -> None:
        self.connections[cave].append(connection)


class Cave:
    def __init__(self, name: str = None, is_big: bool = False, connections: list[str] = None) -> None:
        self.caves = []
        self.visisted = False
        self.is_big = is_big
        self.connections = connections

    def add_cave(self, cave: Cave) -> None:
        self.caves.append(cave)


def create_system(inp: list[str]) -> System:
    # system_dict = defaultdict(list)
    # for line in inp:
    #     k, v = line.split('-')
    #     system_dict[k].append(v)
    #     system_dict[v].append(k)
    system = System()
    for line in inp:
        k, v = line.split('-')
        system.add_cave(k)
        system.add_connection(k, v)
        system.add_connection(v, k)
    return system


def find_path(system: defaultdict(list), paths_taken: list[str] = []) -> list[str] | bool:
    NEW_PATH_FOUND = False
    current_path = ''
    current_cave = 'start'
    caves_visited = []
    move(system, current_cave, caves_visited)


    return paths_taken, NEW_PATH_FOUND


def get_options(system: System, current_cave: str, caves_visited: list[str]) -> list[str]:
    options = []
    for cave in system.connections[current_cave]:
        if cave == 'start':
            continue
        elif cave.isupper():
            options.append(cave)
        elif cave not in caves_visited:
            options.append(cave)
    return options


def move(system: System, current_cave: str, caves_visited: list[str]) -> list[str] | bool:
    caves_visited.append(current_cave)
    if current_cave != 'end':
        opts = get_options(system, current_cave, caves_visited)
        if len(opts) > 0:
            for cave in opts:
                caves_visited = move(system, cave, caves_visited)
        else:
            return caves_visited[:-1]
    else:
        system.add_path(caves_visited)
        return caves_visited[:-1]


def solve1(data: list[str]) -> int:
    result = 0
    system = create_system(data)
    find_path(system)
    print(system.paths)
    return result


def solve2(data: list[int]) -> int:
    result = 0
    return result


print(f"Answer 1: {solve1(test1)}")
print(f"Answer 2: {solve2(inp)}")
