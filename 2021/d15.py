from __future__ import annotations
from pathlib import Path

input_file = Path(__file__).parent / "inputs" / "d15.txt"


def parse_input(txt_file: str = input_file) -> list[int]:
    with open(txt_file, 'r') as f:
        return([[int(y) for y in x] for x in f.read().split("\n")])


inp = parse_input()
print(inp)
test =[
1163751742,
1381373672,
2136511328,
3694931569,
7463417111,
1319128137,
1359912421,
3125421639,
1293138521,
2311944581
]


def solve1(data: list[int], result: int = 0) -> int:
    return result


def solve2(data: list[int], result: int = 0) -> int:
    return result


print(f"Answer 1: {solve1(inp)}")
print(f"Answer 2: {solve2(inp)}")
