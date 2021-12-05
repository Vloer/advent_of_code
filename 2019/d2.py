from __future__ import annotations
from pathlib import Path

input_file = Path(__file__).parent / "inputs" / "d2.txt"


def parse_input(txt_file: str = input_file) -> list[int]:
    with open(txt_file, 'r') as f:
        return([int(x) for x in f.read().split(",")])


inp = parse_input()


def solve1(inp=inp) -> None:
    inp[1] = 12
    inp[2] = 2
    result = 0
    codelist = [inp[i-4:i] for i in range(4, len(inp), 4)]
    for code in codelist:
        if code[0] == 1:
            inp[code[3]] = inp[code[1]] + inp[code[2]]
        elif code[0] == 2:
            inp[code[3]] = inp[code[1]] * inp[code[2]]
        elif code[0] == 99:
            break
    result = inp[0]
    print(f"Answer 1: {result}")


def solve2(inp=inp) -> None:
    result = 0
    print(f"Answer 2: {result}")


solve1()
solve2()
