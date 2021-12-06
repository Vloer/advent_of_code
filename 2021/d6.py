from __future__ import annotations
from pathlib import Path
import math
from collections import Counter
import numpy as np

input_file = Path(__file__).parent / "inputs" / "d6.txt"


def parse_input(txt_file: str = input_file) -> list[int]:
    with open(txt_file, 'r') as f:
        return([int(x) for x in f.read().split(",")])


inp = parse_input()
test_set = [1, 2, 3, 0]


def subtract_num(fish: np.array) -> np.array:
    fish = np.append(fish, np.full(np.count_nonzero(fish == 0), 9))
    fish = np.where(fish == 0, 6, fish-1)
    return fish


def solve1(inp: list[int], days: int) -> None:
    inp = np.array(inp)
    for day in range(days):
        inp = subtract_num(inp)
    result = len(inp)
    print(f"Answer 1: {result}")


def solve2(inp: list[int], days: int) -> None:
    inp = Counter(inp)
    result = 0
    for day in range(days):
        inp_count = Counter()
        for k, v in inp.items():
            if k == 0:
                inp_count.update({6: v, 8: v})
            else:
                inp_count.update({k-1: v})
        inp = inp_count
    result = sum(inp_count.values())
    print(f"Answer 2: {result}")


solve1(inp, 80)
solve2(inp, 256)
