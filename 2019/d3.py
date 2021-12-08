from __future__ import annotations
from pathlib import Path
import numpy as np

input_file = Path(__file__).parent / "inputs" / "d3.txt"


def parse_input(txt_file: str = input_file) -> list[int]:
    with open(txt_file, 'r') as f:
        return(f.read().split("\n"))


inp = parse_input()
test_set = [['R8','U5','L5','D3'], ['U7','R6','D4','L4']]

def instruction(s: str) -> tuple(str, int):
    return s[0], int(s[1:])

def solve1(inp: list[list[str]]) -> None:
    result = 0
    grid = [[]]
    start1 = start2 = (0, 0)
    instructions_1 = list(map(instruction, inp[0]))
    instructions_2 = list(map(instruction, inp[1]))

    for instr in instructions_1:

    return result


def solve2() -> None:
    result = 0
    return result


print(f"Answer 1: {solve1(test_set)}")
# print(f"Answer 2: {solve2(inp)}")