from __future__ import annotations
from pathlib import Path

input_file = Path(__file__).parent / "inputs" / "d1.txt"


def parse_input(txt_file: str = input_file) -> list[int]:
    with open(txt_file, 'r') as f:
        return([int(x) for x in f.read().split("\n")])


def solve_1() -> None:
    inp = parse_input()
    cur = 99999
    count = 0
    for i in inp:
        if i > cur:
            count += 1
        cur = i
    print(f"Answer 1 is {count}")


def solve_2() -> None:
    inp = parse_input()
    cur = 90999999
    count = 0
    for i in range(3, len(inp)+1):
        tot = sum(inp[i-3:i])
        if tot > cur:
            count += 1
        cur = tot
    print(f"Answer 2 is {count}")


solve_1()
solve_2()
