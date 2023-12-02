from __future__ import annotations
from pathlib import Path
from time import perf_counter

input_file = Path(__file__).parent / "inputs" / f'{Path(__file__).stem}.txt'


def parse_input(txt_file: str = input_file) -> list[str]:
    with open(txt_file, 'r') as f:
        return f.read().split("\n")


inp = parse_input()
test = [
    '2-4,6-8',
    '2-3,4-5',
    '5-7,7-9',
    '2-8,3-7',
    '6-6,4-6',
    '2-6,4-8'
]


def solve(data: list[str], result: int = 0, part1=True) -> int:
    total_pairs = 0
    for i, elves in enumerate(data):
        pair1, pair2 = [(int(y) for y in x.split('-')) for x in elves.split(',')]
        a, b = [*pair1]
        c, d = [*pair2]
        if part1:
            if (a <= c and b >= d) or (c <= a and d >= b):
                total_pairs += 1
        else:
            if min(c, d) <= min(a, b) <= max(c, d):
                total_pairs += 1
            elif min(a, b) <= min(c, d) <= max(a, b):
                total_pairs += 1

    return total_pairs

#2-4
#3-6


timing_1 = perf_counter()
answer_1 = solve(inp)
print(f"Answer 1 took {perf_counter() - timing_1}: {answer_1}")
timing_2 = perf_counter()
answer_2 = solve(inp, part1=False)
print(f"Answer 2 took {perf_counter() - timing_2}: {answer_2}")
