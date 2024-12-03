from __future__ import annotations
from pathlib import Path
from time import perf_counter
from collections import Counter

input_file = Path(__file__).parent / "inputs" / f'{Path(__file__).stem}.txt'


def parse_input(txt_file: str = input_file) -> list[str]:
    with open(txt_file, 'r') as f:
        return f.read().split("\n")


inp = parse_input()
test = """3   4
4   3
2   5
1   3
3   9
3   3""".split('\n')


def solve(data: list[str], result: int = 0, part1=True) -> int:
    l1, l2 = [], []
    for r in data:
        a, b = r.split('   ')
        l1.append(int(a))
        l2.append(int(b))
    s = 0
    for _ in range(len(l1)):
        n1 = min(l1)
        n2 = min(l2)
        l1.remove(n1)
        l2.remove(n2)
        s += abs(n2 - n1)

    return s


def solve_2(data: list[str]):
    l1, l2 = [], []
    for r in data:
        a, b = r.split('   ')
        l1.append(int(a))
        l2.append(int(b))
    c = Counter(l2)
    s = 0
    for n in l1:
        s += n * c[n]
    return s


timing_1 = perf_counter()
answer_1 = solve(inp)
print(f"Answer 1 took {perf_counter() - timing_1}: {answer_1}")
timing_2 = perf_counter()
answer_2 = solve_2(inp)
print(f"Answer 2 took {perf_counter() - timing_2}: {answer_2}")
