from __future__ import annotations
from pathlib import Path
from time import perf_counter

input_file = Path(__file__).parent / "inputs" / f'{Path(__file__).stem}.txt'


def parse_input(txt_file: str = input_file) -> list[str]:
    with open(txt_file, 'r') as f:
        # return [int(x) for x in f.read().split("\n")]
        return f.read().split('\n')


inp = parse_input()


def solve(data: list[int | str], result: int = 0, part1=True) -> int:
    calories = 0
    max_cal = [0, 0, 0]
    for i, c in enumerate(data):
        if not c:
            max_cal.sort()
            for j, m in enumerate(max_cal):
                if calories > m:
                    max_cal[j] = calories
                    break
            calories = 0
        else:
            calories += int(c)
    if part1:
        return max(max_cal)
    return sum(max_cal)


timing_1 = perf_counter()
answer_1 = solve(inp)
print(f"Answer 1 took {perf_counter() - timing_1}: {answer_1}")
timing_2 = perf_counter()
answer_2 = solve(inp, part1=False)
print(f"Answer 2 took {perf_counter() - timing_2}: {answer_2}")
