from __future__ import annotations
from pathlib import Path
import statistics
from math import inf

input_file = Path(__file__).parent / "inputs" / "d7.txt"


def parse_input(txt_file: str = input_file) -> list[int]:
    with open(txt_file, 'r') as f:
        return([int(x) for x in f.read().split(",")])


inp = parse_input()
testdata = [16,1,2,0,4,2,7,1,2,14]


def fuel_per_step(start: int, end: int) -> int:
    s = min(start, end)
    e = max(start, end)
    return sum(range(1, len(range(s, e+1))))


def solve1(data: list[int]) -> None:
    result = 0
    med = int(statistics.median(data))
    result = sum([abs(i-med) for i in data])
    print(f"Answer 1: {result}")


def solve2(data: list[int]) -> None:
    result = inf
    med = int(statistics.median(data))
    max_iter = abs(max(inp) - med)
    no_change_ind = 0
    for i in range(max_iter + 1):
        temp_result = sum([fuel_per_step(x, med + i) for x in data])
        temp_result2 = sum([fuel_per_step(x, med - i) for x in data])
        new_result = min(result, temp_result, temp_result2)
        if new_result == result:
            no_change_ind += 1
        if no_change_ind == 50:
            break
        result = new_result
        print(f"Tried {i}: {temp_result}, {temp_result2}, current result is {result}")
    print(f"Answer 2: {result}")

solve1(inp)
solve2(inp)