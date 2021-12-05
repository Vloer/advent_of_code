from __future__ import annotations
from pathlib import Path
import math

input_file = Path(__file__).parent / "inputs" / "d1.txt"


def parse_input(txt_file: str = input_file) -> list[int]:
    with open(txt_file, 'r') as f:
        return([int(x) for x in f.read().split("\n")])


inp = parse_input()


def calc(num: int) -> int:
    return math.floor(num/3)-2


def calc2(num: int) -> int:
    tot = 0


def solve1() -> None:
    result = 0
    result = sum(calc(m) for m in inp)
    print(f"Answer 1: {result}")


def solve2() -> None:
    result = 0
    for m in inp:
        while m > 0:
            m = calc(m)
            if m > 0:
                result += m
    print(f"Answer 2: {result}")


solve1()
solve2()
x = 100756

