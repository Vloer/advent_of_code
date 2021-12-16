from __future__ import annotations
from pathlib import Path
from time import perf_counter

input_file = Path(__file__).parent / "inputs" / "d2.txt"


def parse_input(txt_file: str = input_file) -> list[int]:
    with open(txt_file, 'r') as f:
        return(f.read().split("\n"))


inp = parse_input()


def solve(data: list[int], result: int = 0) -> int:
    return result


start = perf_counter()
print(f"Answer 1 took {time.perf_counter()-start}: {solve(inp)}")
start = perf_counter()
print(f"Answer 2 took {time.perf_counter()-start}: {solve(inp)}")
