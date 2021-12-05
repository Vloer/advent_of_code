from __future__ import annotations
from pathlib import Path

input_file = Path(__file__).parent / "inputs" / "d2.txt"


def parse_input(txt_file: str = input_file) -> list[int]:
    with open(txt_file, 'r') as f:
        return(f.read().split("\n"))


inp = parse_input()


def solve1() -> None:
    result = 0
    print(f"Answer 1: {result}")


def solve2() -> None:
    result = 0
    print(f"Answer 2: {result}")
