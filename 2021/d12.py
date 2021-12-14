from __future__ import annotations
from pathlib import Path
from collections import defaultdict, Counter

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
test2 = ["dc-end",
         "HN-start",
         "start-kj",
         "dc-start",
         "dc-HN",
         "LN-dc",
         "HN-end",
         "kj-sa",
         "kj-HN",
         "kj-dc"]


class System:
    def __init__(self) -> None:
        self.caves: list[str] = []
        self.caves_small: list[str] = []
        self.paths: list[str] = []
        self.connections: dict(str) = defaultdict(list)

    def add_cave(self, cave: str) -> None:
        if cave not in self.caves:
            self.caves.append(cave)
        if cave not in self.caves_small and cave.islower():
            self.caves_small.append(cave)

    def add_path(self, path: list[str]) -> None:
        self.paths.append(path)

    def add_connection(self, cave: str, connection: str) -> None:
        self.connections[cave].append(connection)


def create_system(data: list[str], part2: bool = False) -> System:
    system = System()
    for line in data:
        k, v = line.split('-')
        system.add_cave(k)
        system.add_connection(k, v)
        system.add_connection(v, k)
        if part2:
            if k.islower():
                system.add_connection(v, k)
                system.add_connection(k, v)
            if v.islower():
                system.add_connection(k, v)
                system.add_connection(v, k)

    return system


def find_path(system: System) -> list[str]:
    current_cave = 'start'
    caves_visited = []
    move(system, current_cave, caves_visited)
    return system.paths


def get_options(system: System, current_cave: str, caves_visited: list[str]) -> list[str]:
    options = []
    small_caves_visited = [x for x in caves_visited if x.islower() and not x == 'start']
    counts = Counter(small_caves_visited)
    for cave in system.connections[current_cave]:
        if cave == 'start':
            continue
        elif cave.isupper():
            if cave not in options:
                options.append(cave)
        elif cave not in options:
            if any([v > 1 for v in counts.values()]):
                if counts[cave] + 1 < 2:
                    options.append(cave)
            else:
                options.append(cave)
    return options


def move(system: System, current_cave: str, caves_visited: list[str]) -> list[str] | bool:
    caves_visited.append(current_cave)

    if current_cave == 'end':
        system.add_path(caves_visited.copy())
        caves_visited.pop()
        return
    opts = get_options(system, current_cave, caves_visited)
    if len(opts) > 0:
        for cave in opts:
            move(system, cave, caves_visited)
    caves_visited.pop()


def solve(data: list[str], part2: bool = False) -> int:
    system = create_system(data, part2)
    paths = find_path(system)
    return len(paths)


print(f"Answer 1: {solve(inp)}")
print(f"Answer 2: {solve(inp, True)}")
